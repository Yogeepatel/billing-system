from tkinter import *
from tkinter import ttk
import os
import tempfile

class struct():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1900x1900+0+0')
        self.root.title("BILLING APP")
        self.billnumbercounter=1
        self.gltotalprice=0
        title=ttk.Label(self.root,text="BILLING SYSTEM",font=('times new roman',40,'bold')).place(x=366,y=10)

        self.productcat=["Select Option","Mobile","TV","Fridge","AC"]

        self.mobilesubcat=["Tablet","smartphone"]
        self.tabproductname=["Apple","Samsung","Xiomi"]
        self.Mobileproductname=["Apple","Samsung","Oppo","Vivo"]
        self.appletabprice=18000
        self.appletabdis = 2
        self.samtabprice = 15000
        self.samtabdis = 4
        self.mitabprice = 14000
        self.mitabdis = 10
        self.applesmprice = 12000
        self.applesmdis = 0
        self.samspprice = 8000
        self.samspdis = 3
        self.vivosmprice = 7000
        self.vivosmdis = 5
        self.oppospprice = 7500
        self.oppospdis = 6

        self.tvsubcat=["66 Inch","80 Inch"]
        self.tvproductname=["L.G.","Sony"]
        self.lg6price = 22000
        self.lg6dis = 2
        self.lg8price = 27000
        self.lg8dis = 0
        self.s6price = 24000
        self.s6dis = 5
        self.s8price = 27500
        self.s8dis = 2

        self.fridgesubcat=["Single Door","Double Door"]
        self.fridgeproductname=["L.G.","samsung"]
        self.lg1price = 17500
        self.lg1dis = 0
        self.lg2price = 24000
        self.lg2dis = 3
        self.s1price = 24000
        self.s1dis = 2
        self.s2price = 27500
        self.s2dis = 6


        self.acsubcat=["Cooler","Large"]
        self.acproductname=["L.G.","whirlpool"]
        self.lgcprice = 12000
        self.lgcdis = 4
        self.lglprice = 47000
        self.lgldis = 1
        self.wpcprice = 14000
        self.wpcdis = 0
        self.wplprice = 57500
        self.wpldis = 2



        self.custmerinfo=LabelFrame(self.root, text="", bd=4)
        self.custmerinfo.place(x=10,y=90,width=900,height=50)
        self.labelcustname=Label(self.custmerinfo,text="CUSTMER NAME",font=('times new roman', 20),padx=5, pady=2)
        self.labelcustname.grid(row=0,column=0)
        self.inputcustname=ttk.Entry(self.custmerinfo,font=('times new roman', 15),width=20)
        self.inputcustname.grid(row=0,column=1)
        self.labelmobileno = Label(self.custmerinfo, text="MOBILE NUMBER", font=('times new roman', 20))
        self.labelmobileno.grid(row=0, column=2,stick=W,padx=10, pady=2)
        self.inputmobileno = ttk.Entry(self.custmerinfo, font=('times new roman', 15), width=16)
        self.inputmobileno.grid(row=0, column=3)

        self.billno = LabelFrame(self.root, text="", bd=4)
        self.billno.place(x=950, y=90, width=250, height=50)
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="red")
        #l1 = ttk.Label(text="Test", style="BW.TLabel")
        self.labelbillno=ttk.Label(self.billno,text="BILL NUMBER : ", font=('times new roman', 20), style="BW.TLabel")
        self.labelbillno.grid(row=0,column=0)


        #this need to be constructed properly
        self.billnoval=Label(self.billno,text=self.billnumbercounter, font=('times new roman', 20))
        self.billnoval.grid(row=0,column=1)


        self.billarea = LabelFrame(self.root, text="BILL AREA", bd="4", font=('times new roman', 20))
        self.billarea.place(x=830, y=150, width=430, height=362)
        self.text = Text(self.billarea,height=19,width=52)
        self.text.grid(row=0,column=0)
        self.text.insert(INSERT, "                           BILL RECEIPT\n")
        self.text.tag_add("aa", "1.5", "1.50")
        self.text.tag_config("aa", foreground="orange", font=('times new roman', 15))
        self.text.insert(END, "***********************************************************\n")
        self.text.tag_add("ab", "2.0", "2.80")
        self.text.tag_config("ab", foreground="blue", font=('times new roman', 10))
        self.text.insert(END, "        SHRI RAM ELECTRONICS")
        self.text.tag_add("ac", "3.0", "3.35")
        self.text.tag_config("ac", foreground="red", font=('times new roman', 20))
        self.welcm()





        self.items = LabelFrame(self.root, text="ITEMS", bd="4", font=('times new roman', 20))
        self.items.place(x=10, y=150, width=800, height=340)
        self.itemsframe = Frame(self.items,bd="4",bg="red")
        self.itemsframe.place(x=0,y=0,width=790,height=300)
        self.itemcategory=Label(self.itemsframe,text="ITEM CATEGORY",font=('times new roman', 22))
        self.itemcategory.grid(row=0,column=0)
        self.itemcat=ttk.Combobox(self.itemsframe,value=self.productcat, font=('arial',22,'bold'),width=24, state="readonly")
        self.itemcat.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.itemcat.current(0)
        self.itemcat.bind("<<ComboboxSelected>>",self.categ)
        self.subcategory = Label(self.itemsframe, text="SUB-CATEGORY", font=('times new roman', 23))
        self.subcategory.grid(row=1, column=0)
        self.subcat = ttk.Combobox(self.itemsframe,value=[" "], font=('arial', 22, 'bold'), width=24, state="readonly")
        self.subcat.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.subcat.bind("<<ComboboxSelected>>", self.subcatfun)
        self.productname = Label(self.itemsframe, text="PRODUCT NAME", font=('times new roman', 22))
        self.productname.grid(row=2, column=0)
        self.proname = ttk.Combobox(self.itemsframe, font=('arial', 22, 'bold'), width=24, state="readonly")
        self.proname.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.proname.bind("<<ComboboxSelected>>", self.sol)
        self.quantity = Label(self.itemsframe, text="QUANTITY", font=('times new roman', 25))
        self.quantity.grid(row=3, column=0)
        self.quant = ttk.Entry(self.itemsframe, font=('arial', 22, 'bold'), width=24)
        self.quant.grid(row=3, column=1, sticky=W, padx=5, pady=2)
        self.price = Label(self.itemsframe, text="PRICE", font=('times new roman', 23))
        self.price.grid(row=4, column=0)
        self.ptake=StringVar()
        self.pr = ttk.Label(self.itemsframe,textvariable = self.ptake, font=('arial', 22, 'bold'), width=24)
        self.pr.grid(row=4, column=1, sticky=W, padx=5, pady=2)
        self.discount = Label(self.itemsframe, text="DISCOUNT", font=('times new roman', 25))
        self.discount.grid(row=5, column=0)
        self.take=StringVar()
        self.disc = ttk.Label(self.itemsframe,textvariable = self.take, font=('arial', 22, 'bold'), width=24,relief=RAISED)
        self.disc.grid(row=5, column=1, sticky=W, padx=5, pady=2)



        self.billcounter = LabelFrame(self.root,text= "BILL COUNTER", bd="4", font=('times new roman', 20),fg="blue")
        self.billcounter.place(x=5,y=510,width=1260, height=135)
        self.buttons=Frame(self.billcounter)
        self.buttons.place(x=320,y=0,width=930,height=90)
        self.clearbtn=Button(self.buttons,command=self.clear_button,text= "CLEAR", bd="4", font=('times new roman', 25),bg="orange", height=1)
        self.clearbtn.grid(row=0,column=4)
        self.addtocart=Button(self.buttons,text= "ADD TO CART",command = self.adtocart, bd="4", font=('times new roman', 25),bg="orange", height=1)
        self.addtocart.grid(row=0,column=1)
        self.printbill=Button(self.buttons,text= "PRINT",command = self.iprint ,bd="4", font=('times new roman', 25),bg="orange", height=1)
        self.printbill.grid(row=0,column=3)
        self.total=Button(self.buttons,text= "GENERATE BILL",command=self.fun_genbill, bd="4", font=('times new roman', 25),bg="orange", height=1)
        self.total.grid(row=0,column=2)
        self.exitapp=Button(self.buttons,text= "EXIT", bd="4", command = self.root.destroy, font=('times new roman', 25),bg="red", height=1)
        self.exitapp.grid(row=0,column=5)
        self.subt=Frame(self.billcounter)
        self.subt.place(x=0, y=0, width=300, height=95)
        self.subtotallabel=ttk.Label(self.subt,text= "SUB-TOTAL", font=('times new roman', 15))
        self.subtotallabel.grid(row=0,column=0)
        self.subte=StringVar()
        self.subtotalentry= Label(self.subt,textvariable =self.subte, width=18,font=('times new roman', 15),bg="yellow")
        self.subtotalentry.grid(row=0,column=1)
        self.discountlabel = Label(self.subt, text="DISCOUNT", font=('times new roman', 16),padx=3, pady=5)
        self.discountlabel.grid(row=1, column=0)
        self.disce = StringVar()
        self.discountentry = Label(self.subt,textvariable=self.disce, width=18, font=('times new roman', 15),bg="yellow")
        self.discountentry.grid(row=1, column=1)
        self.totallabel = ttk.Label(self.subt, text="TOTAL", font=('times new roman', 17))
        self.totallabel.grid(row=2, column=0)
        self.te = StringVar()
        self.totalentry = Label(self.subt,textvariable = self.te, width=18, font=('times new roman', 15),bg="yellow")
        self.totalentry.grid(row=2, column=1)


    def welcm(self):
        self.text.insert(END, "\nBILL NUMBER : ")
        self.text.tag_add("ah", "4.0", "4.14")
        self.text.tag_config("ah", foreground="blue", font=('times new roman', 12))
        self.text.insert(END, self.billnumbercounter)
        self.text.tag_add("ai", "4.14", "6.30")
        self.text.tag_config("ai", foreground="black", font=('times new roman', 12))
        self.text.insert(END, "\nNAME : ")
        self.text.tag_add("ad", "5.0", "5.6")
        self.text.tag_config("ad", foreground="blue", font=('times new roman', 12))
        self.text.insert(END, self.inputcustname.get())
        self.text.tag_add("zz", "5.6", "5.26")
        self.text.tag_config("zz", foreground="black", font=('times new roman', 12))
        self.text.insert(END, "\nMOBILE NUMBER : ")
        self.text.tag_add("af", "6.0", "6.16")
        self.text.tag_config("af", foreground="blue", font=('times new roman', 12))
        self.text.insert(END, self.inputmobileno.get())
        self.text.tag_add("ag", "6.16", "6.30")
        self.text.tag_config("ag", foreground="black", font=('times new roman', 12))
        self.text.insert(END,"\n-------------------------------------------------------------------------------------------------------\n")
        self.text.tag_add("aj", "7.0", "7.103")
        self.text.tag_config("aj", foreground="blue", font=('times new roman', 10))
        self.text.insert(END, "PRODUCT                           QTY                                AMOUNT\n")
        self.text.tag_add("al", "8.0", "8.40")
        self.text.tag_config("al", foreground="black", font=('times new roman', 12))

    def fun_genbill(self):
        textarea_data=self.text.get(9.0,END)
        #print(textarea_data)
        self.text.delete(4.0, END)
        self.welcm()
        self.text.insert(END,textarea_data)
        self.text.insert(END,"\n####################################################")
        self.text.insert(END,f"\n\t\t\tTotal Amount :  Rs {self.gltotalprice}")

    def categ(self,event=""):
        if self.itemcat.get()=="Mobile":
            self.subcat.set(value="")
            self.subcat.config(value=self.mobilesubcat)
            #self.subcat.current(0)
            self.proname.set(value='')
            self.take.set("")
            self.ptake.set("")
            self.quant.delete(0, END)
        if self.itemcat.get()=="TV":
            self.subcat.set(value="")
            self.subcat.config(value=self.tvsubcat)
            #self.subcat.current(0)
            self.proname.set(value='')
            self.take.set("")
            self.ptake.set("")
            self.quant.delete(0, END)

        if self.itemcat.get()=="Fridge":
            self.subcat.set(value="")
            self.subcat.config(value=self.fridgesubcat)
            #self.subcat.current(0)
            self.proname.set(value='')
            self.take.set("")
            self.ptake.set("")
            self.quant.delete(0, END)
        if self.itemcat.get()=="AC":
            self.subcat.set(value="")
            self.subcat.config(value=self.acsubcat)
            #self.subcat.current(0)
            self.proname.set(value='')
            self.take.set("")
            self.ptake.set("")
            self.quant.delete(0, END)
        if self.itemcat.get()=="Select Option":
            self.subcat.set(value="")
            self.subcat.config(value='')
            self.proname.set(value="")
            self.proname.config(value="")
            self.take.set("")
            self.ptake.set("")
            self.quant.delete(0, END)


    def subcatfun(self,event=""):
        if self.subcat.get()=="Tablet":
            self.proname.set(value="")
            self.proname.config(value=self.tabproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="smartphone":
            self.proname.set(value="")
            self.proname.config(value=self.Mobileproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="66 Inch":
            self.proname.set(value="")
            self.proname.config(value=self.tvproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="80 Inch":
            self.proname.set(value="")
            self.proname.config(value=self.tvproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="Single Door":
            self.proname.set(value="")
            self.proname.config(value=self.fridgeproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="Double Door":
            self.proname.set(value="")
            self.proname.config(value=self.fridgeproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="Cooler":
            self.proname.set(value="")
            self.proname.config(value=self.acproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="Large":
            self.proname.set(value="")
            self.proname.config(value=self.acproductname)
            self.sol()
            #self.proname.current(0)
        if self.subcat.get()=="":
            self.proname.config(value="")
            self.proname.set(value="")
            self.sol()

    def calc(self,a,b):
        t=(b/100*a)
        x=(a-t)
        return x,t

    def sol(self,event=''):
        self.quant.delete(0,END)
        self.quant.insert(END,"1")
        if self.proname.get()=="Apple" and self.subcat.get()=="Tablet":
            self.take.set(self.appletabdis)
            self.ptake.set(self.appletabprice)
            self.subvalue,self.subdisc = self.calc(self.appletabprice,self.appletabdis)
        if self.proname.get() == "Apple" and self.subcat.get() == "smartphone":
            self.take.set(self.applesmdis)
            self.ptake.set(self.applesmprice)
            self.subvalue, self.subdisc = self.calc(self.applesmprice, self.applesmdis)
        if self.proname.get() == "Samsung" and self.subcat.get() == "Tablet":
            self.take.set(self.samtabdis)
            self.ptake.set(self.samtabprice)
            self.subvalue, self.subdisc = self.calc(self.samtabprice, self.samtabdis)
        if self.proname.get() == "Samsung" and self.subcat.get() == "smartphone":
            self.take.set(self.samspdis)
            self.ptake.set(self.samspprice)
            self.subvalue, self.subdisc = self.calc(self.samspprice, self.samspdis)
        if self.proname.get() == "Oppo" and self.subcat.get() == "smartphone":
            self.take.set(self.oppospdis)
            self.ptake.set(self.oppospprice)
            self.subvalue, self.subdisc = self.calc(self.oppospprice, self.oppospdis)
        if self.proname.get() == "Vivo" and self.subcat.get() == "smartphone":
            self.take.set(self.vivosmdis)
            self.ptake.set(self.vivosmprice)
            self.subvalue, self.subdisc = self.calc(self.vivosmprice, self.vivosmdis)
        if self.proname.get() == "Xiomi" and self.subcat.get() == "Tablet":
            self.take.set(self.mitabdis)
            self.ptake.set(self.mitabprice)
            self.subvalue, self.subdisc = self.calc(self.mitabprice, self.mitabdis)
        if self.proname.get() == "L.G." and self.subcat.get() == "66 Inch":
            self.take.set(self.lg6dis)
            self.ptake.set(self.lg6price)
            self.subvalue, self.subdisc = self.calc(self.lg6price, self.lg6dis)
        if self.proname.get() == "Sony" and self.subcat.get() == "66 Inch":
            self.take.set(self.s6dis)
            self.ptake.set(self.s6price)
            self.subvalue, self.subdisc = self.calc(self.s6price, self.s6dis)
        if self.proname.get() == "L.G." and self.subcat.get() == "80 Inch":
            self.take.set(self.lg8dis)
            self.ptake.set(self.lg8price)
            self.subvalue, self.subdisc = self.calc(self.lg8price, self.lg8dis)
        if self.proname.get() == "Sony" and self.subcat.get() == "80 Inch":
            self.take.set(self.s8dis)
            self.ptake.set(self.s8price)
            self.subvalue, self.subdisc = self.calc(self.s8price, self.s8dis)
        if self.proname.get() == "L.G." and self.subcat.get() == "Single Door":
            self.take.set(self.lg1dis)
            self.ptake.set(self.lg1price)
            self.subvalue, self.subdisc = self.calc(self.lg1price, self.lg1dis)
        if self.proname.get() == "samsung" and self.subcat.get() == "Single Door":
            self.take.set(self.s1dis)
            self.ptake.set(self.s1price)
            self.subvalue, self.subdisc = self.calc(self.s1price, self.s1dis)
        if self.proname.get() == "L.G." and self.subcat.get() == "Double Door":
            self.take.set(self.lg2dis)
            self.ptake.set(self.lg2price)
            self.subvalue, self.subdisc = self.calc(self.lg2price, self.lg2dis)
        if self.proname.get() == "samsung" and self.subcat.get() == "Double Door":
            self.take.set(self.s2dis)
            self.ptake.set(self.s2price)
            self.subvalue, self.subdisc = self.calc(self.s2price, self.s2dis)
        if self.proname.get() == "L.G." and self.subcat.get() == "Cooler":
            self.take.set(self.lgcdis)
            self.ptake.set(self.lgcprice)
            self.subvalue, self.subdisc = self.calc(self.lgcprice, self.lgcdis)
        if self.proname.get() == "L.G." and self.subcat.get() == "Large":
            self.take.set(self.lgldis)
            self.ptake.set(self.lglprice)
            self.subvalue, self.subdisc = self.calc(self.lglprice, self.lgldis)
        if self.proname.get() == "whirlpool" and self.subcat.get() == "Cooler":
            self.take.set(self.wpcdis)
            self.ptake.set(self.wpcprice)
            self.subvalue, self.subdisc = self.calc(self.wpcprice, self.wpcdis)
        if self.proname.get() == "whirlpool" and self.subcat.get() == "Large":
            self.take.set(self.wpldis)
            self.ptake.set(self.wplprice)
            self.subvalue, self.subdisc = self.calc(self.wplprice, self.wpldis)
        if self.proname.get()=="":
            self.take.set("")
            self.ptake.set("")
            self.quant.delete(0,END)

    def adtocart(self):
        self.newval=int(self.quant.get())*self.subvalue
        self.gltotalprice=self.gltotalprice + self.newval
        self.subte.set(self.newval)
        self.te.set(self.gltotalprice)
        self.disce.set(self.subdisc)
        #self.text.insert(END,self.proname.get())
        self.text.insert(END,self.itemcat.get())
        self.text.insert(END,self.subcat.get())
        self.text.insert(END,"\t\t\t")
        self.text.insert(END,self.quant.get())
        self.text.insert(END,"\t\t")
        self.text.insert(END,self.newval)
        self.text.insert(END,'\n')

    def iprint(self):
        q=self.text.get(1.0,END)
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")








    def clear_button(self):
        self.billnumbercounter = self.billnumbercounter + 1
        self.billnoval = Label(self.billno, text=self.billnumbercounter, font=('times new roman', 20))
        self.billnoval.grid(row=0, column=1)
        self.inputcustname.delete(0,END)
        self.inputmobileno.delete(0,END)
        '''self.totalentry.delete(0,END)
        self.subtotalentry.delete(0,END)
        self.discountentry.delete(0,END)'''
        self.subte.set("")
        self.te.set("")
        self.disce.set("")
        self.subcat.set(value='')
        self.itemcat.set(value='')
        self.proname.set(value='')
        self.text.delete(4.0,END)
        self.take.set("")
        self.ptake.set("")
        self.quant.delete(0, END)
        self.welcm()












'''frame1 = Frame()
name = Entry(frame1,font=('Verdana', 30),width=16)
mobno = Entry(frame1)
lname= Label(frame1,text="Name",font=('Verdana', 24, 'bold'))
lmobno= Label(frame1,text = "Mobile Number",font=('Verdana', 24, 'bold'))
name.grid(row=0, column=1,columnspan=4)
mobno.grid(row=0,column=6,columnspan=4)
lname.grid(row=0,column=0)
lmobno.grid(row=0,column = 5)
frame1.grid(row=0, column=0)'''
#user_name = Label(text="Username").grid(row=1,column=0)
#ser_name_input_area = Entry(width=30).grid(row=1,column=1)
'''fr=Frame()
fr.pack()
labelframe = LabelFrame(fr, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="Inside the LabelFrame")

left.pack()'''
root=Tk()
app=struct(root)
mainloop()