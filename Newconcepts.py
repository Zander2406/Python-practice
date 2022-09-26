# split function
'''filename = "houseofdragon.mkv"
first, last = filename.split(".")
print(last)'''

# datetime
from datetime import date as dt
# dtnow = dt.now()
# print(dtnow)
dt1 = dt(2014, 7, 2)
dt2 = dt(2014, 7, 11)
gap = dt2 - dt1 
print(str(gap)[0])