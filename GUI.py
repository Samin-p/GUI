from tkinter import *
from tkinter import ttk

root = Tk()


def calculate():
      amin(iv.get())
    

def amin(x):
        x=x-iv1.get()
        net_nettaxable=x-75000#Standard deduction
        def cess(x):
            return 4/100*x 
                    
        if net_nettaxable<=300000:
            ok="Nil.you don't have to pay tax"
            message.config(text=ok)
                   
        elif 300000<net_nettaxable<=700000:
                ok="No tax charge under section 87 A rebate"
                message.config(text=ok)
                        
        elif 700000<net_nettaxable<=1000000:
            hero=400000*5/100
            hero1=(net_nettaxable-700000)*10/100
              
            op=cess(hero1+hero)+hero+hero1
            message.config(text=op)
                
        elif 1000000<net_nettaxable<=1200000:
            hero=400000*5/100
            hero2=(net_nettaxable-1000000)*15/100
            new=300000*10/100
            print(cess(hero+new+hero2)+hero+new+hero2)
            ok=cess(hero+new+hero2)+hero+new+hero2
            message.config(text=ok)
        elif 1200000<net_nettaxable<=1500000:
                    hero=400000*5/100
                    new=300000*10/100
                    hero4=200000*15/100
                    hero5=(net_nettaxable-1200000)*20/100

                    op=cess(hero+new+hero4+hero5)+hero+new+hero4+hero5
                    message.config(text=op)
        else :
                    hero=400000*5/100 
                    new=300000*10/100
                    hero4=200000*15/100
                    hero5=300000*20/100
                    hero6=(net_nettaxable-1500000)*30/100
                    b=hero+hero4+hero5+hero6+new
                    
                    #surcharge
                    
                    if 5000000<net_nettaxable<=10000000:
                        b=b*10/100
                        op=round(cess(hero+new+hero4+hero5+hero6+b)+hero+new+hero4+hero5+hero6+b,0)
                    elif 10000000<net_nettaxable<=20000000:
                        b=b*15/100
                        op=round(cess(hero+new+hero4+hero5+hero6+b)+hero+new+hero4+hero5+hero6+b,0)
                    elif 20000000<net_nettaxable<=50000000:
                        b=b*25/100
                        op=round(cess(hero+new+hero4+hero5+hero6+b)+hero+new+hero4+hero5+hero6+b,0)
                    elif 50000000<net_nettaxable:
                        b=b*37/100
                        op=round(cess(hero+new+hero4+hero5+hero6+b)+hero+new+hero4+hero5+hero6+b,0)
                    else:
                        b=b
                    op=round(cess(hero+new+hero4+hero5+hero6)+hero+new+hero4+hero5+hero6,0)

                    message.config(text=op)

root.geometry("600x600")
root.minsize(600,600)
root.maxsize(600,600)
root.title("Indigo taxcalc(new regime)")
root["bg"]="light green"

f= Frame(root, height=10, width=30)

f.pack(side=TOP, pady=30)
l = Label(f, text = "Income Tax Calculator", height=1, width=20, font="Aerial 30 bold ", background="light blue", pady=30)
l.pack()

f1= Frame(root, height=10, width=40, bg = "grey")
f1.pack(side=TOP, pady=30)

l1 = Label(f1, text= "Gross Income:", height=1, width=20, font="Aerial 20 bold")
l2 = Label(f1, text= "Deduction(if you have):", height=1, width= 20, font="Aerial 20 bold")
iv= IntVar()
e = Entry(f1, textvar=iv ,width=30)
iv1= IntVar()
e1 = Entry(f1, textvar=iv1, width=30)



l1.grid(row=0, column=0,padx=2,pady=3)
l2.grid(row=1, column=0, padx=2,pady=3)
e.grid(row=0, column=1, padx=2, pady=3)
e1.grid(row=1,column=1,padx=2,pady=3)

def clear():
    e.delete(0,END)
    e1.delete(0,END)
    message.config(text="")

f2 = Frame(root, background="light green")
f2.pack()
b = Button(f2,text="Calculate", height=2, width=10, background="white", font="aerial 10 bold", command=calculate )
b.pack(side=LEFT, padx=30)
b1 = Button(f2,text="Clear", height=2, width=10, background="white", font="aerial 10 bold", command=clear)
b1.pack()
m1 = Label(root,text="Your tax is :", height=2, width=40, font="99", bg="light green")
m1.pack()
message=Label(root,text="", height=2, width=40, font="99", bg="light green")
message.pack()
root.mainloop()