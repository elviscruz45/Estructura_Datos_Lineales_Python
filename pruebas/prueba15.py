def fibonacy(num):
    if num==1 or num==0:
        return 1
    else:
        return fibonacy(num-1)+fibonacy(num-2)


print(fibonacy(10))