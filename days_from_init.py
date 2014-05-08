from datetime import date
from datetime import datetime
init_year=2014
init_month=2
init_day=6
#print (datetime.now().date()-date(init_year, init_month, init_day)).days 
days=(datetime.now().date()-date(init_year, init_month, init_day)).days 
print "Angel has came for %d days." %days
