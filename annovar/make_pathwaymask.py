#!/home/garyc/anaconda3/bin/python

import sys
import numpy as np
import pickle

def main():
	if len(sys.argv)<4:
		print("Usage: [pathwaydef] [genelist] ")
		exit(1)

	filename_pathwaydef = sys.argv[1]
	filename_genelist = sys.argv[2]
	filename_maskout = sys.argv[3]

	# load header of the large input data 

	file = open(filename_pathwaydef,'r')
	file.readline()
	col_by_pathway = {}
	col_by_pathway['none'] = 0
	pathwaycount = 1
	pathways_by_gene = {}
	for line in file:
		tokens = line.rstrip().split('\t')
		pathway = tokens[0]
		col_by_pathway[pathway] = pathwaycount
		pathwaycount+=1
		genes = tokens[3].split(',')
		#print(pathway,genes)
		for gene in genes:
			pathwaylist = []
			if gene in pathways_by_gene:
				#print("fetched existing pathwaylist")
				pathwaylist = pathways_by_gene[gene]
			pathwaylist.append(pathway)
			#print("adding pathway",pathway,"for gene",gene)
			pathways_by_gene[gene] = pathwaylist
	file.close()
		
	for gene in pathways_by_gene:
		#print("gene:",gene)
		pathwaylist = pathways_by_gene[gene]
		#for pathway in pathwaylist:
			#print(" pathway:",pathway)
		
	for pathway in col_by_pathway:
		col = col_by_pathway[pathway]
		#print('pathway:',pathway,', col:',col)

	mask = np.zeros((len(pathways_by_gene),pathwaycount),dtype='float32')
	file = open(filename_genelist,'r')
	row = 0
	for line in file:
		gene = line.rstrip()
		mask[row,0] = 1.0
		if gene in pathways_by_gene:
			pathwaylist = pathways_by_gene[gene]
			for pathway in pathwaylist:
				if pathway in col_by_pathway:
					col = col_by_pathway[pathway]
					mask[row,col] = 1.0
					#print("setting at",row,col)
		row+=1
	
	file.close()
	file = open(filename_maskout+'.txt','w')
	for row in range(mask.shape[0]):
		for col,val in zip(range(mask.shape[1]),mask[row]):
			if col>0:
				file.write("\t")
			file.write(str(val))
		file.write('\n')
	file.close()
	
	
if __name__=='__main__':
	main() 

