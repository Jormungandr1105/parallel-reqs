#### LIGHTS
#define LED_R 51
#define LED_G 52
#define LED_B 53
#### FANS
#define Fan1 1
#define Fan2 2
#### NODE COUPLES
## Nodes 01,02
#define Nodes1 46
## Nodes 03,04
#define Nodes2 47
## Nodes 05,06
#define Nodes3 48
## Nodes 07,08
#define Nodes4 49
####


void set_color();
void get_serial();
void determine_color();


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_R, OUTPUT);
  digitalWrite(LED_R, LOW):
  pinMode(LED_G, OUTPUT);
  digitalWrite(LED_G, LOW):
  pinMode(LED_B, OUTPUT);
  digitalWrite(LED_B, LOW):
  pinMode(Nodes01_02, OUTPUT);
  digitalWrite(Nodes01_02, HIGH);
  pinMode(Nodes03_04, OUTPUT);
  digitalWrite(Nodes03_04, HIGH);
  pinMode(Nodes05_06, OUTPUT);
  digitalWrite(Nodes05_06, HIGH);
  pinMode(Nodes07_08, OUTPUT);
  digitalWrite(Nodes07_08, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    get_serial();
  }

void set_color(int LED, int value) {
  analogWrite(LED, value);
}

void get_serial() {
  while (Serial.available() > 0) {
    char incoming_char = Serial.read();
    Serial.print(incoming_char);
    acceptable = true;
    switch (incoming_char) {
      case 'C':
        determine_color();
        break;
      case 'P':
        determine_nodes();
        break;
    }
  }
}
  
void determine_color() {
  int leds[] = {LED_R, LED_G, LED_B};
  int modifier;
  int color = 0;
  int led_index = 0;
  bool second_digit = false;
  bool acceptable;
  while (Serial.available() > 0) {
    char incoming_char = Serial.read();
    Serial.print(incoming_char);
    acceptable = true;
    switch (incoming_char) {
      case '0':
      case '1':
      case '2':
      case '3':
      case '4':
      case '5':
      case '6':
      case '7':
      case '8':
      case '9':
        modifier = incoming_char - '0';
        break;
      case 'a':
        modifier = 10;
        break;
      case 'b':
        modifier = 11;
        break;
      case 'c':
        modifier = 12;
        break;
      case 'd':
        modifier = 13;
        break;
      case 'e':
        modifier = 14;
        break;
      case 'f':
        modifier = 15;
        break;
      default:
        acceptable = false;
        break;
    }
    if (acceptable) {
      if (second_digit) {
      color += modifier;
      Serial.println("PUSH COLOR"+String(led_index));
      set_color(leds[led_index], color);
      if (led_index == 2) {
        led_index = 0;
      } else {
        led_index = led_index + 1; 
      }
      color = 0;
    } else {
      Serial.println("add digit");
      color = modifier*16;
    }
    second_digit = !second_digit;
    }
  }
}