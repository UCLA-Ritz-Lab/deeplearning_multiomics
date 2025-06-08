#!/home/garyc/anaconda3/envs/peg/bin/python
import pickle
import tensorflow as tf

import sys

def add_to_set(filename,the_set):
	file=open(filename,'r')
	tokens=file.readline().rstrip().split(',')
	for token in tokens:
		the_set.add(token)
	file.close()
		

def main():
	if(len(sys.argv)<6):
		print("Usage: <string headers> <int headers> <float headers> <infile> <outfile>")
		exit(1)

	string_filename=sys.argv[1]
	int_filename=sys.argv[2]
	float_filename=sys.argv[3]
	input_filename=sys.argv[4]
	output_filename=sys.argv[5]

	print("Reading input",input_filename," referencing ",int_filename,float_filename,string_filename)

	ints=set()
	strings=set()
	floats=set()
	add_to_set(int_filename,ints)
	add_to_set(float_filename,floats)
	add_to_set(string_filename,strings)
	

	file =  open(input_filename,"r")
	tokens = file.readline().rstrip().split(',')
	print("Writing to ",output_filename)
	fileout=open(output_filename,'w')

	feature_dict = {}
	for token in tokens:
		if token in floats:
			fileout.write('float\n')
			feature_dict[token] = tf.io.FixedLenFeature([],tf.float32,default_value=0.0)
		elif token in ints:
			fileout.write('int\n')
			feature_dict[token] = tf.io.FixedLenFeature([],tf.int64,default_value=0)
		elif token in strings:
			fileout.write('string\n')
			feature_dict[token] = tf.io.FixedLenFeature([],tf.string,default_value='')
		else:
			fileout.write('string\n')
			feature_dict[token] = tf.io.FixedLenFeature([],tf.string,default_value='')
	fileout.close()
	pickled_file=open('feature_dict.pkl','wb')
	pickle.dump(feature_dict,pickled_file)
	pickled_file.close()
if __name__=="__main__":
	main()
