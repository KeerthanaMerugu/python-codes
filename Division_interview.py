def quotient(divisor, dividend):
    count=1
    while(dividend-divisor)>=divisor:
        r=dividend-divisor
        dividend=r
        count=count+1
    return count





divisor=5;dividend=100
result=quotient(divisor, dividend)
print(result)