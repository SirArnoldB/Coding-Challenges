'''
Atoi() function that:
    # discards all leading whitespaces 
    # sign of the number 
    # overflow
    # invalid input

'''

# Python 3 program for the implementation of atoi
import sys

def myAtoi(Str):

    sign, base, i = 1, 0, 0
    
    # If whitespaces then ignore.
    while (Str[i] == ' '):
        i += 1
    
    # Sign of number
    if (Str[i] == '-' or Str[i] == '+'):
        sign = 1 - 2 * (Str[i] == '-')
        i += 1

    # Checking for valid input
    while (i < len(Str) and
        Str[i] >= '0' and Str[i] <= '9'):
            
        # Handling overflow test case
        # print(sys.maxsize//10) returns 922337203685477580
        # print(sys.maxsize)     returns 9223372036854775807
        if (base > (sys.maxsize // 10) or (base == (sys.maxsize // 10) and (Str[i] - '0') > 7)):
            if (sign == 1):
                return sys.maxsize
            else:
                return -(sys.maxsize)
        
        base = 10 * base + (ord(Str[i]) - ord('0'))
        i += 1
    
    return base * sign

# Driver Code
Str = list(" -123")

# Functional Code
val = myAtoi(Str)

print(val)