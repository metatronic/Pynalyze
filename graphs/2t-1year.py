import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

objects = ('TIME SENSE', 'SUBJ COMMND', 'TEACHNG METHDS', 'HELPING ATT.', 'INTERACTION', 'COMM SKILLS', 'OTHERS')
y_pos = np.arange(len(objects))
performance = [2, 4, 5, 3, 3, 3, 4]
performance2 = [4, 3, 4, 3, 4, 3, 3]

plt.bar(y_pos-0.2, performance, width=0.4, align='center', alpha=1.0)
plt.bar(y_pos+0.2, performance2, width=0.4, align='center', alpha=1.0)
plt.xticks(y_pos, objects, rotation='vertical')
plt.ylabel('Ratings')
plt.title('Teacher XYZ v/s Teacher PQR - March 2017')

plt.show()
