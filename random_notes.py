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










# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
test = n.split(
test2 = []
for i in test:
    test2.append(float(i))


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

sample_mean = mean(test2)

from math import sqrt

def stddev(lst):
    mn = mean(lst)
    variance = sum([(e-mn)**2 for e in lst]) / len(lst)
    return sqrt(variance)

sample_std_dev = stddev(test2)

normalized_pts = []
for i in test2:
    normalized_pts.append((i/sample_mean)/sample_std_dev)
print normalized_pts



# loops:

for i in range(1,11):
    answer = 2 * i
    print '2 X %d = %d' % (i, answer)


# day 6 review (strings, loops):

'''Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated
strings on a single line (see the Sample below for more detail).'''



t = int(raw_input())

for i in range(0, t):
    string = raw_input()
    oddStringValues = ''
    evenStringValues = ''
    for j in range(len(string)):
        if j%2 == 0:
            evenStringValues += string[j]
        elif j%2 ==1:
            oddStringValues += string[j]
    print evenStringValues, oddStringValues


# day 7 (arrays):

#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

# test array:

arr = [1,2,3,4]

#print n
#print arr
#print isinstance(arr[0], int)

arr.reverse()

#print arr

for item in arr:
    print item,

# one liner solution:

print(" ".join(map(str, arr[::-1])))

# or:

print(''.join(map(str, reversed(arr))))

# or:

from __future__ import print_function

print(*reversed(arr)) # the '*' is from 3;

# or:

print(*arr[::-1])


print(*['a','b','c'])


# day 8 (dictionaries and maps):

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())

# print 'n:', n

# arr = raw_input().strip().split(' ')

# print arr[1]

import fileinput

count = 0
phoneBook = {}

for line in fileinput.input():
    count += 1
    if count <= n:  # add first n number of phone book entries:
        # print line.strip().split(' ')[0]
        phoneBook[line.strip().split(' ')[0]] = line.strip().split(' ')[1]
    if count > n:
        # print line.strip()
        if line.strip() in phoneBook:
            output = line.strip(), '=', phoneBook[line.strip()]
            print
            ''.join(output)
        else:
            print('Not found')

# print phoneBook
