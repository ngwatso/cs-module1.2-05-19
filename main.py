def csReverseIntegerBits(n):
    
    newStr = '00000000000000000000000000000000'
    newInt = 0
    
    for i in range(len(newStr)):
        if n == 1:
            n = 0
            newStr = newStr[:-1] + '1'
            break
        if n >= 2**(32-i):
            n = n - 2**(32-i)
            newStr = newStr[:i-1] + '1' + newStr[i:]
        else:
            continue
    if n == 0:
        s = int(newStr)
    else:
        s = int(newStr)+1
            
    x = str(s)[::-1]
    
    l = len(x)
    
    for j in range(len(x)):
        if x[j] == "0":
            continue
        else:
            newInt += (2**(l-(j+1)))
            
    return newInt

'''

U:

256 ==> 100000000
output = 000000001

932 ==> 1101000000
output = 0000001011

622 ==> 1001101110
output = 0111011001

P:

convert integer to binary, convert to string and reverse, convert back to integer

'''