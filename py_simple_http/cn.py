"""
author: Sunil K B

description:
Creating a python script which will bind to a port and listen for any HTTP GET request.
On receving http request, it will check the file name (usually html file) and send the contents of the file back
If the file is not found then a 404 NOT FOUND message is sent
If there are no file mentioned, then by default index.html file will be sent.

usage:
python3 cn.py
"""

from socket import *
import signal
import sys
import re

if __name__ == '__main__':

	# By default use 8000 port
	# If the port is not free, then we increment and check if next port is free
	# If more than 100 ports are also not free, then we quit the program
	server_port = 8000
	server_socket = ''
	connection_socket = ''
	print("")
	while server_port < 8110:
		print("Trying to setup server on localhost with port number {}\n".format(server_port))
		try:
			# Here we are creating TCP socket. SOCK_STREAM is TCP Socket
			# Once the socket is created we bind it to the port which we have got from previous step
			# In bind call, we are not specifying IP address this specifies that the socket is reachable
			# by any address the machine happens to have.
			server_socket = socket(AF_INET, SOCK_STREAM)
			server_socket.bind(('', server_port))
			# Next we call the listen which tells the socket library that we want it to queue
			# up as many as 5 connect requests before refusing outside connections.
			server_socket.listen(5)
		except:
			# We will reach this part, if the port if busy.
			# In this case, we will increment the port number and retry creating the socket
			if server_port < 8100:
				print("Selected Port is busy. Trying with another port..\n")
				server_port = server_port + 1
			else:
				print("--------------------------------------------------------------------------------------------\n\n")
				print("All ports are busy. Try again after sometime")
				print("--------------------------------------------------------------------------------------------\n\n")
				sys.exit(0)
		else:
			break

	print("--------------------------------------------------------------------------------------------")
	print("\tWeb Server is up in your machine. Copy-paste below URL on your browser\n")
	print("\t\thttp://localhost:{}/hello.html".format(server_port))
	print("\n\t\t\t\tor\n")
	print("\t\t\thttp://localhost:{}/".format(server_port))
	print("----------------------------------------------------------------------------------------\n\n")

	while True:
		# Now the socket is created and bind-ed successfully.
		print('Server running.. waiting for http request to arrive..')
		try:
			# Accept any incoming connection request from outside.
			connection_socket, addr = server_socket.accept()
			# Call recv which will read at most 1024 bytes
			#  This is a blocking call.
			message = connection_socket.recv(1024)
			# Here we print the message received which will be a HTTP GET request
			print("\n\nmessage is {}\n\n".format(message))
			# The GET request will have the filename mentioned whcih we are spitting and getting
			filename = message.split()[1]
			filename = filename.decode('UTF-8')
			print("File name is {}".format(filename))
			# In case no filename is given, we get / as filename
			# In such cases, we will send the content of index.html
			# index.html file in placed in the same directory
			if filename == '/':
				print("\n No Filename given. Routing to default page index.html \n")
				filename = '/index.html'
			f = open(filename[1:])
			outputdata = f.read()
			# Once the HTML file is read, encode it in binary stream and send it to the browser.
			# Use HTTP header and 200 code which is http code for success
			connection_socket.send('\nHTTP/1.1 200 OK\n\n'.encode())
			for i in range(0, len(outputdata)):
				connection_socket.send(outputdata[i].encode())
			connection_socket.close()
		except IOError:
			# If we are trying to fetch any other file, other than hello.html or index.html
			# then the file is not present and we will send a 404 Not Found message
			# 404 is HTTP code for resource not found
			print("\n File Not Found. Send 404 \n")
			connection_socket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
			connection_socket.close()
		except KeyboardInterrupt:
			# Keep running the program till we press control-c
			print("Key board interrupt. Close socket and exit")
			server_socket.close()
			sys.exit(0)
		except:
			pass
