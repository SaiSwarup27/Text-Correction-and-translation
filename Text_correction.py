import tkinter as tk
from textblob import TextBlob
import nltk

def correct_spell():
    text=entry1.get()
    text=TextBlob(text)
    text=text.lower()
    label1.config(text=text.correct())
    
def translate():
    text2=entry1.get()
    text2=TextBlob(text2)
    text2=text2.lower()
    text2=text2.correct()
    text3=menu1.get()
    if(text3=="Hindi"):
        label6.config(text=text2.translate(to='hi'))
    if(text3=="Telugu"):
        label6.config(text=text2.translate(to='te'))
    if(text3=="Tamil"):
        label6.config(text=text2.translate(to='ta'))
    if(text3=="Kannada"):
        label6.config(text=text2.translate(to='kn'))
    if(text3=="German"):
        label6.config(text=text2.translate(to='de'))
    if(text3=="French"):
        label6.config(text=text2.translate(to='fr'))
    if(text3=="Chinese"):
        label6.config(text=text2.translate(to='zh-CN'))
    if(text3=="Japanese"):
        label6.config(text=text2.translate(to='ja'))


window=tk.Tk()
window.maxsize(width=450,height=350)
label=tk.Label(master=window,text="NLP Text Correction",font=("Arial", 15))
label.pack()
frame=tk.Frame(master=window,border=2,borderwidth=2,relief=tk.SUNKEN)

label2=tk.Label(master=frame,text="Enter your text here: ")
label2.grid(row=0,column=0)
entry1=tk.Entry(master=frame,width=60)
entry1.grid(row=0,column=1,columnspan=2)
button1=tk.Button(master=frame,text='submit',relief=tk.RAISED,command=correct_spell)
button1.grid(row=1,column=1)

label3=tk.Label(master=frame,text="Corrected text: ")
label3.grid(row=2,column=0)
label1=tk.Label(master=frame,text=" ")
label1.place(x=155,y=47)

label4=tk.Label(master=frame,text="Select language to translate text: ",relief=tk.RAISED)
label4.grid(row=3,column=0)
menu1=tk.StringVar(master=frame)
menu1.set("select language")
options = [
    "Chinese",
    "French",
    "German",
    "Hindi",
    "Japanese",
    "Kannada",
    "Tamil",
    "Telugu"
]
drop=tk.OptionMenu(frame, menu1, *options)
drop.grid(row=3,column=1)
button2=tk.Button(master=frame,text="Translate",command=translate)
button2.grid(row=3,column=2)

label5=tk.Label(master=frame,text="Translated language:")
label5.grid(row=4,column=0,pady=5)
label6=tk.Label(master=frame,text="")
label6.place(x=155,y=105)


frame.pack(padx=10,pady=10)

window.mainloop()
