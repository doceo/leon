
String acq(int x, int y, int tic){
    
  int asseX, asseY, clic;
  String richiesta;
  
  asseX = map(analogRead(x), 0, 996, 0, 9);
  asseY = map(analogRead(y), 0, 996, 0, 9);
  clic = analogRead(tic);

  if (clic>1){
    clic=1;
  }

  richiesta = String(asseX) + "/" + asseY + "/" + clic;
  return richiesta;
  
}

