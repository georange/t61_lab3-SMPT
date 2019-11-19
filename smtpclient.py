from socket import *
import sys

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.uvic.ca"
mailport = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver, mailport))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM: <mail@mail.com>\r\n')

recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('mail from 250 reply not received from server.')

# Send RCPT TO command and print server response. 
clientSocket.send('RCPT TO: <georgiam@uvic.ca>\r\n')

recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('rcpt to 250 reply not received from server.')


# Send DATA command and print server response. 
data = 'Data'
print(data)
clientSocket.send(data)

recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('data 250 reply not received from server.')

# Send message data.
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)

recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('end msg 250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'Quit\r\n'
print(quitCommand)
clientSocket.send(quitCommand)

recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('quit 250 reply not received from server.')

    pass

clientSocket.close()
sys.exit()
