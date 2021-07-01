# function to verify a prime number. 1 is not consider a prime number
def IsPrime(number):
    div = 0
    for i in range(1, number+1):
        if number % i == 0 and number != 1:
            div += 1
    if div == 2:
        return True
    return False


for i in range(1, 101):
    # test if a number is prime.
    test = IsPrime(i)
    if test is True:
        print("Prime!")
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    if i % 3 == 0:  # Some numbers that are multiples of 3 are prime too
        print("Fizz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    print(i)
