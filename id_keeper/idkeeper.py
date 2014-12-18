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
# Then next step should move the critical data to another file. DONE
# and encrypt that file with a different way - double encrypt.
#
# I hope when want to add something new, only need to do one operation, input the account and the password, then the coder encrypt the password and insert the accound info to the hash table automatially. Anyway, the encrypt result is not readable and show it out is meanless. DONE
#
# Then next step may provide binary file to run directly, for both linux and windows.
import pdb
from sys import argv
from code import decode, encode
import getopt
import fileinput
import code

box = {}
candidate = []
def init():
    """Do initialization actions, prepare for encode and decode"""
# load all data to box
    with open("data") as f:
        for line in f:
            (key, val) = line.split(':')
            box[key] = val

init()

# seprate data from the code - DONE
# use getopt to parse the commands - DONE
# auto insert new item to the data file - DONE
# provide delete and modify the item by the key word - DONE
def usage():
    """Help info"""    
    print "usage: python idkeeper.py [-a|-m|-d|-c] <instance account:password>"
    print "\t\t -a to add a new item"
    print "\t\t -m to modify an existed item"
    print "\t\t -d to delete an existed item"
    print "\t\t -h help"
    print "example: python idkeeper.py -a twitter god:123"

def check(account):
    """Fetch the username and password by the input target"""    
    if account == 'all':
        for name in box.keys():
            print name,
            print "\t\t\t",
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

def add(item):
    """Add a new target to the data file, do encrpyt automatically"""    
    # there is no argc in python, get the number of argc by len(argv)
    if len(argv) == 4:
        pw = argv[3]
        code_pw = code.encode(pw)
        line = "%s:%s\n" % (item, code_pw)
        #do I need f.close()? - no, will be auto closed ASAP the file object is garbage collected
        with open("data", "a") as f: 
#            f.write("%s\n" % line) # Risk here, the '\' may be misunderstand, use %r contain the ''
            f.write(line) # not require format is better
    else:
        print "Incorrect command:\t",
        print " ".join([str(x) for x in argv])

def modify(item):
    """Modify the existed target's username and password pair"""    
    if len(argv) == 4:
        if box.has_key(item) == True:
            pw = argv[3]
            code_pw = code.encode(pw)
            new_line = '%s:%s\n' % (item, code_pw)
# The most explict way to modify the line, is read out then write back, 
# a little more operations, but clear enough
            f = open("data", "r")
            lines = f.readlines()
            f.close()
            f = open("data", "w")
            for line in lines:
                if item in line:
                    f.write(new_line)
                else:
                    f.write(line)
            f.close()

#            for line in fileinput.input("data", inplace=True):
#                if item in line:
#                    print "%s" % new_line #redirect the stdout to the file, so print works
#                else:
#                    print "%s" % line
        else:
            print "The target '%s' not exist." % item
            exit(1)
    else:
        print "Incorrect command:\t",
        print " ".join([str(x) for x in argv])
    exit(1) 

def delete(account):
    """Delete the target from the data file"""
    if box.has_key(account) == False:
        print "Can't find the account '%s', try the correct name." % account
        exit(1)
    else:
        f = open("data", "r")
        lines = f.readlines()
        f.close()
        f = open("data", "w")
        for line in lines:
            if account not in line:
                f.write(line)
        f.close()

try:
#    pdb.set_trace()
    opts, args = getopt.getopt(argv[1:], "ha:d:m:c:", ["help=", "add=", "delete=", "modify=", "check="])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err) # will print something like "option -a not recognized"
    usage()
    exit(2)

verbose = False
for o, a in opts:
    if o == "-v":
        verbose = True
    elif o in ("-h", "--help"):
        usage()
        exit(1)
    elif o in ("-c", "--check"):
        check(a)
    elif o in ("-a", "--add"):
        add(a)
    elif o in ("-m", "--modify"):
        modify(a)
    elif o in ("-d", "--delete"):
        delete(a)
    else:
        usage()
        exit(2)

# By doing the main check, you can have that code only execute when you want to run the module as a program 
# and not have it execute when someone just wants to import your module and call your functions themselves.
# If this file is being imported from another module, __name__ will be set to the module's name.
if __name__ == "__main__":
    if not opts: #if opts is empty
        usage()
    pass

