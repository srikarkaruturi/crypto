#! /usr/bin/env python

#SK
#9/21/2019
#1.0

# Ask the user to encrypt with key or decrypt with key or brute force
#-----------------------------------------------------------------------------------------------------------------------------
# Encrypt a message with a key
#	- Ask the user for a input to encrypt
#	- Ask the user for a key, to shift the message
#-----------------------------------------------------------------------------------------------------------------------------
# Decrypt s message with a key
#	- Ask the user for a message to decode
#	- Ask the user to enter the key 
#		- If the user doesn't know the key, ask the user to brute force the input: Y or N
#-----------------------------------------------------------------------------------------------------------------------------
# Brute force the message to decrypt
#	- Ask the user to input a message to brute force	
#------------------------------------------------------------------------------------------------------------------------------

import argparse
import sys



#Ask the user to encrypt or decrpt or bruteforce
# -E: encrypt, -D: decrypt, -B: bruteforce
parser = argparse.ArgumentParser()
parser.add_argument('-E', '--Encrypt', action = 'store_true', help = 'Encrypt a message with a key')
parser.add_argument('-D', '--Decrypt', action = 'store_true', help = 'Decrypt a message with a key')
parser.add_argument('-B', '--Bruteforce', action = 'store_true', help = 'Brute-force a encrypted message')
args = parser.parse_args()

#All the characters that can be used in a message
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

translatedMessage = ""


if args.Encrypt:
	#Ask the user for a message to encrypt and store into a variable
	userMessage = input("\nEnter a message to encrypt: ")
	#Ask the user for a key and store it into a variable
	userKey = int(input("\nEnter a key to encrypt: "))
	
	for character in userMessage:
	
		if character in symbols:
			#Find the index of each character
			characterIndex = symbols.find(character)
			#Shift the index by the userKey
			translatedIndex = characterIndex + userKey
			#Shift the characters with the translatedIndex
			translatedMessage = translatedMessage + symbols[translatedIndex]
	print (translatedMessage)
	
elif args.Decrypt:
	#Ask the user to enter a message to decrypt
	userMessage = input("\nEnter a message to decrypt: ")
	#Ask the user to enter a key for decryption
	userKey = int(input("\nEnter a key to decrypt: "))
	
	for character in userMessage:
		if character in symbols:
			characterIndex = symbols.find(character)
			translatedIndex = characterIndex - userKey
			translatedMessage = translatedMessage + symbols[translatedIndex]
	print (translatedMessage)
	
elif args.Bruteforce:
	print ("\nBrute Force")
	
	


#Ask the user to enter a message to encrypt


