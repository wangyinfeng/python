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

#    __all__ = ['_internal_data']

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

# _single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not 
# import objects whose name starts with an underscore. (not in the __all__ list) 
    _internal_data = 'i'

# __double_leading_underscore: when naming a class attribute, invokes name
# mangling (inside class FooBar, __boo becomes _FooBar__boo)
    __private_data = 'p' # can be accessed by _A__private_data
    def __private_name(self):
        print "Cannot be accessed by others"

# single_trailing_underscore_: used by convention to avoid conflicts with Python keyword
    class_ = 'c'

# __double_leading_and_trailing_underscore__: "magic" objects or attributes that live in 
# user-controlled namespaces.  E.g. __init__, __import__ or __file__.  Never invent such names; only use them
# as documented.

child_of_A = A()        
# it's equivalent to A.myname(child_of_A)
child_of_A.my_name()
print child_of_A.local_name

print A.__dict__

# The instance method can also be stored away and called by this way.
print_my_name = child_of_A.my_name()
# if no return specified in function, will return 'none' by default, so here will print 'a none'
print print_my_name

print child_of_A._A__private_data
#child_of_A.__private_name() #Error
child_of_A._A__private_name()

