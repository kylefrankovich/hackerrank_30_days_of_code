# notes for random coding challenges




format(1, '32b')

'{0:032b}'.format(1)

'{0:032b}'.format(3)


def int2bin(int):
    return '{0:032b}'.format(int)

binary_1 = int2bin(1)

int2bin(65)

isinstance(binary_1,str)

def bin2int(binary):
    return int(binary, 32)

bin2int(int2bin(2147483647))

flipped_1 = '11111111111111111111111111111110'

bin2int(flipped_1)

def flipBinary(binary):
    for i in len(binary):
        if binary[i] == 0:
            binary[i] = 1
        elif binary[i] == 1:
            binary[i] = 0
        return binary


test = flipBinary(binary_1)

print(test)

binary_1[30]

len(binary_1)

int(binary_1)


format(4, 'b')

string = '00001'

len(string)

for e in len(string):
    if string[e] == '0':
        string[e] = '1'
    elif string[e] == '1':
        string[e] = '0'



for e in range(len(string)):
    print string[e]



b = '{:0{width}b}'.format(2, width=32)
int(b[::-1], 2)


# solution to 'flipping bits'
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(raw_input())):
    N = int(raw_input())
    N = N & 0xffffffff # 32 bit representation
    print N ^ 0xffffffff

N = int('1')
N = N & 0xffffffff  # 32 bit representation
print N ^ 0xffffffff


print 1,2



# class vs. instance:

age = 34

if age >= 13 and age < 18:
    print 'You are a teenager.'




class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print 'Age is not valid, setting age to 0.'
            age = 0
        else:
            age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print 'You are young.'
        elif age >= 13 and age < 18:
            print 'You are a teenager.'
        else:
            print 'You are old.'
    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age = age + 1


t = int(raw_input())
for i in range(0, t):
    age = int(raw_input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")



# loops:

for i in range(1,11):
    answer = 2 * i
    print '2 X %d = %d' % (i, answer)




