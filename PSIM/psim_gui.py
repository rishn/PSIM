from tkinter import *
from tkinter import ttk
import sys
import os
import random
import string
def win():
    r0=Tk()
    r0.title('PSIM')
    f=Frame(r0,bg='BLACK')
    f.pack(fill=BOTH,expand=1)
    c=Canvas(f,bg='BLACK')
    c.pack(side=LEFT,fill=BOTH,expand=1)
    s1=ttk.Scrollbar(f,orient=VERTICAL,command=c.yview)
    s1.pack(side=RIGHT,fill=Y)
    c.configure(yscrollcommand=s1.set)
    s2=ttk.Scrollbar(f,orient=HORIZONTAL,command=c.xview)
    s2.pack(side=BOTTOM,fill=X)
    c.configure(xscrollcommand=s1.set)
    c.bind('<Configure>',lambda e:c.configure(scrollregion=c.bbox('all')))
    def mw(event):
        c.yview_scroll(-1*int((event.delta/120)),'units')
    c.bind_all('<MouseWheel>',mw)
    r=Frame(c,bg='BLACK')
    c.create_window((0,0),window=r,anchor='s')
    return r,r0
def scroll(f):
    s1=Scrollbar(f,orient=VERTICAL)
    s1.pack(side=RIGHT,fill=Y)
    s2=Scrollbar(f,orient=HORIZONTAL)
    s2.pack(side=BOTTOM,fill=X)
    return s1,s2
def fr(r):
    f=Frame(r,bg='BLACK')
    f.pack()
    return f
def entry(f,s,i,c):
    Label(f,text=s,bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=i,column=0,sticky=W)
    e=Entry(f,textvariable=StringVar(),font=('Tw Cen MT',13)) if c=='' else Entry(f,textvariable=StringVar(),show=c,font=('Tw Cen MT',13))
    e.grid(row=i,column=1,sticky=W)
    return e
def button(f,l,se,px,rw):
    for i in l:
        Button(f,text=i[0],width=10,command=i[1],font=('Copperplate Gothic Light',10,'bold'),bg=i[2],fg='WHITE',activeforeground=i[2]).grid(row=rw,column=l.index(i),sticky=W) if rw!='' else Button(f,text=i[0],width=25,command=i[1],font=('Copperplate Gothic Light',10,'bold'),bg=i[2],fg='WHITE',activeforeground=i[2]).pack(side=se,padx=px) if se!=0 and px!=0 else Button(f,text=i[0],width=25,command=i[1],font=('Copperplate Gothic Light',10,'bold'),bg=i[2],fg='WHITE',activeforeground=i[2]).pack()
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
def check(b,c,r,r0):
    f3=fr(r)
    if b==c and b!='':
        write(b,r'Sensitive/1.dat')
        f4=fr(r)
        Button(f4,text='Exit And Restart Program',width=25,command=lambda:exitm(r,r0),bg='BLUE',fg='WHITE',activeforeground='BLUE',font=('Copperplate Gothic Light',10,'bold')).pack()
    else:
        Label(f3,text='Invalid key',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=1,sticky=W)
def generate1():
    r3,r0=win()
    f1,f2=fr(r3),fr(r3)
    e=entry(f1,'Passowrd length:',0,'')
    button(f2,[('Submit',lambda:generate2(e.get(),r3),'BLUE'),('Go Back',lambda:[r3.destroy(),r0.destroy()],'BLUE')],0,0,'')
def generate2(n,r):
    f3,f4=fr(r),fr(r)
    try:
        p=''.join([random.choice(string.digits+string.ascii_letters+string.punctuation) for i in range(int(n))])
        Label(f3,text=p,bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=1,sticky=W)
        Button(f4,text='Copy Text',width=10,bg='RED',fg='WHITE',activeforeground='RED',command=lambda:copy(p,r),font=('Copperplate Gothic Light',10,'bold')).grid(row=1,column=1,sticky=W)
    except TypeError as e:
        Label(f3,text='Invalid length',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=1,sticky=W)
