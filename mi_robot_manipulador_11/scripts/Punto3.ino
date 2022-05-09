/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Float32.h>

ros::NodeHandle  nh;
int d_max = 5;
int grados = 0;
double d = 0;

Servo servo;

void servo_cb( const std_msgs::Float32& cmd_msg){
  d = cmd_msg.data-10;
  if (d >= 0 and d <= 5){
      grados = round((d/d_max)*180);
      servo.write(grados);
  }
}


ros::Subscriber<std_msgs::Float32> sub("servo", servo_cb);

void setup(){

  nh.initNode();
  nh.subscribe(sub);
  servo.attach(9); //attach it to pin 9
  
}

void loop(){
  nh.spinOnce();
  delay(1);
}
