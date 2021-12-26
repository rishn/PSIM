from tkinter import *
from tkinter import ttk
import sys
import os
import random
import string
def win(b):
    r=Tk() if b=='PSIM' else Toplevel()
    r.title(b)
    r.config(bg='#3f1148')
    r.wm_attributes('-transparentcolor','#3f1148')
    return r
def scroll(f,b):
    f.configure(bg='#3f1148')
    s1,s2=Scrollbar(f,bg='#3f1148',orient=VERTICAL),Scrollbar(f,bg='black',orient=HORIZONTAL)
    s1.pack(side=RIGHT,fill=Y)
    s2.pack(side=BOTTOM,fill=X)
    l=Listbox(f,yscrollcommand=s1.set,xscrollcommand=s2.set,bg='black',fg='#5fbdbf',font=('Impact',12),width=20,height=9)
    for i in b:
        l.insert(END,i)
    l.pack(side=LEFT,fill=BOTH)
    s1.config(command=l.yview)
    s2.config(command=l.xview)
    return l
def fr(r,b):
    f=Frame(r,bg='black') if b==0 else Frame(r,bg='#c28f98') if b==1 else Frame(r,bg='#3f1148')
    f.pack()
    return f
def entry(f,s,i,c,b):
    Label(f,text=s,bg='black',fg='white',font=('Georgia',12)).grid(row=i,column=0,sticky=W) if b==0 else Label(f,text=s,bg='#c28f98',fg='white',font=('Georgia',12)).grid(row=i,column=0,sticky=W)
    e=Entry(f,textvariable=StringVar(),font=('Tw Cen MT',13)) if c=='' else Entry(f,textvariable=StringVar(),show=c,font=('Tw Cen MT',13))
    e.grid(row=i,column=1,sticky=W)
    return e
def button(f,l,se,px,rw):
    for i in l:
        Button(f,text=i[0],width=10,command=i[1],font=('Copperplate Gothic Light',10,'bold'),bg=i[2],fg='white',activeforeground=i[2]).grid(row=rw,column=l.index(i),sticky=W) if rw!='' else Button(f,text=i[0],width=25,command=i[1],font=('Copperplate Gothic Light',10,'bold'),bg=i[2],fg='white',activeforeground=i[2]).pack(side=se,padx=px) if se!=0 and px!=0 else Button(f,text=i[0],width=25,command=i[1],font=('Copperplate Gothic Light',10,'bold'),bg=i[2],fg='white',activeforeground=i[2]).pack()
def read():
    with open(r'Sensitive/2.dat','rb') as file:
        try:
            b=eval(file.read().decode('utf-8'))
        except (EOFError,SyntaxError) as e:
            b={}
    return b
def write(b,f):
    with open(f,'wb') as file:
        file.write(str(b).encode('utf-8'))
def copy(c,r):
    r.clipboard_clear()
    r.clipboard_append(c)
    r.update()
def check(b,c,r):
    global f3
    f3=fr(r,0)
    if b==c and b!='':
        write(b,r'Sensitive/1.dat')
        f4=fr(r,0)
        Button(f4,text='Exit And Restart Program',width=25,command=lambda:exitm(r),bg='blue',fg='white',activeforeground='blue',font=('Copperplate Gothic Light',10,'bold')).pack()
    else:
        Label(f3,text='Invalid key',bg='black',fg='white',font=('Georgia',12)).grid(row=0,column=1,sticky=W)
def generate1():
    global img2
    global f3
    r3=win('Secure Password Generator')
    img2=PhotoImage(file='Banner.png')
    Label(r3,image=img2).place(x=0,y=0)
    f1,f2,f3=fr(r3,1),fr(r3,1),fr(r3,1)
    e=entry(f1,'Passowrd length:',0,'',1)
    button(f2,[('Submit',lambda:[f3.forget(),generate2(e.get(),r3)],'blue'),('Go Back',lambda:[r3.destroy()],'blue')],0,0,'')
def generate2(n,r):
    global f3
    f3=fr(r,1)
    try:
        p=[random.choice(string.digits+string.ascii_letters+string.punctuation) for i in range(int(n)-3)]
        for i in [(0,string.digits),(1,string.ascii_letters),(2,string.punctuation)]:
            p.insert(random.randint(0,int(n)-3+i[0]),random.choice(i[1]))
        p=''.join(p)
        Label(f3,text=p,bg='#c28f98',fg='white',font=('Georgia',12)).pack()
        Button(f3,text='Copy Text',width=10,bg='red',fg='white',activeforeground='red',command=lambda:copy(p,r),font=('Copperplate Gothic Light',10,'bold')).pack()
    except ValueError as e:
        Label(f3,text='Invalid length',bg='#c28f98',fg='white',font=('Georgia',12)).pack()
