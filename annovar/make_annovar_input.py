#!/usr/bin/python3

import sys

def main():
	if(len(sys.argv)<2):
		print("Usage: make_annovar_input.py [coordinates_file] [pvalue file]")
		exit(1)
	filename_map = sys.argv[1]
	filename_pvalue = sys.argv[2]
		
	file_map = open(filename_map,'r')
	file_pval = open(filename_pvalue,'r')
	pvalues = {}
	
	for line in file_pval:
		tokens = line.rstrip().split('\t')
		if '_' in tokens[0]:
			key = tokens[0].split('_')[0]
		else:
			key = tokens[0]
		pvalues[key] = tokens[1]
	
	file_map.readline()
	for line in file_map:
		tokens = line.rstrip().split('\t')
		key = tokens[0]
		pvalue = '1.0'
		if key in pvalues:
			pvalue = pvalues[key]
		if 'snp' in filename_map:
			print(tokens[1]+'\t'+tokens[2]+'\t'+tokens[2]+'\t'+tokens[3]+'\t'+tokens[4]+'\tcomments: '+pvalue)
		elif 'cpg' in filename_map:
			# this is not a probe SNP and it has a position
			if tokens[3] == '\\N' and tokens[1] != '\\N':
				print(tokens[1]+'\t'+tokens[2]+'\t'+tokens[2]+'\t0\t0'+'\tcomments: '+pvalue)

	file_map.close()
	file_pval.close()
	

if __name__=="__main__":
	main()
