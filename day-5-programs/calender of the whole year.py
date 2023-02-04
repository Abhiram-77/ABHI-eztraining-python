#calender of the whole year
import calendar

print("full calendar")
print(calendar.calendar(2003))
print("particuar month")
print(calendar.month(2003,7))
print("set the first day of week as sunday")
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2021,7))
