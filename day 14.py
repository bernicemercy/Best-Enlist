'''
Exception	Cause of Error
----------------------------------------------------------------------------------------------------------------------------------
AssertionError	        Raised when an assert statement fails.
AttributeError	        Raised when attribute assignment or reference fails.
EOFError	        Raised when the input() function hits end-of-file condition.
FloatingPointError	Raised when a floating point operation fails.
GeneratorExit	        Raise when a generator's close() method is called.
ImportError	        Raised when the imported module is not found.
IndexError	        Raised when the index of a sequence is out of range.
KeyError	        Raised when a key is not found in a dictionary.
KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+C or Delete).
MemoryError	        Raised when an operation runs out of memory.
NameError	        Raised when a variable is not found in local or global scope.
NotImplementedError	Raised by abstract methods.
OSError	                Raised when system operation causes system related error.
OverflowError	        Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	        Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	        Raised when an error does not fall under any other category.
StopIteration	        Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError	        Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError           	Raised when indentation consists of inconsistent tabs and spaces.
SystemError	        Raised when interpreter detects internal error.
SystemExit	        Raised by sys.exit() function.
TypeError	        Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	        Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
ValueError	        Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError	Raised when the second operand of division or modulo operation is zero.

'''

#1.
try:
    x = 1/0
except ZeroDivisionError:
    print("Division by zero")

#2.
loop = 1
choice = 0

while loop == 1:
     print("enter 1 to 4")
     choice = int(input("choose your option: "))
     print(choice)
     a = int(input("Number 1 :"))
     b = int(input("Number 2 :"))
     try:
         if (choice == 1):
            print("hvvj")
            print(a+b)
         elif (choice == 2):
            print(a-b)
         elif (choice == 3):
            print(a*b)
         elif (choice == 4):
            print(a/b)
         else:
            print("enter within 1 to 4")

     except :
        print("u have got an error try again")
     finally:
         loop=0

#3.

a = 5
b = "abracadabra"
try:
    print(a+b)
except NameError:
    print("Error occured")
except:
    print("Error")

#5
try:
    z = int(input("Enter input :"))
    print(z*2)
except:
    print("Error occured")
