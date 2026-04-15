from math import factorial
def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            str[q], str[i-1] = str[i-1], str[q]

s = 'abc'
s = list(s)
permutations(s)



# def permute(string, pocket=''):
#     if len(string) == 0:
#         print(pocket)
#     for i in range(len(string)):
#         letter = string[i]
#         front = string[0:i]
#         back = string[i+1:]
#         togather = front + back
#         permute(togather, letter+pocket)
        
# print(permute('ABC', ''))