
import random

chars = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,./;'[]!@#$%^&*()_+~\|:"<>?'''  // All the characters 
times = int(input('[.]Number of passwords?\n[.]'))  // No of times
length = int(input('[.]Password length?\n[.]'))  // length

f = open('password.txt','w')

for i in range(times):
	password = ''
	for j in range(length):
		password += random.choice(chars)

	print('[.]',password,sep='')
	
	
	password = password + '\n'
	f.write(password)

f.close()
<<<<<<< HEAD
#jdkslwmlmjdosjdjj;dl
=======
#jdkslwmlmk

tarun 
ankit
>>>>>>> a03449b71b782b2a670bba93e13f2a15e67776b3
