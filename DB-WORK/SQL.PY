from tkinter import *

import mysql.connector
from tkinter import messagebox
root = Tk()
root.geometry('1000x500+175+95')
root.title('DATABEASE CONTROLLS')
root.configure(background="#FCF5ED")
root.resizable(False,False)
root.iconbitmap('images/db.ico')
title= Label(root , text=('Database Controlls System'),bg='#1F1717',fg='white',font=('Bauhaus 93',15,'bold'))
title.pack(fill=X)


#----------------------SHOW DATABASES---------------------------------------------------------------
def show_dbs():
      conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
      )
      cur=conn.cursor()
      cur.execute('show databases')
      global F    #defin F in the global scop
      F=Frame(root,bg='#EBE3D5')
      F.place(x=830,y=219,width=170,height=300)
      title_Fr3=Label(F,text='Database Founds',bg='#CE5A67',fg='black',font=('Bauhaus 93',12))
      title_Fr3.pack(fill=X)

      for x in cur:
            Label(F,text=x).pack()
      #__________________________hade this function (show all database)_____________________________
def hade_F_frame():
      F.place_forget()      

#----------------------connect with server----------------------------------------------------------
def ser_connect():
      host     = E_server_name.get()
      user     = E_user_name.get()
      passw = E_password.get()
      try:
            conn = mysql.connector.connect(
                  host     = host,
                  user     = user,
                  password = passw
            )
            messagebox.showinfo('DB [system]','The server was connected without problems🤠')
      except mysql.connector.Error as r:
            messagebox.showerror('error',r)

#----------------------create databases-------------------------------------------------------------
def creat_database():
      name=E_name_db.get()
      try:
            conn= mysql.connector.connect(
             host     ='localhost',
              user     = 'root',
              password = ''
            )
            cur=conn.cursor()
            cur.execute(f'create database {name}')
            messagebox.showinfo('DB [system]','The Database was Create without problems🤠')
      except mysql.connector.Error as r:
            messagebox.showerror('Error',r)
#---------------------drop databases-----------------------------------------------------------------
def drop_database():
      name=E_name_db.get()
      response=messagebox.askyesno('DB [system]',f'Are you sure you want to Drop this Database {name}?')
      if response:
            try:
                  conn= mysql.connector.connect(
                   host     ='localhost',
                    user     = 'root',
                    password = ''
                  )
                  cur=conn.cursor()
                  cur.execute(f'drop database {name}')
                  messagebox.showinfo('DB [system]','The Database was Dropped without problems🤠.')
            except mysql.connector.Error as r:
                  messagebox.showerror('Error',r)           
      else:
            messagebox.showinfo('DB [sestem]','The Database was not Dropped.')

#----------------------create tabels----------------------------------------------------------------
def fitch_creat_tabel():
      def creat_tabel():
            bd_name = E_dbname.get()
            tb_name = E_tbname.get()
            cl_name = E_clname.get()
            cl_type = E_cltype.get()
            cl_lengt = E_clengt.get()
            
            try:
                  conn = mysql.connector.connect(
                        host     = 'localhost',
                        user     = 'root',
                        password = ''
                  )
                  cur=conn.cursor()
                  cur.execute(f'USE {bd_name}; CREATE TABLE {tb_name} (id {cl_type}({cl_lengt}) PRIMARY KEY)')
                  #conn.commit()
                  #conn.close()
                  messagebox.showinfo('DB [system]','The tables was create without problems🤠')
            except mysql.connector.Error as r:
                  messagebox.showerror('error',r)
      global F2
      F2=Frame(root,bg='#EBE3D5')
      F2.place(x=0,y=219,width=209,height=300)
      title_Fr2=Label(F2,text='Create Tables',bg='#CE5A67',fg='black',font=('Bauhaus 93',12))
      title_Fr2.pack(fill=X)
      
      L_dbname=Label(F2,text='Name DB :',bg='#EBE3D5')
      L_dbname.place(x=2,y=37)
      E_dbname=Entry(F2,bg='#F4DFC8')
      E_dbname.place(x=70,y=37,width=130,height=25)

      L_tbname=Label(F2,text='Name TB :',bg='#EBE3D5')
      L_tbname.place(x=2,y=74)
      E_tbname=Entry(F2,bg='#F4DFC8')
      E_tbname.place(x=70,y=74,width=130,height=25)

      L_clname=Label(F2,text='Name CL :',bg='#EBE3D5')
      L_clname.place(x=2,y=111)
      E_clname=Entry(F2,bg='#F4DFC8')
      E_clname.place(x=70,y=111,width=130,height=25)

      L_cltype=Label(F2,text='Type Cl :',bg='#EBE3D5')
      L_cltype.place(x=2,y=148)
      E_cltype=Entry(F2,bg='#F4DFC8')
      E_cltype.place(x=70,y=148,width=130,height=25)

      L_clengt=Label(F2,text='Length Cl :',bg='#EBE3D5')
      L_clengt.place(x=2,y=185)
      E_clengt=Entry(F2,bg='#F4DFC8')
      E_clengt.place(x=70,y=185,width=130,height=25)

      B_creat_tb=Button(F2,text='Creat Tables',bg='#F4BF96' , command=creat_tabel)
      B_creat_tb.place(x=4,y=222,width=200)
      #______________________hade this function (show creat table frame)_______________________________________________________________
