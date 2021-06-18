from tkinter import *
import pymysql
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import pyqrcode
from pyqrcode import QRCode
from tkinter import messagebox


#Main Window
top = Tk()
top.geometry("1920x1080")
#scanning image
photo = PhotoImage(file = "idcard2.png")
#pic=Label(top,image=photo)
photoimage = photo.subsample(5,5)



def open_window():
    
    try:
        def upload_image():
            global file_path
            file_path = filedialog.askopenfilename()
        
        con=pymysql.connect(host='enter-your-localhost',user='root',database='enter-Project-name',password='enter-your-password')
        cur=con.cursor()
        if con:
            print('Connection Is Successful:')
        #q1='create database Project'
        #cur.execute(q1)
        #cur.execute('create table Project(Enrollment_No bigint primary key,Name varchar(30),Dob varchar(30),gender varchar(30),College varchar(30),Branch varchar(30),Mobile_No bigint,Email varchar(30),Bloodg varchar(30),Pimage blob,Qrimage blob)')
         
    #main window will be minimize
        if True:
            top.withdraw()
    
        top1=Toplevel(top)
    
        #Registartion window code(GUI)
        top1.title('Enroll-No:18012011034')
        top1.geometry("1920x1080")
        top1.configure(bg='floral white')

        l1=Label(top1,text='    Roll-No:',font=('bold',18),bg='floral white')
        l2=Label(top1,text='    Name:',font=('bold',18),bg='floral white')
        l3=Label(top1,text='    D.O.B:',font=('bold',18),bg='floral white')
        l4=Label(top1,text='    Gender:',font=('bold',18),bg='floral white')
        l5=Label(top1,text='    College:',font=('bold',18),bg='floral white')
        l6=Label(top1,text='    Branch:',font=('bold',18),bg='floral white')
        l7=Label(top1,text='    Mobile:',font=('bold',18),bg='floral white')
        l8=Label(top1,text='    Email:',font=('bold',18),bg='floral white')
        l9=Label(top1,text='    Blood Group:',font=('bold',18),bg='floral white')
        l10=Label(top1,text='    Image:',font=('bold',18),bg='floral white')
        
        n1=StringVar()
        n2=StringVar()
        n3=StringVar()
        n4=StringVar()
        n5=StringVar()
        n6=StringVar()
        n7=StringVar()
        n8=StringVar()
        n9=StringVar()
        n10=StringVar()

        
        n6.set('Computer Engineering')
        n3.set('dd/mm/yyyy')
        m=Label(top1,text=' * * * Enter Your Information * * * ',font=('algerian',30),bg='floral white').grid(row=0,column=0,columnspan=4)
        m1=Label(top1,text=' \tChoose Your Design ',font=('algerian',30),bg='floral white').grid(row=0,column=4,columnspan=5)
        e1=Entry(top1,textvariable=n1,width=25,bd=5,font=('bold',12)).grid(row=1,column=1,sticky=W)
        e2=Entry(top1,textvariable=n2,width=25,bd=5,font=('bold',12)).grid(row=2,column=1,sticky=W)
        e3=Entry(top1,textvariable=n3,width=25,bd=5,font=('bold',12)).grid(row=3,column=1,sticky=W)
        #e3=DateEntry(top1, width=25, year=2020, month=4, day=18,background='white', foreground='black', borderwidth=5).grid(row=3,column=1,sticky=W)
        e4=Radiobutton(top1,text='Male',variable=n4,value='Male',bg='floral white',activeforeground='red',borderwidth=10,font=('bold',15)).grid(row=4,column=1,sticky=W)
        e5=Radiobutton(top1,text='Female',variable=n4,value='Female',bg='floral white',activeforeground='red',borderwidth=10,font=('bold',15)).grid(row=4,column=2,sticky=W)
        e6=Entry(top1,textvariable=n5,width=25,bd=5,font=('bold',12)).grid(row=5,column=1,sticky=W)
        e7=OptionMenu(top1,n6,"Computer Engineering ","IT Engineering ","Mechanical Engineering").grid(row=6,column=1,sticky=W)
        e8=Entry(top1,textvariable=n7,width=25,bd=5,font=('bold',12)).grid(row=7,column=1,sticky=W)
        e9=Entry(top1,textvariable=n8,width=25,bd=5,font=('bold',12)).grid(row=8,column=1,sticky=W)
        e10=Entry(top1,textvariable=n9,width=25,bd=5,font=('bold',12)).grid(row=9,column=1,sticky=W)


        l1.grid(row=1,column=0,sticky=W,pady=5)
        l2.grid(row=2,column=0,sticky=W,pady=5)
        l3.grid(row=3,column=0,sticky=W,pady=5)
        l4.grid(row=4,column=0,sticky=W,pady=5)
        l5.grid(row=5,column=0,sticky=W,pady=5)
        l6.grid(row=6,column=0,sticky=W,pady=5)
        l7.grid(row=7,column=0,sticky=W,pady=5)
        l8.grid(row=8,column=0,sticky=W,pady=5)
        l9.grid(row=9,column=0,sticky=W,pady=5)
        l10.grid(row=10,column=0,sticky=W,pady=5)

        #asking to upload your image
        b10=Button(top1,text='Upload Image',font=('bold',12),fg='black',command=upload_image,borderwidth=5).grid(row=10,column=1,sticky=W,pady=5)
        #label1 = Label(top1,text=).grid(row=10,column=1,sticky=W,pady=5)
        def disp():
            num1=int(n1.get())
            num2=str(n2.get())
            num3=str(n3.get())
            num4=str(n4.get())
            num5=str(n5.get())
            num6=str(n6.get())
            num7=int(n7.get())
            num8=str(n8.get())
            num9=str(n9.get())
            num10=str(file_path)

            


            
            #value which represent QR code
            s=num1
            h=str(s)+'.png'
            #genrate QR code
            url=pyqrcode.create(s)
            #creating and saving the png file
            url.png(h,scale=4)
            img=(r'D:\WORK\python\Python project\NEW\''+h)
            val=[(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,img)]
            print('Image path',file_path)
            print('Qr Path',img)
            print(val)
            cur.executemany('insert into Project values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',val)
            con.commit()
            messagebox.showinfo("System","Data Submitted")
            
        b11=Button(top1,text='Submit',width=10,font=('bold',14),fg='black',borderwidth=5,command=disp).grid(row=11,column=0,sticky=W,pady=5)
        
        #display code design1
        def disp1():
            num1=int(n1.get())
            num2=str(n2.get())
            num3=str(n3.get())
            num4=str(n4.get())
            num5=str(n5.get())
            num6=str(n6.get())
            num7=int(n7.get())
            num8=str(n8.get())
            num9=str(n9.get())
            num10=str(file_path)

            top2=Toplevel(top1)
            top2.geometry("650x600")
            top2.configure(bg='white')
            
            s=num1
            h=str(s)+'.png'
            img=(r'D:\WORK\python\Python project\NEW\''+h)

            print('qr:',h)
            print('pic:',num10)
            
            #scanning the image we choose
            photo1= PhotoImage(file=num10)

            #scanning the qrcode which was generated
            photo2= PhotoImage(file=h)

            photo3=PhotoImage(file='scard.png')

            
            l0=Label(top2,image=photo3)
            l0.photo=photo3
            l0.grid(row=0,columnspan=4,sticky=W,pady=5)
            l1=Label(top2,text='    Roll-No:',font=('arial black',20),bg='white').grid(row=1,column=0,sticky=W,pady=5)
            l2=Label(top2,text='    Name:',font=('arial black',20),bg='white').grid(row=2,column=0,sticky=W,pady=5)
            l3=Label(top2,text='    D.O.B:',font=('arial black',20),bg='white').grid(row=3,column=0,sticky=W,pady=5)
            l4=Label(top2,text='    Gender:',font=('arial black',20),bg='white').grid(row=4,column=0,sticky=W,pady=5)
            l5=Label(top2,text='    College:',font=('arial black',20),bg='white').grid(row=5,column=0,sticky=W,pady=5)
            l6=Label(top2,text='    Branch:',font=('arial black',20),bg='white').grid(row=6,column=0,sticky=W,pady=5)
            l7=Label(top2,text='    Mobile:',font=('arial black',20),bg='white').grid(row=7,column=0,sticky=W,pady=5)
            l8=Label(top2,text='    Email:',font=('arial black',20),bg='white').grid(row=8,column=0,sticky=W,pady=5)
            l9=Label(top2,text='    Blood Group:',font=('arial black',20),bg='white').grid(row=9,column=0,sticky=W,pady=5)
            #l10=Label(top2,text='Qr Image:',font=('bold',14)).grid(row=9,column=0,sticky=W,pady=5)
            #l11=Label(top2,text='Image:',font=('bold',14)).grid(row=10,column=0,sticky=W,pady=5)

            l12=Label(top2,text=num1,font=('bold',18),bg='white').grid(row=1,column=1,sticky=W,pady=5)
            l13=Label(top2,text=num2,font=('bold',18),bg='white').grid(row=2,column=1,sticky=W,pady=5)
            l14=Label(top2,text=num3,font=('bold',18),bg='white').grid(row=3,column=1,sticky=W,pady=5)
            l15=Label(top2,text=num4,font=('bold',18),bg='white').grid(row=4,column=1,sticky=W,pady=5)
            l16=Label(top2,text=num5,font=('bold',18),bg='white').grid(row=5,column=1,sticky=W,pady=5)
            l17=Label(top2,text=num6,font=('bold',18),bg='white').grid(row=6,column=1,sticky=W,pady=5)
            l18=Label(top2,text=num7,font=('bold',18),bg='white').grid(row=7,column=1,sticky=W,pady=5)
            l19=Label(top2,text=num8,font=('bold',18),bg='white').grid(row=8,column=1,sticky=W,pady=5)
            l20=Label(top2,text=num9,font=('bold',18),bg='white').grid(row=9,column=1,sticky=W,pady=5)
            l21=Label(top2,image=photo1)
            l22=Label(top2,image=photo2)
            l21.photo=photo1
            l21.grid(row=1,rowspan=3,column=2,sticky=W,pady=5)
            l22.photo=photo2
            l22.grid(row=4,rowspan=3,column=2,sticky=W,pady=5)
            
        #display code design2    
        def disp2 ():
            num1=int(n1.get())
            num2=str(n2.get())
            num3=str(n3.get())
            num4=str(n4.get())
            num5=str(n5.get())
            num6=str(n6.get())
            num7=int(n7.get())
            num8=str(n8.get())
            num9=str(n9.get())
            num10=str(file_path)

            top2=Toplevel(top1)
            top2.geometry("650x650")
            top2.configure(bg='white')
            
            s=num1
            h=str(s)+'.png'
            img=(r'D:\WORK\python\Python project\NEW\''+h)

            print('qr:',h)
            print('pic:',num10)
            
            
            photo1= PhotoImage(file=num10)

            photo2= PhotoImage(file=h)

            photo3=PhotoImage(file='gnu1.png')

            
            l0=Label(top2,image=photo3)
            l0.photo=photo3
            l0.grid(row=0,columnspan=4,sticky=W,pady=10)
            l1=Label(top2,text='    Roll-No:',font=('arial black',20),bg='white').grid(row=1,column=0,sticky=W,pady=5)
            l2=Label(top2,text='    Name:',font=('arial black',20),bg='white').grid(row=2,column=0,sticky=W,pady=5)
            l3=Label(top2,text='    D.O.B:',font=('arial black',20),bg='white').grid(row=3,column=0,sticky=W,pady=5)
            l4=Label(top2,text='    Gender:',font=('arial black',20),bg='white').grid(row=4,column=0,sticky=W,pady=5)
            l5=Label(top2,text='    College:',font=('arial black',20),bg='white').grid(row=5,column=0,sticky=W,pady=5)
            l6=Label(top2,text='    Branch:',font=('arial black',20),bg='white').grid(row=6,column=0,sticky=W,pady=5)
            l7=Label(top2,text='    Mobile:',font=('arial black',20),bg='white').grid(row=7,column=0,sticky=W,pady=5)
            l8=Label(top2,text='    Email:',font=('arial black',20),bg='white').grid(row=8,column=0,sticky=W,pady=5)
            l9=Label(top2,text='    Blood Group:',font=('arial black',20),bg='white').grid(row=9,column=0,sticky=W,pady=5)
            
            l12=Label(top2,text=num1,font=('bold',18),bg='white').grid(row=1,column=1,sticky=W,pady=5)
            l13=Label(top2,text=num2,font=('bold',18),bg='white').grid(row=2,column=1,sticky=W,pady=5)
            l14=Label(top2,text=num3,font=('bold',18),bg='white').grid(row=3,column=1,sticky=W,pady=5)
            l15=Label(top2,text=num4,font=('bold',18),bg='white').grid(row=4,column=1,sticky=W,pady=5)
            l16=Label(top2,text=num5,font=('bold',18),bg='white').grid(row=5,column=1,sticky=W,pady=5)
            l17=Label(top2,text=num6,font=('bold',18),bg='white').grid(row=6,column=1,sticky=W,pady=5)
            l18=Label(top2,text=num7,font=('bold',18),bg='white').grid(row=7,column=1,sticky=W,pady=5)
            l19=Label(top2,text=num8,font=('bold',18),bg='white').grid(row=8,column=1,sticky=W,pady=5)
            l20=Label(top2,text=num9,font=('bold',18),bg='white').grid(row=9,column=1,sticky=W,pady=5)
            l21=Label(top2,image=photo1)
            l22=Label(top2,image=photo2)
            l21.photo=photo1
            l21.grid(row=1,rowspan=3,column=2,sticky=W,pady=5)
            l22.photo=photo2
            l22.grid(row=4,rowspan=3,column=2,sticky=W,pady=5)


        design1=PhotoImage(file ="design1.png")
        design2=PhotoImage(file='design3.png')
        l23=Label(top1,image=design1)
        l24=Label(top1,image=design2)
        l23.photo=design1
        l24.photo=design2
        b13=Button(top1,image = design1,compound = LEFT,command=disp1).grid(row=1,column=5,rowspan=6,columnspan=5)
        b14=Button(top1,image = design2,compound = LEFT,command=disp2).grid(row=8,column=5,rowspan=6,columnspan=5)
        
        #reset code  
        def disp3():
            num1=n1.set('')
            num2=n2.set('')
            num3=n3.set('')
            num4=n4.set('')
            num5=n5.set('')
            num7=n7.set('')
            num8=n8.set('')
            num9=n9.set('')
            
        b12=Button(top1,text='Reset',width=10,font=('bold',14),fg='black',borderwidth=5,command=disp3).grid(row=11,column=1,sticky=W,pady=5)
        
        
        

    except pymysql.DatabaseError as e:
        print(e)

        
