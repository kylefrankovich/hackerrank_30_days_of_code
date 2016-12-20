# notes for random coding challenges




format(1, '32b')

'{0:032b}'.format(1)

'{0:032b}'.format(3)


def int2bin(int):
    return '{0:032b}'.format(int)

binary_1 = int2bin(1)

len(binary_1)

range(0,len(binary_1))

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


# day 9 (recursion):

# Task:

# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

# Input:

# A single integer,  (the argument to pass to factorial).

n = int(raw_input())

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print factorial(n)


# day 10 (binary numbers):

'''

Task:

Given a base- integer, , convert it to binary (base-). Then find and print the base- integer
denoting the maximum number of consecutive 's in 's binary representation.'''

import sys


n = int(raw_input().strip())

# n = int(raw_input())

def int2bin(int):
    return '{0:032b}'.format(int)

binary_1 = int2bin(n)

binary_1 = int2bin(439)


current = 0
longest = 0
for i in binary_1:
    if i == '1':
        current += 1
    else:
        longest = max(longest, current)
        current = 0

print max(current, longest)


# one-liner solution (python 3):

print(len(max(bin(int(input().strip()))[2:].split('0'))))

print(len(max(bin(int('13'.strip()))[2:].split('0'))))

'''Python3: for those that don't understand the one liner print(len(max(bin(int(input().strip()))[2:].split('0'))))

for sake of explanation im going to replace input() with '13' and break the code down.

1- int(input().strip()) ==> int('13'.strip()) takes the input of the number and strips
any spaces on either side, then converts it from a string to an interger. the result is the interger 13.

2- bin(13)[2:].split('0') ==> the bin() method takes a number and converts it to binary. in this case when
you enter bin(13) it returns '0b1101'. the [2:] allows us to omit the '0b' at the beginning of the string.
which leaves us with '1101'.split('0'). This string method takes '1101' and splits it into a list.
We end up with ['11','1'].

3-len(max(['11','1'])) ==> the max() method is simply going to look for the biggest value. In this case the
biggest one is '11'. '11' is passed to the len() method which just returns the length of the object in it.
In this case the object is the string '11' which has two characters, so len('11') returns 2. Which in turn is
also the longest consecutive amount of ones.'''



# day 11 (2D arrays)

# Context/Task:

'''Given a 6x6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling
in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task:

Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D
Array A; every value in A will be in the inclusive range of -9 to 9.

Output Format

Print the largest (maximum) hourglass sum found in A.
'''

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

list1 = [1, 1, 1]
list2 = [1]
list3 = [1, 1, 1]

# row 1:

print '\nrow 1, col 1:\n'
print arr[0][0:3]
print [arr[1][1]]
print arr[2][0:3]
print 'hourglass one sum:', sum(arr[0][0:3]) + sum([arr[1][1]]) + sum(arr[2][0:3])

print '\nrow 1, col 2:\n'
print arr[0][1:4]
print [arr[1][2]]
print arr[2][1:4]
print 'hourglass two sum:', sum(arr[0][1:4]) + sum([arr[1][2]]) + sum(arr[2][1:4])

print '\nrow 1, col 3:\n'
print arr[0][2:5]
print [arr[1][3]]
print arr[2][2:5]
print 'hourglass three sum:', sum(arr[0][2:5]) + sum([arr[1][3]]) + sum(arr[2][2:5])

print '\nrow 1, col 4:\n'
print arr[0][3:6]
print [arr[1][4]]
print arr[2][3:6]
print 'hourglass four sum:', sum(arr[0][3:6]) + sum([arr[1][4]]) + sum(arr[2][3:6])


# row 2

print '\nrow 2, col 1:\n'
print arr[1][0:3]
print [arr[2][1]]
print arr[3][0:3]
print 'hourglass 5 sum:', sum(arr[1][0:3]) + sum([arr[2][1]]) + sum(arr[3][0:3])

print '\nrow 2, col 2:\n'
print arr[1][1:4]
print [arr[2][2]]
print arr[3][1:4]
print 'hourglass 6 sum:', sum(arr[1][1:4]) + sum([arr[2][2]]) + sum(arr[3][1:4])

