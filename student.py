# Pran P. Saha
from tkinter import *
from tkinter import ttk
from start import Start
from tkinter import messagebox


class Student(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.std_id = StringVar()
        self.ip = StringVar()

        lf = ttk.LabelFrame(self, text="Student Verification:")
        lf.grid(row=0, column=0, ipadx=10, ipady=10, sticky=(W, E))
        # input strings
        ttk.Label(lf, text="Student ID :").grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        std_id = ttk.Entry(lf, textvariable=self.std_id)
        std_id.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        std_id.focus_set()

        cf = ttk.LabelFrame(self, text="Server Connect:                      ")
        cf.grid(row=1, column=0, ipadx=10, ipady=10, sticky=(W, E))
        ttk.Label(cf, text="Server IP : ").grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        ttk.Entry(cf, textvariable=self.ip).grid(row=1, column=1, sticky=E, padx=5, pady=5)
        print(self.ip.get())

        filler = ttk.Frame(lf)
        filler.grid(row=1, column=1)
        filler.winfo_toplevel().geometry("100x100")

        # button for back and next
        ttk.Button(self, text="Next >", command=lambda: self.student_check(parent, controller))\
            .grid(row=3, column=4, sticky=E)
        ttk.Button(self, text="< Back", command=lambda: controller.show_frame(Start)).\
            grid(row=3, column=3, sticky=W)

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def student_check(self, parent, controller):
        from dbase import DbConnect
        from studentform import StudentForm
        try:
            db_con = DbConnect(self.ip.get())
            sf = StudentForm(parent, controller, self.ip.get())
            c = db_con.db_stu_call(self.std_id, sf)
            if c == 1:
                print(self.ip.get())
                controller.remove_frame()
                sf.grid()
            elif c == 0:
                messagebox.showerror('Pynalyze', 'Select your correct student id please')
            else:
                messagebox.showwarning('Pynalyze', 'Sorry!! you are not allowed to proceed')
        except:
            messagebox.showerror('Pynalyze', 'Server not reachable')
