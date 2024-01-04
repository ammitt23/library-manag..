from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime
class LibraryManagementSystem:      
    def __init__(self,root):
        self.root=root
        self.root.title("library Management System")
        self.root.geometry('1550x800+0+0')
        
        lbltitle=Label(self.root,text='LIBRARY MANAGEMENT SYSTEM',bg="orange",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        
        #========Varriable==============
        self.member_var=StringVar()
     
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar() 
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.moblie_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        
        
        
        
        
        
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

         # library membership information and bd color
        #===========DataFrameleft=================
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)
        
        
        
        lblMember=Label(DataFrameLeft,font=("times new roman",15,"bold"),text="Member Type",padx=2,pady=6,bg="powder blue")
        lblMember.grid(row=0,column=0,sticky=W)
        
        
        
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",font=("times new roman",15,"bold"),width=27)
        
        comMember["value"]=("Admin Staff","Student","lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        
        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN NO:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No.:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
    
        
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,bg="powder blue",text="lastName:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        
        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
         
        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="PostCode:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)
        
        
         
        lblMoblie=Label(DataFrameLeft,bg="powder blue",text="Moblie:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMoblie.grid(row=8,column=0,sticky=W)
        txtMoblie=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.moblie_var,width=29)
        txtMoblie.grid(row=8,column=1)
        
         
        lblBookId=Label(DataFrameLeft,bg="powder blue",text="BookId:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)
        
         
        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="BookTitle:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        
         
        lblAuther=Label(DataFrameLeft,bg="powder blue",text="Auther:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)
        
        
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="DateBorrowed:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)
        
        
        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="DateDue:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)
        
        
        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="DaysOnBook:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)
        
        
        lbllastReturnfine=Label(DataFrameLeft,bg="powder blue",text="late Return fine:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbllastReturnfine.grid(row=6,column=2,sticky=W)
        txtlastReturnfine=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtlastReturnfine.grid(row=6,column=3)
        
        
        lblDateOverDate=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDate.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Final Price",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)
        
        
        #============Data frame Right#==================
        
        
        
        DataFrameRight=LabelFrame(frame,text="Books Details ",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)

        DataFrameRight.place(x=870,y=5,width=580,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
         
        listBooks=["Head First Book","Learn Python The Hard Way","Python Programming", 
                    "Secrets Rahasya","Python CoolBook","Into Machine Learning","Machine Techno",
                    "Joss Elle Guru","Bhagavad Gita","Elite Jungle Python","Machine Python", 
                    "Advanced Python","Basic Java","Computer Basic","Advanced learning java","Black Theroy","Chemistry","Maths"]

        

       

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                (d3)=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.700")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID4343")
                self.booktitle_var.set("Basic of Python")
                self.auther_var.set("Zed A.SHAN")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                (d3)=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.720")

            elif (x=="Python Programming"):
                self.bookid_var.set("BKID3232")
                self.booktitle_var.set("Intro of Python Programming")
                self.auther_var.set("RS Ankit Jha")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                (d3)=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.654")
            elif (x=="Secrets Rahasya"):
                self.bookid_var.set("BKID4623")
                self.booktitle_var.set("Secrets")
                self.auther_var.set("Abhay Gupta")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                (d3)=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.35")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.604")

            elif (x=="Python CoolBook"):
                self.bookid_var.set("BKID4526")
                self.booktitle_var.set("CoolBook")
                self.auther_var.set("Amit Kuamar")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                (d3)=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.689")

            elif (x=="Into Machine Learning"):
                self.bookid_var.set("BKID4533")
                self.booktitle_var.set(" Machine Learning")
                self.auther_var.set("Shetya Kuamari")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                (d3)=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.37")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.670")




        
       
        
        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)


        
        for item in listBooks:
            listBox.insert(END,item)
        
      
        
        
        
        
        
        
        
        
        
        
         #=================Buttons frame=========================#
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)
        
        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        
         #==========information frame========= down table===================#
       
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1",
                                             "address2","postid","moblie","bookid","booktitle","auther","dateborrowed",
                                             "datedue","daysonbook","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        
        self.library_table.heading("moblie",text="Moblie Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("daysonbook",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("moblie",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)                
        self.library_table.column("daysonbook",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100) 
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

   
        
    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Amo@1234",database="amitdb")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                              self.member_var.get(),
                                                                                                              self.prn_var.get(),
                                                                                                              self.id_var.get(),
                                                                                                              self.firstname_var.get(),
                                                                                                              self.lastname_var.get(),
                                                                                                              self.address1_var.get(),
                                                                                                              self.address2_var.get(),
                                                                                                              self.postcode_var.get(),
                                                                                                              self.moblie_var.get(),
                                                                                                              self.bookid_var.get(),
                                                                                                              self.booktitle_var.get(),
                                                                                                              self.auther_var.get(),
                                                                                                              self.dateborrowed_var.get(),
                                                                                                              self.datedue_var.get(),
                                                                                                              self.daysonbook_var.get(),
                                                                                                              self.latereturnfine_var.get(),
                                                                                                              self.dateoverdue_var.get(),
                                                                                                              self.finalprice_var.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member Has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Amo@1234",database="amitdb")
        my_cursor=conn.cursor()
        my_cursor.execute("update library2 set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Moblie=%s,Bookid=%s,Booktitle=%s,Auther=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.moblie_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get()
                                                                                             ))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member Has been updated successfully")



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Amo@1234", database="amitdb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library2")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.moblie_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])


# =====Show data  button==============#

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LasName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Moblie:\t\t"+ self.moblie_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+ self.finalprice_var.get() + "\n")



        # ==========Reset button========#
    def reset(self):
        self.member_var.set(""),
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.moblie_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)



#====== EXIT BUTTON FUNCTION========

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return


## delete button fucntion

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Amo@1234",database="amitdb")
            my_cursor=conn.cursor()
            query="delete from library2 where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("succes","Member has been Deleted")

            

            





                                                                                                         
                                                                                                                 
                                                                                                                
           
            
            
            
            
            
            
            
            
            
            
            
if __name__ =="__main__":
    
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()