# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:15:31 2019

@author: beenugopalsingla sip

"""

import datetime

print(dir(datetime), end=',')
print(dir(datetime.timedelta), end=',')

beenu = datetime.datetime.now()     #we have used datetime 2 times bcz in datatime their is another module in which datatime is their which stores the now function.
print(beenu)
print(beenu.year, beenu.min)
beenu.min
beenu.max
print(beenu.strftime("%A"))

dob = datetime.datetime(1997,9,22,15,27,00)
dob.date()
print(dob.strftime("%B %A : %H %M %S : %Y"))


from datetime import datetime as bc
today = bc.now()
today
bc.strftime(today, '%d - %y')

today
bc.strptime("3/7/2019", "%d/%m/%Y")
date1 = bc.strptime("3/7/2019", "%d/%m/%Y")
type(date1)
date1.weekday()
date1.strftime("%A %d %Y")
date1 + 1   #error


d1 = dt(2019,6,10)
d2 = dt(2019,7,28)
d2 - d1
dob = dt(1997,9,22)
now = dt(2019,7,3)
diff=now - dob
diff
diff/365

d = bc(2019, 7, 4, 15, 30)
d1 = d.replace(day=28)       
d1
import datetime
today = datetime.date.today()
today

today + 1

today + datetime.timedelta(days=1)


# in this date, i did how to import datetime dataset in different ways. learned how to gets number of days, how to convert string into time and then time into string and how to extract different details from a date or day and all...