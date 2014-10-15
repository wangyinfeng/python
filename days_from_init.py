from sys import argv
from datetime import date
from datetime import datetime

init_year=2014
init_month=2
init_day=6

# the input argv has format like 2014.10.15, split year.month.day with '.'
if len(argv) == 2:
#    script_name, date = argv # TypeError: 'str' object is not callable. date is a build-in name
    script_name, the_date = argv
    # so damn easy to split the string.
    specified_date=the_date.split(".") 
    the_year=int(specified_date[0])
    the_month=int(specified_date[1])
    the_day=int(specified_date[2])

    days=(date(the_year, the_month, the_day)-date(init_year, init_month, init_day)).days 
    print "To %s, Angel has came for %d days." %(the_date, days)
else:
#print (datetime.now().date()-date(init_year, init_month, init_day)).days 
    days=(datetime.now().date()-date(init_year, init_month, init_day)).days 
    print "Angel has came for %d days." %days

