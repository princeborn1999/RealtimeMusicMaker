#include <SimpleDHT.h>
#include <Stepper.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
//set pin number 
const int sensorMin = 0;     // sensor minimum
const int sensorMax = 1024;  // sensor maximum
int pinDHT11 = 2;
int trigPin = 12;                  //Trig Pin
int echoPin = 13;                  //Echo Pin
long duration, cm, inches;
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE); 

const  int stepsPerRevolution = 2048;
SimpleDHT11 dht11(pinDHT11);

int on = 0;
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
void setup() {
  Serial.begin(9600);
  myStepper.setSpeed(5);
  pinMode(trigPin, OUTPUT);        //Define inputs and outputs 
  pinMode(echoPin, INPUT);
  Serial.begin(9600);  // 用於手動輸入文字
  lcd.begin(16, 2); 
  
  lcd.backlight(); // 開啟背光
  delay(250);
  lcd.noBacklight(); // 關閉背光
  delay(250);
  lcd.backlight();
  lcd.setCursor(0, 0); // 設定游標位置在第一行行首
  lcd.print("Hello, world!");
  delay(1000);
  lcd.setCursor(0, 1); // 設定游標位置在第二行行首
  lcd.print("AaronPrince");
  delay(1000);
  lcd.clear();

}
  
void loop() {

//SR04部分
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);     // 給 Trig 高電位，持續 10微秒
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT);             // 讀取 echo 的電位
  duration = pulseIn(echoPin, HIGH);   // 收到高電位時的時間
 
  cm = (duration/2) / 29.1;         // 將時間換算成距離 cm 或 inch  
  inches = (duration/2) / 74; 

  Serial.print(cm);Serial.print("cm");
  Serial.println();

//Raindrop
  int sensorReading = analogRead(A0);
    int range = map(sensorReading, sensorMin, sensorMax, 0, 3);
   
   // range value:
    switch (range) {
       case 0:    // Sensor getting wet
         Serial.print(range);Serial.println(" Rain Warning");
       break;
       case 1:    // Sensor drcasy 
          Serial.print(range);Serial.println(" drizzle");
       break;
       case 2:    // Sensor drcasy 
          Serial.print(range);Serial.println(" Not rain");
       break;
                     }

//溫溼度部分
  byte temperature = 0;
  byte humidity =0;
  int err = SimpleDHTErrSuccess;
 if ((err = dht11.read(&temperature, &humidity,NULL)) != SimpleDHTErrSuccess)
 {
  Serial.print("err=");Serial.println(err);delay(1000);
  return;
 }
 // Serial.print((int)temperature); Serial.print(" *C, "); 
  Serial.print((int)humidity); Serial.println(" H");

  if(((int)humidity) > 70)
    on=1;
   else if (int(humidity)<65)
    on = 0;
  if(on==1){
    myStepper.step(256);
  }
   delay(1500);
//LCD
  lcd.setCursor(0, 0); 
  lcd.print(cm); lcd.print("cm");//距離
  lcd.setCursor(7, 0);
  lcd.print(range); lcd.print("rain");//raindrop
  lcd.setCursor(0, 1); 
  lcd.print(humidity); lcd.print("humidity");//濕度
  delay(750);
  lcd.clear();


}
