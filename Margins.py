import sys

#The input data contains the text file and two integers (inches) specifying the left and right margins

FileName = input("Enter the name of the text File: ")
#Test case that makes sure that the extension of the file is .txt
ext = str(FileName.split(".")[1])
if(ext != "txt"):
  print("The Program only accepts text (.txt) files.")
  sys.exit()

LeftMargin = int(input("Size of Left Margin: "))
RightMargin = int(input("Size of Right Margin: "))
print("\n")

#Test Case to make sure that the specified margins are not negative 
if(LeftMargin < 0):
  print("Cannot Process, Margins have to be positive integers.")
  sys.exit()
if(RightMargin < 0):
  print("Cannot Process, Margins have to be positive integers.")
  sys.exit()

#Opens text file to read contents and then stores in Output with specified margins
FileInput = open(FileName, "r")
#Test case to see if the file is readable or ultimately does it exist
if FileInput.readable() == False:
  print("File is not readable.")
  print("Check if file exists.")
  sys.exit()

FileOutput = open("DAT1.TXT", "w+")

#Contents are stored as a string and then split according to range of margins
contents = FileInput.read()
splitting = contents.split()

#holds the left margin 
leftstring = " "
#current line that is being written
currentline = " "
#word(s) that will start on the next line
leftover = " "

for i in range(LeftMargin):
  for j in range(12):
    leftstring += " "
leftstring = leftstring[:-1] 

#Prints 0-9 8 times to show 80 characters 
eightychar = "01234567890123456789012345678901234567890123456789012345678901234567890123456789" 
FileOutput.write(eightychar)
FileOutput.write("\n")

for word in range(len(splitting)):
  if(word == 0):
    FileOutput.write(leftstring)

  if(len(leftstring) + len(currentline) + 1 + len(splitting[word])) > (80 - (RightMargin * 12)):
    FileOutput.write("\n")
    FileOutput.write(leftstring)
    currentline = " "
    
#Finding where the punctuation is so there will be 2 blanks between the sentences
  if (splitting[word].find(".") != -1 or splitting[word].find("?") != -1 or splitting[word].find("!") != -1):
    leftover = " " + splitting[word] + " " 
  else:
    leftover = " " + splitting[word]

  currentline += leftover
  FileOutput.write(leftover)
FileOutput.close()

print(open("DAT1.TXT","r").read()) 