def starter(f1,f2,f3,r,r0,key):
    global a
    a+=1
    Label(f3,text=f'{3-a} attempt(s) left',bg='BLACK',fg='WHITE',font=('Georgia',12)).pack()
    b=read()
    if e.get()==key:
        for i in [f1,f2,f3]:
            i.forget()
        f3,f4,f5=fr(r),fr(r),fr(r)
        for i in [("RJK'S",0),('PSIM',1)]:
            Label(f3,text=i[0],bg='BLACK',fg='WHITE',font=('Niagara Solid',40)).grid(row=i[1],column=2,sticky=W)
        s1,s2=scroll(f4)
        l=Listbox(f4,yscrollcommand=s1.set,xscrollcommand=s2.set,font=('Impact',12))
        for i in b:
            l.insert(END,i)
        l.pack(side=LEFT,fill=BOTH)
        s1.config(command=l.yview)
        s2.config(command=l.xview)
        button(f5,[('View',lambda:view1(l.get(ANCHOR),r1),'RED'),('Add',lambda:add1(l),'RED'),('Delete',lambda:delete1(l,l.get(ANCHOR)),'RED'),('Update',lambda:update1(l,l.get(ANCHOR)),'RED'),('Exit',lambda:exitm(r1,r0),'BLUE')],0,0,0)
    elif a==3:
        exitm(r,r0)
