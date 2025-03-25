import tensorflow as tf
import sys
import os


# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# image_path = sys.argv[1]
image_path=r"C:\Users\Sabeeh\OneDrive\Desktop\Screenshot 2025-03-13 231453.png"
# Read the image_data
def check(path):
    # image_data = tf.gfile.FastGFile("C:\\Users\\asus\\Pictures\\new topics\\images\\ceviche\\2591769.jpg", 'rb').read()
    image_data = tf.io.gfile.GFile(path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                       in tf.io.gfile.GFile(r"C:\Users\Sabeeh\OneDrive\Desktop\Main Project\Early_warning\myapp\static\logs\output_labels.txt")]

    # Unpersists graph from file
    with tf.compat.v1.gfile.FastGFile(r"C:\Users\Sabeeh\OneDrive\Desktop\Main Project\Early_warning\myapp\static\logs\output_graph.pb", 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.compat.v1.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        print(top_k)
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
    nid=top_k[0]
    print(label_lines[nid],predictions[0][nid])
    return label_lines[nid],predictions[0][nid]
check(image_path)