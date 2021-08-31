from tkinter import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from time import strftime
import tkinter.messagebox


options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\V VAMSI MOHAN\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

win = Tk()
win.title('Whatsapp Bot')
win.geometry("1100x600")
win.config(background="black")

name=StringVar()
message=StringVar()
name1=StringVar()
message1=StringVar()
name2=StringVar()
message2=StringVar()
numberofmsg=StringVar()
hrs = StringVar()
mins = StringVar()

def sendmsgs():
    ch = webdriver.Chrome(options=options)
    ch.maximize_window()
    ch.get('https://web.whatsapp.com')
    sleep(20)
    search=ch.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
    search.send_keys(name.get())
    sleep(1)

    name_=ch.find_element_by_xpath(f'//span[@title="{name.get()}"]')
    name_.click()
    sleep(3)

    msg=ch.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    msg.send_keys(message.get())
    msg.send_keys(Keys.RETURN)
    sleep(2)
    ch.close()


def bulk():
    ch = webdriver.Chrome(options=options)
    ch.maximize_window()
    ch.get('https://web.whatsapp.com')
    sleep(20)

    search=ch.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
    search.send_keys(name1.get())
    sleep(1)

    name_=ch.find_element_by_xpath(f'//span[@title="{name1.get()}"]')
    name_.click()
    sleep(3)

    msg=ch.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    msg.click()
    sleep(2)

    for _ in range(int(numberofmsg.get())):
        msg.send_keys(message1.get())
        msg.send_keys(Keys.RETURN)

    sleep(2)
    ch.close()

def sendmsg(present):
    if hrs.get() >= '24' or hrs.get() < '0' or mins.get() > '59' or mins.get() < '0':
        error()
    else:
        while True:
            pre = strftime('%H:%M')
            if pre == present:
                ch = webdriver.Chrome(options=options)
                ch.maximize_window()
                ch.get('https://web.whatsapp.com')
                sleep(20)
                search = ch.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
                search.send_keys(name2.get())
                sleep(1)

                name_ = ch.find_element_by_xpath(f'//span[@title="{name2.get()}"]')
                name_.click()
                sleep(3)

                msg = ch.find_element_by_xpath(
                    '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
                msg.send_keys(message2.get())
                msg.send_keys(Keys.RETURN)
                sleep(2)
                ch.close()


def correct():
    present = hrs.get() + ":" + mins.get()
    sendmsg(present)


def error():
    tkinter.messagebox.showerror("Invalid Time",
                                 hrs.get() + " : " + mins.get() + " is not a Valid Time\nPlease enter a Valid Time")



f1 = Frame(win, background="aqua", highlightbackground="aqua")
f1.place(x=50, y=150, width=300, height=265)
canva = Canvas(f1, width=500, height=270, background="black")
canva.pack()

f2 = Frame(win, background="#2aa19d", highlightbackground="#2aa19d")
f2.place(x=400, y=150, width=310, height=265)
canva1 = Canvas(f2, width=500, height=270, background="black")
canva1.pack()

f3 = Frame(win, background="#2aa19d", highlightbackground="#2aa19d")
f3.place(x=750, y=150, width=310, height=265)
canva2 = Canvas(f3, width=500, height=270, background="black")
canva2.pack()

head = Label(win, text="W h a t s a p p  B O T", font=('Californian FB', 32, "bold","underline"), background="black", fg='aqua')
head.pack(anchor="center")

msg = Label(text="Name of the contact :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
msg.place(x=60, y=190)
entry = Entry(win, textvariable=name, font=15, bd='3')
entry.place(x=150, y=245)

msgs = Label(text="Message :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
msgs.place(x=60, y=290)
entr = Entry(win, textvariable=message, font=15,bd='3')
entr.place(x=150, y=340)

msg1 = Label(text="Name of the contact :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
msg1.place(x=410, y=170)
entry1 = Entry(win, textvariable=name1, font=15, bd='3')
entry1.place(x=510, y=215)

msgs1 = Label(text="Message :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
msgs1.place(x=410, y=250)
entr1 = Entry(win, textvariable=message1, font=15, bd='3')
entr1.place(x=510, y=290)

number=Label(text="Number of messages :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
number.place(x=410, y=330)
num1 = Entry(win, textvariable=numberofmsg, font=15, bd='3')
num1.place(x=510, y=370)

msg2 = Label(text="Name of the contact :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
msg2.place(x=760, y=170)
entry2 = Entry(win, textvariable=name2, font=15, bd='3')
entry2.place(x=860, y=215)

msgs2 = Label(text="Message :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
msgs2.place(x=760, y=250)
entr2 = Entry(win, textvariable=message2, font=15, bd='3')
entr2.place(x=860, y=290)

time=Label(text="Time to send :", font=('Californian FB', 18, "bold"), background="black", fg='aqua')
time.place(x=760, y=330)
hour = Entry(win, textvariable=hrs, font=15, width=3, bd='3')
hour.place(x=900, y=370)
semi = Label(text=" : ", font=('Comic Sans MS', 20, "bold"), background="black", fg='White')
semi.place(x=940, y=360)
minute = Entry(win, textvariable=mins, font=15, width=3, bd='3')
minute.place(x=980, y=370)

 

set = Button(text="Send Message",command=sendmsgs, font=('Californian FB', 15,"bold"), bg='aqua', fg='black')
set.place(x=140, y=500)

set = Button(text="Send Message",command=bulk, font=('Californian FB', 15,"bold"), bg='aqua', fg='black')
set.place(x=490, y=500)

set = Button(text="Send Message",command=correct, font=('Californian FB', 15,"bold"), bg='aqua', fg='black')
set.place(x=830, y=500)


win.mainloop()
