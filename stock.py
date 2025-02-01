from tkinter import *
from tkinter import messagebox,ttk
from datetime import datetime,date
from PIL import ImageTk
import sqlite3 as c
from decimal import Decimal
import subprocess as sp

l_name=""
l_cost=[]
l_quantity=[]
txt_user=txt_users=phone_user=root=log=sow=billing=0
txt_pass=recov_user=c_pass_user=name_user=pass_user=rec_pass=desig_user=name_entry=pro_entry="0"
name_entry=desig_entry=recovery_entry=password_entry=type_entry=code_entry="0"
quantity_entry=cost_entry=phone_entry=p_name_entry=viewarea=u_code_entry=phnno_entry=phnno_entry_new=u_phone_entry=u_phndeechocolate235678943210no_entry_new=0
name_entry=u_name_entry=u_password_entry=u_recovery_entry=u_recovery_entry_new=u_designation_entry=u_name_entry_new=u_password_entry_new=u_designation_entry_new="0"

def first():
    Frame_login=Frame(root,bg="white")
    Frame_login.place(x=70,y=150,height=340,width=600)
        
    title=Label(Frame_login,text="STOCK MANAGEMENT SYSTEM",font=("Impact",30,"bold"),fg="#d77337",bg="white").place(x=50,y=30)
    desc=Label(Frame_login,text="SELECT YOUR CHOICE",font=("Goudy old style",15,"bold"),fg="#d77337",bg="white").place(x=50,y=80)

    add_acc=Button(Frame_login,command=account,cursor="hand2",text="CREATE NEW ACCOUNT",bg="brown",fg="white",font=("times new roman",16,"bold")).place(x=50,y=130)
    login_button=Button(Frame_login,command=login,cursor="hand2",text="    LOGIN HERE    ",fg="white",bg="brown",font=("times new roman",16,"bold")).place(x=50,y=190)

