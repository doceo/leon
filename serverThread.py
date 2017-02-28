#serverThread.py 


import threading
import time

import socket
import sys


def startThread(serverThread):
    serverThread = ServerThread(1, "ServerThread")
    print "\n", serverThread.getName(), "Started",
    serverThread.start()
    return serverThread

def stopThread(a_thread):
    a_thread.stop()
    a_thread.join()
    print "\n", a_thread.getName(), "Stopped",

#funzione che permette di verificare se ci sono dati in ricezione

def askThread(a_thread):
    print "\n", a_thread.getName(), "current string is", a_thread.getValue(),


#classe ereditata da threading.Thread per la gestione del server in ascolto sulla porta 8888

class ServerThread(threading.Thread):
    def __init__(self, threadID, name, debug=False):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.alive = True
        self.debug = debug
        self.msg = 0

    def getName(self):
        return self.name

    def getValue(self):
        return self.msg

    def stop(self):
        self.alive = False

    def run(self):
                
			# Create a TCP/IP socket
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			# Bind the socket to the port
			server_address = ('192.168.1.71', 8888)
			print >>sys.stderr, 'starting up on %s port %s' % server_address
			sock.bind(server_address)

			# Listen for incoming connections
			sock.listen(1)
			
			while self.alive:
				time.sleep(1)
				if self.debug:
					print self.name, self.msg

		    		print >>sys.stderr, 'waiting for a connection'
    				connection, client_address = sock.accept()

    				try:
        				print >>sys.stderr, 'connection from', client_address

        				# Receive the data in small chunks and retransmit it
        				while True:
						data = connection.recv(16)
            					print >> sys.stderr, 'received "%s"' % data
            					if (data):
									#restituisce i dati ricevuti al client (come funzione di test)            					
											print >>sys.stderr, 'sending data back to the client'
											connection.sendall(data)
											
											#salvo la stringa nell'attributo di istanza											
											self.msg = data
            					else:
               						print >>sys.stderr, 'no more data from', client_address
               						break
            
    				finally:
        			# Clean up the connection
        				connection.close()


#il codice seguente parte solo in fase di test, quindi se l'interprete 
#lancia in modo autonomo questo file

if __name__=='__main__':
	
	server = startThread(None)
	
	
	while True:
			
		if(server.getValue()):
			print askThread(server)
			break
			
	server.stop()
			
	
