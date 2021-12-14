//// LIGHTS
#define LED_R 51
#define LED_G 52
#define LED_B 53
//// FANS
#define Fan1 1
#define Therm1 2
#define Fan2 3
#define Therm2 4
//// NODE COUPLES
// Nodes 01,02
#define Nodes1 46
// Nodes 03,04
#define Nodes2 47
// Nodes 05,06
#define Nodes3 48
// Nodes 07,08
#define Nodes4 49
int Nodes[] = {Nodes1, Nodes2, Nodes3, Nodes4};
////


void set_color();
void get_serial();
void determine_color();



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_R, OUTPUT);
  //digitalWrite(LED_R, LOW);
  pinMode(LED_G, OUTPUT);
  //digitalWrite(LED_G, LOW);
  pinMode(LED_B, OUTPUT);
  //digitalWrite(LED_B, LOW);
  pinMode(Nodes1, OUTPUT);
  digitalWrite(Nodes1, HIGH);
  pinMode(Nodes2, OUTPUT);
  digitalWrite(Nodes2, HIGH);
  pinMode(Nodes3, OUTPUT);
  digitalWrite(Nodes3, HIGH);
  pinMode(Nodes4, OUTPUT);
  digitalWrite(Nodes4, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    get_serial();
  }
}

void set_color(int LED, int value) {
  analogWrite(LED, value);
}

void determine_color(String color_str) {
  int leds[] = {LED_R, LED_G, LED_B};
  int modifier;
  int color = 0;
  int led_index = 0;
  bool second_digit = false;
  bool acceptable;
  //Serial.println("Determining Color");
  for (int i=1; i<color_str.length()-1; i++) {
    char incoming_char = color_str[i];
    //Serial.println(incoming_char);
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
        //Serial.println("UNACCEPTABLE");
        break;
    }
    if (acceptable) {
      if (second_digit) {
      color += modifier;
      //Serial.println("PUSH COLOR"+String(led_index));
      set_color(leds[led_index], color);
      if (led_index == 2) {
        led_index = 0;
      } else {
        led_index = led_index + 1; 
      }
      color = 0;
    } else {
      //Serial.println("add digit");
      color = modifier*16;
    }
    second_digit = !second_digit;
    }
    //Serial.println("LOOP BOTTOM");
  }
}

void get_serial() {
  if (Serial.available() > 0) {
    String incoming_str = Serial.readString();
    //Serial.println(incoming_char);
    switch (incoming_str[0]) {
      case 'C':
        determine_color(incoming_str);
        //Serial.println("Set_Color");
        break;
      case 'P':
        determine_nodes(incoming_str);
        //Serial.println("Set Node Power");
        break;
    }
  }
}
  
void determine_nodes(String data_str) {
  //assert(data_str.length()-1 == sizeof(Nodes)/sizeof(int));
  for (int i=1; i<data_str.length()-1; i++) {
    //Serial.println(data_str[i]);
    if (data_str[i] == '0') {
      digitalWrite(Nodes[i-1],HIGH);
    } else if (data_str[i] == '1') {
      digitalWrite(Nodes[i-1],LOW);
    }
  }
}

void set_fan_speeds(float[] &last_temps, int[] &fan_speeds) {
  
}