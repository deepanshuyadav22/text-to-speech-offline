#Imported Modules and Libraries-------------------------------------------

#to implement GUI
from tkinter import *

#to perform TTS
import pyttsx3

#to display heart at bottom right corner
import emoji

#Designing Main Window----------------------------------------------------

#creating main window
w = Tk()

#title of main window
w.title("Text to Speech")

#size of main window
w.geometry("765x500")

#background colour of main window
w.configure(background = '#fff')

#'engine' is just a variable name. We can change it anytime if require.
#creating/initializing an object for text to speech
engine = pyttsx3.init()

#Functions Section--------------------------------------------------------

#function to perform text-to-speech
def order_to_speech(event):
    r = int(rate.get()) #getting speed of output voice

    v = float(volume.get()/100) #getting volume of output voice
    if r == 0: #setting volume to zero if speed of output voice is set to zero
        v = 0

    s = str(text.get()) #getting text to speech

    engine.setProperty('rate', r) #setting speed of output voice
    engine.setProperty('volume', v) #setting volume of output voice
    engine.say(s) #speaking the entered text
    engine.runAndWait()

#function to save output voice as a audio (i.e. MP3) file
def save_as_mp3(event):
    r = int(rate.get())

    v = float(volume.get()/100)
    if r == 0:
        v = 0

    s = str(text.get())

    engine.setProperty('rate', r)
    engine.setProperty('volume', v)
    engine.save_to_file(s, 'TTS.mp3') #saving the MP3 file
    engine.runAndWait()

#Heading Section----------------------------------------------------------

heading = Label(w, text= "Text  to  Speech", bg = '#fff', font = ('algerian', 25))
heading.config(pady = 35)
heading.pack()

#Lables-------------------------------------------------------------------

label_enterText = Label(w, text = "Enter the text:", bg = '#fff', font = ('segoeui', 14))
label_setSpeed = Label(w, text = "Set the speed:", bg = '#fff', font = ('segoeui', 14))
label_setVolume = Label(w, text = "Set the volume:", bg = '#fff', font = ('segoeui', 14))

label_enterText.pack()
label_setSpeed.pack()
label_setVolume.pack()

label_enterText.place(x = 50, y = 120)
label_setSpeed.place(x = 50, y = 200)
label_setVolume.place(x = 50, y = 300)

#Input Section------------------------------------------------------------

#entry widget to take text
text = Entry(width = '50', font = ('calibri', 14), bg = '#f1f1f1', borderwidth = '0')
text.place(x = 200, y = 122)

#slider to adjust speed of output voice
rate = Scale(w, from_ = 0, to = 500, tickinterval = 100, orient = HORIZONTAL, width = 10, length = 496, bg = '#fff', font = ('calibri', 14))

#setting defualt value of speed of output voice (best range 120 to 150)
rate.set(150)

rate.place(x = 200, y = 180)

#slider to adjust volume of output voice
volume = Scale(w, from_ = 0, to = 100, tickinterval = 20, orient = HORIZONTAL, width = 10, length = 496, bg = '#fff', font = ('calibri', 14))

#setting defualt value of volume of output voice
volume.set(100)

volume.place(x = 200, y = 280)

#Buttons------------------------------------------------------------------

button_orderToSpeech = Button(w, text = "Order to Speech", width = 15, height = 2, bg = '#077bff', fg = '#fff', font = ('centurygothic', 14), bd = 0)
button_saveAsMP3 = Button(w, text = "Save as MP3", width = 15, height = 2, bg = '#077bff', fg = '#fff', font = ('centurygothic', 14), bd = 0)

button_orderToSpeech.pack()
button_saveAsMP3.pack()

button_orderToSpeech.bind('<Button-1>', order_to_speech)
button_saveAsMP3.bind('<Button-1>', save_as_mp3)

button_orderToSpeech.place(x = 195, y = 390)
button_saveAsMP3.place(x = 395, y = 390)

#Developer----------------------------------------------------------------

label_developer = Label(w, text = emoji.emojize("Created with :red_heart: by Deepanshu"), bg = '#fff', font = ('verdana', 12))
label_developer.pack()
label_developer.place(x = 510, y = 470)

#-------------------------------------------------------------------------

w.mainloop()
