from pylab import *
import pylab
from dbase import DbConnect


def tg1(t1):
    db = DbConnect()
    db.cu.execute('select * from feedback where t_id='+str(t1))
    row = db.cu.fetchall()
    print(row)
    t = [2008, 2009, 2010, 2011, 2012, 2013, 2014]
    s = [6.2, 7.1, 7.2, 8.3, 8.2, 8.3, 8.0]
    s2 = [7.5, 7.6, 8.0, 7, 7.6, 8.2, 7.9]
    plot(t, s, label='Teacher XYZ')
    plot(t, s2, label='Teacher PQR')
    pylab.legend(loc='upper right')
    xlabel('YEARS')
    ylabel('Ratings')
    title('XYZ v/s PQR')
    grid(True)
    show()

tg1(1)
