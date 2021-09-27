print("""\n\n
   ______                     ______           _                 _    _                       ____   ____  _        __                
 .' ___  |                   |_   _ `.        / |_              / |_ (_)                     |_  _| |_  _|(_)      |  ]               
/ .'   \_| ,--.   _ .--.       | | `. \ .---.`| |-'.---.  .---.`| |-'__   .--.   _ .--.        \ \   / /  __   .--.| | .---.   .--.   
| |       `'_\ : [ `/'`\]      | |  | |/ /__\\| | / /__\\/ /'`\]| | [  |/ .'`\ \[ `.-. |        \ \ / /  [  |/ /'`\' |/ /__\\/ .'`\ \ 
\ `.___.'\// | |, | |         _| |_.' /| \__.,| |,| \__.,| \__. | |, | || \__. | | | | |         \ ' /    | || \__/  || \__.,| \__. | 
 `.____ .'\'-;__/[___]       |______.'  '.__.'\__/ '.__.''.___.'\__/[___]'.__.' [___||__]         \_/    [___]'.__.;__]'.__.' '.__.'  
                                                                                                                                      
\n\n\n""")


print("Opening Modules ...\n")
import cv2
from time import sleep

video_of_us = input("please write the name of video with it's type file in here.\n")

try:
    cap = cv2.VideoCapture(video_of_us)
except:
    print("\nThe File that you gave us is incorrect or not available, Please Try Again\n")
    sleep(5)
    exit()


print("\nOpening the Classifier ...\n")
car_cascade = cv2.CascadeClassifier( r'cars.xml')


print("Entering the Loop")
while True:
    ret, frames = cap.read()

    try:
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale( gray, 1.1, 1)
    except:
        print("\n\nImage that you entered is not available.\n")
        sleep(5)
        exit()

    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frames, 'Car', (x + 6, y - 6), font, 0.5, (0, 0, 255), 1)
        cv2.imshow('Car Detection', frames)
    if cv2.waitKey(33) == 13:
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

#Created By AlPHA