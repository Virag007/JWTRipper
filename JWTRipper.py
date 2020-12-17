#!/usr/bin/env python

##############################################
## Author: Parag Thakur (aka Virag)
## Follow: @_virag007
## Licence: MIT
## Copyright: Copyright 2020, JWTRipper
## Title: JWT Encoder, Decoder & Brute-forcer
## About: CLI Tool
##############################################

import jwt
import base64
from colorama import Fore, Style
from pyfiglet import Figlet
import argparse

#Defining the banner
def banner():
	print(Fore.RED)
	print('\033[1m' + Figlet().renderText('JWTRipper') + '\033[0m')
	print(Style.RESET_ALL)


#Defining the usage help
def usage():
	parser = argparse.ArgumentParser(description = """Title: JWTRipper - JWT Encoder, Decoder & Brute-forcer
		\nAuthor: Parag Thakur (aka Virag)
		\nTwitter Handle: @_virag007
		\nDescription: A command line tool for encoding, decoding and brute-forcing JSON Web Token(JWT).""", formatter_class = argparse.RawTextHelpFormatter, usage = 'use "%(prog)s --help" for more information')

	parser.add_argument('-e', '--encode', action = 'store_true', help = 'Encode a JWT Token')
	parser.add_argument('-d', '--decode', action = 'store_true', help = 'Decode a JWT Token')
	parser.add_argument('-w', '--wordlist', action = 'store_true', help = 'Specify a wordlist for brute-forcing')
	parser.add_argument('--version', action = 'version', version = '%(prog)s v1.0 (Beta)', help = 'Shows the version information and exit')
	args = parser.parse_args()
	return args

#Encoding a JWT Token
def encode():
	print('Encoding in progress')
	print('\nEnter JWT parts: ')
	#header = input('Header: ')
	#payload = input('Payload: ')
	#secret = input('Secret: ')
	wordlist = ['hacker', 'jwt', 'insecurity', 'pentesterlab', 'hacking']

	for word in wordlist:
		encoded_jwt = jwt.encode({"user": null}, word, algorithm='HS256').decode('utf-8')
		print(encoded_jwt)

		if(encoded_jwt == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM'):
			print('Found Secret: ' + word)
			break


#Decoding a JWT Token
def decode():
	print('Decoding under progress')
	print('\nEnter the JWT Token: ')
	jwt_token = input()
	jwt_parts = jwt_token.split('.')
	jwt_parts.pop()

	for base in jwt_parts:
		try:
			print(base64.b64decode(base).decode("utf-8"))
		except:
			try:
				base = base + '='
				print(base64.b64decode(base).decode("utf-8"))
			except:
				base = base + '=='
				print(base64.b64decode(base).decode("utf-8"))


#Brute-forcing a JWT Token to know about secret key
def brute_force():
	print('Brute-forcing under progress')


#Menu-driven program
def menu():
	print('1. Encode JWT')
	print('2. Decode JWT')
	print('3. Brute-force the secret')
	print('4. Exit')

	try:
		choice = int(input('\nEnter your choice: '))

		if(choice == 1):
			encode()
			
		elif(choice == 2):
			decode()

		elif(choice == 3):
			brute_force()

		elif(choice == 4):
			print('\nExiting...\nGood Day')

		else:
			print('\nEnter right option.')

	except ValueError:
		print('Enter an Integer option.')


#Main function
def main():
	args = usage()
	if args.encode:
		print('Encode a JWT Token')
		return

	elif(args.decode):
		print('Decode a JWT Token')
		return
	elif(args.wordlist):
		print('Specify a wordlist')
		return

	banner()
	menu()

if __name__ == '__main__':
	main()