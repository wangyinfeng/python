
# by default all class members are public

# private variables and class-local reference

# member functions are virtual?

# build-in functions


class A:
    """The first example of a Class"""
# message inside """help""" will show when use help(module), some kind of document auto generation
# also can be get by the buildin function __doc__
    def __init__(self):
        pass
# all functions(methods) and variables(data) are attributes of the class
    local_name = 'A'
    def my_name(self):
        """The help info about function my_name"""
# different block has different namespace
# local namesapce for a function is created when the function is called, 
# is deleted when the function exit or expception happens and not be handled
# by the function.
        local_name = 'a'
        my_life = "alive"
        print local_name

# and local variable's life time limited inside block
#    print my_life

child_of_A = A()        
# it's equivalent to A.myname(child_of_A)
child_of_A.my_name()
print child_of_A.local_name

# The instance method can also be stored away and called by this way.
print_my_name = child_of_A.my_name()
# if no return specified in function, will return 'none' by default, so here will print 'a none'
print print_my_name


