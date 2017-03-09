import os, filecmp
def comple(file,lang):
    if (os.path.isfile(file)):
        os.system('c++ '+file)
        os.remove(file)

def run():
    cmd = './a.out'
    r = os.system('./a.out')

def filechecker(path):
	file1 = open(path + "/AO1.txt", 'r')
	file2 = open(path + "/AO1.txt", 'r')
	str1=""
	str2=""
	for line1 in file1:
		str1+=line1
	for line1 in file2:
		str2+=line1

	if(str1==str2):
		return True
	else:
		return False
	file1.close()
	file2.close()

file = 'UserCode.cpp'
testout = 'testout.txt'
timeout = '1' # secs

  # True implies that code is accepted.