def login():
        global txt_user
        global txt_pass
        #main frame
        Frame_login=Frame(root,bg="white")
        Frame_login.place(x=70,y=150,height=340,width=600)
        #login frame
        Frame_login=Frame(root,bg="white")
        Frame_login.place(x=70,y=150,height=340,width=600)        
        title=Label(Frame_login,text="Login Here",font=("Impact",30,"bold"),fg="#d77337",bg="white").place(x=50,y=30)
        desc=Label(Frame_login,text="Accountant Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d77337",bg="white").place(x=50,y=80)        
        phone=Label(Frame_login,text="Login Id:",font=("Goudy old style",22,"bold"),fg="#d77337",bg="white").place(x=50,y=135)
        txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        txt_user.focus()
        txt_user.place(x=310,y=140)        
        password_user=Label(Frame_login,text="Password:",font=("Goudy old style",22,"bold"),fg="#d77337",bg="white").place(x=50,y=200)
        txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show="*")
        txt_pass.place(x=310,y=205)
        add_acc=Button(Frame_login,command=account,cursor="hand2",text="Create New Account",bg="white",fg="green",bd=0,font=("times new roman",16)).place(x=320,y=265)
        login_button=Button(root,command=login_fun,cursor="hand2",text="    Login    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=280,y=470,width=180,height=50)
        forget=Button(Frame_login,command=forget_log,cursor="hand2",text="Forget Password",bg="white",fg="red",bd=0,font=("times new roman",12)).place(x=50,y=265)
    
def login_fun():
        global txt_user
        global txt_pass
        global log
        if txt_pass.get()=="" or txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root)
        elif len(txt_user.get())<10 or len(txt_user.get())>10:
            messagebox.showerror("Error","Phone number should be of 10 digits",parent=root)
        elif not (txt_user.get()).isdigit():
            messagebox.showerror("Error","Phone number should be of digits",parent=root)
        else:
            try:
                user=int(txt_user.get())
                password=str(txt_pass.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from user where login_id=%s and password='%s'"%(user,password))
                cursor.execute(quary)
                data=cursor.fetchone()
                if data==None:
                    messagebox.showerror("Error","Invalid PHONE NUMBER & PASSWORD",parent=root)
                else:
                    name=data[1]
                    messagebox.showinfo("Login success","WELCOME %s, YOUR LOGIN WAS SUCCESSFUL"%(name.upper()),parent=root)
                    log=1
                    root.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def forget_log():
        global root
        global txt_users
        global rec_pass
        #login frame
        Frame_login=Frame(root,bg="white")
        Frame_login.place(x=70,y=150,height=340,width=600)        
        title=Label(Frame_login,text="Login Here",font=("Impact",30,"bold"),fg="#d77337",bg="white").place(x=50,y=30)
        desc=Label(Frame_login,text="Accountant Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d77337",bg="white").place(x=50,y=80)        
        phone=Label(Frame_login,text="Login Id:",font=("Goudy old style",22,"bold"),fg="#d77337",bg="white").place(x=50,y=135)
        txt_users=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        txt_users.focus()
        txt_users.place(x=310,y=140)        
        recovery_user=Label(Frame_login,text="Recovery code:",font=("Goudy old style",22,"bold"),fg="#d77337",bg="white").place(x=50,y=200)
        rec_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        rec_pass.place(x=310,y=205)
        login_button=Button(root,command=login_dash,cursor="hand2",text="    Login    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=280,y=470,width=180,height=50)

def login_dash():
        global txt_users
        global rec_pass
        global log
        if rec_pass.get()=="" or txt_users.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root)
        elif not (txt_users.get()).isdigit():
            messagebox.showerror("Error","Phone number should be of digits",parent=root)
        elif len(txt_users.get())<10 or len(txt_users.get())>10:
            messagebox.showerror("Error","Phone number should be of 10 digits",parent=root)
        else:
            try:
                user=int(txt_users.get())
                recover=str(rec_pass.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from user where login_id=%s and password='%s'"%(user,recover))
                cursor.execute(quary)
                data=cursor.fetchone()
                if data==None:
                    messagebox.showerror("Error","Invalid PHONE NUMBER & PASSWORD",parent=root)
                else:
                    messagebox.showinfo("Login success","WELCOME, YOUR LOGIN WAS SUCCESSFUL",parent=root)
                    log=1
                    root.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def account():
        global phone_user
        global name_user
        global pass_user
        global recov_user
        global desig_user
        global c_pass_user
        Frame_acc=Frame(root,bg="white")
        Frame_acc.place(x=70,y=150,height=340,width=600)
        title=Label(Frame_acc,text="CREATE NEW ACCOUNT",font=("Impact",24,"bold"),fg="#d77337",bg="white").place(x=50,y=10)
        desc=Label(Frame_acc,text="Employee Account Creation Area",font=("Goudy old style",15,"bold"),fg="#d77337",bg="white").place(x=50,y=45)        
        phone=Label(Frame_acc,text="Phone Number:",font=("Goudy old style",18,"bold"),fg="#d77337",bg="white").place(x=50,y=80)
        phone_user=Entry(Frame_acc,font=("times new roman",15),bg="lightgray")
        phone_user.focus()
        phone_user.place(x=280,y=85)
        name=Label(Frame_acc,text="Name:",font=("Goudy old style",18,"bold"),fg="#d77337",bg="white").place(x=50,y=120)
        name_user=Entry(Frame_acc,font=("times new roman",15),bg="lightgray")
        name_user.place(x=280,y=125)
        desig=Label(Frame_acc,text="Designation:",font=("Goudy old style",18,"bold"),fg="#d77337",bg="white").place(x=50,y=160)
        dsg=['OWNER','MANAGER','STAFF','SECURITY GUARD','OTHERS']
        desig_user=ttk.Combobox(Frame_acc,values=dsg,width=30,height=10,state="readonly")
        desig_user.place(x=280,y=165)
        password=Label(Frame_acc,text="Password:",font=("Goudy old style",18,"bold"),fg="#d77337",bg="white").place(x=50,y=200)
        pass_user=Entry(Frame_acc,font=("times new roman",15),bg="lightgray",show="*")
        pass_user.place(x=280,y=205)        
        c_password=Label(Frame_acc,text="Conform Password:",font=("Goudy old style",18,"bold"),fg="#d77337",bg="white").place(x=50,y=240)
        c_pass_user=Entry(Frame_acc,font=("times new roman",15),bg="lightgray",show="*")
        c_pass_user.place(x=280,y=245)
        recovery=Label(Frame_acc,text="Recovery code:",font=("Goudy old style",18,"bold"),fg="#d77337",bg="white").place(x=50,y=280)
        recov_user=Entry(Frame_acc,font=("times new roman",15),bg="lightgray")
        recov_user.place(x=280,y=285)
        login_acc=Button(Frame_acc,command=login,cursor="hand2",text="Login Here",bg="white",fg="green",bd=0,font=("times new roman",16)).place(x=450,y=30)
        acc_button=Button(root,command=acc_fun,cursor="hand2",text="    Create Account    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=280,y=470,width=180,height=50)

def acc_fun():
        global phone_user
        global name_user
        global pass_user
        global recov_user
        global desig_user
        global c_pass_user
        if pass_user.get()=="" or name_user.get()=="" or phone_user.get()=="" or recov_user.get()=="" or desig_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root)
        elif not (phone_user.get()).isdigit():
            messagebox.showerror("Error","Phone number should be of digits",parent=root)
        elif len(phone_user.get())<10 or len(phone_user.get())>10:
            messagebox.showerror("Error","Phone number should be of 10 digits",parent=root)
        elif pass_user.get()!=c_pass_user.get():
            messagebox.showerror("Error","Password doesnot match with Conform password",parent=root)
        elif acc_fun_1(phone_user.get())==1:
            messagebox.showerror("Error","Phone number already exist:",parent=root)
        else:
            try:
                login_id=int(phone_user.get())
                name=str(name_user.get())
                password=str(pass_user.get())
                recovery=str(recov_user.get())
                desig=desig_user.get()
                doj=date.today()
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary="insert into user values({},'{}','{}','{}','{}','{}')".format(login_id,name,desig,password,recovery,doj)
                cursor.execute(quary)
                con.commit()
                messagebox.showinfo("Account created","Account created Successfully, Please Login now",parent=root) 
                login()        
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def acc_fun_1(phn):
        global phone_user
        login_id=int(phn)
        con=c.connect("stock.db")
        cursor=con.cursor()
        quary="select * from user where login_id=%s"%(login_id)
        cursor.execute(quary)
        data=cursor.fetchone()
        if data==None:
            a=0
        else:
            a=1
        return a       
        
def back_menu():
    global root
    root.destroy()
    stock()

def stock():
    global root
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1920x1080")
    title_label=Label(text="STOCK MANAGEMENT SYSTEM",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    pro=Label(root,text="PRODUCT MANAGEMENT",font=("Impact",28),fg="#d77337").place(x=30,y=150)
    pur=Label(root,text="PURCHASE MANAGEMENT",font=("Impact",28),fg="#d77337").place(x=450,y=150)
    usr=Label(root,text="EMPLOYEE MANAGEMENT",font=("Impact",28),fg="#d77337").place(x=900,y=150)
    Frame1st=Frame(root,bg="#ff002a")
    Frame1st.place(x=410,y=130,height=700,width=7)
    Frame2nd=Frame(root,bg="#ff002a")
    Frame2nd.place(x=850,y=130,height=700,width=7)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    adduser_button=Button(root,command=logout,cursor="hand2",text="        LOGOUT        ",fg="white",bg="#44004b",font=("times new roman",14,"bold")).place(x=1130,y=105,width=110,height=30)
    addpro_button=Button(root,command=add_pro,cursor="hand2",text="        ADD PRODUCT        ",fg="white",bg="brown",font=("times new roman",16,"bold")).place(x=80,y=240,width=250,height=50)
    searchpro_button=Button(root,command=search_pro,cursor="hand2",text="        SEARCH PRODUCT        ",fg="white",bg="brown",font=("times new roman",16,"bold")).place(x=80,y=320,width=250,height=50)
    updatepro_button=Button(root,command=update_pro,cursor="hand2",text="        UPDATE PRODUCT        ",fg="white",bg="brown",font=("times new roman",16,"bold")).place(x=80,y=400,width=250,height=50)
    deletepro_button=Button(root,command=delete_pro,cursor="hand2",text="        DELETE PRODUCT        ",fg="white",bg="brown",font=("times new roman",16,"bold")).place(x=80,y=480,width=250,height=50)
    listpro_button=Button(root,command=list_pro,cursor="hand2",text="        LIST PRODUCT        ",fg="white",bg="brown",font=("times new roman",16,"bold")).place(x=80,y=560,width=250,height=50)
    addpur_button=Button(root,command=add_pur,cursor="hand2",text="        ADD PURCHASE        ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=510,y=240,width=250,height=50)
    searchpur_button=Button(root,command=search_pur,cursor="hand2",text="        SEARCH PURCHASE        ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=510,y=320,width=250,height=50)
    listpur_button=Button(root,command=list_pur,cursor="hand2",text="        LIST PURCHASE        ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=510,y=400,width=250,height=50)
    adduser_button=Button(root,command=add_user,cursor="hand2",text="        ADD EMPLOYEE        ",fg="white",bg="#700169",font=("times new roman",16,"bold")).place(x=940,y=240,width=250,height=50)
    searchuser_button=Button(root,command=search_user,cursor="hand2",text="        SEARCH EMPLOYEE        ",fg="white",bg="#700169",font=("times new roman",16,"bold")).place(x=940,y=320,width=250,height=50)
    updateuser_button=Button(root,command=update_user,cursor="hand2",text="        UPDATE EMPLOYEE        ",fg="white",bg="#700169",font=("times new roman",16,"bold")).place(x=940,y=400,width=250,height=50)
    deleteuser_button=Button(root,command=delete_user,cursor="hand2",text="        DELETE EMPLOYEE        ",fg="white",bg="#700169",font=("times new roman",16,"bold")).place(x=940,y=480,width=250,height=50)
    listuser_button=Button(root,command=list_user,cursor="hand2",text="        LIST EMPLOYEE        ",fg="white",bg="#700169",font=("times new roman",16,"bold")).place(x=940,y=560,width=250,height=50)
    root.mainloop()

def logout():
    global root
    root.destroy()
    main()

def add_pro():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="PRODUCT MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    add_product(root)

def add_product(root):
    global name_entry
    global type_entry
    global quantity_entry
    global cost_entry
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=30,y=150,height=410,width=550)
    headline=Label(Frame_p,text="ADD NEW PRODUCT:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=110,y=10)
    p_name=Label(Frame_p,text="PRODUCT NAME:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=130)
    p_type=Label(Frame_p,text="PRODUCT TYPE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=180)
    p_quantity=Label(Frame_p,text="PRODUCT QUANTITY:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=230)
    p_cost=Label(Frame_p,text="PRODUCT COST:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=280)
    name_entry=Entry(Frame_p,font=("times new roman",15))
    name_entry.focus()
    name_entry.place(x=320,y=135)
    p_types=['GROCERY','ELECTRONICS','FASHION','HOME DECORATION','OTHERS']
    type_entry=ttk.Combobox(Frame_p,state="readonly",values=p_types,width=30)
    type_entry.place(x=320,y=185)
    quantity_entry=Entry(Frame_p,font=("times new roman",15))
    quantity_entry.place(x=320,y=235)
    cost_entry=Entry(Frame_p,font=("times new roman",15))
    cost_entry.place(x=320,y=285)
    submit_button=Button(root,command=add_pro_fun,cursor="hand2",text="    ADD PRODUCT    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=200,y=535,width=200,height=50)
    root.mainloop()

def add_pro_fun():
        global root
        global name_entry
        global type_entry
        global quantity_entry
        global cost_entry
        if name_entry.get()=="" or type_entry.get()=="" or quantity_entry.get()==() or cost_entry.get()==():
            messagebox.showerror("Error","All fields are required",parent=root)
        else:
            try:
                name=str(name_entry.get())
                types=str(type_entry.get())
                quantity=(quantity_entry.get())
                cost=(cost_entry.get())
                dat_str=datetime.now()
                dat=dat_str.strftime("%Y/%m/%d %H:%M:%S")
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select max(code) from product;")
                cursor.execute(quary)
                data0=cursor.fetchone()
                data0=data0[0]
                if data0==None:
                    data0=100
                else:
                    data0=int(data0)+1
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("insert into product (code,name,types,quantity,cost,dat)values(%s,'%s','%s',%s,%s,'%s')"%(data0,name,types,quantity,cost,dat))
                cursor.execute(quary)
                con.commit()
                quary1=("select * from product where name='%s'"% name)
                cursor.execute(quary1)
                data=cursor.fetchone()
                viewarea=Frame(root,bg="lightgray")
                viewarea.place(x=595,y=200,height=300,width=480)
                v_area=Label(viewarea,text="VIEW AREA:",font="comicsansm 25 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
                for i in range(0,5):
                    if i==0:   
                        p_c=Label(viewarea,text="PRODUCT CODE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=60)                        
                        p_codeVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=60)
                    elif i==1:
                        p_n=Label(viewarea,text="PRODUCT NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=100)
                        p_nameVAL=Label(viewarea,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=100)
                    elif i==2:
                        p_t=Label(viewarea,text="PRODUCT TYPE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=140)
                        p_typeVAL=Label(viewarea,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=140)
                    elif i==3:
                        p_qe=Label(viewarea,text="PRODUCT QUANTITY:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=180)
                        p_quantityVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=180)
                    elif i==4:
                        p_co=Label(viewarea,text="PRODUCT COST:                      Rs",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=220)
                        p_costVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=220)
                messagebox.showinfo("Product Added","Product added successfully",parent=root)    
                add_product(root)           
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)    

def search_pro():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="PRODUCT MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    search_product(root)

def search_product(root):
    global p_name_entry
    global viewarea
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=30,y=200,height=200,width=500)
    headline=Label(Frame_p,text="SEARCH PRODUCT:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=30,y=10)
    con=c.connect("stock.db")
    cursor=con.cursor()
    quary=("select name from product")
    cursor.execute(quary)
    data=cursor.fetchall()
    p_name1=[]
    for i in data:
        p_name1.append(i[0])
    p_name=Label(Frame_p,text="SELECT PRODUCT NAME WHOSE DATA YOU WANT:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=80)
    p_name_entry=ttk.Combobox(Frame_p,state="readonly",values=p_name1,width=30)
    p_name_entry.place(x=30,y=130)
    submit_button=Button(root,command=search_pro_fun,cursor="hand2",text="    SEARCH    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=60,y=375,width=200,height=50)
    root.mainloop()

def search_pro_fun():
        global root
        global p_name_entry
        global viewarea
        viewarea=Frame(root,bg="lightgray")
        viewarea.place(x=565,y=200,height=400,width=500)
        v_area=Label(viewarea,text="VIEW AREA:",font="comicsansm 25 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
        p_c=Label(viewarea,text="PRODUCT CODE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=60)
        p_n=Label(viewarea,text="PRODUCT NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=100)
        p_t=Label(viewarea,text="PRODUCT TYPE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=140)
        p_qe=Label(viewarea,text="PRODUCT QUANTITY:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=180)
        p_co=Label(viewarea,text="PRODUCT COST:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=220)
        if p_name_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root) 
        else:
            try:
                name=str(p_name_entry.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from product where name='%s'"% name)
                cursor.execute(quary)
                data=cursor.fetchone()
                if data==None:
                    messagebox.showerror("Error","No data found",parent=root) 
                else:
                    viewarea1=Frame(viewarea,bg="lightgray")
                    viewarea1.place(x=290,y=50,height=300,width=200)
                    for i in range(5):
                        if i==0:                           
                            p_codeVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=10)
                        elif i==1:
                            p_nameVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=50)
                        elif i==2:
                            p_typeVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=90)
                        elif i==3:
                            p_quantityVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=130)
                        elif i==4:
                            p_costVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=170)
                            search_product(root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)  

def update_pro():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="PRODUCT MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="#44004b",bg="yellow",font=("times new roman",14,"bold")).place(x=900,y=100,width=180,height=40)
    update_pro_0()

def update_pro_0():
    global root
    global p_name_entry
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=20,y=150,height=200,width=370)
    headline=Label(Frame_p,text="UPDATE PRODUCT:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=30,y=10)
    p_name=Label(Frame_p,text="SELECT PRODUCT NAME WHOSE DATA\nYOU WANT TO UPDATE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=70)
    con=c.connect("stock.db")
    cursor=con.cursor()
    quary=("select name from product")
    cursor.execute(quary)
    data=cursor.fetchall()
    p_name1=[]
    for i in data:
        p_name1.append(i[0])
    p_name_entry=ttk.Combobox(Frame_p,state="readonly",values=p_name1,width=30)
    p_name_entry.place(x=85,y=140)
    submit_button=Button(root,command=update_pro_1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=105,y=325,width=200,height=50)
    root.mainloop()

def update_pro_1():
        global root
        global p_name_entry        
        if p_name_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root) 
        else:
            try:
                viewarea=Frame(root,bg="lightgray")
                viewarea.place(x=20,y=380,height=250,width=400)
                v_area=Label(viewarea,text="OLD DATA:",font="comicsansm 22 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
                p_c=Label(viewarea,text="PRODUCT CODE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=50)
                p_n=Label(viewarea,text="PRODUCT NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=90)
                p_t=Label(viewarea,text="PRODUCT TYPE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=130)
                p_qe=Label(viewarea,text="PRODUCT QUANTITY:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=170)
                p_co=Label(viewarea,text="PRODUCT COST:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=210)
                name=str(p_name_entry.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from product where name='%s'"% name)
                cursor.execute(quary)
                data=cursor.fetchone()
                if data==None:
                    messagebox.showerror("Error","No data found",parent=root) 
                else:
                    viewarea1=Frame(viewarea,bg="lightgray")
                    viewarea1.place(x=230,y=50,height=200,width=200)
                    for i in range(5):
                        if i==0:                           
                            p_codeVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=0)
                        elif i==1:
                            p_nameVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=40)
                        elif i==2:
                            p_typeVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=80)
                        elif i==3:
                            p_quantityVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=120)
                        elif i==4:
                            p_costVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=160)
                            update_pro_2(root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)  

def update_pro_2(root):
    global p_name_entry
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=200,width=600)
    p_name=Label(viewarea2,text="SELECT WHICH YOU WANT TO UPDATE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    name_button=Button(viewarea2,command=update_pro_name,cursor="hand2",text="    NAME    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=50,y=50,width=200,height=50)
    type_button=Button(viewarea2,command=update_pro_type,cursor="hand2",text="    TYPE    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)
    quantity_button=Button(viewarea2,command=update_pro_quantity,cursor="hand2",text="    QUANTITY    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=350,y=50,width=200,height=50)
    cost_button=Button(viewarea2,command=update_pro_cost,cursor="hand2",text="    COST    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=350,y=130,width=200,height=50)

def update_pro_name():
    global p_name_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=200,width=600)
    p_name=Label(viewarea2,text="ENTER NEW NAME OF THE PRODUCT:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    p_name_entry_new=Entry(viewarea2,font=("times new roman",15))
    p_name_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_pro_name1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_pro_name1():
    global root
    global p_name_entry_new
    global p_name_entry
    if p_name_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=str(p_name_entry.get())
            name2=str(p_name_entry_new.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update product set name='%s' where name='%s'"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            update_display1(root,name2)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def update_pro_type():
    global type_entry
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=200,width=600)
    p_name=Label(viewarea2,text="ENTER NEW TYPE OF THE PRODUCT:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    p_types=['GROCERY','ELECTRONICS','FASHION','HOME DECORATION','OTHERS']
    type_entry=ttk.Combobox(viewarea2,state="readonly",values=p_types,width=30)
    type_entry.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_pro_type1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_pro_type1():
    global root
    global type_entry
    global p_name_entry
    if type_entry.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=str(p_name_entry.get())
            name2=str(type_entry.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update product set types='%s' where name='%s'"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            update_display1(root,name1)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def update_pro_quantity():
    global p_quantity_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=200,width=600)
    p_name=Label(viewarea2,text="ENTER NEW QUANTITY OF THE PRODUCT:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    p_quantity_entry_new=Entry(viewarea2,font=("times new roman",15))
    p_quantity_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_pro_quantity1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_pro_quantity1():
    global root
    global p_quantity_entry_new
    global p_name_entry
    if p_quantity_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=str(p_name_entry.get())
            name2=(p_quantity_entry_new.get())
            dat_str=datetime.now()
            dat=dat_str.strftime("%Y/%m/%d %H:%M:%S")
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update product set quantity=%s where name='%s'"%(name2,name1))
            quary1=("update product set dat='%s' where name='%s'"%(dat,name1))
            cursor.execute(quary)
            cursor.execute(quary1)
            con.commit()
            update_display1(root,name1)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def update_pro_cost():
    global p_cost_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=200,width=600)
    p_name=Label(viewarea2,text="ENTER NEW COST OF THE PRODUCT:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    p_cost_entry_new=Entry(viewarea2,font=("times new roman",15))
    p_cost_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_pro_cost1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_pro_cost1():
    global root
    global p_cost_entry_new
    global p_name_entry
    if p_cost_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=str(p_name_entry.get())
            name2=(p_cost_entry_new.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update product set cost=%s where name='%s'"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            update_display1(root,name1)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def update_display1(root,name):
        try:
            viewarea=Frame(root,bg="lightgray")
            viewarea.place(x=480,y=380,height=250,width=400)
            v_area=Label(viewarea,text="NEW DATA:",font="comicsansm 22 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               

            p_c=Label(viewarea,text="PRODUCT CODE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=50)
            p_n=Label(viewarea,text="PRODUCT NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=90)
            p_t=Label(viewarea,text="PRODUCT TYPE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=130)
            p_qe=Label(viewarea,text="PRODUCT QUANTITY:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=170)
            p_co=Label(viewarea,text="PRODUCT COST:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=210)
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("select * from product where name='%s'"%name)
            cursor.execute(quary)
            data=cursor.fetchone()
            if data==None:
                messagebox.showerror("Error","No data found",parent=root) 
            else:
                viewarea1=Frame(viewarea,bg="lightgray")
                viewarea1.place(x=230,y=50,height=200,width=200)
                for i in range(5):
                    if i==0:                           
                        p_codeVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=0)
                    elif i==1:
                        p_nameVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=40)
                    elif i==2:
                        p_typeVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=80)
                    elif i==3:
                        p_quantityVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=120)
                    elif i==4:
                        p_costVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=160)
                        update_pro_0()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def delete_pro():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="PRODUCT MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
    delete_pro_0()

def delete_pro_0():  
    global root
    global p_name_entry  
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=20,y=200,height=200,width=370)
    headline=Label(Frame_p,text="DELETE PRODUCT:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=30,y=10)
    p_name=Label(Frame_p,text="SELECT PRODUCT NAME WHOSE DATA\nYOU WANT TO DELETE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=70)
    con=c.connect("stock.db")
    cursor=con.cursor()
    quary=("select name from product")
    cursor.execute(quary)
    data=cursor.fetchall()
    p_name1=[]
    for i in data:
        p_name1.append(i[0])
    p_name_entry=ttk.Combobox(Frame_p,state="readonly",values=p_name1,width=30)
    p_name_entry.place(x=85,y=140)
    submit_button=Button(root,command=delete_pro_1,cursor="hand2",text="    DELETE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=105,y=385,width=200,height=50)
    root.mainloop()

def delete_pro_1():
        global root
        global p_name_entry
        if p_name_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root) 
        else:
            try:
                name=str(p_name_entry.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from product where name='%s'"% name)
                cursor.execute(quary)
                data=cursor.fetchone()
                viewarea=Frame(root,bg="lightgray")
                viewarea.place(x=595,y=200,height=300,width=480)
                v_area=Label(viewarea,text="VIEW AREA:",font="comicsansm 25 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
                for i in range(0,5):
                    if i==0:   
                        p_c=Label(viewarea,text="PRODUCT CODE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=60)                        
                        p_codeVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=60)
                    elif i==1:
                        p_n=Label(viewarea,text="PRODUCT NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=100)
                        p_nameVAL=Label(viewarea,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=100)
                    elif i==2:
                        p_t=Label(viewarea,text="PRODUCT TYPE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=140)
                        p_typeVAL=Label(viewarea,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=140)
                    elif i==3:
                        p_qe=Label(viewarea,text="PRODUCT QUANTITY:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=180)
                        p_quantityVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=180)
                    elif i==4:
                        p_co=Label(viewarea,text="PRODUCT COST:                      Rs",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=220)
                        p_costVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=220)                
                cursor=con.cursor()                  
                quary=("delete from product where name='%s'"%name)
                cursor.execute(quary)
                data=cursor.fetchone()        
                con.commit()
                messagebox.showinfo("Product Deleted","Product deleted successfully",parent=root) 
                delete_pro_0()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)    
    
def list_pro():
        global root
        root.destroy()
        root=Tk()
        root.title("STOCK MANAGEMENT")
        root.geometry("1100x670")  
        root.minsize(650,630)
        title_label=Label(text="PRODUCT MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
        title_label.pack(fill=X)
        bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar1_label.pack(fill=X)
        bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar2_label.pack(fill=X,side=BOTTOM)
        bar3_label=Label(pady=25)
        bar3_label.pack(fill=X)
        back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
        headline=Label(text="LIST PRODUCT:",font=("Impact",30),fg="#6b0275").place(x=30,y=140)
        con=c.connect("stock.db")
        cursor=con.cursor()
        quary=("select * from product;")
        cursor.execute(quary)        
        tree=ttk.Treeview()
        tree['show']='headings'
        s=ttk.Style(root)
        s.theme_use("clam")
        s.configure(".",font="comicsansm 12 bold")
        s.configure("Treeview.Heading",font="comicsansm 14 bold")
        tree["columns"]=("code","name","types","quantity","cost","dat")
        tree.column("code",width=170,anchor=CENTER)
        tree.column("name",width=170,anchor=CENTER)
        tree.column("types",width=170,anchor=CENTER)
        tree.column("quantity",width=170,anchor=CENTER)
        tree.column("cost",width=170,anchor=CENTER)
        tree.column("dat",width=190,anchor=CENTER)
        #assigning the heading of tree
        tree.heading("code",text="Product Code",anchor=CENTER)
        tree.heading("name",text="Product Name",anchor=CENTER)
        tree.heading("types",text="Product Type",anchor=CENTER)
        tree.heading("quantity",text="Product Quantity",anchor=CENTER)
        tree.heading("cost",text="Product Cost",anchor=CENTER)
        tree.heading("dat",text="Product arrival",anchor=CENTER)
        a=1
        for i in cursor:
            tree.insert('',a,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5]))
            a+=1
        tree.pack()
        root.mainloop()

def add_pur():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="PURCHASE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    l_cost=""
    l_name=[]
    l_quantity=[]
    add_pur0(root)

def add_pur0(root):
    global phone_entry
    global name_entry
    l_cost=[]
    l_quantity=[]
    with open("file.txt","w") as fobj:
        fobj.write("")
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=30,y=150,height=200,width=550)
    headline=Label(Frame_p,text="ADD NEW PURCHASE:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=10,y=7)
    c_phone=Label(Frame_p,text="CUSTOMER PHONE NUMBER:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=10,y=60)
    c_name=Label(Frame_p,text="CUSTOMER NAME:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=10,y=110)   
    Frame_pur=Frame(root)
    Frame_pur.place(x=30,y=400,height=220,width=550)
    Frame_pur1=Frame(root)
    Frame_pur1.place(x=600,y=142,width=200,height=50)
    phone_entry=Entry(Frame_p,font=("times new roman",15))
    phone_entry.focus()
    phone_entry.place(x=320,y=65)
    name_entry=Entry(Frame_p,font=("times new roman",15))
    name_entry.place(x=320,y=115)
    submit_button=Button(root,command=add_pur1,cursor="hand2",text="    SUBMIT    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=100,y=320,width=200,height=50)
    root.mainloop()

def add_pur1():
        global root
        global phone_entry
        global name_entry
        if name_entry.get()=="" or phone_entry.get()==() or phone_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root) 
        elif not (phone_entry.get()).isdigit():
            messagebox.showerror("Error","Phone number should be of digits",parent=root)
        elif len(phone_entry.get())<10 or len(phone_entry.get())>10:
            messagebox.showerror("Error","Phone number should be of 10 digits",parent=root)
        else:
            try:
                c_name=str(name_entry.get())
                c_phone=int(phone_entry.get())
                with open("file.txt","w") as fobj:
                    fobj.write("\t\t\t  CUSTOMER PURCHASE   \t\t\t" + "\n")
                with open ("file.txt","a") as fobj:
                    fobj.write("\t\t\t  CUSTOMER NAME: "+c_name+"\n\t\t\t  "+"CUSTOMER PHONE NUMBER: "+str(c_phone)+"\n"+"\n"+"\n"+"\n")
                    fobj.write("\t\t\t  ------------Your Bill-------------\n\n")
                    fobj.write("\t+"+ "-" * (35) + "+" + "-" * (25) + "+"+ "-" * (25) +"+" + "\n")
                    fobj.write("\t"+"|"+"  PRODUCT NAME"+" "*21+"|"+"  PURCHASE QUANTITY"+" "*6+"|"+"  PRODUCT COST"+" "*11+"|\n")
                    fobj.write("\t+"+ "-" * (35) + "+" + "-" * (25) + "+"+ "-" * (25) +"+" + "\n")
                add_pur2()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)  

def add_pur2():
    global root
    global pro_entry
    global quantity_entry
    Frame_pur=Frame(root,bg="lightgray")
    Frame_pur.place(x=30,y=400,height=190,width=550)
    headline=Label(Frame_pur,text="ADD PRODUCTS:",font=("Impact",25),fg="#6b0275",bg="lightgray").place(x=10,y=7)
    p_head=Label(Frame_pur,text="SELECT PRODUCT NAME:",font=("Impact",17),fg="#6b0275",bg="lightgray").place(x=10,y=60)                    
    p_head=Label(Frame_pur,text="ENTER QUANTITY:",font=("Impact",17),fg="#6b0275",bg="lightgray").place(x=280,y=60)                    
    con=c.connect("stock.db")
    cursor=con.cursor()
    quary=("select name from product")
    cursor.execute(quary)
    data=cursor.fetchall()
    p_name1=[]
    for i in data:
        p_name1.append(i[0])
    pro_entry=ttk.Combobox(Frame_pur,state="readonly",values=p_name1,width=30)
    pro_entry.place(x=20,y=110)
    quantity_entry=Entry(Frame_pur,font=("times new roman",15))
    quantity_entry.place(x=290,y=110)
    submit_button=Button(root,command=add_pur3,cursor="hand2",text="    ADD    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=550,width=200,height=50)

def add_pur3():
        global root
        global pro_entry
        global quantity_entry
        global l_name
        global l_cost 
        global l_quantity
        if pro_entry.get()=="" or quantity_entry.get()==():
            messagebox.showerror("Error","All fields are required",parent=root) 
        else:
            try:
                name=str(pro_entry.get())
                quantity=(quantity_entry.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from product where name='%s'"% name)
                cursor.execute(quary)
                data=cursor.fetchone()
                if data==None:
                    messagebox.showerror("Error","Product with this name doesnot exist:",parent=root) 
                    add_pur2()
                else:
                    l_name+=name+","
                    l_cost.append(data[4])
                    l_quantity.append(quantity)
                    frame_display=Frame(root,bg="lightgray")
                    frame_display.place(x=620,y=230,height=250,width=430)
                    head=Label(frame_display,text="CUSTOMER PURCHASE:",font=("Impact",24),fg="brown",bg="lightgray").place(x=10,y=10)
                    name_lab=Label(frame_display,text="PRODUCT NAME:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=10,y=60)
                    cost_lab=Label(frame_display,text="PRODUCT COST:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=10,y=110)
                    quantity_lab=Label(frame_display,text="PURCHASE QUANTITY:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=10,y=160)
                    name_val=Label(frame_display,text=name.upper(),font=("Impact",20),fg="brown",bg="lightgray").place(x=250,y=60)
                    cost_val=Label(frame_display,text=data[4],font=("Impact",20),fg="brown",bg="lightgray").place(x=250,y=110)
                    quantity_val=Label(frame_display,text=quantity,font=("Impact",20),fg="brown",bg="lightgray").place(x=250,y=160)
                    with open ("file.txt","a") as fobj:
                        pn=len(name)
                        pq=len(str(quantity))
                        costing=(float(quantity))*(data[4])
                        pc=len(str(costing))
                        fobj.write("\t"+"|  "+name+" "*(33-pn)+"|  "+quantity+" "*(23-pq)+"|  "+str(costing)+" "*(23-pc)+"|\n")
                        fobj.write("\t+"+ "-" * (35) + "+" + "-" * (25) + "+"+ "-" * (25) +"+" + "\n")
                    create_button=Button(root,command=add_pur4,cursor="hand2",text="    CREATE BILL    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=600,y=142,width=200,height=50)
                    add_pur5(name,quantity)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)  

def add_pur4():
    global root
    global l_name
    global l_cost 
    global phone_entry
    global name_entry
    global l_quantity
    global billing
    if l_name==[] or l_cost==[]:
        messagebox.showerror("Error","please enter products:",parent=root) 
    else:
        billing=0
        length=0
        for i in l_name:
            if i==",":
                length+=1
            else:
                pass
        for i in range(0,length):
            billing+=(Decimal(l_cost[i])*Decimal(l_quantity[i]))
        Frame_bill=Frame(root,bg="lightgray")
        Frame_bill.place(x=700,y=580,height=50,width=350)
        bill_head=Label(Frame_bill,text="TOTAL BILL :  Rs ",font=("Impact",17),fg="#6b0275",bg="lightgray").place(x=10,y=10)                    
        bill_VAL=Label(Frame_bill,text=billing,font=("Impact",17),fg="brown",bg="lightgray").place(x=150,y=10)
        with open("file.txt","a") as fobj:
            fobj.write("\n"+"\t\t\t  TOTAL BILL:  "+str(billing))
        programName = "notepad.exe" #notepad opening
        fileName = "file.txt"
        sp.Popen([programName, fileName])
        p_cost=""
        p_quantity=""
        for i in l_cost:
            p_cost+=str(i)+","
        for j in l_quantity:
            p_quantity+=str(j)+","
        try:
            c_phone=int(phone_entry.get())
            c_name=str(name_entry.get())
            dat_string=datetime.now()
            dop=dat_string.strftime("%Y/%m/%d %H:%M:%S")
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("insert into purchase (phone,name,p_name,p_cost,p_quantity,bill,dop)values(%s,'%s','%s','%s','%s',%s,'%s')"%(c_phone,c_name,l_name,p_cost,p_quantity,billing,dop))
            cursor.execute(quary)
            con.commit()
            messagebox.showinfo("data entered","bill created successfully:",parent=root)
            with open("file.txt","w") as fobj:
                fobj.write("")
            add_pur0(root)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)  

def add_pur5(name,quantity):
    con=c.connect("stock.db")
    cursor=con.cursor()
    quary=("select * from product where name='%s'"% name)
    cursor.execute(quary)
    data=cursor.fetchone()
    quantity1=data[3]
    p_quantity=Decimal(quantity1)-Decimal(quantity)
    cursor=con.cursor()
    quary=("update product set quantity=%s where name='%s'"%(p_quantity,name))
    cursor.execute(quary)
    con.commit()
    add_pur2()

def list_pur():
        global root
        root.destroy()
        root=Tk()
        root.title("STOCK MANAGEMENT")
        root.geometry("1100x670")  
        root.minsize(650,630)
        title_label=Label(text="PURCHASE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
        title_label.pack(fill=X)
        bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar1_label.pack(fill=X)
        bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar2_label.pack(fill=X,side=BOTTOM)
        bar3_label=Label(pady=25)
        bar3_label.pack(fill=X)
        back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
        headline=Label(text="LIST PURCHASE:",font=("Impact",30),fg="#6b0275").place(x=30,y=140)
        con=c.connect("stock.db")
        cursor=con.cursor()
        quary=("select * from purchase;")
        ptab=cursor.execute(quary)
        tree=ttk.Treeview()
        tree['show']='headings'
        s=ttk.Style(root)
        s.theme_use("clam")
        s.configure(".",font="comicsansm 12 bold")
        s.configure("Treeview.Heading",font="comicsansm 14 bold")
        tree["columns"]=("phnno","name","bill","dop")
        tree.column("phnno",width=260,anchor=CENTER)
        tree.column("name",width=260,anchor=CENTER)
        tree.column("bill",width=260,anchor=CENTER)
        tree.column("dop",width=260,anchor=CENTER)
        #assigning the heading of tree
        tree.heading("phnno",text="Customer Phone Number",anchor=CENTER)
        tree.heading("name",text="Customer Name",anchor=CENTER)
        tree.heading("bill",text="Customer Bill",anchor=CENTER)
        tree.heading("dop",text="Date of Purchase",anchor=CENTER)
        a=1
        for i in cursor:
            tree.insert('',a,text="",values=(i[0],i[1].upper(),i[5],i[6]))
            a+=1
        tree.pack()
        root.mainloop()

def search_pur():
        global root
        root.destroy()
        root=Tk()
        root.title("STOCK MANAGEMENT")
        root.geometry("1100x670")  
        root.minsize(650,630)
        title_label=Label(text="PURCHASE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
        title_label.pack(fill=X)
        bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar1_label.pack(fill=X)
        bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar2_label.pack(fill=X,side=BOTTOM)
        bar3_label=Label(pady=10)
        bar3_label.pack(fill=X,side=BOTTOM)
        back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
        headline=Label(text="SEARCH PURCHASE:",font=("Impact",30),fg="#6b0275").place(x=30,y=140)
        search_pur1()
        root.mainloop()

def search_pur1():
    global root
    global phone_entry
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=30,y=150,height=150,width=420)
    headline=Label(Frame_p,text="ENTER CUSTOMER PHONE NUMBER\nWHOES DATA YOU WANT TO SEARCH:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=10,y=7)
    phone_entry=Entry(Frame_p,font=("times new roman",15))
    phone_entry.focus()
    phone_entry.place(x=105,y=85)
    sow=1
    submit_button=Button(root,command=search_pur2,cursor="hand2",text="    SEARCH    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=135,y=280,width=200,height=50)

def search_pur2():
    global root
    global sow
    global phone_entry
    if phone_entry.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        name=str(phone_entry.get())
        con=c.connect("stock.db")
        cursor=con.cursor()
        quary=("select * from purchase where phone=%s;"%name)
        cursor.execute(quary)
        data=cursor.fetchall()
        if data==[]:
            messagebox.showerror("Error","Data with this phone number does not exist:",parent=root) 
            search_pur1()
        else:
            tree=ttk.Treeview()
            tree['show']='headings'
            s=ttk.Style(root)
            s.theme_use("clam")
            s.configure(".",font="comicsansm 12 bold")
            s.configure("Treeview.Heading",font="comicsansm 14 bold")

            tree["columns"]=("dop","pname","pcost","pquantity")
            tree.column("dop",width=260,anchor=CENTER)
            tree.column("pname",width=260,anchor=CENTER)
            tree.column("pcost",width=260,anchor=CENTER)
            tree.column("pquantity",width=260,anchor=CENTER)
            #assigning the heading of tree
            tree.heading("dop",text="Date of Purchase",anchor=CENTER)
            tree.heading("pname",text="Product Purchased",anchor=CENTER)
            tree.heading("pcost",text="Purchase Cost",anchor=CENTER)
            tree.heading("pquantity",text="Product Quantity",anchor=CENTER)
            for i in data:
                elep=i[2].split(",")
                len_a=len(elep)
                elec=i[3].split(",")
                eleq=i[4].split(",")
                l=0
                b=1
                for j in range(len_a-1):
                    tree.insert('',b,text="",values=(i[6],elep[l].upper(),(int(elec[l])*int(eleq[l])),eleq[l]))
                    l=l+1
                    b+=1
            search_pur1()
            tree.place(x=30,y=350)

def add_user():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="EMPLOYEE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    adduser_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    add_user1()

def add_user1():
    global root
    global phnno_entry
    global password_entry
    global recovery_entry
    global name_entry
    global desig_entry
    global c_pass_user
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=30,y=150,height=410,width=550)
    headline=Label(Frame_p,text="ADD NEW EMPLOYEEE:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=110,y=10)
    u_phnno=Label(Frame_p,text="EMPLOYEE PHONE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=80)
    u_name=Label(Frame_p,text="EMPLOYEE NAME:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=130)
    u_address=Label(Frame_p,text="EMPLOYEE DESIGNATION:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=180)
    u_password=Label(Frame_p,text="EMPLOYEE PASSWORD:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=230)
    u_password1=Label(Frame_p,text="CONFORM PASSWORD:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=280)
    u_recovery=Label(Frame_p,text="EMPLOYEE RECOVERY CODE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=20,y=330)
    phnno_entry=Entry(Frame_p,font=("times new roman",15))
    phnno_entry.focus()
    phnno_entry.place(x=320,y=85)
    name_entry=Entry(Frame_p,font=("times new roman",15))
    name_entry.place(x=320,y=135)
    dsg=['OWNER','MANAGER','STAFF','SECURITY GUARD','OTHERS']
    desig_entry=ttk.Combobox(Frame_p,state="readonly",values=dsg,width=30,height=10)
    desig_entry.place(x=320,y=185)
    password_entry=Entry(Frame_p,font=("times new roman",15),show="*")
    password_entry.place(x=320,y=235)
    c_pass_user=Entry(Frame_p,font=("times new roman",15),show="*")
    c_pass_user.place(x=320,y=285)
    recovery_entry=Entry(Frame_p,font=("times new roman",15))
    recovery_entry.place(x=320,y=335)
    submit_button=Button(root,command=add_user_fun,cursor="hand2",text="    ADD    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=200,y=535,width=200,height=50)
    root.mainloop()

def add_user_fun():
        global root
        global phnno_entry
        global name_entry
        global desig_entry
        global password_entry
        global recovery_entry
        global c_pass_user
        if phnno_entry.get()=="" or name_entry.get()=="" or desig_entry.get()=="" or password_entry.get()=="" or recovery_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root) 
        elif not (phnno_entry.get()).isdigit():
            messagebox.showerror("Error","Phone number should be of digits",parent=root)
        elif len(phnno_entry.get())<10 or len(phnno_entry.get())>10:
            messagebox.showerror("Error","Phone number should be of 10 digits",parent=root)
        elif password_entry.get()!=c_pass_user.get():
            messagebox.showerror("Error","Password doesnot match with Conform password",parent=root)
        elif acc_fun_1(phnno_entry.get())==1:
            messagebox.showerror("Error","Phone number already exist:",parent=root)
        else:
            try:
                login_id=int(phnno_entry.get())
                name=str(name_entry.get())
                password=str(password_entry.get())
                recovery=str(recovery_entry.get())
                desig=str(desig_entry.get())
                doj=date.today()
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary="insert into user values({},'{}','{}','{}','{}','{}')".format(login_id,name,desig,password,recovery,doj)
                cursor.execute(quary)
                con.commit()
                messagebox.showinfo("Employee Added","Employee added successfully",parent=root)
                add_user1()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def search_user():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="EMPLOYEE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    search_user1(root)

def search_user1(root):
    global u_phone_entry
    global viewarea
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=30,y=200,height=200,width=500)
    headline=Label(Frame_p,text="SEARCH EMPLOYEE:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=30,y=10)
    u_name=Label(Frame_p,text="ENTER EMPLOYEE USER ID\nWHOSE DATA YOU WANT:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=60)
    u_phone_entry=Entry(Frame_p,font=("times new roman",15))
    u_phone_entry.focus()
    u_phone_entry.place(x=80,y=130)
    submit_button=Button(root,command=search_user_fun,cursor="hand2",text="    SEARCH    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=110,y=375,width=200,height=50)
    root.mainloop()

def search_user_fun():
        global root
        global u_phone_entry
        global viewarea
        viewarea=Frame(root,bg="lightgray")
        viewarea.place(x=565,y=200,height=250,width=500)
        v_area=Label(viewarea,text="VIEW AREA:",font="comicsansm 25 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
        u_ph=Label(viewarea,text="EMPLOYEE PHONE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=60)
        u_n=Label(viewarea,text="EMPLOYEE NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=100)
        u_p=Label(viewarea,text="EMPLOYEE DESIGNATION:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=140)      
        if u_phone_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root) 
        else:
            try:
                name=int(u_phone_entry.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from user where login_id=%s"% name)
                cursor.execute(quary)
                data=cursor.fetchone()
                if data==None:
                    messagebox.showerror("Error","No data found",parent=root) 
                else:
                    viewarea1=Frame(viewarea,bg="lightgray")
                    viewarea1.place(x=290,y=50,height=300,width=200)
                    for i in range(5):
                        if i==0:                           
                            u_phnnoVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=10)
                        elif i==1:
                            u_nameVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=50)
                        elif i==2:
                            u_desigVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=90)
                            search_user1(root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def update_user():
    global root
    global u_name_entry
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="EMPLOYEE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="#44004b",bg="yellow",font=("times new roman",14,"bold")).place(x=900,y=100,width=180,height=40)
    update_user_0()

def update_user_0():
    global root
    global u_phone_entry
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=20,y=150,height=200,width=370)
    headline=Label(Frame_p,text="UPDATE EMPLOYEE:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=30,y=10)
    u_name=Label(Frame_p,text="ENTER EMPLOYEE ID WHOSE DATA\nYOU WANT TO UPDATE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=70)
    u_phone_entry=Entry(Frame_p,font=("times new roman",15))
    u_phone_entry.focus()
    u_phone_entry.place(x=85,y=140)
    submit_button=Button(root,command=update_user_1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=105,y=325,width=200,height=50)
    root.mainloop()

def update_user_1():
        global root
        global u_phone_entry       
        if u_phone_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root) 
        else: 
            try:
                viewarea=Frame(root,bg="lightgray")
                viewarea.place(x=20,y=420,height=180,width=420)
                v_area=Label(viewarea,text="OLD DATA:",font="comicsansm 22 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
                u_ph=Label(viewarea,text="EMPLOYEE PHONE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=50)
                u_n=Label(viewarea,text="EMPLOYEE NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=90)
                u_p=Label(viewarea,text="EMPLOYEE DESIGNATION:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=130)               
                name=str(u_phone_entry.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from user where login_id=%s"% name)
                cursor.execute(quary)
                data=cursor.fetchone()
                if data==None:
                    messagebox.showerror("Error","No data found",parent=root) 
                else:
                    viewarea1=Frame(viewarea,bg="lightgray")
                    viewarea1.place(x=250,y=50,height=200,width=200)
                    for i in range(5):
                        if i==0:                           
                            u_phnnoVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=0)
                        elif i==1:
                            u_nameVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=40)
                        elif i==2:
                            u_desigVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=80)
                            update_user_2(root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)  

def update_user_2(root):
    global u_name_entry
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=235,width=600)
    u_name=Label(viewarea2,text="SELECT WHICH YOU WANT TO UPDATE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=10)
    phnno_button=Button(viewarea2,command=update_user_phnno,cursor="hand2",text="    PHONE    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=20,y=50,width=200,height=50)
    name_button=Button(viewarea2,command=update_user_name,cursor="hand2",text="    NAME    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=20,y=110,width=200,height=50)
    password_button=Button(viewarea2,command=update_user_password,cursor="hand2",text="    PASSWORD    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=370,y=50,width=200,height=50)
    recovery_button=Button(viewarea2,command=update_user_recovery,cursor="hand2",text="    RECOVERY    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=370,y=110,width=200,height=50)
    designation_button=Button(viewarea2,command=update_user_designation,cursor="hand2",text="    DESIGNATION    ",fg="white",bg="#d77337",font=("times new roman",16,"bold")).place(x=20,y=170,width=200,height=50)    

def update_user_phnno():
    global u_phnno_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=235,width=600)
    u_name=Label(viewarea2,text="ENTER NEW PHONE OF THE EMPLOYEE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    u_phnno_entry_new=Entry(viewarea2,font=("times new roman",15))
    u_phnno_entry_new.focus()
    u_phnno_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_user_phnno1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_user_phnno1():
    global root
    global u_phnno_entry_new
    global u_phone_entry
    if u_phnno_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=int(u_phone_entry.get())
            name2=int(u_phnno_entry_new.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update user set login_id=%s where login_id=%s"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            messagebox.showinfo("updated","phone number updated successfully:",parent=root) 
            update_display(root,name2) 
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def update_user_name():
    global u_name_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=235,width=600)
    u_name=Label(viewarea2,text="ENTER NEW NAME OF THE EMPLOYEE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    u_name_entry_new=Entry(viewarea2,font=("times new roman",15))
    u_name_entry_new.focus()
    u_name_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_user_name1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_user_name1():
    global root
    global u_name_entry_new
    global u_phone_entry
    if u_name_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=int(u_phone_entry.get())
            name2=str(u_name_entry_new.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update user set name='%s' where login_id=%s"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            messagebox.showinfo("updated","Name updated successfully:",parent=root) 
            update_display(root,name1)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def update_user_password():
    global u_password_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=235,width=600)
    u_name=Label(viewarea2,text="ENTER NEW PASSWORD OF THE EMPLOYEE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    u_password_entry_new=Entry(viewarea2,font=("times new roman",15))
    u_password_entry_new.focus()
    u_password_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_user_password1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_user_password1():
    global root
    global u_password_entry_new
    global u_phone_entry
    if u_password_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=int(u_phone_entry.get())
            name2=str(u_password_entry_new.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update user set password='%s' where login_id=%s"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            messagebox.showinfo("updated","Password updated successfully:",parent=root) 
            update_user_0()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def update_user_recovery():
    global u_recovery_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=235,width=600)
    u_name=Label(viewarea2,text="ENTER NEW RECOVERY OF THE EMPLOYEE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    u_recovery_entry_new=Entry(viewarea2,font=("times new roman",15))
    u_recovery_entry_new.focus()
    u_recovery_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_user_recovery1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_user_recovery1():
    global root
    global u_recovery_entry_new
    global u_phone_entry
    if u_recovery_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=int(u_phone_entry.get())
            name2=str(u_recovery_entry_new.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update user set recovery=%s where login_id=%s"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            messagebox.showinfo("updated","Recovery code updated successfully:",parent=root) 
            update_user_0()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def update_user_designation():
    global u_designation_entry_new
    viewarea2=Frame(bg="lightgray")
    viewarea2.place(x=480,y=150,height=235,width=600)
    u_name=Label(viewarea2,text="SELECT NEW DESIGNATION OF THE EMPLOYEE:",font=("Impact",20),fg="#6b0275",bg="lightgray").place(x=50,y=10)
    dsg=['OWNER','MANAGER','STAF','SECURITY GUARD','OTHERS']
    u_designation_entry_new=ttk.Combobox(viewarea2,state="readonly",values=dsg,width=30,height=10)
    u_designation_entry_new.place(x=50,y=80)
    submit_button=Button(viewarea2,command=update_user_designation1,cursor="hand2",text="    UPDATE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=50,y=130,width=200,height=50)

def update_user_designation1():
    global root
    global u_designation_entry_new
    global u_phone_entry
    if u_designation_entry_new.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root) 
    else:
        try:
            name1=str(u_phone_entry.get())
            name2=str(u_designation_entry_new.get())
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("update user set desig='%s' where login_id=%s"%(name2,name1))
            cursor.execute(quary)
            con.commit()
            messagebox.showinfo("updated","Designation updated successfully:",parent=root) 
            update_display(root,name1)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

def update_display(root,name):
        try:
            viewarea=Frame(root,bg="lightgray")
            viewarea.place(x=480,y=420,height=180,width=420)
            v_area=Label(viewarea,text="NEW DATA:",font="comicsansm 22 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
            u_ph=Label(viewarea,text="EMPLOYEE PHONE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=50)
            u_n=Label(viewarea,text="EMPLOYEE NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=90)
            u_p=Label(viewarea,text="EMPLOYEE DESIGNATION:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=130)
            con=c.connect("stock.db")
            cursor=con.cursor()
            quary=("select * from user where login_id=%s"%name)
            cursor.execute(quary)
            data=cursor.fetchone()
            if data==None:
                messagebox.showerror("Error","No data found",parent=root) 
            else:
                viewarea1=Frame(viewarea,bg="lightgray")
                viewarea1.place(x=250,y=50,height=180,width=220)
                for i in range(5):
                    if i==0:                           
                        u_phnnoVAL=Label(viewarea1,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=0)
                    elif i==1:
                        u_nameVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=40)
                    elif i==2:
                        u_DESIGVAL=Label(viewarea1,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=20,y=80)
                        update_user_0()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root) 

def delete_user():
    global root
    root.destroy()
    root=Tk()
    root.title("STOCK MANAGEMENT")
    root.geometry("1100x670")
    root.minsize(650,630)
    title_label=Label(text="EMPLOYEE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
    title_label.pack(fill=X)
    bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar1_label.pack(fill=X)
    bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
    bar2_label.pack(fill=X,side=BOTTOM)
    back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
    delete_user_0()

def delete_user_0():  
    global root
    global u_code_entry  
    Frame_p=Frame(root,bg="lightgray")
    Frame_p.place(x=20,y=200,height=200,width=400)
    headline=Label(Frame_p,text="DELETE EMPLOYEE:",font=("Impact",30),fg="#6b0275",bg="lightgray").place(x=30,y=10)
    u_name=Label(Frame_p,text="ENTER EMPLOYEE PHONE NUMBER WHOSE\nDATA YOU WANT TO DELETE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=20,y=70)
    u_code_entry=Entry(Frame_p,font=("times new roman",15))
    u_code_entry.focus()
    u_code_entry.place(x=85,y=140)
    submit_button=Button(root,command=delete_user_1,cursor="hand2",text="    DELETE    ",fg="white",bg="#6b0275",font=("times new roman",16,"bold")).place(x=105,y=385,width=200,height=50)
    root.mainloop()

def delete_user_1():
        global root
        global u_code_entry
        if u_code_entry.get()==():
            messagebox.showerror("Error","All fields are required",parent=root) 
        else:
            try:
                name=int(u_code_entry.get())
                con=c.connect("stock.db")
                cursor=con.cursor()
                quary=("select * from user where login_id=%s"% name)
                cursor.execute(quary)
                data=cursor.fetchone()
                viewarea=Frame(root,bg="lightgray")
                viewarea.place(x=595,y=200,height=300,width=480)
                v_area=Label(viewarea,text="VIEW AREA:",font="comicsansm 25 bold",fg="#6b0275",bg="lightgray").place(x=30,y=10)               
                for i in range(0,3):
                    if i==0:   
                        u_p=Label(viewarea,text="EMPLOYEE PHONE:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=100)
                        u_phnnoVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=100)
                    elif i==1:
                        u_n=Label(viewarea,text="EMPLOYEE NAME:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=140)
                        u_nameVAL=Label(viewarea,text=data[i].upper(),font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=140)
                    elif i==2:
                        u_a=Label(viewarea,text="EMPLOYEE ADDRESS:",font=("Impact",18),fg="#6b0275",bg="lightgray").place(x=30,y=180)
                        u_addressVAL=Label(viewarea,text=data[i],font=("Impact",18),fg="brown",bg="lightgray").place(x=300,y=180)
                
                cursor=con.cursor()                  
                quary=("delete from user where login_id=%s"%name)
                cursor.execute(quary)       
                con.commit()
                messagebox.showinfo("Employee Deleted","User deleted successfully",parent=root) 
                delete_user_0()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)    
    
def list_user():
        global root
        root.destroy()
        root=Tk()
        root.title("STOCK MANAGEMENT")
        root.geometry("1100x670")  
        root.minsize(650,630)
        title_label=Label(text="EMPLOYEE MANAGEMENT",bg="#44004b",fg="white",pady=10,font="comicsansm 50 bold",borderwidth=3,relief=GROOVE)
        title_label.pack(fill=X)
        bar1_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar1_label.pack(fill=X)
        bar2_label=Label(bg="#ff002a",pady=4,borderwidth=3,relief=GROOVE)
        bar2_label.pack(fill=X,side=BOTTOM)
        bar3_label=Label(pady=25)
        bar3_label.pack(fill=X)
        back_button=Button(root,command=back_menu,cursor="hand2",text="BACK TO MENU",fg="white",bg="brown",font=("times new roman",14,"bold")).place(x=900,y=142,width=180,height=40)
        headline=Label(text="LIST EMPLOYEE:",font=("Impact",30),fg="#6b0275").place(x=30,y=140)
        con=c.connect("stock.db")
        cursor=con.cursor()
        quary=("select * from user;")
        cursor.execute(quary)       
        tree=ttk.Treeview()
        tree['show']='headings'
        s=ttk.Style(root)
        s.theme_use("clam")
        s.configure(".",font="comicsansm 12 bold")
        s.configure("Treeview.Heading",font="comicsansm 14 bold")
        tree["columns"]=("phnno","name","designation","doj")
        tree.column("phnno",width=220,anchor=CENTER)
        tree.column("name",width=220,anchor=CENTER)
        tree.column("designation",width=220,anchor=CENTER)
        tree.column("doj",width=220,anchor=CENTER)

        #assigning the heading of tree
        tree.heading("phnno",text="Employee Phone",anchor=CENTER)
        tree.heading("name",text="Employee Name",anchor=CENTER)
        tree.heading("designation",text="Employee Designation",anchor=CENTER)
        tree.heading("doj",text="Date of Joining",anchor=CENTER)      
        a=1
        for i in cursor:
            tree.insert('',a,text="",values=(i[0],i[1],i[2],i[5]))
            a+=1
        tree.pack()
        root.mainloop()

def add_table():
    mydb=c.connect("stock.db")
    mycursor=mydb.cursor()
    sql = "CREATE TABLE if not exists product (\
        code int(8) ,\
        name char(70) UNIQUE,\
        types varchar(15),\
        quantity decimal(8,2) ,\
        cost decimal(8,2),\
        dat datetime,\
        PRIMARY KEY (CODE));"
    mycursor.execute(sql)
    sql = "CREATE TABLE if not exists purchase (\
        phone bigint(10),\
        name char(30) ,\
        p_name varchar(200),\
        p_cost varchar(200),\
        p_quantity varchar(200),\
        bill decimal(10,2),\
        dop datetime);"
    mycursor.execute(sql)  
    sql = "CREATE TABLE if not exists user (\
        login_id bigint(10) PRIMARY KEY ,\
        name char(30) NOT NULL,\
        desig char(15),\
        password char(16) NOT NULL,\
        recovery char(30) NOT NULL,\
        doj date);"
    mycursor.execute(sql)
    print("ALL TABLE'S CREATED")

def after():
    if log==1:
        stock()

def main1():
    main()
    after()

def main():
    global root
    root=Tk()
    root.title("STOCK MANAGEMENT SYSTEM")
    root.geometry("1100x670")
    root.resizable(False,False)
    # Backgroung Image
    bg=ImageTk.PhotoImage(file="login.png")
    bg_image = Label(root, image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    first()
    root.mainloop()

add_table()
main1()
