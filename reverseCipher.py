#! /usr/bin/env python

#Reverse Cipher
#Cracking Codes with Python
#SK



#Ask the user to input a string to reverse.
userInput = input("\nInput a String: ")

#Variable to hold the translated input.
translatedInput = ""

#Find the len of the user input
i = len(userInput) - 1

#While loop to reverse the input
while i >= 0:
	translatedInput = translatedInput + userInput[i]
	i = i - 1
	
print ("\nTranslated Input is: " + translatedInput)