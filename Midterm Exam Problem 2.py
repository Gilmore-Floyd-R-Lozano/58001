from tkinter import*
class MidtermExamP2():
    def __init__(self,windows):
        self.lbltl= Label(windows,text="My Full Name")
        self.lbltl.place(x=300,y=100)
        self.lbl1 = Label(windows,text="Enter Given Name: ")
        self.lbl1.place(x=200,y=150)
        self.lbl2 = Label(windows,text="Enter Middle Name: ")
        self.lbl2.place(x=200,y=200)
        self.lbl3 = Label(windows,text="Enter Last Name:")
        self.lbl3.place(x=200, y=250)
        self.lbl4 = Label(windows,text="My Full Name is: ")
        self.lbl4.place(x=200,y=300)
        self.tbx1 = Entry(windows, bd=1)
        self.tbx1.place(x=350,y=150)
        self.tbx2 = Entry(windows, bd=1)
        self.tbx2.place(x=350,y=200)
        self.tbx3 = Entry(windows,bd=1)
        self.tbx3.place(x=350,y=250)
        self.tbx4 = Entry(windows,width = 40, bd=1)
        self.tbx4.place(x=350,y=300)
        self.btn = Button(windows,text="Show Full Name")
        self.btn.bind("<Button-1>",self.Display)
        self.btn.place(x=325,y=350)

    def Display(self,Display):
        self.tbx4.delete(0,END)
        Given_name = str(self.tbx1.get())
        Middle_name = str(self.tbx2.get())
        Last_name = str(self.tbx3.get())
        Fullname = Given_name + " " + Middle_name + " " + Last_name
        self.tbx4.insert(END,str(Fullname))
window = Tk()
myWin=MidtermExamP2(window)
window.geometry("700x500")
window.title("Midterm Exam Problem 2")
window.mainloop()


