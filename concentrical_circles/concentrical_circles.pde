void setup() {
  size(600, 600);
  stroke(255);
  strokeWeight(2);
  //noLoop();
}
int m1 = 6;
int m2 = 3;
float r1 = 250;
float r2 = 150;
float t1 = 0;
float t2 = 0;
float r = 10;
void draw() {
  background(0);
  translate(width/2, height/2);
  //r2 = 100*abs(sin(t1-t2))+150; 
  //r2 = 250*noise(t1,t2); 
  for (int j=0; j < m2; j++) {
    float angle2 = TWO_PI/m2;
    float x2 = r2 * cos(angle2 *j - t2);
    float y2 = r2 * sin(angle2 *j - t2);

    for (int i=0; i < m1; i++) {
      float angle1 = TWO_PI/m1;
      float x1 = r1 * cos(angle1 *i + TWO_PI / m1 / 2 );
      float y1 = r1 * sin(angle1 *i + TWO_PI / m1 / 2 );
      float z1 = r1 * cos(angle1 *(i+1) + TWO_PI / m1 / 2 );
      float w1 = r1 * sin(angle1 *(i+1) + TWO_PI / m1 / 2 );
      float z = map(fract(t1), 0, 1, x1, z1);
      float w = map(fract(t1), 0, 1, y1, w1);
      stroke(255);
      line(z, w, x2, y2);
      fill(255, 0, 0);
      noStroke();
      ellipse(z, w, r, r);
    }
    fill(0, 255, 0);
    noStroke();
    ellipse(x2, y2, r, r);
  }
  t1+=0.005;
  //t2+=0.013;
  println(frameRate);
  if (t1 < 1)
    saveFrame("frame###.png");
}


float fract(float x) {
  return x - ceil(x-1);
}
