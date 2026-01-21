FloodBot
What is this?
FloodBot is a low-cost underwater robot I am building to explore flooded areas. In its most basic description, it is a waterproof rover with a camera which can drive through shallow water and send back video. The whole thing is built of PVC pipes, some DC motors, and a Raspberry Pi-nothing fancy, but that is kind of the point.
I am not trying to build something that replaces actual rescue teams; it is more about:

To learn whether inexpensive materials can create anything useful
Having a remote-controlled scout for flooded places
Understanding how robotics, waterproofing, and power systems interact with each other

This is my project in Blueprint, and I am documenting everything so that other students can learn from-or laugh at-my mistakes.

Why Build This?
It seems like floods are always happening, and they're really terrifying. I started to wonder if a student on a limited budget could build something that could actually be useful - or at least for checking out flooded basements or storm drains.
Furthermore, I also needed a reason that would give me the opportunity to learn more about underwater robotics without having to shell out thousands of dollars on a high-end ROV kit.

What I've Done So Far
Currently, I have:

A complete PVC frame designed by me in Fusion 360
The frame is designed to house all the electronics (motors, batteries, Pi, etc.)
A full CAD model for a 3D system with components described
Some research on how to connect all the wires without blowing something up

The CAD Model:
I designed the entire robot in Fusion 360, down to each and every component—frame, motor compartments, electronics case, mounting plates, and even propellers. The STEP files are in the /cad directory if you'd like to take a look and perhaps modify them to suit your needs. The frame consists of a PVC pipe cage, motors situated in each corner, and a water-tight case in the middle.

How It Works (In Theory)
The system breaks down like this:
Brain:

Raspberry Pi handles the camera, WiFi control, and telling the Arduino what to do

Muscles:

Arduino or Pi Pico runs the motors in real-time
Two DC motors (differential drive - like a tank)
Motor driver board safely controls speed and direction

Eyes:

Raspberry Pi camera streams video over WiFi

Power:

One battery pack feeds everything
Buck converter steps voltage down to 5V for the electronics
Motors run directly off battery voltage


The Parts I Need
Electronics (waiting on grant)

Raspberry Pi 3 or 4
Pi Camera Module
Arduino Uno or Raspberry Pi Pico
32GB microSD card

Motion

2x DC geared motors (waterproof housings)
Motor driver (TB6612FNG or L298N)

Power

Battery pack (probably Li-ion)
Buck converter module (LM2596)

Other Stuff

Wires, connectors
Mounting screws
Waterproofing materials (silicone, maybe some gaskets)


The Build Plan
Once I get the parts, here's the order of operations:

Mount motors to the PVC frame corners
Wire up motor driver and Arduino
Install battery and power regulation
Add the Raspberry Pi and camera
Get Pi and Arduino talking to each other
Test if the motors actually work
Get camera streaming
Try not to short circuit anything
Waterproof everything
Test in water (probably my bathtub first)


What I'm Learning
This project is teaching me about:

How to distribute power without frying components
Motor control and PWM signals
Building mechanical structures that don't fall apart
3D CAD modeling and mechanical design
Documentation
How waterproofing is way harder than it looks
