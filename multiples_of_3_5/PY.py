
def verify_nots(digit,args):
    isVerified = False;
    args = set(args);
    for arg in args:
        isVerified = isVerified or not (digit%arg);
    return isVerified;



def multiples(limit=1000, args=(3,5,)):
    sum_of_mulitples = 0;
    minimum = min(args);
    for i in range(minimum,limit):
        if verify_nots(i,args):
            sum_of_mulitples+=i;
    return sum_of_mulitples;


print(multiples())

