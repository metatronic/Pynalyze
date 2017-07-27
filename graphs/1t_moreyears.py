from pylab import *
import pylab

t = [2008, 2009, 2010, 2011, 2012, 2013, 2014]
s = [6.2, 7.1, 7.2, 8.3, 8.2, 8.3, 8.0]
plot(t, s, label='Teacher XYZ')
pylab.legend(loc='upper right')
xlabel('YEARS')
ylabel('Ratings')
title('XYZ Teacher')
grid(True)
show()