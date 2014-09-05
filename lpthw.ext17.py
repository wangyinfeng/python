from sys import argv
from os.path import exists

#unpacking the argv, argument number must be exactly right
script, src, dst = argv

print "%s will copy file %s to %s" % (script, src, dst)

if exists(dst):
    print "The file %s already exist!" % dst
    raw_input("Overwrite? or Ctrl-C to exit.\n")

#It's amazing the efficent about reading and writing data, 
#even for GB size file, only need seconds. How?

#by this way no need to close() the file descript
#And it's so simple to operate the files compare to the C.
#I may understand now the high level language let you focus
#on the problem itself.
data = open(src, 'r').read()
open(dst, 'w').write(data)

