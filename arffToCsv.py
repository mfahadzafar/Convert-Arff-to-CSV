def getCSVFromArff(fileName):
	with open(fileName + '.arff', 'r') as fin:
		data = fin.read().splitlines(True)
	i = 0
	cols = []
	for line in data:
		line = line.lower()
		if ('@data' in line):
			i+= 1
			break
		else:
			#print line
			i+= 1
			if (line.startswith('@attribute')):
				if('{' in line):
					cols.append(line[11:line.index('{')-1])
				else:
					cols.append(line[11:line.index(' ', 11)])
	headers = ",".join(cols)
	with open(fileName + '.csv', 'w') as fout:
		fout.write(headers)
		fout.write('\n')
		fout.writelines(data[i:])

getCSVFromArff("test")				# enter filename here (without extension)