def starter(f1,f2,r,key):
    global a
    global f3
    global f4
    global f5
    global f6
    a+=1
    f3=fr(r,0)
    Label(f3,text=f'{3-a} attempt(s) left',bg='#3f1148',fg='#5fbdbf',font=('Georgia',12)).pack()
    b=read()
    if e.get()==key:
        c,f1,f2,f3,f4,f5,f6=[i.forget() for i in [f1,f2,f3]],fr(r,0),fr(r,2),fr(r,0),fr(r,0),fr(r,0),fr(r,0)
        for i in [("RJK'S",0,28,'Imprint MT Shadow'),('PSIM',1,30,'Imprint MT Shadow'),('Select sub-group',2,12,'Georgia')]:
            Label(f1,text=i[0],bg='#3f1148',fg='yellow',font=(i[3],i[2])).pack()
        l=scroll(f2,b)
        button(f3,[('View',lambda:[f4.forget(),f5.forget(),f6.forget(),view1(l.get(ANCHOR),r1)],'red'),('Add',lambda:add1(l),'red'),('Delete',lambda:delete1(l,l.get(ANCHOR)),'red'),('Update',lambda:update1(l,l.get(ANCHOR)),'red'),('Exit',lambda:exitm(r1),'blue')],0,0,0)
    elif a==3:
        exitm(r)
def view1(c,r):
    global f4
    global f5
    global f6
    b=read()
    try:
        b[c],f4,f5,f6=b[c],fr(r,0),fr(r,0),fr(r,0)
        for i in (c,'Select account'):
            Label(f4,text=i,bg='#3f1148',fg='yellow',font=('Georgia',12)).pack()
        l=scroll(f5,b[c])
        button(f6,[('View',lambda:view2(c,l.get(ANCHOR)),'red'),('Add',lambda:add2(l,c),'red'),('Delete',lambda:delete2(l,c,l.get(ANCHOR)),'red'),('Update',lambda:update2(l,c,l.get(ANCHOR)),'red')],0,0,0)
    except KeyError as e:
        print('',end='')
def view2(c,d):
    global img3
    b=read()
    try:
        b[c][d],r2=b[c][d],win(f'{d} Account Info')
        img3=PhotoImage(file='Banner.png')
        Label(r2,image=img3).place(x=0,y=0)
        f1,f2=fr(r2,1),fr(r2,1)
        for i in [('Name:',0,0),('Username/No.:',0,1),('Password:',0,2),(d,1,0),(b[c][d][0],1,1),(b[c][d][1],1,2)]:
            Label(f1,text=i[0],bg='#c28f98',fg='white',borderwidth=3,relief='groove',font=('Georgia',12)).grid(row=i[1],column=i[2],sticky=W)
        button(f1,[('Copy Text',lambda:copy(d,r2),'red'),('Copy Text',lambda:copy(b[c][d][0],r2),'red'),('Copy Text',lambda:copy(b[c][d][1],r2),'red')],0,0,2)
        Button(f2,text='Go Back',width=25,bg='blue',fg='white',activeforeground='blue',command=r2.destroy,font=('Copperplate Gothic Light',10,'bold')).pack()
    except KeyError as e:
        print('',end='')    
def add1(l):
    global img4
    global fr3
    r2=win('Add Sub-group')
    img4=PhotoImage(file='Banner.png')
    Label(r2,image=img4).place(x=0,y=0)
    f1,f2,fr3=fr(r2,1),fr(r2,1),fr(r2,1)
    e=entry(f1,'New sub-group name:',0,'',1)
    button(f2,[('Submit',lambda:[fr3.forget(),add3(l,e.get(),r2)],'blue'),('Go Back',lambda:[r2.destroy()],'blue')],0,0,'')
def add2(l,c):
    global img5
    global fn3
    r2=win('Add Account')
    img5=PhotoImage(file='Banner.png')
    Label(r2,image=img5).place(x=0,y=0)
    f1,f2,fn3=fr(r2,1),fr(r2,1),fr(r2,1)
    d=[['New account name:',''],['Username:',''],['Password:','']]
    for i in range(len(d)):
        d[i][1]=entry(f1,d[i][0],i,'',1)
    button(f2,[('Genrate Secure Password',lambda:generate1(),'red'),('Submit',lambda:[fn3.forget(),add4(l,c,d[0][1].get(),d[1][1].get(),d[2][1].get(),r2)],'blue'),('Go Back',lambda:[r2.destroy()],'blue')],0,0,'')
