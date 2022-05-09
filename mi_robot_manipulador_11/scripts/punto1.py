#!/usr/bin/env python3
from tokenize import String
import rospy

from pynput import keyboard as kb
from geometry_msgs.msg import Twist
from threading import Thread
from std_msgs.msg import String


class Punto1:

    def __init__(self) -> None:
        #Publisher
        self.cmdPublisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.manPublisher = rospy.Publisher('/manipulador', String, queue_size=10)
        
        print('Ingrese el valor de la velocidad lineal: ')
        self.vel_linear = float(input())
        print('Ingrese el valor de la velocidad angular: ')
        self.vel_angular = float(input())
        print('Robot listo!')

        #Constants
        self.RATE = rospy.Rate(10)

        #Attributes
        self.keyPressed = ""

        thread = Thread(target=self.run)
        thread.start()

    def pressKey(self, key):
        """
        Callback for kb.LIstener: It is called when a key is pressed and depending on the key that is pressed
        a Twist message is published in the cmd_vel topic. Invoke the function 'saveInformation'.
        """
        if key == kb.KeyCode.from_char('w'):
            self.keyPressed = 'w'
        elif key == kb.KeyCode.from_char('q'):
            self.keyPressed = 'q'
        elif key == kb.KeyCode.from_char('s'):
            self.keyPressed = 's'
        elif key == kb.KeyCode.from_char('e'):
            self.keyPressed = 'e'
        elif key == kb.KeyCode.from_char('i'):
            self.keyPressed = 'i'
        elif key == kb.KeyCode.from_char('k'):
            self.keyPressed = 'k'
        elif key == kb.KeyCode.from_char('x'):
            self.keyPressed = 'x'
        elif key == kb.KeyCode.from_char('z'):
            self.keyPressed = 'z'
        else:
            self.keyPressed = ''
    
    def releaseKey(self, key):
        """
        Callback for kb.Listener: It is called when a key is released and a Twist message with all the parameters
        in 0 is published.
        """
        self.keyPressed = ''
    
    def run(self):
        """
        Save in a .txt file the sequence of keys that are pressed.
        """
        """
        Save in a .txt file the sequence of keys that are pressed.
        """
        while not rospy.is_shutdown():
            twistMessage = Twist()
            StringMessage = String()
            if self.keyPressed == 'w':
                twistMessage.linear.x = self.vel_linear
            elif self.keyPressed == 'q':
                twistMessage.angular.z = self.vel_angular
            elif self.keyPressed == 's':
                twistMessage.linear.x = -self.vel_linear
            elif self.keyPressed == 'e':
                twistMessage.angular.z = -self.vel_angular
            elif self.keyPressed == 'i':
                StringMessage.data = 'i'
            elif self.keyPressed == 'k':
                StringMessage.data = 'k'
            elif self.keyPressed == 'z':
                StringMessage.data = 'z'
            elif self.keyPressed == 'x':
                StringMessage.data = 'x'

            self.cmdPublisher.publish(twistMessage)
            self.manPublisher.publish(StringMessage)
            self.RATE.sleep()
if __name__ == '__main__':
    rospy.init_node('turtle_bot_teleop')
    punto1 = Punto1()
    with kb.Listener(punto1.pressKey, punto1.releaseKey) as escuchador:
        escuchador.join()
    rospy.spin()