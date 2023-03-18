'''module contains the function f_to_c that convert F degree into
C degree
'''

def f_to_c(f):
    ''' return the C degree that is equivalent to the F degree 
    '''
    return (f-32)*5/9

def main():
    for i in range(0, 101, 10):
        c = f_to_c(i)
        print(i, "F = ", c, "C")

main()
