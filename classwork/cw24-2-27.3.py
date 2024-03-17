def munny(li):
    ma = mi = li[0]
    for i in range(len(li)):
        if li[i] < mi:
            mi = li[i]
        elif li[i] > ma:
            ma = li[i]
    return(ma - mi)

stocks = [8,10,7,5,7,15]
print(munny(stocks))