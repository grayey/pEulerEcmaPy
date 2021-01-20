#Iterative: Solution 1

def even_fibonacci_numbers():
    counter = 0;
    first = 0;
    second = 1;
    temp = 0;
    evenSum = 0;

    while first < (4 * 10**6):
        if not (first%2):
            evenSum+=first
        temp = first + second
        first = second
        second = temp
        counter += 1
    return evenSum

# print(even_fibonacci_numbers())



#Phi golden ratio: Solution 2
def even_by_phi_ratio():
    pass


