# FloodBot

## Project Overview
FloodBot is a low-cost, student-built flood rescue robot designed to operate in shallow floodwaters and debris-filled environments. The project explores how affordable materials such as PVC framing, DC motors, and accessible single-board computers can be combined to create a functional and educational rescue-assist robot.

FloodBot is not intended to replace first responders. Instead, it serves as:
- A scouting and observation platform for flooded areas
- A proof-of-concept for affordable rescue robotics
- An educational tool for students learning robotics, embedded systems, and power design

This project is being developed and documented as part of Hack Club Blueprint, with the goal of being open-source and reproducible by other students.

---

## Motivation
Flooding is one of the most common and destructive natural disasters worldwide. Many affected communities lack access to advanced robotic equipment due to cost and technical barriers.

FloodBot investigates whether a simple, low-cost design can still provide value by:
- Allowing visual inspection of flooded or unsafe areas
- Demonstrating basic robotic mobility and sensing
- Teaching hands-on engineering concepts through iterative building

---

## Current Progress
As of now, the following progress has been made:
- PVC frame designed and fully assembled
- Frame sized to house motors, battery, and electronics
- Initial research completed on power distribution and motor control

The project currently lacks the electronics required to proceed with motion, sensing, and vision.

---

## System Architecture

### High-Level Breakdown
- Raspberry Pi (3 or 4)  
  Handles camera input, high-level control logic, and communication

- Microcontroller (Arduino Uno or Raspberry Pi Pico)  
  Responsible for real-time motor control and sensor handling

- DC Motors (2x)  
  Differential drive system for movement and steering

- Motor Driver  
  Interfaces between the microcontroller and motors for safe direction and speed control

- Camera Module  
  Provides live video feed for navigation and observation

- Battery System  
  Single battery pack with regulated 5V output for logic electronics

---

## Power Design
Power is distributed from a single battery source:
- Battery to DC-DC buck converter (5.1V) to Raspberry Pi and microcontroller
- Battery directly to motor driver for DC motors

All grounds are shared to ensure signal stability and prevent brownouts.

---

## Parts Needed (Grant-Funded)

### Core Electronics
- Raspberry Pi (3 or 4)
- Raspberry Pi Camera Module (8–12MP)
- Microcontroller (Arduino Uno or Raspberry Pi Pico)
- 32GB microSD card

### Motion and Control
- Two DC geared motors
- Motor driver module (TB6612FNG or L298N)

### Power
- Battery pack (AA or Li-ion)
- DC-DC buck converter (LM2596)

### Miscellaneous
- Jumper wires
- Mounting hardware
- Waterproofing materials (sealant, gaskets)

---

## Build Plan
1. Mount DC motors to the PVC frame
2. Install the motor driver and microcontroller
3. Integrate the battery and regulated power system
4. Install the Raspberry Pi and camera module
5. Establish communication between the Raspberry Pi and microcontroller
6. Test motor control and steering
7. Enable camera streaming
8. Iterate on waterproofing and mechanical stability

---

## Documentation and Journaling
All development progress will be documented in the `journal/` directory, including:
- Build steps
- Design changes
- Issues encountered and solutions
- Photos and diagrams

This ensures the project remains transparent, reproducible, and educational.

---

## Educational Value
FloodBot demonstrates and teaches:
- Embedded systems integration
- Motor control and power safety
- Mechanical prototyping using PVC
- Documentation and open-source development practices

The project is intended to be shared as a learning resource for student builders.

---

## Project Status
In progress — electronics acquisition required to continue development.
