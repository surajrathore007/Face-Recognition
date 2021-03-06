import cv2
import sqlite3
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def insertorUpdate(Id,Name):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id);
    cursor=conn.execute(cmd)
    isRecordExist=0
    
    for row in cursor:
         isRecordExist=1

    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+" WHERE ID="+str(Id);
    else:
        cmd="INSERT INTO People(ID,Name) VALUES("+str(Id)+","+str(Name)+")";
    conn.execute(cmd)
    conn.commit()
    conn.close()


#id to recognize the face
id=input("Enter the user id")
name=input("Enter the user name")
insertorUpdate(id,name)
sampleNumber=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNumber=sampleNumber+1
        cv2.imwrite("dataset/User."+str(id)+"."+str(sampleNumber)+".jpg",gray[y:y+h,x:x+w])
        cv2.waitKey(100)
        cv2.rectangle(img ,(x,y),(x+w,y+h),(1,0,255),2)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sampleNumber>20):
        cam.release()
        cv2.destroyAllWindows()
        break


