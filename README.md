#                                                       BoltIoT-refrigerator

                                                          Assignment 
                                                    Capstone Final Project
                                                    
                                                    
This is the capstone project to summarize all the learnings in the 3 modules of the course and to give you practical hands-on experience by working on a major project. 


Problem Statement:
In the capstone project for the IoT training, we require you to build a proof of concept of the lighting system of a refrigerator which uses data from the Light Dependent Resistor (LDR) and a push button as well as features of the Bolt IoT cloud. You need to use the light intensity and button state to collect light intensity and button data to decide the state of the fridge:
a) Door open: Bright and button released
b) Door closed: Dark and button pressed
c) Door half open: Dim and button released
In your code, send an e-mail with the current state of the door when the state changes. Additionally, irritate the user once every 10 seconds if the door is open (state a and c). Additionally, you should set the intensity of a single indicator LED which clearly indicates the above three states. 

Components:
1) IoT module
2) LDR
3) Push Button
4) Resistors(10k,10k)
5) Breadboard

API's used:
MailGun Email API
Bolt Cloud API
Pyhon Library

