from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

j=[]
r = requests.get('https://api.exchangerate-api.com/v4/latest/INR').json()

def all_keys(dict_obj):
    
  
    for key , value in dict_obj.items():
        yield key
        if isinstance(value, dict):
            for k in all_keys(value):
                j.append(k)
                
for key in all_keys(r):
    pass

root=Tk()
root.title("Currency Convertor")
def prnt(event):
    req = requests.get(f'https://api.exchangerate-api.com/v4/latest/{check.get()}').json()
    try:
        messagebox.showinfo("output",req["rates"][check1.get()]*float(amount.get()))
    except ValueError:
        messagebox.showerror("Error","Enter correct value")
root.geometry("480x280")
root.minsize(480,280)
root.maxsize(480,280)
root.config(background="purple")

r=Label(root,text="Currency Convertor",font="Arial 25 bold",bg="purple")
r.place(relx=.5,rely=.1,anchor="center")

entry=Entry(root,)

cfrom=Label(root,text="From",bg="purple",font="Arial 15 bold")
cfrom.place(relx=.2,rely=.3)

cto=Label(root,text="To",bg="purple",font="Arial 15 bold")
cto.place(relx=.7,rely=.3)
amt=StringVar()
amount=Entry(root,textvariable=amt)
amount.insert(END,"Enter amount")
amount.place(relx=.37,rely=.5)

n=StringVar()
k=StringVar()
check=ttk.Combobox(root,textvariable=n)

check["values"]=(j)
check.place(relx=.1,rely=.4)
check.bind('<<ComboboxSelected>>')

check1=ttk.Combobox(root,textvariable=k)
check1["values"]=(j)
check1.place(relx=.6,rely=.4)
check1.bind("<<ComboboxSelected>>")

btn=Button(root,text="Convert",relief="sunken")
btn.place(relx=.45,rely=.7)
btn.bind("<Button-1>",prnt)

root.mainloop()
