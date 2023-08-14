'''
6. Write a function to compress a stream of characters.
    AAAAAAAABBBBBCCCCCCDDD1111111111DDDDD3333333333DDDEEEEEEFF
    a) Currently the string takes n chars to store. Target is to store it using less than
    n chars.
    b) Is there any case where instead of compression, expansion will take place?
'''
def compress(s):
    if not s:
        return s
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1])
            result.append(str(count))
            count = 1
    result.append(s[-1])
    result.append(str(count))
    return ''.join(result)

s = "AAAAAAAABBBBBCCCCCCDDD1111111111DDDDD3333333333DDDEEEEEEFF"
print(compress(s))