print '\nrow 2, col 3:\n'
print arr[1][2:5]
print [arr[2][3]]
print arr[3][2:5]
print 'hourglass 7 sum:', sum(arr[1][2:5]) + sum([arr[2][3]]) + sum(arr[3][2:5])

print '\nrow 2, col 4:\n'
print arr[1][3:6]
print [arr[2][4]]
print arr[3][3:6]
print 'hourglass 8 sum:', sum(arr[1][3:6]) + sum([arr[2][4]]) + sum(arr[3][3:6])



# row 3

print '\nrow 3, col 1:\n'
print arr[2][0:3]
print [arr[3][1]]
print arr[4][0:3]
print 'hourglass 9 sum:', sum(arr[2][0:3]) + sum([arr[3][1]]) + sum(arr[4][0:3])

print '\nrow 3, col 2:\n'
print arr[2][1:4]
print [arr[3][2]]
print arr[4][1:4]
print 'hourglass 10 sum:', sum(arr[2][1:4]) + sum([arr[3][2]]) + sum(arr[4][1:4])

print '\nrow 3, col 3:\n'
print arr[2][2:5]
print [arr[3][3]]
print arr[4][2:5]
print 'hourglass 11 sum:', sum(arr[2][2:5]) + sum([arr[3][3]]) + sum(arr[4][2:5])

print '\nrow 3, col 4:\n'
print arr[2][3:6]
print [arr[3][4]]
print arr[4][3:6]
print 'hourglass 12 sum:', sum(arr[2][3:6]) + sum([arr[3][4]]) + sum(arr[4][3:6])


# row 4

print '\nrow 4, col 1:\n'
print arr[3][0:3]
print [arr[4][1]]
print arr[5][0:3]
print 'hourglass 13 sum:', sum(arr[3][0:3]) + sum([arr[4][1]]) + sum(arr[5][0:3])

print '\nrow 4, col 2:\n'
print arr[3][1:4]
print [arr[4][2]]
print arr[5][1:4]
print 'hourglass 14 sum:', sum(arr[3][1:4]) + sum([arr[4][2]]) + sum(arr[5][1:4])

print '\nrow 4, col 3:\n'
print arr[3][2:5]
print [arr[4][3]]
print arr[5][2:5]
print 'hourglass 15 sum:', sum(arr[3][2:5]) + sum([arr[4][3]]) + sum(arr[5][2:5])

print '\nrow 4, col 4:\n'
print arr[3][3:6]
print [arr[4][4]]
print arr[5][3:6]
print 'hourglass 16 sum:', sum(arr[3][3:6]) + sum([arr[4][4]]) + sum(arr[5][3:6])


total = sum(list1) + sum(list2) + sum(list3)


num_row_shifts = 4
current_highest = 0
for i in range(0,num_row_shifts):
    col1_sum = sum(arr[0+i][0:3]) + sum([arr[1+i][1]]) + sum(arr[2+i][0:3])
    col2_sum = sum(arr[0+i][1:4]) + sum([arr[1+i][2]]) + sum(arr[2+i][1:4])
    col3_sum = sum(arr[0+i][2:5]) + sum([arr[1+i][3]]) + sum(arr[2+i][2:5])
    col4_sum = sum(arr[0+i][3:6]) + sum([arr[1+i][4]]) + sum(arr[2+i][3:6])

    current_highest = max(col1_sum,col2_sum,col3_sum,col4_sum)

    if i == 0: # need this step to deal with negative values
        highest_sum = current_highest

    highest_sum = max(highest_sum,current_highest)

print highest_sum


failed_input = [[-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]]



arr = failed_input

# from discussion:

res = []

for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)

print(max(res))

# and:

int maxsum=-64;  # she used this value, as explained here:
'''Since there are 7 elements that make up the hourglass shape, and the
minimum value for each element is -9, we take 7*-9, or -63, as the minimum
value possible for each hourglass.'''
int hoursum;
for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
        hoursum=arr[i+1][j+1];
        for(int k=0;k<3;k++){
            hoursum = hoursum + arr[i][j+k] + arr[i+2][j+k];
        }
        if(hoursum > maxsum)
         maxsum = hoursum;
    }
}
printf("%d",maxsum);


# day 12 (Inheritance):

