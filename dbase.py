from MySQLdb import *


class DbConnect:
    def __init__(self, host):
        self.db = connect(host=host, user="root", passwd="", db="pz")
        self.cu = self.db.cursor()

    def db_admin_call(self, adm, psw):
        stmt = "Select a_id from admin where un='"+str(adm.get())+"' and uk='"+str(psw.get())+"'"
        self.cu.execute(stmt)
        rows = self.cu.rowcount
        if rows == 1:
            stmt = "select get_lock('admin_exe',2)"
            self.cu.execute(stmt)
            x = self.cu.fetchone()
            if x[0] == 0:
                return 2
            else:
                return 1
        else:
            return 0

    def db_stu_call(self, s_id, controller):
        stmt = "select * from student where s_id='"+str(s_id.get())+"'"
        self.cu.execute(stmt)
        row = self.cu.rowcount
        if row == 1:
            result = self.cu.fetchone()
            div = result[2]
            dept = result[3]
            sem = result[4]
            atd = result[7]
            # print(str(div)+" "+str(dept)+" "+str(sem))
            controller.set_var(dept, sem, div)
            if atd < 75.0:
                return 2
            else:
                return 1
        else:
            return 0

    def db_close(self):
        self.db.close()
