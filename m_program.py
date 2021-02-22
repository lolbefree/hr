import datetime
import holidays

vacation = input("Введіть кількість відпустки в к.д.: ")
date_entry = input('Дата приняття на роботу: ')
use_entry = int(input("Кількість використаної відпустки: "))
vacation_data = int(vacation) / (365 - 10)

"""
print(len(date_entry))
print(type(date_entry))
for i, item in enumerate(date_entry, start=1):
    print(i-1,item)
"""

try:
    if len(date_entry) == 10:
        year = date_entry[6:10]
        month = date_entry[3:5]
        day = date_entry[0:2]
    if len(date_entry) == 8:
        year = date_entry[4:8]
        month = date_entry[2:4]
        day = date_entry[0:2]
    if len(date_entry) == 6:
        year = "20" + date_entry[4:6]
        month = date_entry[2:4]
        day = date_entry[0:2]
    if len(date_entry) > 10 or len(date_entry) < 6:
        raise ValueError()
except ValueError:
    print("Вы ввели не коректную дату!")
    raise SystemExit

try:
    d0 = datetime.date(int(year), int(month), int(day))
    d1 = datetime.date.today()
    #print("d0 is: ", d0)
except (NameError, ValueError):
    raise SystemExit

# праздніки
start = d0
end = d1
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
lost_day = 0
ua_holidays = holidays.CountryHoliday('UA')
for date in date_generated:
    tmp_day = ua_holidays.get(date)
    if tmp_day != None:
        lost_day += 1
        #print("lost_dayis", lost_day)


delta = d1 - d0
deys_data = delta.days - lost_day
#vacation_data = int(vacation) / deys_data       # узнаем коэфициент
print("vacation data is:", vacation_data)
#print(deys_data)

days_for_holiday = (vacation_data * deys_data) - use_entry
print("print tyt", days_for_holiday)
if days_for_holiday >= 0:
    print("Працівник має право на", round(days_for_holiday), "к.д.")
if days_for_holiday < 0:
    print("Працівник використав відпустку на перед", round(days_for_holiday), "к.д.")


