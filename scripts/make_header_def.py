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
	if(len(sys.argv)<5):
		print("Usage: <csv_file> <comma sep list of non-numeric col indices> <header_def_file> <pickle file>")
		exit(1)

	input_filename=sys.argv[1]
	non_numeric_list = sys.argv[2].split(',')
	non_numeric_indices = set(int(x) for x in non_numeric_list)
	fileoutname = sys.argv[3]
	picklefilename = sys.argv[4]

	file =  open(input_filename,"r")
	fileout = open(fileoutname,"w")
	headertokens = file.readline().rstrip().split(',')

	feature_dict={}
	print('nonnumeric',non_numeric_indices)
	for i,token in enumerate(headertokens):
		if i in non_numeric_indices:
			fileout.write("string\n")
			feature_dict[token] = tf.io.FixedLenFeature([],tf.string,default_value='')
		else:
			fileout.write("float\n")
			feature_dict[token] = tf.io.FixedLenFeature([],tf.float32,default_value=0.0)
	fileout.close()
	pickled_file=open(picklefilename,'wb')
	pickle.dump(feature_dict,pickled_file)
	pickled_file.close()

if __name__=="__main__":
	main()
