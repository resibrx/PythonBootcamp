import datetime

#create timestamp hour minutes seconds
thisIsMyTime = datetime.time(5,25,1)
print(thisIsMyTime)
print(thisIsMyTime.hour)
print(thisIsMyTime.minute)
print(thisIsMyTime.second)

#time instance only hold times without date reference
print(datetime.time.min)
# before 24h mark
print(datetime.time.max)

#dates
today = datetime.date.today()
print('Today is : ', today)
# more information
print('Some more information about today: ',today.timetuple())
print('Current year: ',today.year)
print('Current month: ',today.month)

print(datetime.date.min)
print(datetime.date.max)

d1 = datetime.date(2015,3,11)
print(d1)
#replace
d2 = d1.replace(year=1999)
print(d2)

#show difference between this years in days
print(d1-d2)
