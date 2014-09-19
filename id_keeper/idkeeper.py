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
# Then next step should provide encrypt for the accounts content, some accounts are critical.
#
# Then next step may provide binary file to run directly, for both linux and windows.
from sys import argv

box = { "pip.io":"mfrc531:16", 
        "pip":"m:16",
        "pipop":"f:16",
        "pinterest":"mfrc531:16", 
        "kanbox":"batman.wang@qq.com:16"}

if len(argv) == 2:
    script_name, account = argv
else:
    account = raw_input("Input the web name:")

candidate = []
if account == 'all':
    for name in box.keys():
        print name,
        print "\t",
        print box[name]
elif box.has_key(account) == False:
    for name in box.keys():
        if name.find(account) == -1:
            pass
        else:
            candidate.append(name)
    if len(candidate):
        print "Do you mean:"
        for n in candidate:
            print "\t",
            print n
        account = raw_input(">")    
        print box[account]
    else:
        print "Can't find the account '%s', try the correct name." % account
        exit(1)
else:
    print box[account]

