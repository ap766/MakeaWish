import tkinter as tk
from tkinter import*
def clicked():
    Remove_Buttons(button)
def raise_frame(frame):
    frame.tkraise()
    command=clicked
root=tk.Tk()
root.geometry("1350x700")
root.title("dreams come true")
root.configure()
Home=tk.Frame(root)
facilities=tk.Frame(root,width=1300,height=1400,relief='raised',borderwidth=10)
about=tk.Frame(root,width=300,height=400,relief='raised',borderwidth=10)
fulfiller=tk.Frame(root,width=300,height=400,relief='raised',borderwidth=10)
wish=tk.Frame(root,width=700,height=900,relief='raised',borderwidth=10)
flogin=tk.Frame(root,width=700,height=900,relief='raised',borderwidth=10)
wlogin=tk.Frame(root,width=700,height=900,relief='raised',borderwidth=10)
ORG=tk.Frame(root,width=700,height=900,relief='raised',borderwidth=10)
delete=tk.Frame(root,width=300,height=400,borderwidth=10)
f2=tk.Frame(root,width=300,height=400,borderwidth=10)
organiser=tk.Frame(root)
Home=tk.Frame(root)
C =Canvas(Home, bg="blue", height=1, width=1)
filename = PhotoImage(file = r"C:\Users\lenovo\Pictures\reach-touch-star-human-hand-touching-finger-sky-94900910.png")
background_label =Label(Home, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
for frame in(Home,facilities,about,fulfiller,wish,flogin,wlogin,organiser,delete,f2,ORG):
    frame.grid(row=1,column=0,sticky='new')
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

title_label = tk.Label(facilities, text = 'FACILITIES', font=('calibre',15,'bold'))
title_label.pack(padx=5,pady=0)
intr_label = tk.Label(facilities, text = 'Dreams Come True headquaters is a 15 storey building standing tall on the bangalore avenue welcoming people from all walks of life to join us in this fulfilling journey of dreaming and believing. ', font=('calibre',10))
intr_label.pack(padx=5,pady=0)

img4a =tk.PhotoImage(file=r"C:\Users\lenovo\Pictures\building - Copy (2).png")
pimg4=img4a.subsample(0,0)
button40=tk.Button(facilities,image=img4a,compound='left',width='0',height='0',font="Times 23 bold",activeforeground='black').pack(padx=5,pady=5)#

intr1_label = tk.Label(facilities, text = 'In keeping with the spirit of a tranquil and inviting nature of the organisation, the doors open to a furnished lobby facing an aesthetic green wall', font=('calibre',10,))
intr1_label.pack(padx=6,pady=0)
intr2_label = tk.Label(facilities, text = 'gracing the lift adjacent to a lucent waiting area with comfortable seating arrangements for all visitors. The reception backed by a polished wall listing', font=('calibre',10))
intr2_label.pack(padx=7,pady=0)
intr3_label = tk.Label(facilities, text = 'our innumerable achievements and empowering ambitions is organised into a spacious counter accomodating a helpdesk led by a team of our professionals happy to answer all queries', font=('calibre',10))
intr3_label.pack(padx=8,pady=0)
intr4_label = tk.Label(facilities, text = 'and guide all visitors in the best manner possible by offering excellent insights', font=('calibre',10))
intr4_label.pack(padx=9,pady=0)
img5a =tk.PhotoImage(file=r"C:\Users\lenovo\Pictures\reception - Copy (3).png")
pimg5=img5a.subsample(0,0)
button50=tk.Button(facilities,image=img5a,compound='left',width='0',height='0',font="Times 23 bold",activeforeground='black').pack(padx=6,pady=5)#
intr5_label = tk.Label(facilities, text = 'The invaluable assets of the organisation are undoubtedly the volunteers whose sincerity and dedication uplifts this noble cause further.  ', font=('calibre',10))
intr5_label.pack(padx=10,pady=0)
intr6_label = tk.Label(facilities, text = 'To further encourage their admirable work, their workspace is designed to offer a collaborative and engaging work environment surrounded by flexible and supportive coworkers creating a heathy and interactive atmosphere.  ', font=('calibre',10))
intr6_label.pack(padx=11,pady=0)
img6a =tk.PhotoImage(file=r"C:/Users/lenovo/Pictures/office,.png")
pimg6=img6a.subsample(0,0)
buttonX=tk.Button(facilities,text='back',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(Home))
buttonX.pack(side='bottom')
button60=tk.Button(facilities,image=img6a,compound='left',width='0',height='0',font="Times 23 bold",activeforeground='black').pack(padx=7,pady=5)#
button=tk.Button(Home,text='DREAMS COME TRUE  ',width='0',height='0',activebackground='Pink1',bg='azure',font="Times 30 bold",activeforeground='black').pack(side="top",expand=True,padx=0,pady=0)
button=tk.Button(Home,text='   FACILITIES   ',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(facilities)).pack(side="top",expand=True,padx=0,pady=10)
button=tk.Button(Home,text='     ABOUT    ',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(about)).pack(side="top",padx=10,pady=10)
button=tk.Button(Home,text='GRANT A WISH',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(fulfiller)).pack(side="top",expand=True,padx=20,pady=10)
buttond=tk.Button(Home,text='MAKE A WISH',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(wish)).pack(side="top",expand=True,padx=20,pady=10)
buttone=tk.Button(Home,text='LOGIN AS FULFILLER',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(flogin)).pack(side="top",expand=True,padx=20,pady=10)
buttond=tk.Button(Home,text='LOGIN AS WISHMAKER',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(wlogin)).pack(side="top",expand=True,padx=20,pady=10)
buttond=tk.Button(Home,text='LOGIN AS ORGANISER',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(ORG)).pack(side="top",expand=True,padx=20,pady=10)
buttonA=tk.Button(fulfiller,text='back',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(Home))
buttonA.grid(row=20,column=0)
import mysql.connector as sqltor
import numpy as np
from matplotlib.pyplot import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
mycon = sqltor.connect(host="localhost", user="root", passwd="bcgs",database='dreams_come_true1')
a=b=c=d=0
cursor=mycon.cursor()
cursor.execute("select * from make_a_wish")
data=cursor.fetchall()
count=cursor.rowcount
for row in data:
   if row[3]<12:
      a=a+1
   elif row[3]>12 and row[3]<=17:
      b=b+1
   elif row[3]<65 and row[3]>18:
      c=c+1
   else:
      d=d+1
z=[a,b,c,d]
Age=['<12','12-17','18+','>65']
values=[a,b,c,d]
actualFigure = figure(figsize = (2,2))
actualFigure.suptitle("Age wise distribution", fontsize = 10)
explode = list()
for k in Age:
    explode.append(0.1)
title_label = tk.Label(about, text = 'ABOUT', font=('calibre',15,'bold'))
title_label.pack(padx=5,pady=0)
intro1_label = tk.Label(about, text = '"Dreams Come True" is a locally based wish granting organisation dedicated to using the power of a dream to bring hope and joy to every citizen battling with a physical disability.', font=('calibre',10))
intro1_label.pack(padx=10,pady=0)
intro2_label=tk.Label(about,text='Dreams come in all shapes and sizes, serving as a momentary reprieve from the doctors tests, medical treatments and hospital visits.', font=('calibre',10))
intro2_label.pack(padx=10,pady=0)
intro3_label=tk.Label(about,text='They go a long way in inspiring courage to battle every hardship coming our way, spreading positivity and in keeping the flames of hope glowing warm and strong as we strive to become the best versions of ourselves.',font=('calibre',10))
intro3_label.pack(padx=10,pady=0)
intro4_label=tk.Label(about,text='Heres to celebrating the Dreamer and Believer in each one of us.',font=('calibre',10))
intro4_label.pack(padx=10,pady=0)
chart_label=tk.Label(about,text="Statistics of development of organisation in the past decade",font=('calibre',15,"bold"))
chart_label.pack(padx=10,pady=0)
chart1_label=tk.Label(about,text="Dreams Come True has dedicated its efforts towards fulfilling dreams of individuals of every age group likewise owing to our firm belief in the ageless and limitless power of dreaming and believing",font=('calibre',10))
chart1_label.pack(padx=10,pady=0)
pie= pie(values, labels=Age , explode = explode, shadow=True)
gender_label = tk.Label(about, text = '<12:children, 12-17:teenagers, 18+:adults,+65:seniors', font=('calibre',10,'bold'))
canvas = FigureCanvasTkAgg(actualFigure, about)
canvas.get_tk_widget().pack(padx=1,pady=0)
canvas.draw()
gender_label.pack(padx=2,pady=2)
team_label = tk.Label(about, text = 'NOTE FROM THE DIRECTOR', font=('calibre',15,'bold'))
team_label1 = tk.Label(about, text = '"Hope lies in dreams, in imagination, and in the courage of those who dare to make dreams into reality.Let your hopes, not your hurts, shape your future.”', font=('calibre',10,'bold'))
team_label.pack(padx=5,pady=0)
img4 =tk.PhotoImage(file=r"C:/Users/lenovo/Pictures/mickey mousea.png")
pimg4=img4.subsample(0,0)
button4=tk.Button(about,image=img4,compound='left',justify='right',width='0',height='0',font="Times 23 bold",activeforeground='black').pack(padx=5,pady=5)#
team_label1.pack(padx=7,pady=0)
button=tk.Button(about,text='back',width='0',height='0',activebackground='SlateGray1',bg='turquoise1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(Home)).pack(side="top",expand=True,padx=20,pady=20)
cursor=mycon.cursor()
first_name_var=tk.StringVar() 
last_name_var=tk.StringVar()
address_var1=tk.StringVar()
dob_var24=tk.StringVar()
age_var=tk.IntVar() 
phone_number_var11=tk.IntVar()
amount_willing_to_pay_var=tk.IntVar()
gender_var=tk.StringVar()
def submit(): 
   first_name=first_name_entry.get()  
   first_name_var.set("")
   last_name=last_name_entry.get()  
   last_name_var.set("")
   address1=address_entry1.get()  
   address_var1.set("")
   dob24=dob_entry24.get()  
   dob_var24.set("")
   age=age_entry.get()
   age_var.set("")
   phone_number11=phone_number_entry11.get()
   phone_number_var11.set("")
   amount_willing_to_pay=amount_willing_to_pay_entry.get()
   amount_willing_to_pay_var.set("")
   gender=gender_entry.get()  
   gender_var.set("")
   
   st="insert into grant_a_wish1(Name,email,address, dob, age, phone_number, amount_willing_to_pay,password) values('{}','{}','{}','{}',{},{},{},'{}')".format(first_name,last_name,address1,dob24,age,phone_number11, amount_willing_to_pay,gender)
   
   cursor.execute(st)
   mycon.commit()

first_name_label = tk.Label(fulfiller, text = 'Name', font=('calibre',10,'bold'))
first_name_entry = tk.Entry(fulfiller, textvariable = first_name_var,font=('calibre',10,'normal'))
last_name_label = tk.Label(fulfiller, text = 'Email ', font=('calibre',10,'bold'))
last_name_entry = tk.Entry(fulfiller, textvariable =last_name_var ,font=('calibre',10,'normal'))
address_label1 = tk.Label(fulfiller, text = 'Address', font=('calibre',10,'bold'))
address_entry1 = tk.Entry(fulfiller, textvariable = address_var1,font=('calibre',10,'normal'))
dob_label24 = tk.Label(fulfiller, text = 'Date Of Birth(yyyy-mm-dd)', font=('calibre',10,'bold'))
dob_entry24 = tk.Entry(fulfiller, textvariable = dob_var24,font=('calibre',10,'normal'))
age_label = tk.Label(fulfiller, text = 'Age', font=('calibre',10,'bold'))
age_entry = tk.Entry(fulfiller, textvariable = age_var,font=('calibre',10,'normal'))
phone_number_label11 = tk.Label(fulfiller, text = 'Phone Number', font=('calibre',10,'bold'))
phone_number_entry11 = tk.Entry(fulfiller, textvariable = phone_number_var11,font=('calibre',10,'normal'))
amount_willing_to_pay_label = tk.Label(fulfiller, text = 'Amount Paid', font=('calibre',10,'bold'))
amount_willing_to_pay_entry = tk.Entry(fulfiller, textvariable = amount_willing_to_pay_var,font=('calibre',10,'normal'))
gender_label = tk.Label(fulfiller, text = 'Password', font=('calibre',10,'bold'))
gender_entry = tk.Entry(fulfiller, textvariable = gender_var,font=('calibre',12,'normal'))  
sub_btn=tk.Button(fulfiller,text = 'Submit', command = submit)
welcome_label = tk.Label(fulfiller, text = '  WELCOME TO THE DREAMS COME TRUE FAMILY' ,font=('calibre',15))
welcome1_label=tk.Label(fulfiller,text=', KINDLY ENTER YOUR CREDENTIALS CAREFULLY',font=('calibre',15))
thank_label = tk.Label(fulfiller, text = 'THANK YOU FOR THIS GENEROUS CONTRIBUTION.' ,font=('calibre',15))
thank1_label=tk.Label(fulfiller,text='WE ARE DEEPLY GRATEFUL FOR YOUR SUPPORT.',font=('calibre',15))
thank2_label=tk.Label(fulfiller,text='ALSO, KEEP DREAMING AND KEEP BELIEVING.  ',font=('calibre',15))
first_name_label.grid(row=1,column=0)
first_name_entry.grid(row=1,column=1,padx=0, pady=15)
last_name_label.grid(row=2,column=0)
last_name_entry.grid(row=2,column=1,padx=0, pady=15)
address_label1.grid(row=3,column=0)
address_entry1.grid(row=3,column=1,ipadx=120, ipady=15)
dob_label24.grid(row=5,column=0)
dob_entry24.grid(row=5,column=1,padx=0, pady=15)
age_label.grid(row=6,column=0)
age_entry.grid(row=6,column=1,padx=0, pady=15)
phone_number_label11.grid(row=7,column=0)
phone_number_entry11.grid(row=7,column=1,padx=0, pady=15)
amount_willing_to_pay_label.grid(row=8,column=0)
amount_willing_to_pay_entry.grid(row=8,column=1,padx=0, pady=15)
gender_label.grid(row=9,column=0)
gender_entry.grid(row=9,column=1,padx=0, pady=15)
sub_btn.grid(row=10,column=1)
welcome_label.grid(row=0,column=0)
welcome1_label.grid(row=0,column=1)
thank_label.grid(row=11,column=0)
thank1_label.grid(row=11,column=1)
thank2_label.grid(row=12,column=0)
def submit2():
   name=name_entry.get()  
   name_var.set("")
   address=address_entry.get()  
   address_var.set("")
   dob1=dob_entry1.get()  
   dob_var1.set("")
   age1=age_entry1.get()
   age_var1.set("")
   disease=disease_entry.get()  
   disease_var.set("")
   wish=wish_entry.get() 
   wish_var.set("") 
   phone_number=phone_number_entry.get()
   phone_number_var.set("") 
   usernamez=username_entryz.get() 
   username_varz.set("")
   password=password_entry.get() 
   password_var.set("")
   st="insert into make_a_wish(name,address,dob,age,disease,wish,phoneno,email,password) values('{}','{}','{}',{},'{}','{}',{},'{}','{}')".format(name,address,dob1,age1,disease,wish,phone_number,usernamez,password)  
   cursor.execute(st)
   mycon.commit()
name_var=tk.StringVar()
address_var=tk.StringVar()
dob_var1=tk.StringVar()
age_var1=tk.IntVar()
disease_var=tk.StringVar()
username_varz=tk.StringVar()
password_var=tk.StringVar()
wish_var=tk.StringVar()
phone_number_var=tk.IntVar()
name_label = tk.Label(wish, text = 'Name', font=('calibre',10,'bold'))
name_entry = tk.Entry(wish, textvariable = name_var,font=('calibre',10,'normal'))
address_label = tk.Label(wish, text = 'Address', font=('calibre',10,'bold'))
address_entry = tk.Entry(wish, textvariable = address_var,font=('calibre',10,'normal')) 
dob_label1 = tk.Label(wish, text = 'Date of Birth(yyyy-mm-dd)', font=('calibre',10,'bold'))
dob_entry1= tk.Entry(wish, textvariable = dob_var1,font=('calibre',10,'normal'))
age_label1 = tk.Label(wish, text = 'Age', font=('calibre',10,'bold'))
age_entry1 = tk.Entry(wish, textvariable = age_var1,font=('calibre',10,'normal')) 
disease_label = tk.Label(wish, text = 'Disability', font=('calibre',10,'bold'))
disease_entry = tk.Entry(wish, textvariable = disease_var,font=('calibre',10,'normal'))
username_labelz = tk.Label(wish, text = 'Username', font=('calibre',10,'bold'))
username_entryz = tk.Entry(wish, textvariable = username_varz,font=('calibre',10,'normal'))
password_label = tk.Label(wish, text = 'Password', font=('calibre',10,'bold'))
password_entry = tk.Entry(wish, textvariable = password_var,font=('calibre',10,'normal'))
phone_number_label = tk.Label(wish, text = 'Phone Number', font=('calibre',10,'bold'))
phone_number_entry = tk.Entry(wish, textvariable = phone_number_var,font=('calibre',10,'normal'))
wish_label = tk.Label(wish, text = 'Wish', font=('calibre',10,'bold'))
wish_entry = tk.Entry(wish, textvariable = wish_var,font=('calibre',10,'normal'))
welcome_label = tk.Label(wish, text = '  WELCOME TO THE DREAMS COME TRUE FAMILY' ,font=('calibre',15))
welcome1_label=tk.Label(wish,text=', KINDLY ENTER YOUR CREDENTIALS CAREFULLY',font=('calibre',15))
thank_label = tk.Label(wish, text = 'DATA RECORDED, THANK YOU FOR MAKING A WISH.' ,font=('calibre',15))
thank1_label=tk.Label(wish,text='OUR TEAM WILL GET BACK TO YOU VERY SOON.',font=('calibre',15))
thank2_label=tk.Label(wish,text='UNTIL THEN, KEEP DREAMING AND KEEP BELIEVING ',font=('calibre',15))
sub_btn=tk.Button(wish,text = 'Submit', command = submit2)
name_label.grid(row=1,column=0)
welcome_label.grid(row=0,column=0)
welcome1_label.grid(row=0,column=1)
thank_label.grid(row=11,column=0)
thank1_label.grid(row=11,column=1)
thank2_label.grid(row=12,column=0)
name_entry.grid(row=1,column=1,padx=0, pady=15) 
address_label.grid(row=2,column=0) 
address_entry.grid(row=2,column=1,ipadx=120, ipady=15)
dob_label1.grid(row=3,column=0) 
dob_entry1.grid(row=3,column=1,padx=0, pady=15)
age_label1.grid(row=4,column=0) 
age_entry1.grid(row=4,column=1,padx=0, pady=15)
disease_label.grid(row=5,column=0) 
disease_entry.grid(row=5,column=1)
username_labelz.grid(row=6,column=0)
username_entryz.grid(row=6,column=1,padx=0, pady=15)
password_label.grid(row=7,column=0)
password_entry.grid(row=7,column=1,padx=0, pady=15)
phone_number_label.grid(row=8,column=0)
phone_number_entry.grid(row=8,column=1,padx=0, pady=15)
wish_label.grid(row=9,column=0)
wish_entry.grid(row=9,column=1,ipadx=120, ipady=15)
sub_btn.grid(row=10,column=1,ipadx=0, ipady=15)
buttonC=tk.Button(wish,text='back',width='0',height='0',activebackground='turquoise',bg='turquoise1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(Home))
buttonC.grid(row=100,column=0)
def submit3():
   username21=username_entry21.get() 
   username21_var.set("") 
   password21=password_entry21.get() 
   password21_var.set("")
   print(username21)
   print(password21)
   st="select * from grant_a_wish1  where email='{}' and password='{}' ".format(username21,password21)
   cursor.execute(st)
   e=cursor.fetchall()
   print(e)
   print('z')
   for row in e:
       print(row)
       z=tk.Label(flogin,text=row)
       z.grid(row=3,column=0)
   mycon.commit()
username21_var=tk.StringVar()
password21_var=tk.StringVar()
username_label21 = tk.Label(flogin, text = 'Username', font=('calibre',10,'bold'))
username_entry21=tk.Entry(flogin, textvariable = username21_var,font=('calibre',10,'normal'))
password_label21 = tk.Label(flogin, text = 'Password', font=('calibre',10,'bold'))
password_entry21= tk.Entry(flogin, textvariable = password21_var,font=('calibre',10,'normal'))
sub_btnA=tk.Button(flogin,text = 'Submit', command = submit3)
username_label21.grid(row=0,column=0)
username_entry21.grid(row=0,column=1)
password_label21.grid(row=1,column=0)
password_entry21.grid(row=1,column=1)
sub_btnA.grid(row=10,column=1)
def submit4():
   username1=username1_entry.get() 
   username1_var.set("")
   password1=password1_entry.get() 
   password1_var.set("")
   i=(username1,password1)
   st="select * from make_a_wish  where email='{}' and password='{}' ".format(username1,password1)
   cursor.execute(st)
   d=cursor.fetchall()
   for row in d:
       print(row)
       z=tk.Label(wlogin,text=row)
       z.grid(row=3,column=0)
   mycon.commit()
username1_var=tk.StringVar()
password1_var=tk.StringVar()
username1_label = tk.Label(wlogin, text = 'Username', font=('calibre',10,'bold'))
username1_entry = tk.Entry(wlogin, textvariable = username1_var,font=('calibre',10,'normal'))
password1_label = tk.Label(wlogin, text = 'Password', font=('calibre',10,'bold'))
password1_entry = tk.Entry(wlogin, textvariable = password1_var,font=('calibre',10,'normal'))
sub_btn=tk.Button(wlogin,text = 'Submit', command = submit4)
username1_label.grid(row=0,column=0)
username1_entry.grid(row=0,column=1)
password1_label.grid(row=1,column=0)
password1_entry.grid(row=1,column=1)
sub_btn.grid(row=10,column=1)
sub_btn2=tk.Button(organiser,text = 'Update table grant a wish',command=lambda:raise_frame(delete))
sub_btn1=tk.Button(organiser,text = 'Update table make a wish',command=lambda:raise_frame(f2))
buttonz=tk.Button(organiser,text='Back To Home Page',width='0',height='0',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(Home))
sub_btn2.grid(row=7,column=0,ipadx=12,ipady=12)
sub_btn1.grid(row=5,column=0,ipadx=12,ipady=12)
buttonz.grid(row=100,column=0)
def submit6():
   st="select * from grant_a_wish1"
   cursor.execute(st)
   d=cursor.fetchall()
   z=tk.Label(organiser,text=d)
   z.grid(row=3,column=0)
   mycon.commit()
def submit7():
   st="select * from make_a_wish"
   cursor.execute(st)
   d=cursor.fetchall()
   z=tk.Label(organiser,text=d)
   z.grid(row=2,column=0)
   mycon.commit()
sub_btn=tk.Button(organiser,text = 'View table grant a wish', command = submit6)
sub_btn.grid(row=0,column=0,ipadx=12,ipady=12)
sub_btnaa=tk.Button(organiser,text = 'View table make a wish', command = submit7)
sub_btnaa.grid(row=1,column=0,ipadx=12,ipady=12)
def close_window():
    organiser.destroy()#
def submit1():
   username=username_entry2.get() 
   username_var2.set("")
   sname=s_entry.get()
   s_var.set("")
   
   st1="update make_a_wish set status='{}' where email='{}'".format(sname,username)
   cursor.execute(st1)
   mycon.commit()
s_var=tk.StringVar()
username_var2=tk.StringVar()
username_label2= tk.Label(f2, text = 'Email', font=('calibre',10,'bold'))
username_entry2 = tk.Entry(f2, textvariable = username_var2,font=('calibre',10,'normal'))
#sub_btn1=tk.Button(f2,text = 'update a record',command=submit1)
username_label2.grid(row=7,column=0)
username_entry2.grid(row=7,column=1)
Status= tk.Label(f2, text = 'New Status', font=('calibre',10,'bold'))
s_entry = tk.Entry(f2, textvariable = s_var,font=('calibre',10,'normal'))
blank_label = tk.Label(f2, text = '', font=('calibre',10,'bold'))
blank_label.grid(row=13,column=0)
blank_label2 = tk.Label(f2, text = '', font=('calibre',10,'bold'))
blank_label2.grid(row=14,column=0)
blank_label3 = tk.Label(f2, text = '', font=('calibre',10,'bold'))
blank_label3.grid(row=25,column=0)
blank_label4 = tk.Label(f2, text = '', font=('calibre',10,'bold'))
blank_label4.grid(row=30,column=0)
blank_label5 = tk.Label(f2, text = '', font=('calibre',10,'bold'))
blank_label5.grid(row=34,column=0)
blank_label6 = tk.Label(f2, text = '', font=('calibre',10,'bold'))
blank_label6.grid(row=40,column=0)
blank_label7= tk.Label(f2, text = '', font=('calibre',10,'bold'))
blank_label7.grid(row=52,column=0)
sub_btn411=tk.Button(f2,text = 'Submit', command = submit1)
sub_btn411.grid(row=10,column=1,ipadx=12,ipady=12)
Status.grid(row=9,column=0)
s_entry.grid(row=9,column=1,ipadx=0,ipady=15)
button=tk.Button(f2,text='Back to Organisers page',width='0',height='0',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(organiser))
button.grid(row=16,column=1,ipadx=1,ipady=1)
def submit8():
   username=username_entry.get() 
   username_var.set("")
   sname2=s_entry2.get()
   s_var2.set("")
   st1="update grant_a_wish1 set status='{}' where email='{}'".format(sname2,username)
   cursor.execute(st1)
   mycon.commit()
s_var2=tk.StringVar()
blank_label = tk.Label(delete, text = '', font=('calibre',10,'bold'))
username_var=tk.StringVar()
username_label = tk.Label(delete, text = 'Email', font=('calibre',10,'bold'))
username_entry = tk.Entry(delete, textvariable = username_var,font=('calibre',10,'normal'))
Status2= tk.Label(delete, text = 'New Status', font=('calibre',10,'bold'))
s_entry2 = tk.Entry(delete, textvariable = s_var2,font=('calibre',10,'normal'))
button=tk.Button(delete,text='Back to Organisers page',width='0',height='0',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(organiser))
button.grid(row=14,column=1,ipadx=1,ipady=1)
blank_label.grid(row=13,column=0)
blank_label12 = tk.Label(delete, text = '', font=('calibre',10,'bold'))
blank_label12.grid(row=26,column=0)
blank_label13 = tk.Label(delete, text = '', font=('calibre',10,'bold'))
blank_label13.grid(row=39,column=0)
blank_label14 = tk.Label(delete, text = '', font=('calibre',10,'bold'))
blank_label14.grid(row=50,column=0)
blank_label15 = tk.Label(delete, text = '', font=('calibre',10,'bold'))
blank_label15.grid(row=60,column=0)
#sub_btn1=tk.Button(f2,text = 'update a record',command=lambda:raise_frame())
username_label.grid(row=7,column=0)
username_entry.grid(row=7,column=1)
Status2.grid(row=9,column=0)
s_entry2.grid(row=9,column=1,padx=0,pady=15)
sub_btn1.grid(row=25,column=0,ipadx=12,ipady=12)
sub_btn41=tk.Button(delete,text = 'Submit', command = submit8)
sub_btn41.grid(row=10,column=1,ipadx=12,ipady=12)
def submit5():
   username212=username_entry212.get() 
   username212_var.set("") 
   password212=password_entry212.get() 
   password212_var.set("")
   st="select * from organiser  where email='{}' and password='{}' ".format(username212,password212) 
   cursor.execute(st)
   e=cursor.fetchall()
   if e!=[]:
      buttonf1=tk.Button(ORG,text='ORGANISER',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(organiser))
      buttonf1.grid()
   mycon.commit()
username212_var=tk.StringVar()
password212_var=tk.StringVar()
username_label212 = tk.Label(ORG, text = 'Username', font=('calibre',10,'bold'))
username_entry212=tk.Entry(ORG, textvariable = username212_var,font=('calibre',10,'normal'))
password_label212 = tk.Label(ORG, text = 'Password', font=('calibre',10,'bold'))
password_entry212= tk.Entry(ORG, textvariable = password212_var,font=('calibre',10,'normal'))
sub_btnA=tk.Button(ORG,text = 'Submit', command = submit5)
username_label212.grid(row=0,column=0)
username_entry212.grid(row=0,column=1)
password_label212.grid(row=1,column=0)
password_entry212.grid(row=1,column=1)
sub_btnA.grid(row=10,column=1)
