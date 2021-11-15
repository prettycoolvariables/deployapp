
import streamlit
import cv2
import numpy
from PIL import Image
uploadedfile=streamlit.file_uploader("upload your file here",type=['png','jpg','jpeg','jfif'])
print(uploadedfile)
if uploadedfile:
    imageplace=streamlit.empty()
    imageplace2=streamlit.empty()
    imageplace3=streamlit.empty()
    image=Image.open(uploadedfile)
    image1=numpy.array(image)
    #print(image1.shape)
    imageplace.image(image1,width=300)
    #streamlit.image(image,width=300)
    a=streamlit.sidebar.slider("lower hue",0,179)
    b=streamlit.sidebar.slider("lower saturation",0,255)
    c=streamlit.sidebar.slider("lower value",0,255)
    d=streamlit.sidebar.slider("upper hue",0,179)
    e=streamlit.sidebar.slider("upper saturation",0,255)
    f=streamlit.sidebar.slider("upper value",0,255)
    lower=(a,b,c)
    upper=(d,e,f)
    print("hi")
    hsvimage=cv2.cvtColor(image1,cv2.COLOR_RGB2HSV)
    i1=cv2.inRange(hsvimage,lower,upper)
    i2=cv2.erode(i1,None)
    i3=cv2.dilate(i2,None)
    #final=cv2.cvtColor(i3,cv2.COLOR_BGR2RGB)
    #if streamlit.button("click to see output"):
    imageplace2.image(i3,width=300)
    contours,hierarchy=cv2.findContours(i3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print(contours)
    #apples=0
    for c in contours:
        (x,y),radius=cv2.minEnclosingCircle(c)
        #print(radius)
        if radius>=10:
            cv2.circle(image1,(int(x),int(y)),int(radius),(0,0,255),2)
            cv2.circle(image1,(int(x),int(y)),int(2),(255,255,0),2)
            #apples+=1
            #print(apples)
    frame1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
    imageplace3.image(image1,width=300)
    #streamlit.text("number of apples = "+str(apples))
        
