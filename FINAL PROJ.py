from tkinter import *
import re
import tkinter.ttk as ttk
from tkinter import messagebox
root = Tk()
root.title('Final Project')
root.geometry ('1200x600')

f1z=0
f2z=0
f3z=0
def addMenu(uk):
    global f1z,f2z,f3z

    if uk == '1':        
        if f1z==0:
            f2.place(x=205,y=230)
            f3.place(x=5000, y=5000)
            f4.place(x=2000,y=2000)
            f1z = 1
            f2z = 0
            f3z= 0
        else:
            f2.place(x=20115,y=23011)
            f1z = 0

    elif uk == '2':        
        if f2z==0:
            f3.place(x=205,y=230)
            f2.place(x=5000, y=5000)
            f4.place(x=2000,y=2000)
            f2z = 1
            f1z = 0
            f3z=0
        else:
            f3.place(x=20115,y=23011)
            f2z = 0

    elif uk=='3':
         if f3z==0:
            f4.place(x=205,y=230)
            f3.place(x=5000, y=5000)
            f2.place(x=2000,y=2000)
            f3z = 1
            f1z = 0
            f2z = 0
         else:
            f4.place(x=20115,y=23011)
            f3z = 0
    
Tops = Frame(root, width=1000, height= 65, bd= 12, relief= 'ridge',bg='peachpuff2')
Tops.pack(side=TOP)
lblTitle =Label(Tops, font=('helvetica',24, 'bold'), text='\t\t\tPic-A-Yum\t\t\t\t',bg='ivory2')
lblTitle.grid(row=0, column=0)


f1= Frame(root,bd=5, bg='slategray1',relief='raise')
f1.place(x=100,y=70)

f2=Frame(root, bd=5, bg='darkseagreen1',relief='raise')
f2.place(x=28805,y=23870)
f3=Frame(root,bd=5, bg='darkseagreen2',relief='raise')
f3.place(x=20588,y=23770)
f4=Frame(root,bd=5, bg='darkseagreen3',relief='raise')
f4.place(x=26605,y=28830)

b1=Button(f1, width=20,height=8, text='DRINKS',anchor='center',bd = 3, command = lambda: addMenu('1'), bg='lightcyan2')
b1.pack(side=LEFT)
b2=Button(f1, width=20,height=8, text='MEAL',anchor='center',bd = 3, command = lambda: addMenu('2'),bg='lightcyan3')
b2.pack(side=LEFT)
b3=Button(f1, width=20,height=8, text='DESSERT',anchor='center',bd = 3, command = lambda: addMenu('3'),bg='lightblue3')
b3.pack(side=RIGHT)

d1=Button(f2, width=15,height=5, text='DRINKING WATER \nP15.00',anchor='center',bd = 3, bg='lightcyan2', command = lambda: getOrder(sell_18))
d1.grid(row=0,column=0)
d2=Button(f2, width=15,height=5, text='LEMONADE \nP15.00',anchor='center',bd = 3,bg='lightcyan2',command = lambda: getOrder(sell_17))
d2.grid(row=0,column=1)
d3=Button(f2, width=15,height=5, text='BUKO JUICE \nP20.00',anchor='center',bd = 3,bg='lightcyan2',command = lambda: getOrder(sell_16))
d3.grid(row=1,column=0)
d4=Button(f2, width=15,height=5, text='COKE \nP12.00',anchor='center',bd = 3,bg='lightcyan2',command = lambda: getOrder(sell_15))
d4.grid(row=2,column=0)
d5=Button(f2, width=15,height=5, text='ICED TEA \nP15.00',anchor='center',bd = 3,bg='lightcyan2',command = lambda: getOrder(sell_14))
d5.grid(row=1,column=1)
d6=Button(f2, width=15,height=5, text='SPRITE \nP12.00',anchor='center',bd = 3,bg='lightcyan2',command = lambda: getOrder(sell_13))
d6.grid(row=2,column=1)

m1=Button(f3, width=15,height=5, text='TAPSILOG \nP55.00',anchor='center',bd = 3,bg='lightcyan3',command = lambda: getOrder(sell_12))
m1.grid(row=0,column=0)
m2=Button(f3, width=15,height=5, text='BACONSILOG \nP55.00',anchor='center',bd = 3,bg='lightcyan3',command = lambda: getOrder(sell_11))
m2.grid(row=0,column=1)
m3=Button(f3, width=15,height=5, text='PORKSILOG \nP55.00',anchor='center',bd = 3,bg='lightcyan3',command = lambda: getOrder(sell_10))
m3.grid(row=1,column=0)
m4=Button(f3, width=15,height=5, text='TOSILOG \nP55.00',anchor='center',bd = 3,bg='lightcyan3',command = lambda: getOrder(sell_9))
m4.grid(row=1,column=1)
m5=Button(f3, width=15,height=5, text='SISILOG \nP55.00',anchor='center',bd = 3,bg='lightcyan3',command = lambda: getOrder(sell_8))
m5.grid(row=2,column=0)
m6=Button(f3, width=15,height=5, text='CORNEDSILOG \nP55.00',anchor='center',bd = 3,bg='lightcyan3',command = lambda: getOrder(sell_7))
m6.grid(row=2,column=1)

