/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/String.h>
#include <Servo.h>


ros::NodeHandle nh;
Servo myservo;
Servo myservo2;

int pos = 0;
int pos2 = 0;

void messageCb( const std_msgs::String& string){
  nh.loginfo(string.data);
  if(String(string.data).equals("x")){
    nh.loginfo("Pinzón es gay");
    while(pos <= 150) { // goes from 0 degrees to 180 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    pos = pos+1;
    }
   }else if(String(string.data).equals("z")){
    while (pos >=0) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    pos = pos-1;
    }
  }else if(String(string.data).equals("i")){
    if (pos2<180){
      pos2=pos2+30;
      myservo2.write(pos2);
    }
  }else if(String(string.data).equals("k")){
    if (pos2>=0){
      pos2=pos2-30;
      myservo2.write(pos2);
    }
  }
  }

ros::Subscriber<std_msgs::String> sub("toggle_ledd", &messageCb );

void setup()
{
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo2.attach(10);
  myservo.write(0);
  myservo2.write(0);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
