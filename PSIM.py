from getpass import getpass
import sys
from tabulate import tabulate
import string
import random
import os
import time
def clearance():
    with open(r"Sensitive\key.dat","ab+") as file:
        file.seek(0,0)
        k=file.read().decode("utf-8")
    if len(k)==0:
        while True:
            nk=getpass(prompt="New clearance key:".center(172))
            print("\n"+("*"*len(nk)).center(172))
            c=getpass(prompt="Confirm new clearance key:".center(172))
            print("\n"+("*"*len(c)).center(172))
            a=1 if nk not in ["",k] and c==nk else print("Invalid key".center(172))
            if a==1:
                with open(r"Sensitive\key.dat","wb") as file:
                    file.write(nk.encode("utf-8"))
                    print("Saving key... Re-boot program to access operational features...".center(172),flush=True)
                    time.sleep(2)
                    break
    else:
        for i in range(3):
            ui=getpass(prompt="Clearance key:".center(172))
            print("\n"+("*"*len(ui)).center(172))
            a=1 if ui==k else print("Invalid key".center(172))
            if a==1:
                return "Clear"
        else:
            print("Authorization failed... Access denied...".center(172),flush=True)
            time.sleep(2)
def search(a,c):
    print("\n"+tabulate([[i+1,list(a.keys())[i]] for i in range(len(a.keys()))],["Sl. no.",f"{c}"],tablefmt="grid"))
    if a=={}:
        return {}
    while True:
        try:
            d=int(input(f"\n{c} serial no. : "))
            if d>0:
                f=list(a.keys())[d-1]
                b=a[f]
                break
            else:
                print("Invalid")
        except (IndexError,ValueError) as e:
            print(f"Invalid {c}")
    return b,f
def erase(a,b,c,d):
    if a!={}:
        print()
        while True:
            reply=input(f"Delete {c}? ").lower()
            for i in a.items():
                b=i[0] if b==i[1] else b
            if reply in yes:
                del a[b]
            if reply in yes or reply in no:
                break
            else:
                print("Invalid")
    else:
        print(d)
def save(d):
    u=input("Username/e-mail/head/id: ")
    while True:
        reply,a,b=input("Self-generate secure password? ").lower(),0,0
        if reply in yes:
            while True:
                try:
                    p=''
                    for i in range(int(input("Length of password: "))):
                        p+=(random.choice(string.digits+string.ascii_letters+string.punctuation))
                    print(p)
                    while True:
                        reply1=input("Are you satisfied with generated password? ").lower()
                        if reply1 in yes:
                            break
                        elif reply1 in no:
                            a=1
                            break
                        else:
                            print("Invalid")
                    break
                except ValueError as e:
                    print("Invalid")
            if a==0:
                break
        elif reply in no:
            p=input("Password/no.: ")
            break
        else:
            print("Invalid")
    d[input("Name/description of account/id/no.: ")]=[u,p]
    return d
def view(a):
    print("\nDisplaying fields...\n")
    b,e=search(a,"Sub-group")
    if a!={}:
        d,e=search(b,"Account/ID/No.")
        if b!={}:
            print("\n"+tabulate([[e]+list(d)],["Name/Description","Username/E-Mail/Head/ID","Password/No."],tablefmt="rst"))
            return b,d
def add(a):
    print("\nAdding fields...\n")
    while True:
        reply=input("Add sub-groups? ").lower()
        b=1 if reply in yes else 2 if reply in no else print("Invalid")
        if b==2:
            break
        elif b==1:
            a[input("Name of sub-group: ")]={}
            while True:
                reply=input("Add more sub-groups? ").lower()
                c=1 if reply in yes else 2 if reply in no else print("Invalid")
                if reply in yes:
                    a[input("Name of sub-group: ")]={}
                elif reply in no:
                    break
            if c==2:
                break
    while True:
        reply=input("Add account/id/no.(s) to a sub-group? ").lower()
        c=1 if reply in yes else 2 if reply in no else print("Invalid")
        if c==2:
            break
        elif c==1:
            d,f=search(a,"Sub-group")
            d=save(d)
            while True:
                reply=input("Add more account/id/no.(s)? ").lower()
                e=1 if reply in yes else 2 if reply in no else print("Invalid")
                if reply in yes:
                    d=save(d)    
                elif reply in no:
                    break
            if e==2:
                break
    with open(r"Sensitive\persinfo.dat","wb") as file:
        file.write(str(a).encode("utf-8"))
