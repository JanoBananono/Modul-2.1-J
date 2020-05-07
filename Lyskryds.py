from time import sleep
from gpiozero import LED

NSred= LED(13) #Definere alle dioder
NSyel=LED(19)
NSgreen=LED(26)
ØVred=LED(21)
ØVyel=LED(20)
ØVgreen=LED(16)

print("Test!") #Tester at alle dioder virker
ØVred.on()
sleep(1)
ØVgreen.on()
sleep(1)
ØVyel.on()
sleep(1)
NSred.on()
sleep(1)
NSgreen.on()
sleep(1)
NSyel.on()
sleep(1)
ØVred.off()
ØVgreen.off()
ØVyel.off()
NSred.off()
NSgreen.off()
NSyel.off()

def RedRed(x): #Begge er røde
    global tid
    if x == "NS":
        x = "ØV"
        print("Red! NS")
        print("Red! ØV")
        NSred.on()
        ØVred.on()
        sleep(5)
        return NS(x)
    elif x == "ØV":
        x = "NS"
        print("Red! NS")
        print("Red! ØV")
        NSred.on()
        ØVred.on()
        sleep(5)
        return ØV(x)
        
    
def NS(x): #NS cyklus
    global tid
    if x == "ØV":
        x = "NS"
        print("Red and Yellow! Stop NS")
        NSyel.on()
        sleep(2)
        NSyel.off()
        NSred.off()
        print("Green! Go NS")
        NSgreen.on()
        sleep(5)
        NSgreen.off()
        print("Yellow! Stop NS")
        NSyel.on()
        sleep(2)
        NSyel.off()
        print("Red! Stop NS")
        NSred.on()
        sleep(5)
        return ØV(x) #Starter ØV cyklussen efter

def ØV(x): #ØV cyklus
    if x == "NS":
        x = "ØV"
        print("Red and Yellow! Stop ØV")
        ØVyel.on()
        sleep(2)
        ØVyel.off()
        ØVred.off()
        print("Green! Go ØV")
        ØVgreen.on()
        sleep(5)
        ØVgreen.off()
        print("Yellow! Stop ØV")
        ØVyel.on()
        sleep(2)
        ØVyel.off()
        print("Red! Stop ØV")
        ØVred.on()
        sleep(5)
        return NS(x) #Starter NS cyklussen efter
       

      
state=RedRed(x="NS") #Sætter x til NS fra start
while state: state=RedRed(x="NS")          

        