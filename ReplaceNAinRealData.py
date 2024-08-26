import sys
import difflib



def readFile(fileName):
	
	fd = open(fileName, "r")
	fileList = fd.readlines()
	return fileList

def findReplacableValueAtSpecificIndex(similarStrList,index):

	for stri in similarStrList:
		stri=stri.strip().split(",")
		
		if stri[index] != "NA":
			return stri[index]


	return False


def replaceAllNaOfAString(str_index,str1,similarStrList):

	str1_list = str1.strip().split(",")

	na_indexs = [i for i,value in enumerate(str1_list) if value == "NA"]

	for index in na_indexs:

		new_value_at_index = findReplacableValueAtSpecificIndex(similarStrList, index)

		if new_value_at_index:
			str1_list[index] = new_value_at_index
		else:
			print(f"A good replacement for the NA value at [{str_index},{index}] was not found")

	new_str = ",".join(x for x in str1_list)
	new_str += "\n"

	return new_str

def replaceNaInDataSet(fileList):
	
	is_first = True
	for index,line in enumerate(fileList):
		print(index)
		if is_first:
			is_first = False
			continue

		fileList[index] = "temp_null"
		similarStrList = difflib.get_close_matches(line, fileList)
		fileList[index] = replaceAllNaOfAString(index,line,similarStrList)

	return fileList

def writeDataToFile(fileList,outputFileName):
	
	outputFileName=open(outputFileName,"w")
	for line in fileList:
		outputFileName.write(line)



if __name__ == '__main__':

	file_List=readFile(sys.argv[1])
	after_na_replacement_file_list=replaceNaInDataSet(file_List)
	writeDataToFile(after_na_replacement_file_list,sys.argv[2])
