#!/usr/bin/env python

##############################################
## Author: Parag Thakur (aka Virag)
## Follow: @_virag007
## Licence: MIT
## Copyright: Copyright 2020, Virag
## Title: JWT Encoder, Decoder & Brute-forcer
## About: CLI Tool
##############################################

import jwt
import base64
from colorama import Fore, Style
from pyfiglet import Figlet
import argparse
import json


wordlists = []

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

	parser.add_argument('-d', '--decode', nargs = 1,  help = 'Decode a JWT Token')
	parser.add_argument('--brute', action = 'store_true', help = 'Enable brute-force mode')
	parser.add_argument('-w', '--wordlist', type = argparse.FileType('r'), help = 'Specify a wordlist for brute-forcing')
	parser.add_argument('--version', action = 'version', version = '%(prog)s v1.0 (Beta)', help = 'Shows the version information and exit')
	args = parser.parse_args()
	return args

#Encoding a JWT Token
def encode(payload, secret, algo, header):
	payload = json.loads(payload)
	encoded_jwt = ''
	
	if(header != ''):
		try:
			header = json.loads(header)
			encoded_jwt = jwt.encode(payload, secret, algorithm=algo, headers=header).decode('utf-8')
		except:
			print('Wrong algorithm provided.')
	else:
		try:
			encoded_jwt = jwt.encode(payload, secret, algorithm=algo).decode('utf-8')
		except:
			print('Wrong algorithm provided.')
	
	return encoded_jwt


#Decoding a JWT Token
def decode(token):
	jwt_parts = token.split('.')
	jwt_parts.pop()
	jwt_data = []

	for base in jwt_parts:
		try:
			jwt_data.append(base64.b64decode(base).decode("utf-8"))
		except:
			try:
				base = base + '='
				jwt_data.append(base64.b64decode(base).decode("utf-8"))
			except:
				base = base + '=='
				jwt_data.append(base64.b64decode(base).decode("utf-8"))

	return jwt_data


#Brute-forcing a JWT Token to know about secret key
def brute_force():
	jwt_token = input('Enter the JWT Token: ')
	jwt_data = decode(jwt_token)
	
	for word in wordlists:
		encoded_jwt = encode(jwt_data[1], word, 'HS256', jwt_data[0])
		if(encoded_jwt != ''):
			if(encoded_jwt == jwt_token):
				print(Fore.RED)
				print('\033[1m' + 'Found Secret: ' + '\033[0m', end = '')
				print(Style.RESET_ALL, end = '')
				print(Fore.CYAN, end = '')
				print(word)
				print(Style.RESET_ALL)
				break

			else:
				flag = True
			
	if(flag == True):
		print('No key matches.')


#Display
def display(jwt_data):
	header = json.loads(jwt_data[0])
	payload = json.loads(jwt_data[1])
	print('Header:')
	print(json.dumps(header, indent = 4))
	print('\nPayload:')
	print(json.dumps(payload, indent = 4))


#Menu-driven program
def menu():
	global wordlists
	print('1. Encode JWT')
	print('2. Decode JWT')
	print('3. Brute-force the secret')
	print('4. Exit')

	try:
		choice = int(input('\nEnter your choice: '))

		if(choice == 1):
			algorithm = input('Algorithm: ').upper()
			payload = input('Payload {"key": "value"}: ')
			secret = input('Secret Key: ')
			print('Do you want to add headers (Yes/No): ', end = '')
			option = input()

			if(option.lower()[0] == 'y'):
				header = input('Header {"key": "value"}: ')
				token = encode(payload, secret, algorithm, header)
				if(token != ''):
					print('\nJWT Token: ' + token)
			elif(option.lower()[0] == 'n'):
				token = encode(payload, secret, algorithm, '')
				if(token != ''):
					print('\nJWT Token: ' + token)
			else:
				print('Enter yes or no only.')
			
		elif(choice == 2):
			jwt_token = input('\nEnter the JWT Token: ')
			display(decode(jwt_token))

		elif(choice == 3):
			wordlist_path = input('Enter the location of wordlist: ')
			f = open(wordlist_path, 'r')
			keys = f.read()
			f.close()

			keys = keys.split('\n')
			keys.pop()
			wordlists = keys
			brute_force()

		elif(choice == 4):
			print('\nExiting...\nGood Day')

		else:
			print('\nEnter right option.')

	except ValueError:
		print('\nEnter an integer value')
	except KeyboardInterrupt:
		print('\nForced Exit\nGood Day')


#Main function
def main():
	global wordlists
	args = usage()
	if(args.decode):
		display(decode(args.decode[0]))
		return

	elif(args.brute):
		if(args.wordlist):
			for word in args.wordlist:
				wordlists.append(word.strip('\n'))
			
			brute_force()
			return
		else:
			print('Insufficient wordlist.')
			return

	elif(args.wordlist):
		for word in args.wordlist:
			wordlists.append(word.strip('\n'))

		if(args.brute):
			brute_force()
			return
		else:
			print('Missing --brute option.')
			return

	banner()
	menu()

if __name__ == '__main__':
	main()