def hade_F2_frame():
      F2.place_forget()
#----------------------drop table--------------------------------------------------------------------
def fitch_drop_table():
      def drop_tabel():
            bd_name = E_dbname.get()
            tb_name = E_tbname.get()
            try:
                  conn = mysql.connector.connect(
                        host     = 'localhost',
                        user     = 'root',
                        password = ''
                  )
                  cur=conn.cursor()
                  cur.execute(f'USE {bd_name}; DROP TABLE {tb_name} ')
                  #conn.commit()
                  #conn.close()
                  messagebox.showinfo('DB [system]','The Tables was Dropped without problems🤠')
            except mysql.connector.Error as r:
                  messagebox.showerror('error',r)
      global F4
      F4=Frame(root,bg='#EBE3D5')
      F4.place(x=418,y=219,width=209,height=300)
      title_Fr4=Label(F4,text='Drop Tables',bg='#CE5A67',fg='black',font=('Bauhaus 93',12))
      title_Fr4.pack(fill=X)
      
      L_dbname=Label(F4,text='Name DB :',bg='#EBE3D5')
      L_dbname.place(x=2,y=37)
      E_dbname=Entry(F4,bg='#F4DFC8')
      E_dbname.place(x=70,y=37,width=130,height=25)

      L_tbname=Label(F4,text='Name TB :',bg='#EBE3D5')
      L_tbname.place(x=2,y=74)
      E_tbname=Entry(F4,bg='#F4DFC8')
      E_tbname.place(x=70,y=74,width=130,height=25)

      B_drop_tb=Button(F4,text='Drop Tables',bg='#F4BF96',command=drop_tabel)
      B_drop_tb.place(x=4,y=222,width=200)
def hade_F4_frame():
      F4.place_forget()

#----------------------add a new column in table----------------------------------------------------
def new_column():
      def add_new_column():
            db_name_C = E_dbname_C.get()
            tb_name_C = E_tbname_C.get()
            cl_name_C = E_clname_C.get()
            cl_type_C = E_cltype_C.get()
            cl_lengt_C = E_clengt_C.get()
            
            try:
                  conn = mysql.connector.connect(
                        host     = 'localhost',
                        user     = 'root',
                        password = ''
                  )
                  cur=conn.cursor()
                  #cur.execute(f'USE {db_name_C} ; ALTER TABLE {tb_name_C} ADD COLUMN {cl_name_C} {cl_type_C}({cl_lengt_C})')
                  cur.execute(f'USE {db_name_C} ; ALTER TABLE {tb_name_C} ADD COLUMN {cl_name_C} {cl_type_C}({cl_lengt_C})') 
                  messagebox.showinfo('DB [system]','The Column was added without problems🤠')
            except mysql.connector.Error as r:
                  messagebox.showerror('error',r)
      global F3
      F3=Frame(root,bg='#EBE3D5')
      F3.place(x=209,y=219,width=209,height=300)
      title_Fr3=Label(F3,text='New Column',bg='#CE5A67',fg='black',font=('Bauhaus 93',12))
      title_Fr3.pack(fill=X)
      
      L_dbname_C=Label(F3,text='Name DB :',bg='#EBE3D5')
      L_dbname_C.place(x=2,y=37)
      E_dbname_C=Entry(F3,bg='#F4DFC8')
      E_dbname_C.place(x=70,y=37,width=130,height=25)

      L_tbname_C=Label(F3,text='Name TB :',bg='#EBE3D5')
      L_tbname_C.place(x=2,y=74)
      E_tbname_C=Entry(F3,bg='#F4DFC8')
      E_tbname_C.place(x=70,y=74,width=130,height=25)

      L_clname_C=Label(F3,text='Name CL :',bg='#EBE3D5')
      L_clname_C.place(x=2,y=111)
      E_clname_C=Entry(F3,bg='#F4DFC8')
      E_clname_C.place(x=70,y=111,width=130,height=25)

      L_cltype_C=Label(F3,text='Type Cl :',bg='#EBE3D5')
      L_cltype_C.place(x=2,y=148)
      E_cltype_C=Entry(F3,bg='#F4DFC8')
      E_cltype_C.place(x=70,y=148,width=130,height=25)

      L_clengt_C=Label(F3,text='Length Cl :',bg='#EBE3D5')
      L_clengt_C.place(x=2,y=185)
      E_clengt_C=Entry(F3,bg='#F4DFC8')
      E_clengt_C.place(x=70,y=185,width=130,height=25)

      B_add_C=Button(F3,text='Add New Column',bg='#F4BF96',command=add_new_column)
      B_add_C.place(x=4,y=222,width=200)
      #__________________________hade this function(show creat column)___________________________________________________________
