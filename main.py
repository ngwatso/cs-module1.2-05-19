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

256 ==>  100000000
output = 000000001

932 ==>  1101000000
output = 0000001011

622 ==>  1001101110
output = 0111011001

P:

convert integer to binary, convert to string and reverse, convert back to integer

'''

# ===============

def csBinaryToASCII(binary):

    counter = 0
    newStr = ""
    
    while counter < len(binary):
        x = binary[counter:counter+8]
        l = int(x, 2)
        newStr += chr(l)
        counter += 8
        
    return newStr


'''

U:

"011011000110000101101101011000100110010001100001"
output = "lambda"

iterate through binary, slice out the first 8-bit binary, convert to letter, push to newStr.  Increment slice by 8, continue.

'''

# ===============

def csRaindrops(number):
    
    newStr = ""
    arr = [3, 5, 7]
    arr_2 = ["Pling", "Plang", "Plong"]
    
    for i in range(len(arr)):
        if number % arr[i] == 0:
            newStr += arr_2[i]
    
    if newStr == "":
        return str(number)
    else:
        return newStr

'''

U:

28 
output = "Plong"

30
output = "PlingPlang"

'''