import Augmentor
import os

try:
	for files in os.listdir('/home/sathvik/Documents/ML_concepts/recognition'):
		try:
			p= Augmentor.Pipeline('/home/sathvik/Documents/ML_concepts/recognition/%s' % files)
			p.ground_truth('home/sathvik/Documents/ML_concepts/recognition/%s/ground_truth' % files)
			p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
			p.flip_left_right(probability=0.5)
			p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
			#p.flip_top_bottom(probability=0.5)
			p.sample(20,multi_threaded=False)
		except NotADirectoryError:
			print("THIS IS AMERICA")
		except IndexError:
			print("Fuck this shit")
		except AttributeError:
			print('$#@')
except NotADirectoryError:
	print("THIS IS AMERICA")
except IndexError:
	print("Fuck this shit")
