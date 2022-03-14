import random

total = 10
correct = 0
nums = range(1,11)
for _ in range(total):
    ops = random.choice("+-*/")
    a,b = random.choices(nums,k=2)

    # you only allow integer input - your division therefore is
    # limited to results that are integers - make sure that this
    # is the case here by rerolling a,b until they match
    while ops == "/" and (a%b != 0 or a<=b):
        a,b = random.choices(nums,k=2)

    # make sure not to go below 0 for -
    while ops == "-" and a<b:
        a,b = random.choices(nums,k=2)

    # as a formatted text 
    result = askNum("What is {a}+{ops}-{b} = ".format(a,ops,b))

    # calculate correct result
    corr = calc(a,ops,b)
    if  result == corr:
        correct += 1
        print("Correct")
    else:
        print("Wrong. Correct solution is: {} {} {} = {}".format(a,ops,b,corr))

print("You have {} out of {} correct.".format(correct,total))