# Pran P. Saha
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class StudentForm(ttk.Frame):
    def __init__(self, parent, controller, host):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        self.div = StringVar()
        self.sem = StringVar()
        self.t = StringVar()
        self.tent = []
        self.ip = host
        self.ent = []
        self.block = BooleanVar(self, FALSE)
        self.count = 1
        self.inc = 0
        self.dept = None

        # frame for teacher's list
        # variable to store questions
        self.q = StringVar()
        self.question_loop()
        # ttk.Frame(self, width=400).grid(row=0, column=0)
        q_box = ttk.Frame(self, height=40, width=300)
        q_box.grid(row=1, column=1, sticky=(W, E))
        q_box.grid_propagate(0)

        question = Message(q_box, textvariable=self.q, width=300)
        question.grid(row=1, column=1, sticky=(W, E))

        # frame for radio buttons

        r_frame = ttk.Frame(self, borderwidth=5, relief=GROOVE)
        r_frame.grid(row=2, column=1, sticky=W)

        self.marks = IntVar()

        # radio buttons for the grading
        ttk.Radiobutton(r_frame, text="Excellent", variable=self.marks, value=5).grid(row=0, column=0, sticky=W)
        ttk.Radiobutton(r_frame, text="Very Good", variable=self.marks, value=4).grid(row=1, column=0, sticky=W)
        ttk.Radiobutton(r_frame, text="Good", variable=self.marks, value=3).grid(row=2, column=0, sticky=W)
        ttk.Radiobutton(r_frame, text="Needs Improvement", variable=self.marks, value=2).grid(row=3, column=0, sticky=W)
        ttk.Radiobutton(r_frame, text="Unsatisfactory", variable=self.marks, value=1).grid(row=4, column=0, sticky=W)

        ttk.Button(self, text="Confirm >", command=lambda: self.eval_quest(self.count)).grid(row=3, column=1, sticky=E,
                                                                                             padx=10)

        for child in self.winfo_children():
            child.grid_configure(padx=6, pady=6)

    def eval_quest(self, i):
        from dbase import DbConnect
        db = DbConnect(self.ip)
        stmt = 'select t_id,t_sub from teacher where dept="' + str(self.dept) + '" and t_div="' + str(
            self.div) + '" and sem=' + str(self.sem)
        db.cu.execute(stmt)
        res = db.cu.rowcount
        if self.inc <= res:
            if self.marks.get() != 0:
                db.cu.execute('select * from mt_question')
                q_count = db.cu.rowcount
                if i <= q_count:
                    self.eval()
                    self.question_loop()
                else:
                    self.eval()
                    self.tent.append(self.ent)
                    print(self.tent)
                    self.ent = []
                    self.count = 1
                    self.question_loop()
                    self.show_teacher()
            else:
                messagebox.showwarning('Pynalyze', 'Select an option')

    def question_loop(self):

        from dbase import DbConnect

        db = DbConnect(self.ip)
        db.cu.execute('select i from con')
        row = db.cu.fetchone()
        if row[0]:
            db.cu.execute('select q_text from mt_question where q_id='+str(self.count))
            res = db.cu.fetchone()
            self.count += 1
            self.q.set(res[0])
        else:
            db.cu.execute('select q_text from mt_question where q_id='+str(33+self.count)+'')
            res = db.cu.fetchone()
            self.count += 1
            try:
                self.q.set(res[0])
            except self.q:
                self.show_teacher()

    def eval(self):
        self.ent.append(self.marks.get())
        print(self.ent)
        self.marks.set(0)

    def set_var(self, dept, sem, div):
        self.dept = dept
        self.sem = sem
        self.div = div
        self.show_teacher()

    def show_teacher(self):
        from dbase import DbConnect
        self.inc += 1

        top_list = ttk.Frame(self, height=200, width=100, borderwidth=2, relief=GROOVE)
        top_list.grid(row=0, column=0, rowspan=3, sticky=(N, W), padx=6, pady=6)
        top_list.grid_propagate(0)

        db = DbConnect(self.ip)
        stmt = 'select t_id,t_sub from teacher where dept="'+str(self.dept)+'" and t_div="'+str(self.div)+'" and sem='\
               + str(self.sem)
        db.cu.execute(stmt)
        res = db.cu.fetchall()
        name = []
        sub = []
        for t in res:
            db.cu.execute('select t_name from mt_teacher where t_id='+str(t[0]))
            row = db.cu.fetchall()
            name.append(row[0])
            sub.append(t[1])
        for t in name:
            ttk.Label(top_list, text=t).grid(padx=6, pady=6)
        info = ttk.Frame(self, height=100, width=400, borderwidth=2, relief=GROOVE)
        info.grid(row=0, column=1, columnspan=3, sticky=(N, W), padx=6, pady=6)
        try:
            n = ''.join(name[self.inc-1])
            s = ''.join(sub[self.inc-1])
            self.t.set('Name:   '+n+'      Dept:  '+str(self.dept)+'      Subject:  '+s)
            ttk.Label(info, textvariable=self.t).grid(row=0, column=0, ipadx=25, ipady=20, sticky=E)
        except db:
            self.grid_remove()
            messagebox.showinfo('Pynalyze', 'Thank You')
            # update to database
            self.controller.destroy()
