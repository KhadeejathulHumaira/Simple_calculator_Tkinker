from tkinter import *
root=Tk()
root.title("Calculator")
expression=""
def evaluate(number):
    global expression
    expression=expression+str(number)
    equation.set(expression)

def button_clear():
    global expression
    expression=""
    equation.set("")

def equal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression=""

equation=StringVar()
input=Entry(root,width=60,borderwidth=5,fg="white",bg="black",textvariable=equation)
input.grid(column=0,row=0,columnspan=4,padx=10,pady=15)
# Define Buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda :evaluate(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda :evaluate(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda :evaluate(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda :evaluate(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda :evaluate(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda :evaluate(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda :evaluate(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda :evaluate(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda :evaluate(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda :evaluate(0))
button_add=Button(root,text="+",padx=40,pady=20,command=lambda:evaluate("+"))
button_sub=Button(root,text="-",padx=40,pady=20,command=lambda :evaluate("-"))
button_multi=Button(root,text="x",padx=40,pady=20,command=lambda :evaluate("*"))
button_div=Button(root,text="/",padx=40,pady=20,command=lambda :evaluate("/"))
button_equal=Button(root,text="=",padx=40,pady=20,command=equal)
button_clear=Button(root,text="C",padx=40,pady=20,command=button_clear)



#Put the buttons on the screen
#row3
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_sub.grid(row=3,column=3)
#row2
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_multi.grid(row=2,column=3)
#row 1
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_div.grid(row=1,column=3)
#row4
button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_add.grid(row=4,column=3)




root.mainloop()