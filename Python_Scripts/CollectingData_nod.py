from NeuroPy import NeuroPy
from time import sleep
from time import time
import csv

neuropy = NeuroPy("/dev/rfcomm1") 

neuropy.start()
sleep(3)


with open('VIVEK_NOD.csv', 'w') as csvfile:
    fieldnames = ['attention', 'delta', 'meditation', 'rawValue', 'theta', 
    'lowAlpha', 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'midGamma', 'poorSignal', 'blinkStrength' ,'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    """i = time()
    j = time()
    print "Action 1 = blink"
    while(j-i<140):
    	writer.writerow({'attention': neuropy.attention, 'delta': neuropy.delta, 
    		'meditation': neuropy.meditation, 'rawValue': neuropy.rawValue, 
    		'theta': neuropy.theta, 'lowAlpha': neuropy.lowAlpha, 'highAlpha': neuropy.highAlpha, 
    		'lowBeta': neuropy.lowBeta, 'highBeta': neuropy.highBeta, 
    		'lowGamma' : neuropy.lowGamma, 'midGamma' : neuropy.midGamma, 
    		'poorSignal' : neuropy.poorSignal, 'blinkStrength': neuropy.blinkStrength, 'label': '1'})
        sleep(0.1)
        j = time()

    i = time()
    j = time()
    print "Action 2 = Clap"
    sleep(2)
    while(j-i<140):
        writer.writerow({'attention': neuropy.attention, 'delta': neuropy.delta, 
            'meditation': neuropy.meditation, 'rawValue': neuropy.rawValue, 
            'theta': neuropy.theta, 'lowAlpha': neuropy.lowAlpha, 'highAlpha': neuropy.highAlpha, 
            'lowBeta': neuropy.lowBeta, 'highBeta': neuropy.highBeta, 
            'lowGamma' : neuropy.lowGamma, 'midGamma' : neuropy.midGamma, 
            'poorSignal' : neuropy.poorSignal, 'blinkStrength': neuropy.blinkStrength, 'label': '2'})
        sleep(0.1)
        j = time()

    i = time()
    j = time()      
    print "Action 3 = leg tap"
    sleep(2)
    while(j-i<140):
        writer.writerow({'attention': neuropy.attention, 'delta': neuropy.delta, 
            'meditation': neuropy.meditation, 'rawValue': neuropy.rawValue, 
            'theta': neuropy.theta, 'lowAlpha': neuropy.lowAlpha, 'highAlpha': neuropy.highAlpha, 
            'lowBeta': neuropy.lowBeta, 'highBeta': neuropy.highBeta, 
            'lowGamma' : neuropy.lowGamma, 'midGamma' : neuropy.midGamma, 
            'poorSignal' : neuropy.poorSignal, 'blinkStrength': neuropy.blinkStrength, 'label': '3'})
        sleep(0.1)
        #print "att",neuropy.attention
        #print "Blink",neuropy.blinkStrength
        j = time()    
        #print j-i"""
    i = time()
    j = time()
    print "Action 4 = nod"
    sleep(2)
    while(j-i<120):
        writer.writerow({'attention': neuropy.attention, 'delta': neuropy.delta, 
            'meditation': neuropy.meditation, 'rawValue': neuropy.rawValue, 
            'theta': neuropy.theta, 'lowAlpha': neuropy.lowAlpha, 'highAlpha': neuropy.highAlpha, 
            'lowBeta': neuropy.lowBeta, 'highBeta': neuropy.highBeta, 
            'lowGamma' : neuropy.lowGamma, 'midGamma' : neuropy.midGamma, 
            'poorSignal' : neuropy.poorSignal, 'blinkStrength': neuropy.blinkStrength, 'label': '4'})
        sleep(0.1)
        #print "att",neuropy.attention
        #print "Blink",neuropy.blinkStrength
        j = time()    
        #print j-i

#print "While Complete"
csvfile.close()
neuropy.stop()

"""
 #To connect headset to laptop
#sudo rfcomm bind /dev/rfcomm1 74:E5:43:D5:6C:07
#ls -l /dev/rfcomm1


    Action 1 = Blink
    Action 2 = Clap
        #attention
        #delta
        #meditation
        #rawValue
        #theta
        #lowAlpha
        #highAlpha
        #lowBeta 
        #highBeta
        #lowGamma
        #midGamma
        #poorSignal
        #blinkStrength_value

"""
