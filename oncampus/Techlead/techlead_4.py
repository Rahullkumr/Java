'''
4. Remove invalid parentheses.
    Given a string S that contains parentheses and letters, remove the minimum number
    of invalid parentheses to make the input string valid.
    Ex: Input = "()())()"
    Output: "()()()"
'''
def remove_invalid_parentheses(s):
    stack = []
    result = []
    
    for char in s:
        if char == '(':
            stack.append(char)
            result.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                result.append(char)
        else:
            result.append(char)
    
    # Remove any remaining unmatched opening parentheses 
    # like in case of ()(((
    for char in stack:
        result.pop(-1)
    
    # joining the elements of the list: result into a string and returning the string
    return ''.join(result)

# Example usage
input_string = ")()()))((("
output_string = remove_invalid_parentheses(input_string)
print("Input:", input_string)
print("Output:", output_string)
