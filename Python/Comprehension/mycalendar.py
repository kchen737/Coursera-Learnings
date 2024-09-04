import sys
#from .... import ...variable...
locations = sys.path
print(locations)
for i in locations:
    print(i)
    
import calendar #press comand and click on it to access the file

leapdays = calendar.leapdays(2000,2050)
print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)

#check out python standard library