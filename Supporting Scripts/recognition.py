import tensorflow as tf,sys

image_path = sys.argv[1]

#read in the image data
image_data = tf.gfile.FastGFile(image_path,'rb').read()

#Lods label file, strips off carriage return
label_lines = [line.strip() for line in tf.gfile.Gfile("labels_file.txt")]

#unpersists graph from file

with tf.gfile.FastGFile("retrained.pb",'rb') as f:
	graph_def=tf.GraphDef()
	graph_def.ParseFromString(f.read())
	_=tf.import_graph_def(graph_def,name='')

with tf.session() as sess:
	#Feed the image_data as input to the graph and get first prediction
	softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

	predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0':image_data})

	#sort to show labels of first prediction in order of confidence
	top_k = predictions[0].argsort()[-len(predictions[0]):] [::-1]

	for node_id in top_k:
		human_string = label_lines[node_id]
		score=predictions[0][node_id]
		print('%s (score=%.5f)' % (human_string, score)) 