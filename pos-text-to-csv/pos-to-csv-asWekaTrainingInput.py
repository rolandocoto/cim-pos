import os
import sys

def cleanLine(line):

	line = line.lower();

	line = line.replace("\r", "")
	line = line.replace("\n", "")
	line = line.replace("'", "q")
	line = line.replace(",", ";")
	line = line.replace("\"", "quot")
	

	line = line.replace("ā", "ax")
	line = line.replace("ē", "ex")
	line = line.replace("ī", "ix")
	line = line.replace("ō", "ox")
	line = line.replace("ū", "ux")

	

	return line

if __name__ == "__main__":


	inFilePath = os.path.join("",sys.argv[1])
	input = open(inFilePath, encoding='utf-8').readlines()
	posDivider = "|"

	title = "prePrePreToken,prePreToken,preToken,token,tokenPOS,postToken\r\n"
	output = ""

	preToken = ""
	prePreToken = ""
	postToken = ""
	token = ""
	tokenPOS = ""


	for line in input:

		line = cleanLine(line)

		words = line.split(" ")

		for i in range(0,len(words)):

			if (i==0):
				
				preToken = "-"
				prePreToken = "-"
				prePrePreToken = "-"

			elif (i==1): 
				
				prePrePreToken = "-"
				prePreToken = "-"
				preToken = words[i-1].split(posDivider)[0]

			elif (i==2):
				
				prePrePreToken = "-"
				prePreToken = words[i-1].split(posDivider)[0]
				preToken = words[i-2].split(posDivider)[0]
			
			else:

				preToken = words[i-1].split(posDivider)[0]
				prePreToken = words[i-2].split(posDivider)[0]
				prePrePreToken = words[i-3].split(posDivider)[0]


			#print(i)
			#print(line)
			#print(token)
			if ("|" not in words[i]):
				print(line)
				print(words[i])
			token = words[i].split(posDivider)[0]
			#print(token)
			tokenPOS = words[i].split(posDivider)[1]


			if (i == len(words)-1):

				#print("último: " + words[i])
				postToken = "-"

			else:

				postToken = words[i+1].split(posDivider)[0]


			output = output + prePrePreToken + "," + prePreToken + "," + preToken + "," + token + "," + tokenPOS + "," + postToken + "\r\n"


	output = title + output
	open("weka-pos-training-set.csv", "wb").write((output.encode('utf-8','replace')))


	#for word in words:

	#	print(word)

	#	token = word.split("|")
	#	print(token[0])