def hade_F3_frame():
      F3.place_forget()
#----------------------drop column-----------------------------------------------------------------
def fitch_drop_column():
      def drop_column():
            db_name = E_dbname_C.get()
            tb_name = E_tbname_C.get()
            cl_name = E_clname_C.get()

            try:
                  conn = mysql.connector.connect(
                     host='localhost',
                     user='root',
                    password=''
                  )
                  cur = conn.cursor()
                  cur.execute(f'USE {db_name}; ALTER TABLE {tb_name} DROP COLUMN {cl_name}')
                  messagebox.showinfo('DB [system]', 'The Column was Dropped without problems🤠')
            except mysql.connector.Error as r:
              messagebox.showerror('error', r)

      global F5
      F5=Frame(root,bg='#EBE3D5')
      F5.place(x=627,y=219,width=209,height=300)
      title_Fr5=Label(F5,text='Drop Column',bg='#CE5A67',fg='black',font=('Bauhaus 93',12))
      title_Fr5.pack(fill=X)
      
      L_dbname_C=Label(F5,text='Name DB :',bg='#EBE3D5')
      L_dbname_C.place(x=2,y=37)
      E_dbname_C=Entry(F5,bg='#F4DFC8')
      E_dbname_C.place(x=70,y=37,width=130,height=25)

      L_tbname_C=Label(F5,text='Name TB :',bg='#EBE3D5')
      L_tbname_C.place(x=2,y=74)
      E_tbname_C=Entry(F5,bg='#F4DFC8')
      E_tbname_C.place(x=70,y=74,width=130,height=25)

      L_clname_C=Label(F5,text='Name CL :',bg='#EBE3D5')
      L_clname_C.place(x=2,y=111)
      E_clname_C=Entry(F5,bg='#F4DFC8')
      E_clname_C.place(x=70,y=111,width=130,height=25)

      B_drop_cl=Button(F5,text='Drop Column',bg='#F4BF96',command=drop_column)
      B_drop_cl.place(x=4,y=222,width=200)
def hade_F5_frame():
      F5.place_forget()

#----------------------SQL FUNCTION-----------------------------------------------------------------
def fitch_sql_frame():
      def sql_frame():
            sql=E_sql.get()
            try :
                  conn = mysql.connector.connect(
                        host     = 'localhost',
                        user     = 'root',
                        password = ''
                  )
                  cur = conn.cursor()
                  cur.execute(f'{sql}')
                  messagebox.showinfo('DB[system]', 'the command sql was success without problems😎')
            except mysql.connector.Error as r:
                  messagebox.showerror('error',r)

      global F_sql
      F_sql= Frame(root,bg='#EBE3D5')
      F_sql.place(x=691,y=29,width=309,height=190)

      title_sql=Label(F_sql,text='Structured Query Language',bg='#CE5A67',font=('Bauhaus 93',12))
      title_sql.pack(fill=X)

      l_sql=Label(F_sql,text='SQL :' ,bg='#EBE3D5')
      l_sql.place(x=9,y=37)

      E_sql=Entry(F_sql,bg='#F4DFC8')
      E_sql.place(x=50,y=37,width=230,height=100)

      B_sql=Button(F_sql,text='GO',bg='#F4DFC8',font=('Bauhaus 93',13),command=sql_frame)
      B_sql.place(x=100,y=148,width=130)
def hade_F_sql():
      F_sql.place_forget()

#____________________________frame1_________________________________________________________________
frame_control= Frame(root,bg='#EBE3D5')
frame_control.place(x=0,y=29,width=690,height=190)

title_Fr1=Label(frame_control,text='Database Controlls',bg='#776B5D',fg='white',font=('Bauhaus 93',12))
title_Fr1.pack(fill=X)

     #___________________________show all databases__________________________________________________
L_show_db=Label(frame_control,text='Show DB :',bg='#EBE3D5')
L_show_db.place(x=9,y=37)

B1_show_db=Button(frame_control,text='All Database',bg='#F4DFC8',command=show_dbs)
B1_show_db.place(x=80,y=37,width=130)

B_show_db_hide=Button(frame_control,text='hide',bg='#F4BF96',command=hade_F_frame)
B_show_db_hide.place(x=230,y=37,width=100)

      #___________________________creat database______________________________________________________
