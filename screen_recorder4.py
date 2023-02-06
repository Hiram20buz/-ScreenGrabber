import cv2
import numpy as np
import pyautogui
import time


SCREEN_SIZE=pyautogui.size()

fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("output.avi",fourcc,20.0,(SCREEN_SIZE))

#fps=120
fps=60

prev=0

def grab():
    global prev
    while True:
        try:
            time_elapsed=time.time()-prev
            
            img=pyautogui.screenshot()
            #print(time_elapsed)
            print(time.time())
            print(prev)
            if time_elapsed > 1.0/fps:
                prev=time.time()
                frame=np.array(img)
                frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                out.write(frame)
                
            cv2.waitKey(100)
            
        except KeyboardInterrupt:
            continue
    
    out.release()    
    cv2.destroyAllWindows()
    
grab()