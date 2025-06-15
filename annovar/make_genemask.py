#!/home/garyc/anaconda3/bin/python

import sys
import numpy as np
import pickle

def main():
	if len(sys.argv)<9:
		print("Usage:  [annovar_output] [featureinfo] [pvalues] [pvalue_threshold] [outfiles mask] [outfiles row_label] [outfiles col_label] [tfrecord header]")

		exit(1)
	filename_annovarout = sys.argv[1]
	filename_featureinfo = sys.argv[2]
	filename_pvalues = sys.argv[3]
	pvalue_threshold = float(sys.argv[4])
	filename_maskout = sys.argv[5]
	filename_rowsout = sys.argv[6]
	filename_colsout = sys.argv[7]
	filename_header = sys.argv[8]

	# load header of the large input data 

	file = open(filename_header,'r')
	headertokens = file.readline().rstrip().split(',')
	headerset = set(headertokens)
	print("There are ",str(len(headerset)),"features in the tfrecordset")
	file.close()

	# load pvalue map
	# only consider things with that are in the tfrecord
	# data set and are under a pvalue threshold

	old_key_dict = {}
	file = open(filename_pvalues,'r')
	for line in file:
		linetokens = line.rstrip().split('\t')
		old_key = linetokens[0]
		if '_' in old_key:
			key = old_key.split('_')[0]
		else:
			key = old_key
		pvalue = float(linetokens[1])
		if old_key in headerset and pvalue < pvalue_threshold:
			#print("Adding oldkey",old_key," with key ",key)
			old_key_dict[key] = old_key
	file.close()
	print("There are ",str(len(old_key_dict)),"features in the pvalue data")
	# annotate featureinfo with pvalues

	file = open(filename_featureinfo,'r')
	file.readline()
	snp_dict = {}
	for line in file:
		linetokens = line.rstrip().split('\t')
		key = linetokens[0]
		if key in old_key_dict:
			oldkey = old_key_dict[key]
			pos = linetokens[1]+'-'+linetokens[2]
			#print("Adding old key",oldkey," to snpdict at pos",pos)
			snp_dict[pos] = oldkey
	file.close()
	print("There are ",str(len(snp_dict)),"features in the snp_dict")

	file = open(filename_annovarout,'r')
	file.readline()
	annotations = {}
	rowlist = []
	collist = []
	# first pass to get matrix columns
	rows = 0
	# add dummy gene
	collist.append('none')
	annot_counter = 1
	for line in file:
		linetokens = line.rstrip().split('\t')
		position = linetokens[0]+'-'+linetokens[1]
		if position in snp_dict:
			function = linetokens[5]
			genes = linetokens[6].split(',')
			#print(position,function,genes)
			genes.append(function)
			for gene in genes:
				if gene not in annotations:
					annotations[gene] = annot_counter
					#print("Adding annotation",gene)
					annot_counter+=1
					collist.append(gene)
			#print("snp at ",position,"is",snp_dict[position])
			rowlist.append(snp_dict[position])
			rows+=1
	file.close()

	# second pass to make the matrix
	print("The number of annotations is ",annot_counter)
	print("Creating mask of ",rows," by ",annot_counter,"cols")
	mask = np.zeros((rows,annot_counter),dtype='float32')
	file = open(filename_annovarout,'r')
	file.readline()
	row = 0
	for line in file:
		linetokens = line.rstrip().split('\t')
		position = linetokens[0]+'-'+linetokens[1]
		if position in snp_dict:
			function = linetokens[5]
			genes = linetokens[6].split(',')
			#print(position,function,genes)
			genes.append(function)
			# dummy gene
			mask[row,0] = 1.0	
			for gene in genes:
				col = annotations[gene]
				mask[row,col] = 1.0	
			row+=1
	file.close()
	file = open(filename_maskout+'.pkl','wb')
	pickle.dump(mask,file)
	file.close()	
	file = open(filename_maskout+'.txt','w')
	for row in range(mask.shape[0]):
		for col,val in zip(range(mask.shape[1]),mask[row]):
			if col>0:
				file.write("\t")
			file.write(str(val))
		file.write('\n')
	file.close()	
	file = open(filename_rowsout+'.pkl','wb')
	pickle.dump(rowlist,file)
	file.close()	
	file = open(filename_rowsout+'.txt','w')
	for val in rowlist:
		file.write(val+'\n')
	file.close()
	file = open(filename_colsout+'.pkl','wb')
	pickle.dump(collist,file)
	file.close()	
	file = open(filename_colsout+'.txt','w')
	for val in collist:
		file.write(val+'\n')
	file.close()

if __name__=='__main__':
	main()