def remove(a):
    print("\nRemoving fields...\n")
    d=1
    while True:
        reply=input("Remove sub-groups? ").lower()
        b=1 if reply in yes else 2 if reply in no else print("Invalid")
        if b==2:
            break
        elif b==1:
            d=0
            b,f=search(a,"Sub-group")
            erase(a,b,"sub-group","No sub-groups")
            break
    if d==1:
        while True:
            reply=input("Remove account/id/no.(s) in a sub-group? ").lower()
            b=1 if reply in yes else 2 if reply in no else print("Invalid")
            if b==2:
                break
            elif b==1:
                b,c=view(a)
                erase(b,c,"account/id/no.","No account/id/no.(s) in sub-group")
                break
    with open(r"Sensitive\persinfo.dat","wb") as file:
        file.write(str(a).encode("utf-8"))
def update(a):
    while True:
        reply=input("Update sub-group names? ").lower()
        b=1 if reply in yes else 2 if reply in no else print("Invalid")
        if b==2:
            break
        elif b==1:
            b,f=search(a,"Sub-group")
            a[input("New name of subgroup: ")],d=b,len(a)
            if len(a)>d:
                del a[list(a.keys())[list(a.values()).index(b)]]
            break
    while True:
            reply=input("Update account/id/no. details in a sub-group? ").lower()
            b=1 if reply in yes else 2 if reply in no else print("Invalid")
            if b==2:
                break
            elif b==1:
                b,c=view(a)
                e=len(b)
                print("\nProvide new acccount/id/no. details below...\n")
                save(b)
                if len(b)>e:
                    del a[list(a.keys())[list(a.values()).index(b)]][list(b.keys())[list(b.values()).index(c)]]
                break
    with open(r"Sensitive\persinfo.dat","wb") as file:
        file.write(str(a).encode("utf-8"))
def quitgame():
    while True:
        reply=input("Quit? (Yes/No): ").lower()
        b=1 if reply in yes else 2 if reply in no else print("Invalid")
        if b==1:
            print("Have a good day BOSS".center(172),flush=True)
            time.sleep(2)
            sys.exit()
        elif b==2:
            return
if os.path.isdir("Sensitive")==False:
    os.mkdir("Sensitive")
print("+"*172+"("*60+">"*26+"<"*26+")"*60+"$"*172+"="*172+"RJK'S".center(172)+"P.S.I.M".center(172)+"="*172+"$"*172+"("*60+">"*26+"<"*26+")"*60+"+"*172)
yes,no=['yes','yeah','y'],['n','no','nah']
if clearance()=="Clear":
    print("Welcome BOSS".center(172))
    time.sleep(2)
    while True:
        with open(r"Sensitive\persinfo.dat","ab+") as file:
            file.seek(0,0)
            try:
                a=eval(file.read().decode("utf-8"))
            except SyntaxError as e:
                a={}
        print("\n"+"+"*172+":"*172+"MAIN MENU".center(172)+":"*172)
        reply=input(f"1. View{' '*20}2. Add{' '*20}3. Remove{' '*20}4. Update{' '*20}5. Exit".center(172)+"What would you like to do sir? ")
        print("\n"+":"*172+"+"*172)
        view(a) if reply=='1' else add(a) if reply=='2' else remove(a) if reply=='3' else update(a) if reply=='4' else quitgame() if reply=='5' else print("Invalid")
