print("""\n\n
   ______                     ______           _                 _    _                        _                                     
 .' ___  |                   |_   _ `.        / |_              / |_ (_)                      (_)                                    
/ .'   \_| ,--.   _ .--.       | | `. \ .---.`| |-'.---.  .---.`| |-'__   .--.   _ .--.       __   _ .--..--.   ,--.   .--./) .---.  
| |       `'_\ : [ `/'`\]      | |  | |/ /__\\| | / /__\\/ /'`\]| | [  |/ .'`\ \[ `.-. |     [  | [ `.-. .-. | `'_\ : / /'`\;/ /__\\ 
\ `.___.'\// | |, | |         _| |_.' /| \__.,| |,| \__.,| \__. | |, | || \__. | | | | |      | |  | | | | | | // | |,\ \._//| \__., 
 `.____ .'\'-;__/[___]       |______.'  '.__.'\__/ '.__.''.___.'\__/[___]'.__.' [___||__]    [___][___||__||__]\'-;__/.',__`  '.__.' 
                                                                                                                     ( ( __))        
\n\n""")




print("Importing Modules ...")
import cv2
import matplotlib.pyplot as plt
from time import sleep

imgae_f_us = input("\nplease write the name of picture with it's type file in here.\n")

try:
    cap = cv2.imread(imgae_f_us,cv2.IMREAD_COLOR)
except:
    print("\nThe File that you gave us is incorrect or not available, Please Try Again\n")
    sleep(5)
    exit()

print("\nOpening the Classifier ...\n")
car_cascade = cv2.CascadeClassifier( r'cars.xml')

try:
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
except:
    print("\n\nImage that you entered is not available.\n")
    sleep(5)
    exit()

cars = car_cascade.detectMultiScale(gray, 1.1, 1)

ncars=0

for (x, y, w, h) in cars:
    cv2.rectangle(cap, (x,y), (x+w,y+h), (0,0,255), 2)
    ncars = ncars + 1


plt.figure(figsize=(10,20))
plt.imshow(cap)
plt.savefig('detection.png')
print("\nImage is Saved!")
sleep(5)

#Created By AlPHA