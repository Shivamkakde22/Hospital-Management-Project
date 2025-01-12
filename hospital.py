from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.Nameoftablets = StringVar()
        self.ReferenceNo = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.furtherinformation = StringVar()
        self.bloodPressure = StringVar()
        self.Storage = StringVar()
        self.Medication = StringVar()
        self.patientID = StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.Address = StringVar()

        lbtitle = Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)

        # =======================================Dataframe========================================
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=970,height=350)

        self.DataFrameRight = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        self.DataFrameRight.place(x=990,y=5,width=500,height=350)

        # ======================================ButtonFrame====================================================
        self.ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        self.ButtonFrame.place(x=0,y=530,width=1530,height=70)

        # ======================================DetailFrame======================================================
        self.DetailFrame=Frame(self.root,bd=20,relief=RIDGE)
        self.DetailFrame.place(x=0,y=600,width=1530,height=190)

        #=======================================DataFrame Left=========================================================
        lbNameTablet = Label(DataFrameLeft,text="Name Of Tablet",font=("times new roman",12,"bold"))
        lbNameTablet.grid(row=0,column=0)

        contactNameTablet = ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=33)
        contactNameTablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","A,lodipine","Ativan")
        contactNameTablet.grid(row=0,column=1)

        lblref = Label(DataFrameLeft,text="Reference No.",font=("arial",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ReferenceNo,width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataFrameLeft,text="Dose : ",font=("arial",12,"bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets = Label(DataFrameLeft,text="No. of Tablets::",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLots = Label(DataFrameLeft,text="Lots :",font=("arial",12,"bold"),padx=2,pady=6)
        lblLots.grid(row=4,column=0,sticky=W)
        txtLots=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLots.grid(row=4,column=1)

        lblIssueDate = Label(DataFrameLeft,text="Issue Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.IssueDate,width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDates = Label(DataFrameLeft,text="Exp Date: ",font=("arial",12,"bold"),padx=2,pady=6)
        lblExpDates.grid(row=6,column=0,sticky=W)
        txtExpDates=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDates.grid(row=6,column=1)

        lblDailyDose = Label(DataFrameLeft,text="Daily Dose: ",font=("arial",12,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect = Label(DataFrameLeft,text="Side Effect :",font=("arial",12,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.SideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInformation = Label(DataFrameLeft,text="Further Information :",font=("arial",12,"bold"),padx=4)
        lblFurtherInformation.grid(row=0,column=2,sticky=W)
        txtFurtherInformation=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.furtherinformation,width=35)
        txtFurtherInformation.grid(row=0,column=3)

        lblBloodPressure = Label(DataFrameLeft,text="Blood Pressure :",font=("arial",12,"bold"),padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bloodPressure,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorageAdvice = Label(DataFrameLeft,text="Storage Advice :",font=("arial",12,"bold"),padx=2,pady=6)
        lblStorageAdvice.grid(row=2,column=2,sticky=W)
        txtStorageAdvice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Storage,width=35)
        txtStorageAdvice.grid(row=2,column=3)

        lblMedication = Label(DataFrameLeft,text="Medication :",font=("arial",12,"bold"),padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Medication,width=35)
        txtMedication.grid(row=3,column=3)

        lblPateintID = Label(DataFrameLeft,text="Patient Id :",font=("arial",12,"bold"),padx=2,pady=6)
        lblPateintID.grid(row=4,column=2,sticky=W)
        txtPateintID=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.patientID,width=35)
        txtPateintID.grid(row=4,column=3)

        lblNHSNumber = Label(DataFrameLeft,text="NHS Number: ",font=("arial",12,"bold"),padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NHSNumber,width=35)
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName = Label(DataFrameLeft,text="Patient Name :",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth = Label(DataFrameLeft,text="Date of Birth :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataFrameLeft,text="Patient Address :",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Address,width=35)
        txtPatientAddress.grid(row=8,column=3)

#========================================DataFrame Right=====================================================
class Prescription:
    def __init__(self, DataFrameRight):
        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=50, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

# ==============================================Buttons===========================================================
class Buttons:
    def __init__(self, ButtonFrame,hospital):
        self.hospital = hospital
        self.isPreciptionData = False
        self.btnPrescription = Button(ButtonFrame, text="Prescription", bg="green", fg="white", 
                                      font=("arial", 12, "bold"), width=25, height=2, 
                                      padx=2, pady=6)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPresciptiondata = Button(ButtonFrame,command=self.isPreciptionData, text="Prescription Data", bg="green", fg="white",
                              font=("arial", 12, "bold"), width=25, height=2, padx=2, pady=6)
        self.btnPresciptiondata.grid(row=0, column=1)

        self.btnUpadate = Button(ButtonFrame,command=self.update, text="Update", bg="green", fg="white", 
                                      font=("arial", 12, "bold"), width=25, height=2, 
                                      padx=2, pady=6)
        self.btnUpadate.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame, text="Delete", bg="green", fg="white", 
                                      font=("arial", 12, "bold"), width=25, height=2, 
                                      padx=2, pady=6)
        self.btnDelete.grid(row=0, column=3)  

        self.btnClear = Button(ButtonFrame, text="Clear", bg="green", fg="white", 
                                      font=("arial", 12, "bold"), width=25, height=2, 
                                      padx=2, pady=6)
        self.btnClear.grid(row=0, column=4)

        self.btnExit = Button(ButtonFrame, text="Exit", bg="green", fg="white", 
                                      font=("arial", 12,"bold"), width=24, height=2, 
                                      padx=2, pady=6)
        self.btnExit.grid(row=0, column=5)

    def isPreciptionData(self):
        if self.nameoftablets=="" or self.ReferenceNo=="":
            messagebox.showerror("Error","All details are required")
        else:
           conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ecom"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
            self.nameoftablets.get(),
            self.ReferenceNo.get(),
            self.dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.SideEffect.get(),
            self.furtherinformation.get(),
            self.bloodPressure.get(),
            self.Storage.get(),
            self.Medication.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Prescription Added Successfully")


    def update(self):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ecom"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set NameOftablets=%s,ReferenceNo=%s,Dose=%s,No_of_tablets=%s,Lots=%s,Issue_Date=%s,Exp_Date=%s,Daily_Dose=%s,Storage=%s,nhsNumber=%s,Patienname=%s,dateOfBirth=%s,PatientAddress=%s,")

    

   

#==============================================TABLE====================================================
#=============================================ScrollBar=================================================

class ScrollBars:
    def __init__(self, DetailFrame):
        self.scroll_x = ttk.Scrollbar(DetailFrame, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(DetailFrame, orient=VERTICAL)
        
        self.hospital_table = ttk.Treeview(DetailFrame, 
                                           columns=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", 
                                                    "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), 
                                           xscrollcommand=self.scroll_x.set, 
                                           yscrollcommand=self.scroll_y.set)
        
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        
        self.scroll_x.config(command=self.hospital_table.xview)
        self.scroll_y.config(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="Number of Tablets")
        self.hospital_table.heading("lot", text="Lots")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Experied Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")
        
        self.hospital_table["show"] = "headings"
        
        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def get_cursor(self):
        cursor_row  =self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0]),
        self.ReferenceNo.set(row[1]),
        self.Dose.set(row[2]),
        self.NumberofTablets.set(row[3]),
        self.Lot.set(row[4]),
        self.IssueDate.set(row[5]),
        self.ExpDate.set(row[6]),
        self.DailyDose.set(row[7]),
        self.Storage.set(row[8]),
        self.NHSNumber.set(row[9]),    
        self.PatientName.set(row[10]),
        self.DateOfBirth.set(row[11]),
        self.Address.set(row[12])

    def fetch_data(self):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ecom"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#========================================Functionality Declaration======================================
    def isPresiption(self):
       self.txtPrescription.insert(END, "Name of Tablets:\t\t" + self.Nameoftablets.get() + "\n")
       self.txtPrescription.insert(END, "Reference No:\t\t" + self.ReferenceNo.get() + "\n")
       self.txtPrescription.insert(END, "Dose:\t\t" + self.Dose.get() + "\n")
       self.txtPrescription.insert(END, "Number of Tablets:\t" + self.NumberofTablets.get() + "\n")
       self.txtPrescription.insert(END, "Lot:\t\t" + self.Lot.get() + "\n")
       self.txtPrescription.insert(END, "Issue Date:\t\t" + self.IssueDate.get() + "\n")
       self.txtPrescription.insert(END, "Exp Date:\t\t" + self.ExpDate.get() + "\n")
       self.txtPrescription.insert(END, "Daily Dose:\t\t" + self.DailyDose.get() + "\n")
       self.txtPrescription.insert(END, "Side Effect:\t\t" + self.SideEffect.get() + "\n")
       self.txtPrescription.insert(END, "Further Information:\t\t" + self.FurtherInformation.get() + "\n")
       self.txtPrescription.insert(END, "Storage Advice:\t\t" + self.StorageAdvice.get() + "\n")
       self.txtPrescription.insert(END, "Driving Using Machine:\t\t" + self.DrivingUsingMachine.get() + "\n")
       self.txtPrescription.insert(END, "Storage:\t\t" + self.Storage.get() + "\n")
       self.txtPrescription.insert(END, "NHS Number:\t\t" + self.NHSNumber.get() + "\n")
       self.txtPrescription.insert(END, "Patient Name:\t\t" + self.PatientName.get() + "\n")
       self.txtPrescription.insert(END, "Date of Birth:\t\t" + self.DateOfBirth.get() + "\n")
       self.txtPrescription.insert(END, "Address:\t\t" + self.Address.get() + "\n")

    def idelete(self):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ecom"
        )
        my_cursor = conn.cursor()





root = Tk()
ob = Hospital(root)
ob1 = Prescription(ob.DataFrameRight)
ob2 = Buttons(ob.ButtonFrame,ob)
ob3 = ScrollBars(ob.DetailFrame)

root.mainloop()
