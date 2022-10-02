import pandas as pd
from tkinter import *
import webbrowser
from PIL import ImageTk, Image
import data_scrapi

def start():
    dat=data_scrapi.start(item.get())
    print(dat)
    root1.destroy()
    ini(dat)

def shorten(title):
    max_length=35
    title_split = title.split()
    out = ""
    if len(title_split[0]) <= max_length:
        out += title_split[0]
    for word in title_split[1:]:
        if len(word)+len(out)+1 <= max_length:
            out += ' '+word
        else:
            break
    return out[0:]


def ini(dat):
    data = dat
    link=data['Link To Site']
    price=data['Price']
    name=data['Product Info']
    root=Tk()
    root.geometry("1140x480")
    root.config(bg="white")
    frame1 = Frame(root, highlightbackground="grey",highlightthickness=2,padx=60,pady=40)
    frame1.place(x=60,y=80)
    frame2 = Frame(root, highlightbackground="grey",highlightthickness=2,padx=60,pady=40)
    frame2.place(x=610,y=80)      
    img1 = ImageTk.PhotoImage(Image.open("download (1).png"))
    img2 = ImageTk.PhotoImage(Image.open("Flipkart-logo (1).png"))
    label1 = Label(root, image = img1)
    label2 = Label(root, image = img2)
    label1.place(x=220,y=25)
    label2.place(x=800,y=25)
    Label(frame1,text="Product Name",font='Helvetica 10 bold').grid(row=0,column=0)
    Label(frame1,text="Price",font='Helvetica 10 bold').grid(row=0,column=1)
    Label(frame1,text="Link To Site",font='Helvetica 10 bold').grid(row=0,column=2)
    Label(frame2,text="Product Name",font='Helvetica 10 bold').grid(row=0,column=0)
    Label(frame2,text="Price",font='Helvetica 10 bold').grid(row=0,column=1)
    Label(frame2,text="Link To Site",font='Helvetica 10 bold').grid(row=0,column=2)

    def callback(url):
        webbrowser.open_new_tab(url)

    for i in range(10):
        if(i<5):
            Label(frame1,text="Rs "+price[i]).grid(row=i+1,column=1,padx=10)
            Label(frame1,text=shorten(name[i])).grid(row=i+1,column=0)
        else:
            Label(frame2,text="Rs "+price[i]).grid(row=i-4,column=1,padx=10)
            Label(frame2,text=shorten(name[i])).grid(row=i-4,column=0)
    # 0
    link0= Label(frame1, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link0.grid(row=1,column=2)
    link0.bind("<Button-1>", lambda e:callback(link[0]))
    # 1
    link1= Label(frame1, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=2,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[1]))
    # 2
    link1= Label(frame1, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=3,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[2]))
    # 3
    link1= Label(frame1, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=4,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[3]))
    # 4
    link1= Label(frame1, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=5,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[4]))
    # 5
    link1= Label(frame2, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=1,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[5]))
    # 6
    link1= Label(frame2, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=2,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[6]))
    # 7
    link1= Label(frame2, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=3,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[7]))
    # 8
    link1= Label(frame2, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=4,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[8]))
    # 9
    link1= Label(frame2, text="link",font=('Helvetica 15 underline'), fg="blue", cursor="hand2")
    link1.grid(row=5,column=2)
    link1.bind("<Button-1>", lambda e:callback(link[9]))

    root.mainloop()

root1=Tk()
root1.geometry("350x350")

Label(root1,text="").grid(row=0,column=0)
Label(root1,text="").grid(row=1,column=0)
Label(root1,text="").grid(row=2,column=0)
Label(root1,text="").grid(row=3,column=0)
Label(root1,text="Enter the product",font=("",12)).grid(row=4,column=0,pady=10,columnspan=3)

item=Entry(root1,width=25,font=("Bahnschrift SemiLight",13))
item.grid(row=5,column=0,columnspan=3,padx=60)
bt=Button(root1,text="Search",command=start,padx=15,pady=10).grid(row=6,column=0,columnspan=5,pady=10,padx=60)
Label(root1,text =" I agree to the Terms & Conditions ",fg='grey').grid(row=7,column=0,pady=90,padx=30,columnspan=20)
root1.mainloop()