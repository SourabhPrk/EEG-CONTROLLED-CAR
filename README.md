# EEG-CONTROLLED-CAR
_A car is controlled using eeg signal sent via a neuroheadset._

The aim of this project is to collect the raw electrical signals from a human brain using a neuroheadset and then process these signals using machine learning so as to recognise the activity performed by the user and then send that data to the bot to perform the corresponding activity.

### Applications:
- This project may serve the purpose of user friendly prosthetic organs directly controlled by brain.
- It may also have application in Automation (Internet of Things) by controlling various devices using signals from brain.

### Requirements:

- Neurosky Mindwave Mobile Headset
- Python 3.0 / jupyter notebook (python 3.0 compatible)
- 1 Motor Deiver(L2981)
- NodeMcu(ESP8266)
- Two Motors
- Jumpers
- Chassis
- 2 Wheels

### With HeadSet:

For those who have the neuro headset, they may proceed as following to utilise my project-

1. Switch On the headset and hold the key for On position until the headset flash starts blinking faster, which means it is in pairing mode.

2. Pair your computer with the headset using bluetooth of your computer(The name of the headset for bluetooth connections is Mindwave Mobile).

3. You only have to pair using the bluetooth. To connect the headset, you have to use the following python code in Terminal

``` bash
sudo rfcomm bind /dev/rfcomm1 74:E5:43:D5:6C:07
ls -l /dev/rfcomm1
```

You need to go to your bluetooth settings and then find out the port by which you are connecting to the headset(example-COM3,COM2 etc.) and then replace that port instead of rfcomm1 in the above code(example- rfcomm2,rfcomm3 etc.)

4. You are now connected to the headset.

5. To implement my model, you may use "HOST_DATA_READ.py" script present in my repository under Python_scripts folder.In this script you have to make a change in the following line of code-