L_name_db=Label(frame_control,text='Name DB :',bg='#EBE3D5')
L_name_db.place(x=9,y=74)

E_name_db=Entry(frame_control,bg='#F4DFC8')
E_name_db.place(x=80,y=74,width=130,height=25)

B_creat_db=Button(frame_control,text='Creat',bg='#F4BF96',command=creat_database)
B_creat_db.place(x=230,y=74,width=50)

B_drop_db=Button(frame_control,text='Drop',bg='#F4BF96',command=drop_database)
B_drop_db.place(x=280,y=74,width=50)

      #__________________________creat table___________________________________________________________
L_tabel_cols=Label(frame_control,text='Table Cols :',bg='#EBE3D5')
L_tabel_cols.place(x=9,y=111)

B1_creat_table=Button(frame_control,text='Creat Tables',bg='#F4DFC8',command=fitch_creat_tabel)
B1_creat_table.place(x=80,y=111,width=130)

B_creat_table_hide=Button(frame_control,text='hide',bg='#F4BF96',command=hade_F2_frame)
B_creat_table_hide.place(x=230,y=111,width=100)
      #___________________________drop table______________________________________________________________________
L_tabel_drop=Label(frame_control,text='Drop Tables :',bg='#EBE3D5')
L_tabel_drop.place(x=339,y=37)

B1_drop_table=Button(frame_control,text='Drop Table',bg='#F4DFC8',command=fitch_drop_table)
B1_drop_table.place(x=419,y=37,width=130)

B_drop_table_hide=Button(frame_control,text='hide',bg='#F4BF96',command=hade_F4_frame)
B_drop_table_hide.place(x=569,y=37,width=100)
      #____________________________add coleuns__________________________________________________________
L_add_cls=Label(frame_control,text='Add Cls :',bg='#EBE3D5')
L_add_cls.place(x=9,y=148)

B1_add_cls=Button(frame_control,text='Add Coleuns',bg='#F4DFC8',command=new_column)
B1_add_cls.place(x=80,y=148,width=130)

B_add_cls_hide=Button(frame_control,text='hide',bg='#F4BF96',command=hade_F3_frame)
B_add_cls_hide.place(x=230,y=148,width=100)
      #______________________________drop coleums___________________________________________________________
L_cl_drop=Label(frame_control,text='Drop Cls :',bg='#EBE3D5')
L_cl_drop.place(x=339,y=74)

B1_drop_cl=Button(frame_control,text='Drop Columns',bg='#F4DFC8',command=fitch_drop_column)
B1_drop_cl.place(x=419,y=74,width=130)

B_drop_cl_hide=Button(frame_control,text='hide',bg='#F4BF96',command=hade_F5_frame)
B_drop_cl_hide.place(x=569,y=74,width=100)
      #_______________________________command SQL____________________________________________________________
L_sql=Label(frame_control,text='SQL Comd :',bg='#EBE3D5')
L_sql.place(x=339,y=111)

B_sql=Button(frame_control,text='SQL',bg='#F4DFC8',command=fitch_sql_frame)
B_sql.place(x=419,y=111,width=130)

B_sql_hide=Button(frame_control,text='hide',bg='#F4BF96',command=hade_F_sql)
B_sql_hide.place(x=569,y=111,width=100)
#____________________________frame2______________________________________________________________________
frame_connect= Frame(root,bg='#EBE3D5')
frame_connect.place(x=691,y=29,width=309,height=190)

title_Fr2=Label(frame_connect,text='Database Connect',bg='#776B5D',fg='white',font=('Bauhaus 93',12))
title_Fr2.pack(fill=X)

      #_________________server name______________________________________________________________________
L_server_name=Label(frame_connect,text='Server-N :',bg='#EBE3D5')
L_server_name.place(x=9,y=37)

E_server_name=Entry(frame_connect,bg='#F4DFC8')
E_server_name.place(x=80,y=37,width=130,height=25)

      #___________________user name______________________________________________________________________
L_user_name=Label(frame_connect,text='User-N :',bg='#EBE3D5')
L_user_name.place(x=9,y=74)

E_user_name=Entry(frame_connect,bg='#F4DFC8')
E_user_name.place(x=80,y=74,width=130,height=25)

      #__________________pass word________________________________________________________________________
L_password=Label(frame_connect,text=' Password:',bg='#EBE3D5')
L_password.place(x=9,y=111)

E_password=Entry(frame_connect,bg='#F4DFC8')
E_password.place(x=80,y=111,width=130,height=25)

      #__________________button connect___________________________________________________________________
B_connect=Button(frame_connect,text='Connect',bg='#F4BF96',command=ser_connect)
B_connect.place(x=230,y=37,width=60,height=100)
#fitch_sql_frame()
root.mainloop()