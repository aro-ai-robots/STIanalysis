#!/usr/bin/python
#ASU 2017
#
#    This is a script to split the STIDUMP files down to
#the STI values only. This will alow us to do a 'normal'
#distribution of the values for a given node. 
#

#Import the needed libraries
import sys
import csv
import os, time, shutil, stat, math
import matplotlib.pyplot as plt
import array

"""____________________________________________________________
__________________________Global Varibles______________________
___________________________________________________________ """
matlab_row_count = 0
matlab_collum_count = 0

uuid_array = []
sti_array = []
time_stamp_array = []

histograms_dir = '/home/roboroot8/STIanalysis/histograms'
histograms_file_path = 'histograms/sti_hist_exp_'

time_series_dir = '/home/roboroot8/STIanalysis/time_series'
time_series_file_path = '/home/roboroot8/STIanalysis/time_series/sti_time_sreies_exp_'

iit_path = '/home/roboroot8/STIanalysis/iit'
iit_file_path = '/home/roboroot8/STIanalysis/iit/iit_exp_'

#Declares the paths to the inputfile. It will takle user input, or input from shell scripts.
input_file_path = sys.argv[1]
input_file = open(input_file_path, "r")#It opens the input file
lines = csv.reader(input_file)#It prepares the reader

if not os.path.exists(histograms_dir):#If we can't find Hiistoigrams dir, lets make it
	os.makedirs(histograms_dir)
	print "Made a histogram directory"
else:#If we find it, lets tell the humans
	print "Found the histograms dir"
file_number = 1
noFileYet = True
while noFileYet:
	#See if the current file we are on, exists.
	if os.path.exists(histograms_file_path+str(file_number)+ '.sql'):
		#If it does, lets iterate, and try again
		file_number = file_number +1
	else:#Once we find a name that doesn't exist, make it.
		output_STI_file = open(histograms_file_path+str(file_number)+ '.sql', "w+")
		print ("Made file "+histograms_file_path+str(file_number)+ '.sql')
		noFileYet = False
		break # Lets break the loop.


""" ---------------------------------------------"""

if not os.path.exists(time_series_dir):#If we can't find time_series dir, lets make it
	os.makedirs(time_series_dir)
	print "Made a time series directory"
else:#If we find it, lets tell the humans
	print "Found the time series dir"
file_number = 1
noFileYet = True
while noFileYet:
	#See if the current file we are on, exists.
	if os.path.exists(time_series_file_path+str(file_number)+ '.sql'):
		#If it does, lets iterate, and try again
		file_number = file_number +1
	else:#Once we find a name that doesn't exist, make it.
		time_series_file = open(time_series_file_path+str(file_number)+ '.sql', "w+")
		print ("Made file "+time_series_file_path+str(file_number))
		noFileYet = False
		break#Lets break the loop.

if not os.path.exists(iit_path):#If we can't find iit dir, lets make it
	os.makedirs(iit_path)
	print "Made a iit directory"
else:#If we find it, lets tell the humans
	print "Found the iit dir"
file_number = 1
noFileYet = True
while noFileYet:
	#See if the current file we are on, exists.
	if os.path.exists(iit_file_path+str(file_number)+ '.sql'):
		#If it does, lets iterate, and tray again
		file_number = file_number +1
	else:#Once we find a name that doesn't exist, make it.
		iit_file = open(iit_file_path+str(file_number)+ '.sql', "w+")
		print ("Made file "+iit_file_path+str(file_number))
		noFileYet = False
		break#Lets break the loop.

#This funtion makes a uuid array. It hold a list of all of the uuid's,
#they are then used as varible names in other functions.
def make_uuid_array(uuid):
	found_array = False
	if not (len(uuid_array) == 0):# if ther eis nothing in the array, dont look
		for i in range( 0, len(uuid_array)): #lets see is the uuid is already in the array
			if (uuid == uuid_array[i]):
				found_array = True
		if not found_array: #If its not found in the array, lets append it
			uuid_array.append(str(uuid))
	else: uuid_array.append(uuid)

#This function takes each one of the uuid(s) and makes them into their own arrays. So uuid 12345...
#has an array named 12345...
def make_arrays():
	for i in range(0, len(uuid_array)):
		globals()[uuid_array[i]]=[]

