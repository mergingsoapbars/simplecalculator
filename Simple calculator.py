#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox
import math
import tkinter.font as tkfont


# In[2]:


root = Tk()


# In[3]:


app_wdth = 600
app_hght = 550

scrn_wdth = root.winfo_screenwidth()
scrn_hght = root.winfo_screenheight()

x = (scrn_wdth / 2) - (app_wdth / 2)
y = (scrn_hght / 2) - (app_hght / 2)


# In[4]:


root.title("Simple calculator")
root.geometry(f"{app_wdth}x{app_hght}+{int(x)}+{int(y)}")
root.configure(bg='#86BEAF')
root.iconbitmap("icon.ico")


# In[5]:


helv = tkfont.Font(family="Helvetica", size=10)


# In[6]:


e = Entry(root, width=50, borderwidth=3, bd=5, justify="right")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=15)


# In[7]:


e_1 = Entry(root, bg="#cfcfcf")
e_1.grid(row=8, column=1, pady=10, ipadx=15, sticky="") 


# In[8]:


def button_click(numeral):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(numeral))


# In[9]:


def button_clear():
    e.delete(0, END)
    e_1.delete(0, END)


# In[10]:


def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)


# In[11]:


def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)


# In[12]:


def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)


# In[13]:


def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)


# In[14]:


def button_power():
    first_num = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_num)
    e.delete(0, END)


# In[15]:


def button_percent():
    first_num = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_num)
    e.delete(0, END)


# In[16]:


def button_equals():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_num))
        e_1.insert(0, str(f_num) + "+" + str(second_num) + "=" + str(f_num + int(second_num)))
    if math == "multiplication":
        e.insert(0, f_num * int(second_num))
        e_1.insert(0, str(f_num) + "*" + str(second_num) + "=" + str(f_num * int(second_num)))
    if math == "division":
        e.insert(0, f_num / int(second_num))
        e_1.insert(0, str(f_num) + "/" + str(second_num) + "=" + str(f_num / int(second_num)))
    if math == "subtraction":
        e.insert(0, f_num - int(second_num))
        e_1.insert(0, str(f_num) + "−" + str(second_num) + "=" + str(f_num - int(second_num)))
    if math == "power":
        e.insert(0, f_num ** int(second_num))
        e_1.insert(0, str(f_num) + "**" + str(second_num) + "=" + str(f_num ** int(second_num)))
    if math == "percentage":
        e.insert(0, (f_num / int(second_num) * 100))
        e_1.insert(0, str(f_num) + " is " + str((f_num / int(second_num)) * 100) + "% of " + str(second_num))


# In[17]:


button1 = Button(root, text="1", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(1))
button2 = Button(root, text="2", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(2))
button3 = Button(root, text="3", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(3))
button4 = Button(root, text="4", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(4))
button5 = Button(root, text="5", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(5))
button6 = Button(root, text="6", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(6))
button7 = Button(root, text="7", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(7))
button8 = Button(root, text="8", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(8))
button9 = Button(root, text="9", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(9))
button0 = Button(root, text="0", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_click(0))

buttona = Button(root, text="+", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_add())
buttons = Button(root, text="−", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_subtract())
buttonm = Button(root, text="*", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_multiply())
buttond = Button(root, text="/", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_divide())
buttonp = Button(root, text="**", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_power())
buttonq = Button(root, text="%", bg="#dbefe1", height=3, width=20, bd=5, command=lambda: button_percent())

buttone = Button(root, text="=", bg="#b6d4bf", height=3, width=20, bd=5, command=lambda: button_equals())
buttonc = Button(root, text="Clear", bg="#b6d4bf", height=3, width=20, bd=5, command=lambda: button_clear())

button1['font'] = helv
button2['font'] = helv
button3['font'] = helv
button4['font'] = helv
button5['font'] = helv
button6['font'] = helv
button7['font'] = helv
button8['font'] = helv
button9['font'] = helv
button0['font'] = helv
buttona['font'] = helv
buttone['font'] = helv
buttonc['font'] = helv
buttons['font'] = helv
buttonm['font'] = helv
buttond['font'] = helv
buttonp['font'] = helv
buttonq['font'] = helv


# In[18]:


button1.grid(row=3, column=0, pady=2, sticky="")
button2.grid(row=3, column=1, pady=2, sticky="")
button3.grid(row=3, column=2, pady=2, sticky="")
button4.grid(row=2, column=0, pady=2, sticky="")
button5.grid(row=2, column=1, pady=2, sticky="")
button6.grid(row=2, column=2, pady=2, sticky="")
button7.grid(row=1, column=0, pady=2, sticky="")
button8.grid(row=1, column=1, pady=2, sticky="")
button9.grid(row=1, column=2, pady=2, sticky="")
button0.grid(row=4, column=0, pady=2, sticky="")
buttona.grid(row=4, column=1, pady=2, sticky="")
buttons.grid(row=4, column=2, pady=2, sticky="")
buttonm.grid(row=5, column=0, pady=2, sticky="")
buttond.grid(row=5, column=1, pady=2, sticky="")
buttonp.grid(row=5, column=2, pady=2, sticky="")