def view1(c,r):
    b=read()
    try:
        b[c],f4,f5,f6=b[c],fr(r),fr(r),fr(r)
        Label(f4,text=c,bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
        Label(f4,text='Select account',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
        s1,s2=scroll(f5)
        l=Listbox(f5,yscrollcommand=s1.set,xscrollcommand=s2.set,font=('Impact',12))
        for i in b[c]:
            l.insert(END,i)
        l.pack(side=LEFT,fill=BOTH)
        s1.config(command=l.yview)
        s2.config(command=l.xview)
        button(f6,[('View',lambda:view2(c,l.get(ANCHOR),r),'RED'),('Add',lambda:add2(l,c),'RED'),('Delete',lambda:delete2(l,c,l.get(ANCHOR)),'RED'),('Update',lambda:update2(l,c,l.get(ANCHOR)),'RED'),('Exit',lambda:exitm(r,r0),'BLUE')],0,0,0)
    except KeyError as e:
        print('',end='')
def view2(c,d,r):
    b=read()
    try:
        b[c][d],f7=b[c][d],fr(r)
        for i in [('Name:',0,0),('Username/No.:',0,1),('Password:',0,2),(d,1,0),(b[c][d][0],1,1),(b[c][d][1],1,2)]:
            Label(f7,text=i[0],bg='BLACK',fg='WHITE',borderwidth=3,relief='groove',font=('Georgia',12)).grid(row=i[1],column=i[2],sticky=W)
        button(f7,[('Copy Text',lambda:copy(d,r),'RED'),('Copy Text',lambda:copy(b[c][d][0],r),'RED'),('Copy Text',lambda:copy(b[c][d][1],r),'RED')],0,0,2)
    except KeyError as e:
        print('',end='')    
def add1(l):
    r2,r0=win()
    f1,f2=fr(r2),fr(r2)
    e=entry(f1,'New sub-group name:',0,'')
    button(f2,[('Submit',lambda:add3(l,e.get(),r2),'BLUE'),('Go Back',lambda:[r2.destroy(),r0.destroy()],'BLUE')],0,0,'')
def add2(l,c):
    r2,r0=win()
    f1,f2=fr(r2),fr(r2)
    d=[['New account name:',''],['Username:',''],['Password:','']]
    for i in range(len(d)):
        d[i][1]=entry(f1,d[i][0],i,'')
    button(f2,[('Genrate Secure Password',lambda:generate1(),'RED'),('Submit',lambda:add4(l,c,d[0][1].get(),d[1][1].get(),d[2][1].get(),r2),'BLUE'),('Go Back',lambda:[r2.destroy(),r0.destroy()],'BLUE')],0,0,'')
def add3(l,c,r):
    b=read()
    if c not in list(b.keys()):
        b[c]={}
        l.insert(END,c)
    else:
        f3=fr(r)
        Label(f1,text='Sub-group name already exists!',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    write(b,r'Sensitive/2.dat')
def add4(l,c,d,e,f,r):
    b=read()
    if d not in list(b[c].keys()):
        b[c][d]=[e,f]
        l.insert(END,d)
    else:
        f3=fr(r)
        Label(f3,text='Account name already exists!',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    write(b,r'Sensitive/2.dat')
def delete1(l,c):
    b=read()
    try:
        b[c]=b[c]
        r2,r0=win()
        f1,f2=fr(r2),fr(r2)
        Label(f1,text=f'Delete sub-group {c}?',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
        button(f2,[('Yes',lambda:[delete3(l,b,c),r2.destroy(),r0.destroy()],'RED'),('No',lambda:[r2.destroy(),r0.destroy()],'BLUE')],LEFT,10,'')
    except KeyError as e:
        print('',end='')
def delete2(l,c,d):
    b=read()
    try:
        b[c][d]=b[c][d]
        r2,r0=win()
        f1,f2=fr(r2),fr(r2)
        Label(f1,text=f'Delete account {d} from sub-group {c}?',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
        button(f2,[('Yes',lambda:[delete4(l,b,c,d),r2.destroy(),r0.destroy()],'RED'),('No',lambda:[r2.destroy(),r0.destroy()],'BLUE')],LEFT,10,'')
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
    b=read()
    try:
        b[c]=b[c]
        r2,r0=win()
        f1,f2=fr(r2),fr(r2)
        e=entry(f1,'New sub-group name:',0,'')
        button(f2,[('Submit',lambda:update3(l,b,c,e.get()),'BLUE'),('Go Back',lambda:[r2.destroy(),r0.destroy()],'BLUE')],0,0,'')
    except KeyError as e:
        print('',end='') 
def update2(l,c,d):
    b=read()
    try:
        b[c][d]=b[c][d]
        r2,r0=win()
        f1,f2=fr(r2),fr(r2)
        e=[['New account name:',''],['Username:',''],['Password:','']]
        for i in range(len(e)):
            e[i][1]=entry(f1,e[i][0],i,'')
        button(f2,[('Genrate Secure Password',lambda:generate1(),'RED'),('Submit',lambda:update4(l,b,c,d,e[0][1].get(),e[1][1].get(),e[2][1].get()),'BLUE'),('Go Back',lambda:[r2.destroy(),r0.destroy()],'BLUE')],0,0,'')
    except KeyError as e:
        print('',end='')
def update3(l,b,c,d):
    b[c]=b[d]
    if c!=d:
        l.insert(END,d)
    write(b,r'Sensitive/2.dat')
def update4(l,b,c,d,e,f,g):
    b[c][e]=[f,g]
    l.insert(END,e)
    l.delete(l.get(0,END).index(d))
    if d!=e:
        del b[c][d]
    write(b,r'Sensitive/2.dat')
def exitm(r,r0):
    r.destroy()
    r0.destroy()
    sys.exit()
if os.path.isdir('Sensitive')==False:
    os.mkdir('Sensitive')
with open(r'Sensitive/1.dat','ab+') as file1,open(r'Sensitive/2.dat','ab+') as file2:
    file1.seek(0,0)
    key=file1.read().decode('utf-8')
r1,r0=win()
if key=='':
    f1,f2=fr(r1),fr(r1)
    Label(f1,text='No clearance key saved',bg='BLACK',fg='WHITE',font=('Georgia',12)).grid(row=0,column=0,sticky=W)
    nkey,ckey=entry(f1,'New clearance key:',1,'*'),entry(f1,'New clearance key:',2,'*')
    Button(f2,text='Submit',width=25,command=lambda:check(nkey.get(),ckey.get(),r1,r0),bg='BLUE',fg='WHITE',activeforeground='BLUE',font=('Copperplate Gothic Light',10,'bold')).pack()
else:
    f1,f2,f3,a=fr(r1),fr(r1),fr(r1),0
    e=entry(f1,'Clearance key:',0,'*')
    Button(f2,text='Submit',width=25,command=lambda:starter(f1,f2,f3,r1,r0,key),bg='BLUE',fg='WHITE',activeforeground='BLUE',font=('Copperplate Gothic Light',10,'bold')).pack()
