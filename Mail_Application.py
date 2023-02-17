from tkinter import *
import smtplib

window  = Tk()
window.title('Mail Application')
def send():
    try: 
        username = temp_username.get()
        password = temp_password.get()
        to       = temp_receiver.get()
        subject  = temp_subject.get()
        body     = temp_body.get()
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username,to,finalMessage)
            notif.config(text="Email has been sent successfully", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")


def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete(0,'end')


Label(window, text="Email App", font=('Calibri',40)).grid(row=0, sticky=N)
Label(window, text="Please use the form below to send an email", font=('Calibri',20)).grid(row=1, sticky=W, padx=5 ,pady=10)

Label(window, text="Email", font=('Calibri', 20)).grid(row=2,sticky=W, padx=5)
Label(window, text="Password", font=('Calibri', 20)).grid(row=3,sticky=W, padx=5)
Label(window, text="To", font=('Calibri', 20)).grid(row=4,sticky=W, padx=5)
Label(window, text="Subject", font=('Calibri', 20)).grid(row=5,sticky=W, padx=5)
Label(window, text="Body", font=('Calibri', 20)).grid(row=6,sticky=W, padx=5)
notif = Label(window, text="", font=('Calibri', 20),fg="red")
notif.grid(row=7,sticky=S)


temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject  = StringVar()
temp_body     = StringVar()


usernameEntry = Entry(window,font=('Calibri', 15), textvariable = temp_username)
usernameEntry.grid(row=2,ipadx=28,column=0)
passwordEntry = Entry(window, show="*",font=('Calibri', 15), textvariable = temp_password)
passwordEntry.grid(row=3,ipadx=28,column=0)
receiverEntry  = Entry(window,font=('Calibri', 15), textvariable = temp_receiver)
receiverEntry.grid(row=4,ipadx=28,column=0)
subjectEntry  = Entry(window,font=('Calibri', 15), textvariable = temp_subject)
subjectEntry.grid(row=5,ipadx=28,column=0)
bodyEntry     = Entry(window,font=('Calibri', 15), textvariable = temp_body)
bodyEntry.grid(row=6,ipadx=28,column=0)


Button(window, text = "Send",font=('Calibri', 20), command = send).grid(row=7,   sticky=W,  pady=30, padx=30)
Button(window, text = "Reset",font=('Calibri', 20), command = reset).grid(row=7, padx=0, pady=30)

window.mainloop()