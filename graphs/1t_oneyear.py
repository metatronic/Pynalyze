import matplotlib.pyplot as plt
from dbase import DbConnect
plt.rcdefaults()


def tg1():
    db = DbConnect()
    db.cu.execute('select distinct t_id from feedback')
    res = db.cu.fetchall()
    print(res[0])
    r = []
    x = []
    for t in res:
        db.cu.execute('select sum(sum) from feedback where t_id='+str(t[0]))
        row = db.cu.fetchone()
        x.append(int(float(row[0])))
        r.append(row)
        print(x)
    db.cu.execute('select distinct t_id from feedback')
    res = db.cu.fetchall()
    objects = [int(i[0]) for i in res]
    print(objects)
    #  objects = ('TIME SENSE', 'SUBJ COMMND', 'TEACHNG METHDS', 'HELPING ATT.', 'INTERACTION', 'COMM SKILLS', 'OTHERS')

    performance = x

    name = []
    for i in objects:
        db.cu.execute('select t_name from mt_teacher where t_id='+str(i))
        res = db.cu.fetchone()
        name.append(res[0])
        print(name)

    plt.bar(objects, x, align='center', alpha=1.0)
    plt.xticks(objects, name)
    plt.ylabel('Ratings')
    plt.title('Teachers - March 2017')

    plt.show()