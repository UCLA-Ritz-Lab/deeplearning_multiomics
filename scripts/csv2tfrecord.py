#!/home/garyc/anaconda3/envs/peg/bin/python

import sys
import tensorflow as tf

def main():
	if(len(sys.argv)<4):
		print("Usage: csv2tfrecord.py [csv_file] [header types def file(one type per line)] [tfrecord outputfile]")
		exit(1)

	csv_file=sys.argv[1]
	types_file=sys.argv[2]
	tfrecord_filename=sys.argv[3]
	print("Reading csv ",csv_file,". Using types file ",types_file)
	types=[]
	file =  open(types_file,"r")
	for line in file:
		types.append(line.rstrip())
	file.close()
	writer = tf.io.TFRecordWriter(tfrecord_filename) 
	file =  open(csv_file,"r")
	header_tokens = file.readline().rstrip().split(",")
	header_types = {}
	for type,header_token in zip(types,header_tokens):
		header_types[header_token] = type
		#print("header ",header_token," is ",type)
	counter = 0
	for line in file:
		line_tokens = line.rstrip().split(',')
		feature_dic={}
		for header_token,type,token in zip(header_tokens,types,line_tokens):
			if type == 'string':
				feature=tf.train.Feature(bytes_list=tf.train.BytesList(value=[token.encode('utf-8')]))
			elif type == 'int':
				try:
					i=int(token)
				except ValueError:
					i=0
				feature=tf.train.Feature(int64_list=tf.train.Int64List(value=[i]))
			elif type == 'float':
				try:
					i=float(token)
				except ValueError:
					i=0.0
				feature=tf.train.Feature(float_list=tf.train.FloatList(value=[i]))
			else:
				feature=tf.train.Feature(bytes_list=tf.train.BytesList(value=[token.encode('utf-8')]))
				print("Warning type not found")
			feature_dic[header_token] = feature
		tf_example = tf.train.Example(features=tf.train.Features(feature=feature_dic))
		writer.write(tf_example.SerializeToString())
		counter+=1
		print("Lines written:",counter)

	writer.close()
	file.close()
if __name__=="__main__":
	main()