s1=Button(f4, width=15,height=5, text='MANGO FLOAT \nP20.00',anchor='center',bd = 3,bg='lightblue3',command = lambda: getOrder(sell_6))
s1.grid(row=0,column=0)
s2=Button(f4, width=15,height=5, text='CHOCOLATE CAKE \nP20.00',anchor='center',bd = 3,bg='lightblue3',command = lambda: getOrder(sell_5))
s2.grid(row=0,column=1)
s3=Button(f4, width=15,height=5, text='LECHE FLAN \nP25.00',anchor='center',bd = 3,bg='lightblue3',command = lambda: getOrder(sell_4))
s3.grid(row=1,column=0)
s4=Button(f4, width=15,height=5, text='SUNDAE \n(CHOCOLATE \nWITH STRAWBERRY) \nP25.00',anchor='center',bd = 3,bg='lightblue3',command = lambda: getOrder(sell_3))
s4.grid(row=1,column=1)
s5=Button(f4, width=15,height=5, text='FRUIT SALAD \nP20.00',anchor='center',bd = 3,bg='lightblue3',command = lambda: getOrder(sell_2))
s5.grid(row=2,column=0)
s6=Button(f4, width=15,height=5, text='PALITAW \nP20.00',anchor='center',bd = 3,bg='lightblue3',command = lambda: getOrder(sell_1))
s6.grid(row=2,column=1)

def getOrder(baligya):
    food.delete(*food.get_children())
    
    global all_sold
    ex = 0

    for items in all_sold:
        if items[0] == baligya[0]:
            items[1] = int(items[1]) + 1
            items[3]= int(items[1])*int(items[2])
            ex = 1

    if ex == 0:
        all_sold.append(baligya)

    for item in all_sold:
        
        food.insert('','end', value = item)
    global gtotal
    gtotal=0
    for total in all_sold:
        gtotal=gtotal + int(total[3])

    gnd['text']=gtotal

def payment():
    global gtotal
    if int(amount.get())<gtotal:
        messagebox.showinfo('Payment Check', 'Your payment is not enough!')
    else:
        change=int(amount.get())-gtotal
        chng['text']=change
    
def reset():
    global all_sold
    amount.delete(0,END)
    gnd['text']= 0.00
    chng['text']=0.00
    food.delete(*food.get_children())
    all_sold.clear()
     
grand=Label(root, text = 'Grand Total:', font=('Arial',12,'bold'))
grand.place(x=900, y=320)

gnd=Label(root, text = '0.00', font=('Arial',12,'bold'))
gnd.place(x=1005, y=320)

sukli=Label(root, text = 'Change:', font=('Arial',14,'bold'))
sukli.place(x=900, y=350)

chng=Label(root, text = '0.00', font=('Arial',14,'bold'))
chng.place(x=1005, y=350)

out=Button(root, text = 'Exit',width = '10',command = root.destroy)
out.place(x=1000, y=550)

rst=Button(root, text = 'New Customer',width = '15',command= lambda:reset())
rst.place(x=890, y=550)

amount = Entry(root, font = ('Verdana', 15,'bold'),width = 15)
amount.place(x = 780, y = 500)
pay_btn =Button(root, text = 'Pay', command= lambda:payment())
pay_btn.place(x = 1000, y = 500)

sell_1 = ['PALITAW','1','20','20']
sell_2 = ['FRUIT SALAD','1','20','20']
sell_3 = ['SUNDAE','1','25','25']
sell_4 = ['LECHE FLAN','1','25','25']
sell_5 = ['CHOCOLATE CAKE','1','20','20']
sell_6 = ['MANGO FLOAT','1','20','20']

sell_7 = ['CORNEDSILOG','1','55','55']
sell_8 = ['SISILOG','1','55','55']
sell_9 = ['TOSILOG','1','55','55']
sell_10 = ['PORKSILOG','1','55','55']
sell_11 = ['BACONSILOG','1','55','55']
sell_12 = ['TAPSILOG','1','55','55']

sell_13 = ['SPRITE','1','12','12']
sell_14 = ['ICED TEA','1','15','15']
sell_15 = ['COKE','1','12','12']
sell_16 = ['BUKO JUICE','1','20','20']
sell_17 = ['LEMONADE','1','15','15']
sell_18 = ['DRINKING WATER','1','15','15']

all_sold=[]

my_head = ['ORDER','QTY','PRICE','TOTAL']

food = ttk.Treeview(root, columns = my_head, show = 'headings')
food.place(x = 620, y = 90)

for h in my_head:
    food.heading(h, text = h.title())
    food.column(h, anchor = CENTER, width= 130)


mainloop()
