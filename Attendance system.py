import speech_recognition as SR
from tkinter import *
import mysql.connector as mys
import MySQLvoice

mycon=mys.connect(host='localhost',user='root',passwd='1234',database='attendancedb')
mycursor=mycon.cursor()
mycursor.execute('create database project')
mycursor.execute('''create table details
(rollno varchar(9) primary key,
name varchar(20),
voice blob(10000)''')
root=Tk()
root.geometry("500x500")
root.title("Voice Recognition Attendance System")
student_name=Label(root, text="Enter student name",font="Courier 12 ").place(x=20,y=70)
student_name_area=Entry(root, width=30).place(x=210,y=70)
student_rollno=Label(root, text="Enter student Rollno",font="Courier 12 ").place(x=20,y=150)
student_rollno_area=Entry(root, width=20).place(x=230,y=150)
submit_button = Button(root, text = "Submit").place(x = 50,y = 250)

r = SR.Recognizer()

# Using system microphone for Input audio
with SR.Microphone() as source:
    # Adjusting energy threshold value
    r.adjust_for_ambient_noise(source)

    # Listening and storing voice input
    print("Listening...")
    audio = r.listen(source)

    # Recognizing audio speech based on internet speed and storing it in voicenote variable
    print("Recognizing...")
    voicenote = r.recognize_google(audio)

# Printing the input
print("User Said : ", voicenote)

# Passing voicenote in mySQLvoice Library
print(MySQLvoice.query(voicenote))
root.mainloop()
