#date time module
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")#lower case
fv=a.strftime("%Y")#upper case
print("year short version",sv)
print("year full version",fv)
