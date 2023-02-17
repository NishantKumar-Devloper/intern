from tkinter import *
from PIL import ImageTk , Image
import os
from tkinter.filedialog import askdirectory
from pygame import mixer

#colors
co1="#ffffff"
co2="#3C1DC6"
co3="#333333"
co4="#CFC7F8"

window=Tk()
window.title("Music player")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

#Functions
def play_music():
    running=lb.get(ACTIVE)
    running_song['text']=running
    mixer.music.load(running)
    mixer.music.play()
def pause_music():
    mixer.music.pause()
def open_file():   
    path=askdirectory()
    os.chdir(path)
    return path

def next_song():
    playing=running_song['text']
    index=songs.index(playing)
    new_index=index+1
    if(new_index==len(songs)):
        new_index=0
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    songs.clear()
    lb.delete(0,END)
    show()
    lb.select_set(new_index)
    running_song['text']=playing
def prev_song():        
    playing=running_song['text']
    index=songs.index(playing)
    new_index=index-1
    if(new_index==-1):
        new_index=len(songs)-1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    songs.clear()
    lb.delete(0,END)
    show()
    lb.select_set(new_index)
    running_song['text']=playing

#Frames
left_frame=Frame(window,width=150,height=150,bg=co1)
left_frame.grid(row=0,column=0,padx=1,pady=1)

right_frame=Frame(window,width=250,height=150,bg=co3)
right_frame.grid(row=0,column=1,padx=0)

down_frame=Frame(window,width=400,height=100,bg=co4)
down_frame.grid(row=1,column=0,columnspan=3, padx=0,pady=1)

lb=Listbox(right_frame,selectmode=SINGLE,font="Arial 9 bold",width=22,bg=co3,fg=co1)
lb.grid(row=0,column=0)

#images
img1=Image.open("icon.png")
img1=img1.resize((130,130))
img1=ImageTk.PhotoImage(img1)
app_img=Label(left_frame,height=130,image=img1,padx=10,bg=co1)
app_img.place(x=10,y=15)

img2=Image.open("play.png")
img2=img2.resize((30,30))
img2=ImageTk.PhotoImage(img2)
play_button=Button(down_frame,height=40,width=40,image=img2,padx=10,bg=co4,font=("Ivy 10"),command=play_music)
play_button.place(x=40+28,y=35)

img3=Image.open("next.png")
img3=img3.resize((30,30))
img3=ImageTk.PhotoImage(img3)
next_button=Button(down_frame,height=40,image=img3,padx=10,bg=co4,command=next_song)
next_button.place(x=85+28,y=35)

img4=Image.open("prev.png")
img4=img4.resize((30,30))
img4=ImageTk.PhotoImage(img4)
pre_button=Button(down_frame,height=40,image=img4,padx=10,bg=co4,command=prev_song)
pre_button.place(x=10+28,y=35)

img5=Image.open("pause.png")
img5=img5.resize((30,30))
img5=ImageTk.PhotoImage(img5)
pause_button=Button(down_frame,height=40,image=img5,padx=10,bg=co1,command=pause_music)
pause_button.place(x=148+28,y=35)

img6=Image.open("open.png")
img6=img6.resize((100,100))
img6=ImageTk.PhotoImage(img6)
Open_btn=Button(down_frame,height=40,image=img6,padx=10,bg=co1,command=open_file)
Open_btn.place(x=198+28,y=35)

running_song=Label(down_frame,text="Choose a song",font=("Ivy 10"), width=44,height=1,padx=10,bg=co1,fg=co3,anchor=NW)
running_song.place(x=0,y=1)
songss=os.listdir(open_file())
songs=[]
def show():
    for i in songss:
        if i.endswith(".mp3"):
            songs.append(i)
            lb.insert(END,i)
show()
mixer.init()
music_state=StringVar()
music_state.set("choose one!")
window.mainloop()