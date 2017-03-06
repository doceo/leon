#serverThread.py
import threading
import time
from serial import *
import socket
import sys

#conSerial serve a stabilire una connessione con arduino  

def conSerial():
	try:
		ardSerial = Serial('/dev/ttyACM0',9600)
		return 1
	except:
		return -1

def invia(comando):
	
	ardSerial.write(comando)
	risposta = ardSerial.readline()
	print risposta

#le funzioni seguenti riguardano la classe ServerThread


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
        server_address = ('localhost', 3332)
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
                    data = connection.recv(260)
                    comando = data[4:10]
                    print >> sys.stderr, 'received "%s"' % comando
                    print "blocco"
                    if (data):
                        #restituisce i dati ricevuti al client (come funzione di test)
                        print >>sys.stderr, 'messaggio acquisito'
                        #connection.sendall(data)
                        
                        #salvo la stringa nell'attributo di istanza
                        self.msg = comando
                    else:
                        print >>sys.stderr, 'nessuna stringa in coda', client_address
                        self.msg = -1;
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
			#print server.getValue()
			if(server.getValue() == -1):
				print askThread(server)

				
				server.stop()
				break
			else:
				#print server.getValue()
				server.stop()
				break
    
	server.stop()