#This is the function resposible for making the matrix, it never actually assembles a matrix. Its wierd.
#You have a uuid_array, which is like the row number. Each row has an array, but each have a differnt varible 
#name of the uuid
def compile_matrix(uuid, sti, indexer):
	global matlab_collum_count
	global matlab_row_count
	#If we have gone through the whole uuid list, then lets add another collum
	if  ((indexer//(len(uuid_array))) > matlab_collum_count ): 
		matlab_collum_count = (indexer//(len(uuid_array)))
	#This is a simple looping counter 0,1,2....23,24,0,1,2...
	if matlab_row_count == (len(uuid_array) - 1):
		matlab_row_count = 0
	else: #if the matlab_row_count isn't too big, lets add one
		matlab_row_count = matlab_row_count + 1
	#Once we know that our indexing varibles are correct, we will append the current sti to the matrix
	globals()[str(uuid_array[matlab_row_count])].append(sti)

#counts the input file
number_of_lines = 0
for line in input_file:#Read the file line by line
	#We need to skip the first line, its comments.
	if number_of_lines == 0:
		print "Initializing matlab matricies."
	else:#Split the current line into its components
		UUID,STI,TimeStamp = line.split(",")
		make_uuid_array(UUID)
	number_of_lines = number_of_lines + 1 #Iterate
make_arrays() #Make UUID arrays to hold all of the time series
#   Tell the humans how far we have gone
print "File opened properly, a total of " + str(number_of_lines)+" lines"			
					



""" ---------------------------------------------"""

#Splits the input file
input_file.seek(0) #This puts the csv reader to the begging of the file
number_of_lines = 0
sti_array = []
time_stamp_array = []
for line in input_file: #Read the file line by line
	#We need to skip the first line, its comments.
	if number_of_lines == 0:
		print "Started splittter"
	else:
		#Split the current line into its components
		UUID,STI,TimeStamp = line.split(",")
		#Write the info to the arrays
		sti_array.append(int(STI))
		time_stamp_array.append(int(TimeStamp))
		compile_matrix(UUID,STI, number_of_lines)
	number_of_lines = number_of_lines + 1 #Iterate
input_file.close() #Close the input file
#  Tell the humans how far we have gone
print "File split properly, a total of " + str(number_of_lines)+" lines"

""" ---------------------------------------------"""
#Time Series Analysis
#   This sets the intial time that the experiment started
exp_start_time = time_stamp_array[0]
#   Now we are goin to make everything in time since experiment started rather than time since epoch
for i in range (0, len(time_stamp_array)):
	time_stamp_array[i] = time_stamp_array[i] - exp_start_time
	time_series_file.write(str(sti_array[i]) +','+str(time_stamp_array[i]) +'\n')
time_series_file.close()


""" ---------------------------------------------"""
#Histogram analysis
#   Used to get the min and max
sti_array.sort()
#   Find the min and max
Min = 0
print Min
Max = sti_array[(len(sti_array)-1)] + 1
#Calculate the range, delta, and the # of bins
Range = Max - Min
BinCount = 100
Delta = Range/BinCount
#This will hold the first array of output
frequency = []
for i in range(0, BinCount):
	frequency.append(0)
#Now we will go throu the sti_array vector and sort it
for i in range(0,len(sti_array)):
	cur_num = sti_array[i]
	for j in range(0, BinCount):
		if((cur_num >= (Min + (j*Delta)) )& (cur_num < (Min + ((j+1)*Delta)))):
			frequency[j] = frequency[j] +1
		#print str((Min + j*Delta)) + str((Min + ((j+1)*Delta)))
		#print "Low = " + str((Min + (j*Delta))) + " High = " + str((Min + ((j+1)*Delta)))
#Now we will write to the file
for i in range (0, BinCount):
	output_STI_file.write(str(frequency[i]) +'\n')
#Close the file, we are done
output_STI_file.close()

""" ---------------------------------------------"""
#iit file writting	
for i in range(0, len(uuid_array)):
	for j in range(0, (matlab_collum_count-1)):
		#This goes through every sti and writes it to a csv file containg a matrix
		iit_file.write(str(globals()[str(uuid_array[i])][j])+ ',')
	iit_file.write('\n')
iit_file.close()



	