#main window content
#c= Canvas (top,bg="red", height="50").grid(row=0,column=1,columnspan=2)
m=Label(top,text='-*-*-*-Student ID CARD GENERATOR-*-*-*-',font=('algerian',35)).grid(row=0,column=1)
a1=Label(top,text='--> The current times demand for desperate measures to assure security and safety in campuses.', font = ('Comic Sans MS',18)).grid(row=1,column=0,columnspan=3,sticky=W)
a2=Label(top,text='--> Educational establishments including universities,schools and colleges need to ensure certain reliable environment and conditions.',font = ('Comic Sans MS',18)).grid(row=2,column=0,columnspan=3,sticky=W)
a3=Label(top,text='--> The first step in acquiring such standards begins by issuing IDs for staff, students and visitors.',font = ('Comic Sans MS',18)).grid(row=3,column=0,columnspan=3,sticky=W)
a4=Label(top,text='--> While ID cards are inclined to abuse and falsification, actualizing right arrangements to produce the cards is essential.',font = ('Comic Sans MS',18)).grid(row=4,column=0,columnspan=3,sticky=W)
a5=Label(top,text='--> This problem can be settled by utilizing This ID Card Generator',font = ('Comic Sans MS',18)).grid(row=6,column=0,columnspan=3,sticky=W)
a5=Label(top,text='--> Click on the below image.',font = ('Comic Sans MS',18)).grid(row=7,column=0,columnspan=3,sticky=W)
a6=Label(top,text='---------------------------------------------------------------------------------------------------------------',font = ('algerian',32)).grid(row=19,column=0,columnspan=5,sticky=W)
a7=Label(top,text='  Name:Ronak Kanthariya',font = ('Comic Sans MS',12)).grid(row=20,column=0,sticky=W)
a8=Label(top,text='  Roll-No:18012011034',font = ('Comic Sans MS',12)).grid(row=21,column=0,sticky=W)
a9=Label(top,text='  Class:CE-A (A2) ',font = ('Comic Sans MS',12)).grid(row=22,column=0,sticky=W)
a11=Label(top,text='  Sem:IV',font = ('Comic Sans MS',12)).grid(row=24,column=0,sticky=W) 
b1=Button(top,image = photo,compound = LEFT,command=open_window).grid(row=9,column=1,rowspan=5)


top.mainloop()

