

#include <Bridge.h>
#include <HttpClient.h>


String server = "192.168.1.97";
String porta = "3333";
String url;

int X = 10;    
int Y = 9;     
int tap = 8;  

String parametri;

void setup() {

  pinMode(tap, INPUT);
  pinMode(X, INPUT);
  pinMode(Y, INPUT);
  
  Serial.begin(9600);

  while (!Serial); // wait for a serial connection
}

void loop() {
  // Initialize the client library
  HttpClient client;

  // Make a HTTP request:

  parametri = acq(X, Y, tap);
  
  url = "GET http://" + server + ":" + porta + "/" + parametri + " HTTP/1.1\n";
  url = url + "Host: "+ server + ":" + porta + "\n" + "Connection: close";

  client.get(url);
  Serial.println(url);

  delay(3000);
}


