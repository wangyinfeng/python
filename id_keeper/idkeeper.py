# The task is simple, print the password and username for the input key word.
# First step run as: DONE
#   #python idkeeper.py gmail
#   #wang@gmail.com:123456
#
# Then next step may provide interactive mode: DONE
#   #python idkeeper.py
#   #Input the web name:
#    > gmail
#   #Your account for gmail is:
#   #wang@gmail.com:123456
#
# Then next step may provide fuzzy matching in case you can't remember the full/correct name of the web: DONE
#   #python idkeeper.py
#   #Input the web name:
#     > mail
#   #Do you mean:
#    gmail
#    amail
#    bmail
#   Select the correct name and input again:
#    >gmail
#   #Your account for gmail is:
#   #wang@gmail.com:123456
#
# Then next step should provide encrypt for the accounts content, some accounts are critical. DONE
# 
# Then next step should move the critical data to another file, and encrypt that file with a different way.
#
# I hope when want to add something new, only need to do one operation, input the account and the password, then the coder encrypt the password and insert the accound info to the hash table automatially. Anyway, the encrypt result is not readable and show it out is meanless.
#
# Then next step may provide binary file to run directly, for both linux and windows.
from sys import argv
from code import decode

# seprate data from the code - DONE
# auto insert new item to the data file
# provide delete and modify the item by the key word

box = {}

if len(argv) == 2:
    script_name, account = argv
else:
    account = raw_input("Input the web name:")

# load all data to box
with open("data") as f:
    for line in f:
        (key, val) = line.split(':')
        box[key] = val

candidate = []
if account == 'all':
    for name in box.keys():
        print name,
        print "\t\t",
        print decode(box[name])
elif box.has_key(account) == False:
    for name in box.keys():
        if name.find(account) == -1:
            pass
        else:
            candidate.append(name)
    if len(candidate):
        print "Do you mean:"
        for n in candidate:
            print "\t\t",
            print n
        account = raw_input(">")    
        if len(account):
            print decode(box[account])
        else:
            exit(1)
    else:
        print "Can't find the account '%s', try the correct name." % account
        exit(1)
else:
    print decode(box[account])

