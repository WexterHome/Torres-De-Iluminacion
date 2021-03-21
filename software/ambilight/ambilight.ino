#include <FastLED.h>

#define NUM_LEDS_BASE 14
#define NUM_LEDS_TORRE 21
#define DATA_PIN_BASE 7   
#define DATA_PIN_TORRE 6
#define LED_TYPE WS2812B
#define COLOR_ORDER GRB
#define MAX_BRIGHTNESS 200


byte R[NUM_LEDS_TORRE];
byte G[NUM_LEDS_TORRE];
byte B[NUM_LEDS_TORRE];
char recv[1];


CRGB leds_base[NUM_LEDS_BASE];
CRGB leds_torre[NUM_LEDS_TORRE];


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //Serial.setTimeout(5);
  //G[0] = 255;
  FastLED.addLeds<LED_TYPE, DATA_PIN_BASE, COLOR_ORDER>(leds_base, NUM_LEDS_BASE);
  FastLED.addLeds<LED_TYPE, DATA_PIN_TORRE, COLOR_ORDER>(leds_torre, NUM_LEDS_TORRE);
  FastLED.setBrightness(MAX_BRIGHTNESS);


  for(int dot = 0; dot < NUM_LEDS_TORRE; dot++) { 
      leds_torre[dot].setRGB(255,0,0);
      FastLED.show();
      delay(10);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    //Serial.readBytes(recv, 1);
    if(Serial.read()== 'w'){
      for(int i = NUM_LEDS_TORRE - 1; i>=0; i--){
        
        while(!Serial.available());
        String r = Serial.readStringUntil('a');
        //r.remove(r.length()-2);
        int R = r.toInt();
        
        while(!Serial.available());
        String g = Serial.readStringUntil('a');
        //g.remove(g.length()-2);
        int G = g.toInt();
        
        while(!Serial.available());
        String b = Serial.readStringUntil('a');
        //b.remove(b.length()-2);
        int B = b.toInt();
        
        leds_torre[i].r = R;
        leds_torre[i].g = G;
        leds_torre[i].b = B;
        
        //FastLED.show();
        
      }
      //FastLED.show();
      
      for(int i = NUM_LEDS_BASE - 1; i>=0; i--){
        
        while(!Serial.available());
        String r = Serial.readStringUntil('a');
        //r.remove(r.length()-2);
        int R = r.toInt();
        
        while(!Serial.available());
        String g = Serial.readStringUntil('a');
        //g.remove(g.length()-2);
        int G = g.toInt();
        
        while(!Serial.available());
        String b = Serial.readStringUntil('a');
        //b.remove(b.length()-2);
        int B = b.toInt();
        
        leds_base[i].r = R;
        leds_base[i].g = G;
        leds_base[i].b = B;
        
        //FastLED.show();
        
      }
      FastLED.show();
    }   
  }
}

/*
while(!Serial.available());
String r = Serial.readString();
int R = r.toInt();

while(!Serial.available());
String g = Serial.readString();
int G = g.toInt();

while(!Serial.available());
String b = Serial.readString();
int B = b.toInt();

leds[i].r = R;
leds[i].g = G;
leds[i].b = B;

FastLED.show();
*/
