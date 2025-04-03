import datetime
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2
import imutils
import tensorflow as tf
from myapp.DBConnection import Db
from pygame import mixer

CAM_LAT = "11.9213572"
CAM_LONG = "75.7903065"

STATIC_PATH = r"C:/Users/Sabeeh/OneDrive/Desktop/Main Project/Early_warning/myapp/static/"
MODEL_PATH = os.path.join(STATIC_PATH, "logs/output_graph.pb")
LABELS_PATH = os.path.join(STATIC_PATH, "logs/output_labels.txt")
BUZZERS_PATH = os.path.join(STATIC_PATH, "buzzers/")

EMAIL_USER = "wildanimal2k25@gmail.com"
EMAIL_PASS = "ghbf puhp abau hsrl"

last_buzzer_time = 0

def play_buzzer(anml):
    global last_buzzer_time
    current_time = time.time()
    mixer.init()
    buzzer_map = {
		"bear": "buzzer-bear.mp3",
		"elephant": "buzzer-elephant.mp3",
		"leopard": "buzzer-leopard.mp3",
		"boar": "buzzer-boar.mp3",
		"bison": "buzzer-bison.mp3",
		"deer": "buzzer-deer.wav"
	}
    if current_time - last_buzzer_time >= 3:
        last_buzzer_time = current_time
        if anml in buzzer_map:
            mixer.music.load(os.path.join(BUZZERS_PATH, buzzer_map[anml]))
            mixer.music.play()

def get_office(anml, dt, tm, lati, longi):
	db = Db()
	res = db.select("SELECT * FROM `myapp_forest_officer`")
	for i in res:
		send_mail(i['email'], anml, dt, tm, lati, longi)

def send_mail(mail, anml, dt, tm, lati, longi):
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(EMAIL_USER, EMAIL_PASS)
	msg = MIMEMultipart()  # create a message.........."
	msg['From'] = EMAIL_USER
	msg['To'] = mail
	msg['Subject'] = "Wild animal alert"
	body = f'Wild animal ({anml}) detected on {dt} {tm}. Location: http://maps.google.com/?q={lati},{longi}'
	msg.attach(MIMEText(body, 'plain'))
	s.send_message(msg)

def save_detection(frame, human_string, cam_lati, cam_longi, db):
	try:
		now = datetime.datetime.now()
		t = now.strftime("%H:%M")
		dt = now.strftime("%Y%m%d_%H%M%S")

		img_path = f"{STATIC_PATH}detections/{dt}.jpg"
		cv2.imwrite(img_path, frame)
		path=f"/static/detections/{dt}.jpg"
		db = Db()
		db.insert("INSERT INTO `myapp_animal_notification`(content, longitude, latitude, DATE, TIME, detected) VALUES('"+path+"', '"+cam_longi+"', '"+cam_lati+"', CURDATE(), '"+t+"', '"+human_string+"')")

		get_office(human_string, now.date(), t, cam_lati, cam_longi)
	except Exception as e:
		print(f"Database error: {e}, skipping detection save.")

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
#vs = cv2.VideoCapture(r"C:\Users\Sabeeh\OneDrive\Desktop\samples\amazing-giant-wild-boar-shots--dev-azılı-domuz-vuruşları.mp4")	#	 from video
vs = cv2.VideoCapture(0)	#	from live cam
time.sleep(2.0)

# Load the model
# with tf.gfile.FastGFile("logs/output_graph.pb", 'rb') as f:
with tf.gfile.FastGFile(MODEL_PATH, 'rb') as f:
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(f.read())
	_ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
	softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

	
	domestic_animals = {"cat", "cattle", "dog"}
	# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		ret, frame = vs.read()
		if not ret:
			print("[ERROR] Failed to read frame. Exiting...")
			break

		frame = imutils.resize(frame, width=400)
		img_path = os.path.join(STATIC_PATH, "captured_image.jpg")
		cv2.imwrite(img_path, frame)

		image_data = tf.gfile.FastGFile(img_path, 'rb').read()

		label_lines = [line.rstrip() for line in tf.gfile.GFile(LABELS_PATH)]

		predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
		top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

		for node_id in top_k:
			human_string = label_lines[node_id]
			score = predictions[0][node_id]

			if human_string not in domestic_animals and score * 100 > 50.0:
				print(f"{human_string} detected (score = {score:.2f})")

				text = f"{human_string}: {score:.2f}%"
				cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

				play_buzzer(human_string)

				try:
					db = Db()
					res = db.selectOne("SELECT TIMEDIFF(CURTIME(), TIME) as tm FROM `myapp_animal_notification` WHERE DATE=CURDATE() AND latitude='"+CAM_LAT+"' AND longitude='"+CAM_LONG+"' AND detected='"+human_string+"' order by id desc")

					if res is None:
						print("No previous record found, saving detection.")
						save_detection(frame, human_string, CAM_LAT, CAM_LONG, db)
					else:
						try:
							diff_mins = int(str(res['tm']).split(":")[1])
							print(f"Time since last detection: {diff_mins} minutes")

							if diff_mins >= 1:
								save_detection(frame, human_string, CAM_LAT, CAM_LONG, db)
						except Exception as e:
							print(f"Error parsing time difference: {e}, saving detection anyway.")
							save_detection(frame, human_string, CAM_LAT, CAM_LONG, db)

				except Exception as e:
					print(f"Database error: {e}, skipping detection save.")

			elif score * 100 > 50.0:
				print("Domestic Animal detected, no action taken.")

		# show the output frame
		cv2.imshow("Detection", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

# do a bit of cleanup
vs.stop()