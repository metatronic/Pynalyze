# Pran P. Saha
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tg1 import tg1


class AdminPanel(ttk.Frame):
    def __init__(self, parent, controller, host):
        from dbase import DbConnect
        ttk.Frame.__init__(self, parent)
        menu_bar = Menu(controller)
        controller['menu'] = menu_bar
        menu_file = Menu(menu_bar)
        menu_edit = Menu(menu_bar)
        menu_setting = Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_bar.add_cascade(menu=menu_edit, label='Edit')
        menu_setting.add_cascade(menu=menu_edit, label='setting')
        self.percent = DoubleVar()
        self.fb = StringVar()
        self.ip = host
        self.db = DbConnect(self.ip)

        n = ttk.Notebook(self)
        general = ttk.Frame(n)  # first page, which would get widgets gridded into it
        tools = ttk.Frame(n)  # second page
        stats = ttk.Frame(n)  # graph page

        graph = ttk.Combobox(stats)
        graph['values'] = ('', 'All teachers')
        graph.current(0)
        graph.grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(stats, text='Generate graph', command=lambda: tg1()).grid(row=0, column=1, padx=10, pady=10)

        mail = ttk.Combobox(stats)
        db = DbConnect(self.ip)
        db.cu.execute('select t_name from mt_teacher')
        row = db.cu.fetchall()
        # print(row)
        mail['values'] = row
        mail.grid(row=1, column=0)
        ttk.Button(stats, text="Send Mail", command=lambda: messagebox.showinfo('Pynalyze', 'Message sent successfully')
                   ).grid(row=1, column=1)

        sel = ttk.LabelFrame(general, text='Selection')
        sel.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(sel, text='Select Department code').grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.dept = ttk.Combobox(sel)
        self.dept.grid(row=0, column=1, sticky=W)
        self.db.cu.execute('select distinct s_dept from student')
        self.dept['values'] = self.db.cu.fetchall()

        ttk.Entry(sel, textvariable=self.percent).grid(row=1, column=1, sticky=W)
        ttk.Label(sel, text='Minimum Percentage : ').grid(row=1, column=0, padx=10, pady=10, sticky=W)

        ttk.Label(sel, text='Select Semester').grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.sem = ttk.Combobox(sel)
        self.sem.grid(row=2, column=1, sticky=W)
        self.db.cu.execute('select distinct s_sem from student')
        self.sem['values'] = self.db.cu.fetchall()

        ttk.Label(sel, text='Select Division').grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.div = ttk.Combobox(sel)
        self.div.grid(row=3, column=1, sticky=W)
        self.db.cu.execute('select distinct s_div from student')
        self.div['values'] = self.db.cu.fetchall()

        ttk.Label(sel, text='Type of Feedback').grid(row=4, column=0, padx=10, pady=10, sticky=W)
        sf = ttk.Frame(sel, borderwidth=2, relief=GROOVE)
        sf.grid(row=4, column=1, sticky=E)
        ttk.Radiobutton(sf, variable=self.fb, text='Standard', value='0').grid(row=0, column=0)
        ttk.Radiobutton(sf, variable=self.fb, text='Behavioral', value='1').grid(row=0, column=1)
        ttk.Button(sel, text='Start', command=lambda: self.update_all()).grid(row=5, column=2)
        self.db.db.close()
        n.add(general, text='General')
        n.add(tools, text='Tools')
        n.add(stats, text='Stats')
        n.grid()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def update_all(self):
        from dbase import DbConnect
        db = DbConnect(self.ip)
        db.cu.execute('update con set i='+str(self.fb.get())+' where p=1')
        db.db.commit()
        messagebox.showinfo("Pynalyze", "feedback session  has started")
