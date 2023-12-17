from tkinter import *
med= Tk()
med.geometry('1000x500+175+95')
med.title('DATABEASE CONTROLLS')
med.configure(background="#FCF5ED")
med.resizable(False,False)
med.iconbitmap('images/db.ico')
title= Label(med , text=('Database Controlls System'),bg='#1F1717',fg='white',font=('Bauhaus 93',15,'bold'))
title.pack(fill=X)
def hhh():
  F1= Frame(med,bg='#EBE3D5')
  F1.place(x=0,y=50,width=1000,height=450)

  title_F1=Label(F1,text='Database Controlls',bg='#776B5D',fg='white',font=('Bauhaus 93',12))
  title_F1.pack(fill=X)

  
def ddd():
  F2= Frame(med,bg='#EBE3D5')
  F2.place(x=0,y=50,width=1000,height=450)

  title_F2=Label(F2,text='Tables Controlls',bg='#776B5D',fg='white',font=('Bauhaus 93',12))
  title_F2.pack(fill=X)

B1=Button(med,text='Creat database',bg='#F4BF96' ,command=hhh)
B1.place(x=0,y=28,width=150)

B2=Button(med,text='Creat Tables',bg='#F4BF96' ,command=ddd)
B2.place(x=150,y=28,width=150)


med.mainloop()