

#include <Bridge.h>
#include <HttpClient.h>

String server = "192.168.1.71";
String porta = "8888";
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
  
  url = "http://" + server + ":" + porta;

  Serial.println(url);

  client.get(url);
  delay(50);
}


