#-#-# Project3 -: Youtube downloader #-#-#

from pytube import YouTube
from tkinter import *

#For Crating GUI
root=Tk()
root.geometry("400x400")
root.title("Youtube Video downloader")

#Function for download function
def downloaded():
    a=var.get() #https://www.youtube.com/watch?v=AI6Nk70Vvew
    yt_video=YouTube(a).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    yt_video.download(output_path=r'C:\Users\Admin\Downloads')
    #print("Entry box",a)

l1=Label(root,text="YOutube Video",fg='Red',font=("bold",20))
l1.place(x=30,y=20)

var=StringVar()
e1=Entry(root,textvariable=var,width=60)
e1.place(x=60,y=70)

b1=Button(root,text="Dounload",command=downloaded,bg="green",width=20,fg="White")
b1.place(x=100,y=100)


root.mainloop()
