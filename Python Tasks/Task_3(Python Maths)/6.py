'''
Problem :

You are given a positive integer N. Print a numerical triangle of height N - 1 like the one below:

1
22
333
4444
55555
......

refer full qution : https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true

'''
#Solution

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(i * 10**i / 9))
