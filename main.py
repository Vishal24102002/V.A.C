from vosk import Model, KaldiRecognizer
import pyaudio
import time
from tkinter import *
from pygame import mixer
import math
from PIL import Image,ImageTk
import pyttsx3 as pt
def clear():
    for widget in frame.winfo_children():
    widget.destroy()

def speak(text):
    engine=pt.init()
    engine.say(text)
    Voices=engine.getProperty('voices') 
    Print(Voices) 
    engine.setProperty('voice',Voices[0].id) 
    engine.runAndWait() 
def audio():
    model = Model("C:/Users/Administrator/PycharmProjects/pythonProject2/vosk/vosk-model-small-en-in-0.4")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    time.sleep(1.5)
    speak("your audio is being captured")
    print("your voice is recorded")
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            speak("unable to recognizze your voice")
            time.sleep(1.5)
            speak("please try again")

        elif recognizer.AcceptWaveform(data):
            PYAUDIO = recognizer.Result()
            print(PYAUDIO)
            time.sleep(2.5)
            break



def form():
    root = Toplevel()
    root.title('digital')
    root.iconbitmap("vac.ico")
    root.geometry('680x486+100+100')
    root.maxsize(680,486)
    root.minsize(680,486)

    gif3 = Image.open("images - 2022-10-22T192356.420.jpeg")
    resize3 = gif3.resize((450, 300), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(resize3)
    lab6 = Label(root, image=image3)
    lab6.place(x=0, y=0)

    #logoImage = PhotoImage(file='logo.png')
    #logoLabel = Label(root,bg='dodgerblue3')
    #logoLabel.grid(row=0, column=0)

    entryField = Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white', bd=10, relief=SUNKEN, width=50)
    entryField.grid(row=0, column=0, columnspan=8)

    #micImage = PhotoImage(file='download.png')
    #micButton = Button(root, image=micImage, bd=20, bg='blue', activebackground='dodgerblue3')
    #micButton.grid(row=0, column=7)
    mixer.init()

    def click(value):
        ex = entryField.get()  # 789 ex[0:len(ex)-1]
        answer = ''

        try:

            if value == 'C':
                ex = ex[0:len(ex) - 1]  # 78
                entryField.delete(0, END)
                entryField.insert(0, ex)
                return

            elif value == 'CE':
                entryField.delete(0, END)

            elif value == '√':
                answer = math.sqrt(eval(ex))

            elif value == 'π':
                answer = math.pi

            elif value == 'cosθ':
                answer = math.cos(math.radians(eval(ex)))

            elif value == 'tanθ':
                answer = math.tan(math.radians(eval(ex)))

            elif value == 'sinθ':
                answer = math.sin(math.radians(eval(ex)))

            elif value == '2π':
                answer = 2 * math.pi

            elif value == 'cosh':
                answer = math.cosh(eval(ex))

            elif value == 'tanh':
                answer = math.tanh(eval(ex))

            elif value == 'sinh':
                answer = math.sinh(eval(ex))

            elif value == chr(8731):
                answer = eval(ex) ** (1 / 3)

            elif value == 'x\u02b8':  # 7**2
                entryField.insert(END, '**')
                return

            elif value == 'x\u00B3':
                answer = eval(ex) ** 3

            elif value == 'x\u00B2':
                answer = eval(ex) ** 2

            elif value == 'ln':
                answer = math.log2(eval(ex))

            elif value == 'deg':
                answer = math.degrees(eval(ex))

            elif value == "rad":
                answer = math.radians(eval(ex))

            elif value == 'e':
                answer = math.e

            elif value == 'log₁₀':
                answer = math.log10(eval(ex))

            elif value == 'x!':
                answer = math.factorial(eval(ex))

            elif value == chr(247):  # 7/2=3.5
                entryField.insert(END, "/")
                return

            elif value == '=':
                answer = eval(ex)

            else:
                entryField.insert(END, value)
                return

            entryField.delete(0, END)
            entryField.insert(0, answer)

        except SyntaxError:
            pass

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    def mod(a, b):
        return a % b

    def lcm(a, b):
        l = math.lcm(a, b)
        return l

    def hcf(a, b):
        h = math.gcd(a, b)
        return h

    button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                            "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                            "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                            "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                            "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
    rowvalue = 1
    columnvalue = 0
    for i in button_text_list:
        button = RoundedButton(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='yellow',
                            font=('arial', 18, 'bold'), activebackground='blue',cursor="hand2", 
                            command=lambda button=i: click(button))
        button.grid(row=rowvalue, column=columnvalue, pady=1)
        columnvalue += 1
        if columnvalue > 7:
            rowvalue += 1
            columnvalue = 0

    root.mainloop()

#defining command 2 over here
def command2():
    speak("you have chossen digit method that typing or clicking")
    time.sleep(3.5)
    speak("hope you like the applicaton ")
    time.sleep(1.5)
    speak("our only job is to make calculation a enjoyable")

#click mode for calculation
def digital():
    asish=Toplevel()
    asish.title('digital form')
    x=300
    y=150
    asish.geometry("300x150")
    asish.maxsize(x,y)
    asish.minsize(300,150)
    asish.iconbitmap("vac.ico")
    #speaking command for better interaction
    asish.after(ms=2000,func=command2)
    #labels are that available

    #image file path
    gif1=Image.open("CAL.png.jpeg")
    resize1=gif1.resize((x,y),Image.ANTIALIAS)
    image1=ImageTk.PhotoImage(resize1)

    #initialising the labels
    lab3=Label(asish,image=image1)
    lab1=Label(asish,bg="red",height=9,width=20)
    lab2=Label(asish,text='please wait while loading ....',bg="red",width=46)

    #packing labels
    lab3.place(x=0,y=0)
    lab1.grid(row=0,column=3)
    lab2.grid_anchor("s")
    #lab2.pack(side=BOTTOM)

    lab2.grid(row=0, column=0,pady=55)

    asish.after(ms=10000,func=form)
    asish.after(ms=10100,func=asish.quit)


    asish.mainloop()
def voice():
    speak("thanks for selecting voice input")

    speak("what is the numbers ")
    #taking the data from user
    audio()
    NUMBER=PYAUDIO[14:-3]
    NO(NUMBER)
    print("the value of data",dat)






    # taking operation from user using speech
    speak("tell us the operation to be performed")
    audio()
    DATA=PYAUDIO[14:-3]
    


def get_audio():
    speak("do you want to select the voice input reply in yes or no")

    #function for speech recognition in offline module

    model = Model("C:/Users/Administrator/PycharmProjects/pythonProject2/vosk/vosk-model-small-en-in-0.4")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    time.sleep(1.5)
    speak("your audio is being captured")
    print("your voice is recorded")
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            speak("unable to recognizze your voice")
            time.sleep(1.5)
            speak("please try again")
            get_audio()

        elif recognizer.AcceptWaveform(data):
            PYAUDIO = recognizer.Result()
            choice = PYAUDIO[14:-3]
            print(PYAUDIO)
            time.sleep(2.5)
            break
    if choice=='yes':
        voice()
    elif choice=="no":
        speak("please while loading the digital calculator")
        digital()
    else:
        speak("please reply in yes or no")
        get_audio()

def EXIT():
    exIT = Toplevel()
    exIT.geometry("300x125")
    exIT.minsize(300, 125)
    exIT.maxsize(300, 125)
    exIT.Configure(bg="Black") 
    label1 = Label(exIT, text="Do You Want To EXIT ??? ", font={'bold', 'ariel'},fg="White")
    but1 = Button(exIT, text="YES", width=10,fg="Yellow",activebackground="blue",bg="Black", cursor="hand2") 
    but2 = Button(exIT, text="NO", width=10,fg="Yellow",activebackground="blue",bg="Black", cursor="hand2") 
    label1.grid(row=0, column=0, padx=50, pady=25, columnspan=4)
    but1.grid(row=2, column=1)
    but2.grid(row=2, column=2)
    exIT.mainloop()


def contact():
    filmenu = Menu(menu)
    menu.add_cascade(label='contact', menu=filmenu)
    filemenu.add_command(label='vishalsharma@gmail.com')


#main frame code
def mainframe():
    pradeep=Frame(vishal)
    gif4=Image.open("images - 2022-10-29T120216.392.jpeg")
    resize5=gif4.resize((450,300),Image.ANTIALIAS)
    image5=ImageTk.PhotoImage(resize5)
    lab7=Label(pradeep,image=image5)
    lab7.place(x=0,y=0)
    
    
    # upper options
    pradeep.config(bg='black')
    
    menu=Menu(vishal)
    filemenu = Menu(menu,tearoff=0)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=exIT)
    helpmenu = Menu(menu,tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About',command=contact)
    vishal.config(menu=menu)
    

    speak("you have sucessfully loaded the application")
    pradeep.after(ms=2000,func=get_audio) 

#defining th speak commands
def command1():
    speak("starting up")
    time.sleep(2.5)
    speak("please wait while loading the required files")

def destro():
    lab4.destory()


vishal=Tk()
vishal.title('Voice Age Calculator --> V.A.C')
vishal .geometry('300x150')
#JPEG=Image.open("vac.ico")
#JPEG1=ImageTk.PhotoImage(JPEG)
vishal.iconbitmap("vac.ico")
vishal.configure(bg='black')
image6=None
def nam():
    global lab8
    gif5 = Image.open('vac.jpg')
    resize6 = gif5.resize((150, 150), Image.ANTIALIAS)
    image6 = ImageTk.PhotoImage(resize6)
    lab8 = Label(vishal, image=image6)
nam()
lab8.pack()
time.sleep(1.5) 

#inserting image

gif2=Image.open("images - 2022-10-29T120010.636.jpeg")
resize2=gif2.resize((300,150),Image.ANTIALIAS)
image2=ImageTk.PhotoImage(resize2) 

lab5=Label(vishal,image=image2)

lab4=Label(vishal,text="Starting up ...",width=150,cursor="watch",fg='red',bg='blue', font={"arial",28,"bold"},relief=SUNKEN)

lab5.place(x=0,y=0)
#lab4.grid(row=7,column=10)
lab4.pack(side='bottom',anchor='center')
vishal.after(ms=12000,fun=destro)
vishal.after(ms=12999,func=mainframe)
vishal.after(ms=200,func=command1)
vishal.mainloop()

# hi thanks
