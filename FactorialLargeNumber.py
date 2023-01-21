"""
https://www.geeksforgeeks.org/factorial-large-number/

"""


def factorial(N):
    result = 1
    for x in range(2, N + 1):
        result *= x
    return result


print("Factorial of a number is : ", factorial(10))


def factorialRecursive(N):
    def fact(N):
        if N == 1:
            return 1
        return N * fact(N - 1)

    return fact(N)


print("Factorial of a number in Recursive way : ", factorialRecursive(11))


def factorialDynamic(N):
    memory = [0] * (N + 1)
    memory[0] = 1
    for x in range(1, N + 1 ):
        memory[x] = x * memory[x - 1]
    return memory[N]


print("Factorial of a number in Dynamic Prog. way : ", factorialRecursive(110))