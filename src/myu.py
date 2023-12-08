import cv2
import numpy as np
from PIL import ImageGrab
while (True):
    screen = np.array(ImageGrab.grab())    
    facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
            cv2.rectangle(screen, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            #prediction = model.predict(cropped_img)
           # maxindex = int(np.argmax(prediction))
            #cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
    # press escape to exit
    if (cv2.waitKey(30) == 27):
       break
    cv2.imshow('RESULT', cv2.resize(screen,(1080,720),interpolation = cv2.INTER_CUBIC))
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()