#Herons Formula
import math

#returns the square root of the number n
def root(n):
    root = math.sqrt(n)
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a,b,c):
    perimeter = (a+b+c)/2
    return perimeter
    pass


def multiplyDifferences(dif,a,b,c):
    dif = dif*(dif-a)*(dif-b)*(dif-c)
    return dif

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    inside = multiplyDifferences(s, a, b, c)# dif = s
    heron = root(inside)
    return heron
    pass


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(w):
    denominator = w*2
    return denominator
    pass

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(d,e):
    minus = d*-1
    add = minus + e
    subtract = minus - e
    return add, subtract
    pass
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    squared = b**2 - (4*a*c)
    return squared
    pass

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    x = mainCalc(a,b,c)
    x = root(x)
    x,y = plusMinus(b,x)
    denom = denominator(a)
    x = x/denom
    y = y/denom
    return (x,y)
    pass
