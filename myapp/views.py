import base64, datetime, os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *
STATIC_PATH = "D:/Main Project/Early_warning/myapp/static"
MODEL_PATH = os.path.join(STATIC_PATH, "logs/output_graph.pb")
LABELS_PATH = os.path.join(STATIC_PATH, "logs/output_labels.txt")
BUZZERS_PATH = os.path.join(STATIC_PATH, "buzzers/")

def login(request):
    return render(request,'login_new.html')
def login_post(request):
    username = request.POST['uname']
    password = request.POST['passwd']
    res = Login.objects.get(username=username,password=password)

    if res is not None:
        request.session['lid']=res.id
        if res.type =='admin':
            return redirect('/admin_home/')
        elif res.type =='officer':
            return redirect('/ohome/')
        else:
            return HttpResponse("<script>alert('Unauthorised user');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid details');window.location='/'</script>")

def forest_division(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
        return render(request,'Admin/forest division.html')
def forest_division_post(request):
    fd = request.POST['textfield']
    obj=Division()
    obj.division=fd
    obj.save()
    return HttpResponse('''<script>alert("Forest division added");window.location="/view_forest_division/";</script>''')

def view_forest_division(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
        res = Division.objects.all()
        return render(request,'Admin/view_forestdivision.html',{'data':res})
def search_division(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
        ser = request.POST['textfield']
        res = Division.objects.filter(division__icontains=ser)
    return render(request,'Admin/view_forestdivision.html',{'data':res})

def edit_forest_division(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
        res = Division.objects.get(id=did)
        return render(request,'Admin/editforest division .html',{'data':res})
def edit_forest_division_post(request):
    did = request.POST['id1']
    fd = request.POST['textfield']
    obj = Division.objects.get(id=did)
    obj.division = fd
    obj.save()
    return HttpResponse('''<script>alert("Updated");window.location="/view_forest_division/";</script>''')

def delete_division(request,did):
    res = Division.objects.get(id=did).delete()
    return redirect('/view_forest_division/')

def station(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        ss=Division.objects.all()
        return render(request,'Admin/station.html',{'data':ss})

def station_post(request):
    station = request.POST['textfield']
    contact = request.POST['textfield2']
    district = request.POST['textfield3']
    pin = request.POST['textfield4']
    place = request.POST['textfield5']
    division = request.POST['select']
    dd = Division.objects.get(id=division)
    obj = Station()
    obj.name = station
    obj.phone = contact
    obj.district = district
    obj.place = place
    obj.pin = pin
    obj.DIVISION = dd
    obj.save()
    return HttpResponse('''<script>alert("Forest station added");window.location="/view_station/";</script>''')

def view_station(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
        res=Station.objects.all()
        return render(request,'Admin/view_sation.html',{'data':res})
def search_station(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        ser = request.POST['textfield']
        res = Station.objects.filter(name__icontains=ser)
        print(res)
        return render(request,'Admin/view_sation.html',{'data':res})


def delete_station(request,did):
    res = Station.objects.get(id=did).delete()
    return redirect('/view_station/')

def edit_station(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        ss=Division.objects.all()
        res = Station.objects.get(id=did)
        return render(request,'Admin/Edit_station.html',{'data':ss,'data1':res})

def edit_station_post(request):
    did = request.POST['id1']
    station = request.POST['textfield']
    contact = request.POST['textfield2']
    district = request.POST['textfield3']
    pin = request.POST['textfield4']
    place = request.POST['textfield5']
    dd = request.POST['select']
    obj = Station.objects.get(id=did)
    obj.name = station
    obj.phone = contact
    obj.district = district
    obj.place = place
    obj.pin = pin
    obj.DIVISION_id= dd
    obj.save()
    return HttpResponse('''<script>alert("Forest station updated");window.location="/view_station/";</script>''')


def animal(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
        ss=Category.objects.all()
        return render(request,'Admin/animal.html',{'data':ss})

def animal_post(request):
    name = request.POST['textfield']
    category = request.POST['select']
    description = request.POST['textarea']
    image = request.FILES['filefield']
    dd = Category.objects.get(id=category)
    obj = Animal()
    obj.name = name
    obj.CATEGORY = dd
    obj.description = description
    obj.image = image
    obj.save()
    return HttpResponse('''<script>alert("Animal details added");window.location="/view_animal/";</script>''')

def view_animal(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        res = Animal.objects.all()
        return render(request,'Admin/view_animal.html',{'data':res})
def search_animal(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        ser = request.POST['src']
        res = Animal.objects.filter(name__icontains=ser)
        return render(request, 'Admin/view_animal.html', {'data': res})

def edit_animal(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        ss = Category.objects.all()
        res = Animal.objects.get(id=did)
        return render(request,'Admin/animal - edit.html',{'data':res,'data1':ss})

def edit_animal_post(request):
    did = request.POST['id1']
    name = request.POST['textfield']
    category = request.POST['select']
    image = request.FILES['filefield']
    description = request.POST['textarea']
    dd = Category.objects.get(id=category)
    obj = Animal.objects.get(id=did)
    obj.name = name
    obj.CATEGORY = dd
    obj.image = image
    obj.description = description
    obj.save()
    return HttpResponse('''<script>alert("Animal details updated");window.location="/view_animal/";</script>''')

def delete_animal(request,did):
    res=Animal.objects.get(id=did).delete()
    return redirect('/view_animal/')

def category(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        return render(request,'Admin/category.html')

def category_post(request):
    name = request.POST['textfield']
    obj=Category()
    obj.category_name=name
    obj.save()
    return HttpResponse('''<script>alert("Category added");window.location="/view_category/";</script>''')

def view_category(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        res = Category.objects.all()
        return render(request,'Admin/view_category.html',{'data':res})
def search_category(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
        ser = request.POST['src']
        res = Category.objects.filter(category_name__icontains=ser)
        return render(request, 'Admin/view_category.html', {'data': res})

def edit_category(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
     res = Category.objects.get(id=did)
     return render(request,'Admin/editcategory.html',{'data':res})

def edit_category_post(request):
    did = request.POST['id1']
    categoryname = request.POST['textfield']
    obj=Category.objects.get(id=did)
    obj.category_name=categoryname
    obj.save()
    return HttpResponse('''<script>alert("Category updated");window.location="/view_category/";</script>''')

def delete_category(request,did):
    res=Category.objects.get(id=did).delete()
    return redirect('/view_category/')

def reserved(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login rquerd");window.location="/";</script>;''')

    else:
     res=Animal.objects.filter(pk=did).update(status='reserved')
     return HttpResponse('''<script>alert("Added as reserved");window.location="/view_receved/";</script>''')
def view_receved(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     res=Animal.objects.filter(status='reserved')
     return render(request,'Admin/reserved.html',{'data':res})
def search_reseved(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     ser= request.POST['src']
     pp=Animal.objects.filter(name__icontains=ser)
     return render(request,'Admin/reserved.html',{'data':pp})

def forest_officer(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     ss = Station.objects.all()
     return render(request,'Admin/officer.html',{'data':ss})

def forest_offecer_post(request):
    station = request.POST['select']
    s= Station.objects.get(id=station)
    name = request.POST['textfield2']
    email = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    age = request.POST['textfield4']
    phone = request.POST['textfield5']
    place = request.POST['textfield6']
    city = request.POST['textfield7']
    state = request.POST['textfield8']
    pin = request.POST['textfield9']
    passw = request.POST['textfield10']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fn = fs.save(date, photo)
    lob = Login()
    lob.username = email
    lob.password = passw
    lob.type = "officer"
    lob.save()
    obj = Forest_officer()
    obj.STATION=s
    obj.name=name
    obj.email=email
    obj.gender=gender
    obj.age=age
    obj.phone=phone
    obj.city=city
    obj.place=place
    obj.pin=pin
    obj.state=state
    obj.photo=fs.url(date)
    obj.LOGIN=lob
    obj.save()
    return HttpResponse('''<script>alert("Forest officer added");window.location="/view_officer/";</script>''')

def view_officer(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     res = Forest_officer.objects.all()
     return render(request,'Admin/view_officer.html',{'data':res})
def delete_officer(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     res=Forest_officer.objects.get(id=did).delete()
     return redirect('/view_officer/')

def search_officer(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')
    else:
     ser = request.POST['src']
     pp = Forest_officer.objects.filter(name__icontains=ser)
     return render(request,'Admin/view_officer.html',{'data':pp})

def edit_officer(request,did):
    ss=Station.objects.all()
    rs=Forest_officer.objects.get(id=did)
    return render(request,'Admin/edit_officer.html',{'data':ss,'data1':rs})
def edit_officer_post(request):
    did = request.POST['id1']
    station = request.POST['select']
    s = Station.objects.get(id=station)
    name = request.POST['textfield2']
    email = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    age = request.POST['textfield4']
    phone = request.POST['textfield5']
    place = request.POST['textfield6']
    city = request.POST['textfield7']
    state = request.POST['textfield8']
    pin = request.POST['textfield9']
    if 'photo' in request.FILES:
        photo = request.FILES['fileField']
        if photo != "":
            fs = FileSystemStorage()
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fn = fs.save(date, photo)
            obj = Forest_officer.objects.get(id=did)
            obj.STATION = s
            obj.name = name
            obj.email = email
            obj.gender = gender
            obj.age = age
            obj.phone = phone
            obj.city = city
            obj.place = place
            obj.pin = pin
            obj.state = state
            obj.photo = fs.url(date)
            obj.save()
    else:
        obj = Forest_officer.objects.get(id=did)
        obj.STATION = s
        obj.name = name
        obj.email = email
        obj.gender = gender
        obj.age = age
        obj.phone = phone
        obj.city = city
        obj.place = place
        obj.pin = pin
        obj.state = state
        obj.save()

    return HttpResponse('''<script>alert("Officer details updated");window.location="/view_officer/";</script>''')


def view_usercomplaint(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     res=Complaint.objects.filter(status="forwarded")

     return render(request,'Admin/View complaint.html',{'data':res})
def view_usercomplaint_search(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     f=request.POST["textfield"]
     t=request.POST["textfield2"]
     var=Complaint.objects.filter(status="forwarded", date__range=[f,t])
     return render(request, 'Admin/View complaint.html', {'data':var})
def send_reply(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login rquerd");window.location="/";</script>;''')

    else:
     res=Complaint.objects.get(id=did)
     return render(request,'Admin/Send reply.html',{'data':res})
def send_reply_post(request):
    did=request.POST['id1']
    val1=request.POST['textfield']
    obj=Complaint.objects.get(id=did)
    obj.status='replied'
    obj.reply=val1
    obj.save()
    return HttpResponse('''<script>alert("Reply sent");window.location="/view_usercomplaint/";</script>''')
def notification(request,did):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     res = Forest_officer.objects.get(id=did)
     return render(request,'Admin/notification.html',{'data':res})
def notification_post(request):
    # lid=Forest_officer.objects.get(LOGN=request.session['lid'])
    did = request.POST['id1']
    cont=request.POST['textfield']
    # od=request.POST['fid']


    obj=Notification()
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    obj.date = date
    obj.content=cont
    # obj.type='officer'
    obj.OFFICER_id= did

    obj.save()
    return HttpResponse('''<script>alert("Notification sent");window.location="/notification_v/";</script>''')
def notification_view(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     res= Notification.objects.all()
     return render(request,'Admin/view_notification.html',{'data':res})

def search_notification(request):
    f= request.POST['textfield']
    t= request.POST['textfield2']
    pp=Notification.objects.filter(date__range=[f,t])
    return render(request,'Admin/view_notification.html',{'data':pp})

# def allocation(request):
#     return render(request,'Admin/allocation.html')
# def view_allocation(request):
#     return render(request,'Admin/view_allocation.html')
# def edit_allocation(request):
#     return render(request,'Admin/allocation -Edit.html')
def admin_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
       return render(request,'Admin/template.html')
def logout(request):
    request.session['lid']=''
    return redirect('/')

def contact(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     return render(request,'Admin/contact.html')

def contact_post(request):
    name=request.POST['textfield']
    phone= request.POST['textfield2']
    email= request.POST['textfield3']
    place = request.POST['textfield4']
    obj=Contact()
    obj.name=name
    obj.phone=phone
    obj.email=email
    obj.place=place
    obj.save()
    return HttpResponse('''<script>alert("Contact added");window.location="/admin_home/";</script>''')


def admin_view_detections(request):
    res=Animal_notification.objects.all().order_by("-id")
    return render(request, "admin/view_detections.html", {"data":res})



import time, os, cv2, imutils, smtplib
import numpy as np
from pygame import mixer
import tensorflow as tf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from myapp.DBConnection import Db

CAM_LAT = "11.9213572"
CAM_LONG = "75.7903065"

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

def admin_add_video(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    else:
     return render(request,'Admin/video_interface.html')

def admin_add_video_post(request):
    action = request.POST.get('action')

    if action == "live":
        vid_path = 0
    else:
        if 'fileField' not in request.FILES:
            return HttpResponse('''<script>alert("Please select a file to upload."); window.location="/admin_add_video/";</script>''')
        vid = request.FILES['fileField']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".mp4"
        fs.save(date, vid)

        vid_path = r"C:\Users\Sabeeh\OneDrive\Desktop\Main Project\Early_warning\media\\" + date

    # Disable tensorflow compilation warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    vs = cv2.VideoCapture(vid_path)  # from live cam
    time.sleep(2.0)

    # Load the model
    # with tf.gfile.FastGFile("logs/output_graph.pb", 'rb') as f:
    with tf.gfile.FastGFile(MODEL_PATH, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        domestic_animals = {"cat", "cow", "dog", "porcupine", "fox"}
        # loop over the frames from the video stream
        while True:
            # grab the frame from the threaded video stream and resize it
            # to have a maximum width of 400 pixels
            ret, frame = vs.read()
            if not ret:
                print("[ERROR] Failed to read frame. Exiting...")
                break

            frame = imutils.resize(frame, width=400)
            # Prepare the blank white info panel
            height, width, _ = frame.shape
            info_panel = np.ones((100, width, 3), dtype=np.uint8) * 255
            text = ""
            color = (128, 128, 128)

            img_path = os.path.join(STATIC_PATH, "captured_image.jpg")
            cv2.imwrite(img_path, frame)

            image_data = tf.gfile.FastGFile(img_path, 'rb').read()
            label_lines = [line.rstrip() for line in tf.gfile.GFile(LABELS_PATH)]
            predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]

                if score * 100 > 80.0:
                    text = f"{human_string}: {score:.2f}%"
                    color = (0, 0, 0)  # Black text for valid detection
                    if human_string not in domestic_animals:
                        print(f"{human_string} detected (score = {score:.2f})")
                        play_buzzer(human_string)

                        try:
                            db = Db()
                            res = db.selectOne(
                                "SELECT TIMEDIFF(CURTIME(), TIME) as tm FROM `myapp_animal_notification` WHERE DATE=CURDATE() AND latitude='" + CAM_LAT + "' AND longitude='" + CAM_LONG + "' AND detected='" + human_string + "' order by id desc")

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

                    else:
                        print("Domestic Animal detected, no action taken.")


            cv2.putText(info_panel, text, (20, 65), cv2.FONT_HERSHEY_DUPLEX, 1.0, color, 2)
            combined = np.vstack((info_panel, frame))
            # show the output frame
            cv2.imshow("Detection", combined)
            cv2.setWindowProperty("Detection", cv2.WND_PROP_TOPMOST, 1)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break

    # do a bit of cleanup
    cv2.destroyAllWindows()

    return HttpResponse('''<script>window.location="/admin_add_video/";</script>''')
















#############       officer
def ohome(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("login required");window.location="/";</script>;''')

    return render(request, "officer/officer.home.html")
    # return render(request, "officer/ohome.html")

def officer_view_detections(request):
    res=Animal_notification.objects.all().order_by("-id")
    return render(request, "officer/view_detections.html", {"data":res})
def view_complaint(request):
    res=Complaint.objects.filter(status="pending")
    return render(request, "officer/view_complaint.html", {'data':res})

def view_complaint_search(request):
    fdate=request.POST['f']
    tdate=request.POST['t']
    res=Complaint.objects.filter(status="pending", date__range=[fdate, tdate])
    return render(request, "officer/view_complaint.html", {'data':res})

def forward(request, id):
    Complaint.objects.filter(id=id).update(status="forwarded")
    return HttpResponse('''<script>alert("Forwarded to admin");window.location="/view_complaint/";</script>;''')

def alert(request):
    return render(request, "officer/alert.html")

def alert_post(request):
    alr=request.POST['textfield3']
    obj=Alert()
    obj.OFFICER=Forest_officer.objects.get(LOGIN_id=request.session['lid'])
    obj.alert=alr
    obj.date=datetime.datetime.now().date()
    obj.save()
    return HttpResponse('''<script>alert("Alert sent");window.location="/alert/";</script>;''')

def view_alert(request):
    res=Alert.objects.filter(OFFICER__LOGIN_id=request.session['lid'])
    return render(request, "officer/view_alert.html", {'data':res})

def view_alert_search(request):
    f=request.POST['f']
    t=request.POST['t']
    res=Alert.objects.filter(OFFICER__LOGIN_id=request.session['lid'], date__range=[f,t])
    return render(request, "officer/view_alert.html", {'data':res})

def delete_alert(request, id):
    Alert.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("Alert deleted");window.location="/view_alert/";</script>;''')

def view_notification(request):
    res=Notification.objects.filter(OFFICER__LOGIN_id=request.session['lid']).order_by("-id")
    return render(request, "officer/view_notification.html", {'data':res})

def search_notification_view(request):
    f=request.POST['textfield']
    t=request.POST['textfield2']
    res=Notification.objects.filter(OFFICER__LOGIN_id=request.session['lid'], date__range=[f, t]).order_by("-id")
    return render(request, "officer/view_notification.html", {'data':res})



#####       android
def User_Registration(request):
    Name=request.POST['Name']
    Gender=request.POST['Gender']
    Email=request.POST['Email']
    Phone=request.POST['Phone']
    Place=request.POST['Place']
    City=request.POST['City']
    Pin=request.POST['Pin']
    Password=request.POST['Password']
    Img=request.POST['Img']
    res=Login.objects.filter(username=Email, password=Password)
    if res.exists():
        return JsonResponse({'status': "no"})
    else:
        timestr = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        a = base64.b64decode(Img)
        fh = open(r"C:\Users\Sabeeh\OneDrive\Desktop\Main Project\Early_warning\media\user\\" + timestr + ".jpg", "wb")
        path = "/media/user/" + timestr + ".jpg"
        fh.write(a)
        fh.close()

        obj=Login()
        obj.username=Email
        obj.password=Password
        obj.type="user"
        obj.save()

        obj2=User()
        obj2.LOGIN=obj
        obj2.name=Name
        obj2.gender=Gender
        obj2.email=Email
        obj2.phone=Phone
        obj2.place=Place
        obj2.city=City
        obj2.pin=Pin
        obj2.photo=path
        obj2.save()
        return JsonResponse({'status': "ok"})

def and_login(request):
    usr=request.POST['username']
    psw=request.POST['password']
    res=Login.objects.filter(username=usr, password=psw)
    if res.exists():
        res=res[0]
        if res.type == "user":
            return JsonResponse({'status':"ok", "lid":res.id})
        else:
            return JsonResponse({'status':"no"})
    else:
        return JsonResponse({'status': "invalid"})

def and_profile(request):
    lid=request.POST['lid']
    res=User.objects.get(LOGIN_id=lid)
    return JsonResponse({"status":"ok", "name":res.name, "email":res.email, "phone":res.phone, "gender":res.gender,
                         "place":res.place, "city":res.city, "pin":res.pin, "photo":res.photo})

def and_update_profile(request):

    lid=request.POST['lid']
    Name=request.POST['Name']
    Gender=request.POST['Gender']
    Email=request.POST['Email']
    Phone=request.POST['Phone']
    Place=request.POST['Place']
    City=request.POST['City']
    Pin=request.POST['Pin']
    Img=request.POST['Img']

    if Img!="":
        timestr = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        a = base64.b64decode(Img)
        fh = open(r"EC:\Users\Sabeeh\OneDrive\Desktop\Main Project\Early_warning\Early_warning\media\user\\" + timestr + ".jpg", "wb")
        path = "/media/user/" + timestr + ".jpg"
        fh.write(a)
        fh.close()
        obj2 = User.objects.get(LOGIN_id=lid)
        obj2.photo = path
        obj2.save()


    obj2 = User.objects.get(LOGIN_id=lid)
    obj2.name = Name
    obj2.gender = Gender
    obj2.email = Email
    obj2.phone = Phone
    obj2.place = Place
    obj2.city = City
    obj2.pin = Pin
    obj2.save()
    return JsonResponse({'status': "ok"})


def Search_Animals(request):
    nm=request.POST['search']
    res=Animal.objects.all()
    ar=[]
    for i in res:
        if nm == "":
            ar.append({
                "animal_name":i.name, "category":i.CATEGORY.category_name, "descr":i.description, "image":i.image
            })
        else:
            if nm.lower() in i.name.lower():
                ar.append({
                    "animal_name": i.name, "category": i.CATEGORY.category_name, "descr": i.description,
                    "image": i.image
                })
    print(ar)
    return JsonResponse({'status':"ok", "data":ar})

def and_contact(request):
    res=Contact.objects.all()
    ar = []
    for i in res:
        ar.append({
            "name": i.name, "phone": i.phone, "email": i.email, "place": i.place
        })
    print(ar)
    return JsonResponse({'status': "ok", "data": ar})

def and_view_reply(request):
    lid=request.POST['lid']
    res=Complaint.objects.filter(USER__LOGIN_id=lid)
    ar = []
    for i in res:
        ar.append({
            "complaint": i.complaint, "date": i.date, "reply": i.reply, "id": i.id
        })
    print(ar)
    return JsonResponse({'status': "ok", "data": ar})

def and_del_comp(request):
    cid=request.POST['cid']
    Complaint.objects.filter(id=cid).delete()
    return JsonResponse({"status":"ok"})

def and_send_complaint(request):
    lid=request.POST['lid']
    comp=request.POST['comp']
    obj=Complaint()
    obj.USER=User.objects.get(LOGIN_id=lid)
    obj.complaint=comp
    obj.reply="pending"
    obj.status="pending"
    obj.date=datetime.datetime.now().date()
    obj.save()
    return JsonResponse({'status': "ok"})


def and_view_alerts(request):
    res=Alert.objects.all().order_by("-id")
    ar = []
    for i in res:
        ar.append({
            "date": i.date, "alert": i.alert, "oname": i.OFFICER.name, "sname": i.OFFICER.STATION.name
        })
    print(ar)
    return JsonResponse({'status': "ok", "data": ar})

def and_view_divisions(request):
    res=Division.objects.all()
    ar = []
    for i in res:
        ar.append({
            "id": i.id, "division": i.division
        })
    print(ar)
    return JsonResponse({'status': "ok", "data": ar})

def and_view_stations(request):
    did=request.POST['did']
    res=Station.objects.filter(DIVISION_id=did)
    ar = []
    for i in res:
        ar.append({
            "id": i.id, "name": i.name, "phone":i.phone, "loc":i.district+"\n"+i.place+"\n"+i.pin
        })
    print(ar)
    return JsonResponse({'status': "ok", "data": ar})

def and_view_detections(request):
    res=Animal_notification.objects.all().order_by("-id")
    ar = []
    for i in res:
        ar.append({
            "id": i.id, "detected": i.detected, "content":i.content, "date":i.date, "time":i.time, "lati":i.latitude, "longi":i.longitude
        })
    print(ar)
    return JsonResponse({'status': "ok", "data": ar})

def getallnots(request):
    lastid=request.POST['lastid']
    res=Animal_notification.objects.all().order_by("-id")
    if res.exists():
        res2=res[0]
        if res2.id > int(lastid):
            return JsonResponse({"status":"ok", "id":res2.id, "data": res2.detected + " on " + str(res2.date) + " " + res2.time, "ln":len(res)})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status":"no"})

