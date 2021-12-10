<p align="center">
  <img  src="https://user-images.githubusercontent.com/25025173/51177457-37460a00-18f2-11e9-8858-9c51f6c987a1.gif">
</p>

-	Emotion detection

Credit to: https://github.com/hfahrudin/FastEmotRecognition for the emotion recognition model

The emotion detection model uses the mobilenetv2 model architecture, and it is trained on affectnet, jaffe and ck+ datasets. The model is converted to tf-lite model for smoother use on raspberry pi 3. The current model can classify 7 different emotions (neutral, happy, sad, angry, disgust, fear, surprise), but we only use three of those for our current project (happy, sad, angry).

-	Hat movement 

We are using 4 micro servos (MG90S) to control the movement of the hat through the RPi.GPIO library. The hat is designed as follow :
<p align="center">
  <img  src="https://user-images.githubusercontent.com/91775734/145547381-41a32b53-d967-483b-87f4-05ca813f9fcd.png">
</p>

The motor 1 and 3 should be linked respectively to pin 9 (variable name pin1) and pin 11 (variable name pin2)

The motor 2 and 4 should be linked respectively to pin 12 (variable name pin3) and pin 13 (variable name pin4)

Those can be changed at any time by precising the argument -pinX (X = 1,2,3,4) when running the main code.

main_lite_test.py is the script to run the whole pipeline (emotion detection through the camera + hat movement accordingly). Make sure to have a camera connected, as well as all 4 servos on the correct pin number (using board numeration) of the raspberry pi. 

Dependencies:
1. python 3.8
2. tensorflow + tflite for raspberry pi
3. opencv 3.2
4. RPi.GPIO 0.7.0