def add3(l,c,r):
    global fr3
    b=read()
    if c!='' and c not in list(b.keys()):
        b[c]={}
        l.insert(END,c)
    else:
        fr3=fr(r,1)
        Label(fr3,text='Invalid sub-group',bg='#c28f98',fg='white',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    write(b,r'Sensitive/2.dat')
def add4(l,c,d,e,f,r):
    global fn3
    b=read()
    if d!='' and d not in list(b[c].keys()):
        b[c][d]=[e,f]
        l.insert(END,d)
    else:
        fn3=fr(r,1)
        Label(fn3,text='Invalid account',bg='#c28f98',fg='white',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    write(b,r'Sensitive/2.dat')
def delete1(l,c):
    global img6
    b=read()
    try:
        b[c],r2=b[c],win(f'Delete {c}')
        img6=PhotoImage(file='Banner.png')
        Label(r2,image=img6).place(x=0,y=0)
        f1,f2=fr(r2,1),fr(r2,1)
        Label(f1,text=f'Delete sub-group {c}?',bg='#c28f98',fg='white',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
        button(f2,[('Yes',lambda:[delete3(l,b,c),r2.destroy()],'red'),('No',lambda:[r2.destroy()],'blue')],LEFT,10,'')
    except KeyError as e:
        print('',end='')
def delete2(l,c,d):
    global img7
    b=read()
    try:
        b[c][d],r2=b[c][d],win(f'Delete {d}')
        img7=PhotoImage(file='Banner.png')
        Label(r2,image=img7).place(x=0,y=0)
        f1,f2=fr(r2,1),fr(r2,1)
        Label(f1,text=f'Delete account {d} from sub-group {c}?',bg='#c28f98',fg='white',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
        button(f2,[('Yes',lambda:[delete4(l,b,c,d),r2.destroy()],'red'),('No',lambda:[r2.destroy()],'blue')],LEFT,10,'')
    except KeyError as e:
        print('',end='') 
def delete3(l,b,c):
    del b[c]
    l.delete(l.get(0,END).index(c))
    write(b,r'Sensitive/2.dat') 
def delete4(l,b,c,d):
    del b[c][d]
    l.delete(l.get(0,END).index(d))
    write(b,r'Sensitive/2.dat')   
def update1(l,c):
    global img8
    global ft3
    b=read()
    try:
        b[c],r2=b[c],win(f'Update {c}')
        img8=PhotoImage(file='Banner.png')
        Label(r2,image=img8).place(x=0,y=0)
        f1,f2,ft3=fr(r2,1),fr(r2,1),fr(r2,1)
        e=entry(f1,'New sub-group name:',0,'',1)
        button(f2,[('Submit',lambda:[ft3.forget(),update3(l,b,c,e.get(),r2)],'blue'),('Go Back',r2.destroy,'blue')],0,0,'')
    except KeyError as e:
        print('',end='') 
def update2(l,c,d):
    global img9
    global fl3
    b=read()
    try:
        b[c][d],r2=b[c][d],win(f'Update {d}')
        img9=PhotoImage(file='Banner.png')
        Label(r2,image=img9).place(x=0,y=0)
        f1,f2,fl3=fr(r2,1),fr(r2,1),fr(r2,1)
        e=[['New account name:',''],['Username:',''],['Password:','']]
        for i in range(len(e)):
            e[i][1]=entry(f1,e[i][0],i,'',1)
        button(f2,[('Genrate Secure Password',lambda:generate1(),'red'),('Submit',lambda:[fl3.forget(),update4(l,b,c,d,e[0][1].get(),e[1][1].get(),e[2][1].get(),r2)],'blue'),('Go Back',lambda:r2.destroy(),'blue')],0,0,'')
    except KeyError as e:
        print('',end='')
def update3(l,b,c,d,r):
    global ft3
    if d!='' and d not in list(b.keys()):
        b[d]=b[c]
        l.insert(END,d)
        l.delete(l.get(0,END).index(c))
        del b[c]
    else:
        ft3=fr(r,1)
        Label(ft3,text='Invalid sub-group',bg='#c28f98',fg='white',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    write(b,r'Sensitive/2.dat')
def update4(l,b,c,d,e,f,g,r):
    global fl3
    if e!='' and (e==d or e not in list(b.keys())):
        b[c][e]=[f,g]
    else:
        fl3=fr(r,1)
        Label(fl3,text='Invalid account',bg='#c28f98',fg='white',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    if e!=d:
        l.insert(END,e)
        l.delete(l.get(0,END).index(d))
        del b[c][d]
    write(b,r'Sensitive/2.dat')
def exitm(r):
    r.destroy()
    sys.exit()
if os.path.isdir('Sensitive')==False:
    os.mkdir('Sensitive')
with open(r'Sensitive/1.dat','ab+') as file1,open(r'Sensitive/2.dat','ab+') as file2:
    file1.seek(0,0)
    key,r1=file1.read().decode('utf-8'),win('PSIM')
img1=PhotoImage(file='Palm Print.png')
Label(r1,image=img1).place(x=0,y=0)
f1,f2,f3=fr(r1,2),fr(r1,0),fr(r1,0)
if key=='':
    Label(f1,text='No clearance key saved',bg='#3f1148',fg='#5fbdbf',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    nkey,ckey=entry(f1,'New clearance key:',1,'*',0),entry(f1,'New clearance key:',2,'*',0)
    Button(f2,text='Submit',width=25,command=lambda:[f3.forget(),check(nkey.get(),ckey.get(),r1)],bg='blue',fg='white',activeforeground='blue',font=('Copperplate Gothic Light',10,'bold')).pack()
else:
    a,e=0,entry(f1,'Clearance key:',0,'*',0)
    Button(f2,text='Submit',width=25,command=lambda:[f3.forget(),starter(f1,f2,r1,key)],bg='blue',fg='white',activeforeground='blue',font=('Copperplate Gothic Light',10,'bold')).pack()
    Label(f3,text='3 attempts left',bg='#3f1148',fg='#5fbdbf',font=('Georgia',12)).pack()
