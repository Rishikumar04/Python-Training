def calculator():
    
    '''To perform simple multiplication, division, subtraction, addition'''
    operation=input('Which operation to perform multiplication or division or subtraction or addition:')
    if operation.lower()=='addition':
        x= int(input('First number: '))
        y= int(input('Second number: '))
        return(x+y)
    elif operation.lower()=='subtraction':
        x= int(input('First number: '))
        y= int(input('Second number: '))
        return (x-y)
    elif operation.lower()=='multiplication':
        x= int(input('First number: '))
        y= int(input('Second number: '))
        return (x*y)
    elif operation.lower()=='division':
        x= int(input('First number: '))
        y= int(input('Second number: '))
        return (x/y)
    else:
        return ("Wrong operation, Type the correct operation")
               
               
               
def simple_sum(*x):
    '''To perform simple sum operation'''
    return (sum(x))
              
def multiplicator(x,y):
    '''To perform simple multiply operation'''
    return (x*y)

def average(*x):
    '''To find average '''
               
    return(sum(x)/len(x))
              
               
def modulo(x,y):
   ''' To find quotient of number'''
   return (x%y)
               
def subtractor(x,y):
   '''Subtract two number'''
   return (x-y)
               
def floor_division(x,y):
   ''' Execute floor division'''
   return (x//y)
               
               
    
