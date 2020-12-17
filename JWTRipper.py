import jwt
import base64

print('1. Encode JWT')
print('2. Decode JWT')
print('3. Brute-force the secret')
print('4. Exit')

choice = int(input('Enter your choice: '))

if(choice == 1):
	print('\nEnter JWT parts: ')
	#header = input('Header: ')
	#payload = input('Payload: ')
	#secret = input('Secret: ')
	wordlist = ['hacker', 'jwt', 'insecurity', 'pentesterlab', 'hacking']

	for word in wordlist:
		encoded_jwt = jwt.encode({"user": 'null'}, word, algorithm='HS256').decode('utf-8')
		print(encoded_jwt)

		if(encoded_jwt == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM'):
			print('Found Secret: ' + word)
			break

elif(choice == 2):
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

elif(choice == 3):
	print('\nSecret Brute-force')

elif(choice == 4):
	print('\nExiting...')

else:
	print('\nEnter right option.')