# arrays 
myUniqueList = []
myLeftovers = []

# function where if the element is not in the array, append it to unique list and return true, else append to leftover list and return false
def allowAp (a, myUniqueList):
    if a not in myUniqueList:
        myUniqueList.append(a)
        return True
    else:
        myLeftovers.append (a)
        return False
        
# test list
myUniqueList = [2,3,4,5]

# testing a new string
st = 'hello'

allowAp(st, myUniqueList)
print(myUniqueList)
print(myLeftovers)

# testing repetition of string
allowAp(st, myUniqueList)
print(myUniqueList)
print(myLeftovers)

# testing if all the repetitions appear on leftover array
allowAp(st, myUniqueList)
print(myUniqueList)
print(myLeftovers)

# testing a new number 
number = 6
allowAp(number, myUniqueList)
print(myUniqueList)
print(myLeftovers)

# testing number repetition
number = 6
allowAp(number, myUniqueList)
print(myUniqueList)
print(myLeftovers)