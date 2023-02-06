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

def grab(delay):
    next_time = time.time() + delay
    global prev
    while True:
        time.sleep(max(0, next_time - time.time()))
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
        
        next_time += (time.time() - next_time) // delay * delay + delay
    
    out.release()    
    cv2.destroyAllWindows()
    
grab(5)