buttonq.grid(row=6, column=0, pady=2, sticky="")
buttone.grid(row=6, column=2, pady=2, sticky="")
buttonc.grid(row=6, column=1, pady=2, sticky="")

root.grid_columnconfigure((0, 2), weight=1)


# In[19]:


def openwindow():
    top = Toplevel()
    top.title("Converter")
    top.geometry("425x500")
    top.configure(bg='#86BEAF')
        
    e_2 = Entry(top, width=20, borderwidth=3)
    e_2.grid(row=1, column=1, padx=10, pady=20)
    
    e_3 = Entry(top, width=20, borderwidth=3)
    e_3.grid(row=2, column=1, padx=10, pady=20)
    
    e_4 = Entry(top, width=20, borderwidth=3)
    e_4.grid(row=3, column=1, padx=10, pady=20)
    
    e_5 = Entry(top, width=20, borderwidth=3)
    e_5.grid(row=4, column=1, padx=10, pady=20)
    
    e_6 = Entry(top, width=20, borderwidth=3)
    e_6.grid(row=5, column=1, padx=10, pady=20)
    
    e_7 = Entry(top, width=20, borderwidth=3)
    e_7.grid(row=6, column=1, padx=10, pady=20)
    
    def button_convert():
        get = e_2.get()
        num = int(get)
        conv = num * 2.205
        e_2.delete(0, END)
        e_2.insert(0, conv)
        e_8.insert(0, str(num) + " kg is " + str(conv) + " lb.")

    button_conv = Button(top, text="Convert kg to lb", bg="#dbefe1", height=1, width=30, bd=5, command=lambda: button_convert())
    button_conv.grid(row=1, column=2, pady=2)
    button_conv['font'] = helv

    def button_convert_2():
        get = e_3.get()
        num = int(get)
        conv = num / 2.205
        e_3.delete(0, END)
        e_3.insert(0, conv)
        e_8.insert(0, str(num) + " lb is " + str(conv) + " kg.")

    button_conv = Button(top, text="Convert lb to kg", bg="#dbefe1", height=1, width=30, bd=5, command=lambda: button_convert_2())
    button_conv.grid(row=2, column=2, pady=2)
    button_conv['font'] = helv
    
    def button_convert_3():
        get = e_4.get()
        num = int(get)
        conv = (num * 1.8) + 32
        e_4.delete(0, END)
        e_4.insert(0, conv)
        e_8.insert(0, str(num) + "° Celsius is " + str(conv) + "° Fahrenheit.")

    button_conv = Button(top, text="Convert Celcius to Fahrenheit", bg="#dbefe1", height=1, width=30, bd=5, command=lambda: button_convert_3())
    button_conv.grid(row=3, column=2, pady=2)
    button_conv['font'] = helv

    def button_convert_4():
        get = e_5.get()
        num = int(get)
        conv = (num - 32) * 0.5556
        e_5.delete(0, END)
        e_5.insert(0, conv)
        e_8.insert(0, str(num) + "° Fahrenheit is " + str(conv) + "° Celsius.")

    button_conv = Button(top, text="Convert Fahrenheit to Celsius", bg="#dbefe1", height=1, width=30, bd=5, command=lambda: button_convert_4())
    button_conv.grid(row=4, column=2, pady=2)
    button_conv['font'] = helv
    
    def button_convert_5():
        get = e_6.get()
        num = int(get)
        conv = num * 2.54
        e_6.delete(0, END)
        e_6.insert(0, conv)
        e_8.insert(0, str(num) + " inches is " + str(conv) + " cm.")

    button_conv = Button(top, text="Convert inches to cm", bg="#dbefe1", height=1, width=30, bd=5, command=lambda: button_convert_5())
    button_conv.grid(row=5, column=2, pady=2)
    button_conv['font'] = helv

    def button_convert_6():
        get = e_7.get()
        num = int(get)
        conv = num / 2.54
        e_7.delete(0, END)
        e_7.insert(0, conv)
        e_8.insert(0, str(num) + " cm is " + str(conv) + " inches.")

    button_conv = Button(top, text="Convert cm to inches", bg="#dbefe1", height=1, width=30, bd=5, command=lambda: button_convert_6())
    button_conv.grid(row=6, column=2, pady=2)
    button_conv['font'] = helv
    
    e_8 = Entry(top, width=40, borderwidth=3, bg="#cfcfcf")
    e_8.grid(row=7, column=2, padx=10, pady=20)
    
    def clearfields():
        e_2.delete(0, END)
        e_3.delete(0, END)
        e_4.delete(0, END)
        e_5.delete(0, END)
        e_6.delete(0, END)
        e_7.delete(0, END)
        e_8.delete(0, END)
        
    button_clearfield = Button(top, text="Clear fields", bd=5, command = lambda: clearfields())
    button_clearfield.grid(row=7, column=1)
             
openbutton = Button(root, text="Open the converter", bd=5, command = openwindow)
openbutton.grid(row=8,column=0)

closebutton = Button(root, text="Close the program", bd=5, command = root.destroy)
closebutton.grid(row=8,column=2)


# In[20]:


root.mainloop()

