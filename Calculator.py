from tkinter import *

#CALCULATOR

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.display=""
        self.position1=""
        self.position2=""
        self.operator=""
        self.total=""
    def create_widgets(self):
        self.button0=Button(self)
        self.button0.configure(text="0", bg="black", fg="white", height=2, width=5, command=self.button_click0)
        self.button0.grid(row=4, column=2)

        self.button9 = Button(self)
        self.button9.configure(text="9", bg="black", fg="white", height=2, width=5, command=self.button_click9)
        self.button9.grid(row=1, column=3)

        self.button8 = Button(self)
        self.button8.configure(text="8", bg="black", fg="white", height=2, width=5, command=self.button_click8)
        self.button8.grid(row=1, column=2)

        self.button7 = Button(self)
        self.button7.configure(text="7", bg="black", fg="white", height=2, width=5, command=self.button_click7)
        self.button7.grid(row=1, column=1)

        self.button6=Button(self)
        self.button6.configure(text="6", bg="black", fg="white", height=2, width=5, command=self.button_click6)
        self.button6.grid(row=2, column=3)

        self.button5 = Button(self)
        self.button5.configure(text="5", bg="black", fg="white", height=2, width=5, command=self.button_click5)
        self.button5.grid(row=2, column=2)

        self.button4 = Button(self)
        self.button4.configure(text="4", bg="black", fg="white", height=2, width=5, command=self.button_click4)
        self.button4.grid(row=2, column=1)

        self.button3 = Button(self)
        self.button3.configure(text="3", bg="black", fg="white", height=2, width=5, command=self.button_click3)
        self.button3.grid(row=3, column=3)

        self.button2 = Button(self)
        self.button2.configure(text="2", bg="black", fg="white", height=2, width=5, command=self.button_click2)
        self.button2.grid(row=3, column=2)

        self.button1 = Button(self)
        self.button1.configure(text="1", bg="black", fg="white", height=2, width=5, command=self.button_click1)
        self.button1.grid(row=3, column=1)

        self.button_add = Button(self)
        self.button_add.configure(text="+", bg="black", fg="white", height=2, width=5, command=self.add)
        self.button_add.grid(row=3, column=4)

        self.button_sub = Button(self)
        self.button_sub.configure(text="-", bg="black", fg="white", height=2, width=5, command=self.sub)
        self.button_sub.grid(row=4, column=4)

        self.button_div = Button(self)
        self.button_div.configure(text="/", bg="black", fg="white", height=2, width=5, command=self.div)
        self.button_div.grid(row=1, column=4)

        self.button_mult = Button(self)
        self.button_mult.configure(text="x", bg="black", fg="white", height=2, width=5, command=self.mult)
        self.button_mult.grid(row=2, column=4)

        self.button_equals = Button(self)
        self.button_equals.configure(text="=", bg="black", fg="white", height=2, width=10, command=self.equals)
        self.button_equals.grid(row=5, column=5)

        self.text_box=Text(self, height=10, width=10)
        self.text_box.grid(row=0, column=0, columnspan=6, sticky=NSEW)

    def add(self):
        self.position1=self.display
        self.display=""
        self.operator="+"
        self.text_box.delete(0.0, END)

    def sub(self):
        self.position1 = self.display
        self.display = ""
        self.operator = "-"
        self.text_box.delete(0.0, END)
    def div(self):
        self.position1 = self.display
        self.display = ""
        self.operator = "/"
        self.text_box.delete(0.0, END)
    def mult(self):
        self.position1 = self.display
        self.display = ""
        self.operator = "x"
        self.text_box.delete(0.0, END)
    def button_click1(self):
        self.display+="1"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click2(self):
        self.display+="2"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click3(self):
        self.display+="3"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click4(self):
        self.display+="4"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click5(self):
        self.display+="5"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click6(self):
        self.display+="6"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click7(self):
        self.display+="7"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click8(self):
        self.display+="8"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click9(self):
        self.display+="9"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)
    def button_click0(self):
        self.display+="0"
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.display)

    def equals(self):
        self.position2=self.display
        self.display=""
        if self.operator=="+":
            self.total=int(self.position1)+int(self.position2)
        elif self.operator=="-":
            self.total=int(self.position1)-int(self.position2)
        elif self.operator=="x":
            self.total=int(self.position1)*int(self.position2)
        elif self.operator=="/":
            self.total=int(self.position1)/int(self.position2)
        self.display=self.total
        self.text_box.delete(0.0, END)#forgot .0 after 0
        self.text_box.insert(0.0, self.display)#forgot .0 after 0
root=Tk()
root.title("Calculator")
root.geometry("500x500")
app=Application(root)
root.mainloop()