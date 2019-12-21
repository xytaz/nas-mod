// ------------------- Example for LCD ------------------- //

///* Arduino Tutorial: Learn how to use an LCD 16x2 screen
//   More info: http://www.ardumotive.com/how-to-use-an-lcd-dislpay-en.html  */
//
////Include LCD library
//#include <LiquidCrystal.h>
//
//// initialize the library with the numbers of the interface pins
//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
//
//
//void setup() {
//  // set up the LCD's number of columns and rows: 
//  lcd.begin(16, 2);
//  // Print a message to the LCD.
//  lcd.print("Hello, World!");
//}
//
//void loop() {
//  // set the cursor to column 0, line 1
//  // (note: line 1 is the second row, since counting begins with 0):
//  lcd.setCursor(0, 1);
//  //Print a message to second line of LCD
//  lcd.print("Bitraf");
//}


// ------------------- Example for switches and LED's ------------------- //

int sw1 = 1;
int sw2 = 6;
int sw3 = 3;
int sw4 = 0;
int sw5 = 7;
int led1 = 4;
int led2 = 5;
int sw1out = 2;

void setup() {

  Serial.begin(9600);

  pinMode(sw1, INPUT_PULLUP);
  pinMode(sw1out, OUTPUT);
  pinMode(sw2, INPUT_PULLUP);
  pinMode(sw3, INPUT_PULLUP);
  pinMode(sw4, INPUT_PULLUP);
  pinMode(sw5, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  digitalWrite(sw1out, LOW);
  
}

void loop() {

  if (digitalRead(sw1) == LOW) {
    Serial.println("sw1");
  }

  if (digitalRead(sw2) == LOW) {
    Serial.println("sw2");
  }

  if (digitalRead(sw3) == LOW) {
    Serial.println("sw3");
  }

  if (digitalRead(sw4) == HIGH) {
    Serial.println("sw4");
  }

  if (digitalRead(sw5) == LOW) {
    Serial.println("sw5");
  }

  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW);
  delay (250);
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay (250);

}
