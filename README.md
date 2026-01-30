FloodBot


What is this?

 FloodBot is a low-cost flood-exploration robot designed to drive through shallow water and send back live video. It’s built from PVC pipe, DC motors, and a Raspberry Pi, with the goal of learning how waterproofing, power systems, and robotics interact in real conditions.

Why I Built This


Floods happen often and are dangerous, but most rescue robots are expensive and inaccessible. I wanted to explore whether a student-built robot using inexpensive materials could be useful as a scouting or inspection tool, while also giving me hands-on experience with underwater robotics and system integration.

How It Works


FloodBot uses a Raspberry Pi for camera streaming and high-level control, and an Arduino for real-time motor control. A single battery powers the system through a buck converter, providing regulated 5V for logic electronics and higher voltage for the motors. Motors are paired by side to simplify control and improve stability in moving water.

Design & CAD


The entire robot was designed by me in Fusion 360, including the PVC frame, motor mounts, electronics enclosure, and internal layout. A complete assembled STEP file including electronics and mechanical components is included in the /cad directory, along with the source design files.

Firmware


This project includes preliminary firmware for both the Raspberry Pi and Arduino. The Raspberry Pi handles camera streaming and sends movement commands to the Arduino over USB serial. The Arduino firmware controls motor direction and speed through a dual H-bridge motor driver. The code is untested but reflects the intended system architecture.

Project Status


The design is complete and has been sanity-checked by others. Parts are pending, after which I plan to assemble, waterproof, and test the robot in controlled water environments.



Wiring Diagram


<img width="1342" height="1100" alt="image" src="https://github.com/user-attachments/assets/11e60e1f-fd6f-4e0b-abf7-5d3c6a9a22a9" />




CAD/RENDER


<img width="1670" height="1182" alt="image" src="https://github.com/user-attachments/assets/c044d8d3-00b4-4492-af6e-a27e0f7f6b40" />



BOM.csv


<img width="2122" height="646" alt="image" src="https://github.com/user-attachments/assets/eb168a52-fe86-4501-b296-5d97138f4b30" />










