def evenlyDivides(x, y):
    return y % x == 0

def evenlyDivisibleElements(x, lst):
    divisors = []
    for element in lst:
        if evenlyDivides(element, x):
            divisors.append(element)
    return divisors

def evenlyDivisible(lst):
    for i in lst:
        divList = evenlyDivisibleElements(i,lst)
        print(i, "is evenly divisible by", str(divList).strip('[]'))

s = input("Please enter a list of ints separated by spaces: ")
lst = []
for x in s.split():
    lst.append(int(x))

evenlyDivisible(lst)