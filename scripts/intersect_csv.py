#!/usr/bin/python3

import sys

def main():
	if(len(sys.argv)<3):
		print("Usage: intersect_csv.py [comma sep list of files] [comma list of labels]")
		exit(1)
	filenames=sys.argv[1].split(',')
	labelnames=sys.argv[2].split(',')
	totalfiles=len(filenames)
	print("total files:",totalfiles)
	headercounts=dict()
	for filename in filenames:
		file=open(filename,'r')
		header=file.readline().rstrip()
		headertokens = header.split(',')
		for headertoken in headertokens:
			count = 0
			if headertoken in headercounts:
				count = headercounts[headertoken]
			count+=1
			headercounts[headertoken]=count
		file.close()
	#for k,v in headercounts.items():
		#print("counts",k,v)
	# now begin writing out
	for filename,label in zip(filenames,labelnames):
		print(filename)
		mask = []
		fileout=open(filename+'.new','w')
		file=open(filename,'r')
		header=file.readline().rstrip()
		headertokens = header.split(',')
		for headertoken in headertokens:
			if headercounts[headertoken]==totalfiles:
				mask.append(1)
			else:
				mask.append(0)
		fileout.write('label')
		for m,h in zip(mask,headertokens):
			#print('mask,header',m,h)
			if m==1:
				fileout.write(',')
				fileout.write(h)
		fileout.write('\n')
		linenum=0
		for line in file:
			line = line.rstrip()
			linetokens = line.split(',')
			fileout.write(label)
			for m,h in zip(mask,linetokens):
				#print('mask,header',m,h)
				if m==1:
					fileout.write(',')
					fileout.write(h)
			fileout.write('\n')
			linenum+=1
			print("line number written:",linenum)
		fileout.close()
		file.close()



		

if __name__=="__main__":
	main()
