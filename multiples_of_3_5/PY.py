

def multiples_of_3_and_5():

    sum_of_mulitples = 0;
    for i in range(1000):
        if not (i%3) or not (i%5):
            sum_of_mulitples+=i;
    return sum_of_mulitples;


print(multiples_of_3_and_5())


