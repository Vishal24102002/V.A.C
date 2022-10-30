from tkinter import *
from PIL import Image,ImageTk
import time
def contact():
    filmenu = Menu(menu)
    menu.add_cascade(label='contact', menu=filmenu)
    filemenu.add_command(label='vishalsharma@gmail.com')


#main frame code
def mainframe():
    pradeep=Tk()
    pradeep.title("pradeep")
    pradeep.iconbitmap("vac.ico")
    pradeep.geometry('450x300')
    """
    gif4=Image.open("images - 2022-10-29T120216.392.jpeg")
    resize5=gif4.resize((450,300),Image.ANTIALIAS)
    image5=ImageTk.PhotoImage(resize5)
    lab7=Label(pradeep,image=image5)
    lab7.place(x=0,y=0)
    """
    # upper option

    menu = Menu(pradeep)
    #pradeep.configure(bg='black')
    pradeep.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit')#command=exIT)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)

    contact=Menu(filemenu)
    helpmenu.add_command(label='About', filemenu=contact)


    contact.add_cascade(label='vishalsharma@gmail.com')



    #speak("you have sucessfully entered the application")
    #pradeep.after(ms=2000,func=get_audio)
    pradeep.mainloop()
mainframe()