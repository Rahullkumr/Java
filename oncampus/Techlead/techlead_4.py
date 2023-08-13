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
    
    # Iterate through the string and process each character
    for char in s:
        if char == '(':
            stack.append('(')
            result.append('(')
        elif char == ')':
            if stack:
                stack.pop()
                result.append(')')
        else:
            result.append(char)
    
    # Remove any remaining unmatched opening parentheses
    for char in stack:
        result.remove('(')
    
    return ''.join(result)

# Example usage
input_string = "()())()"
output_string = remove_invalid_parentheses(input_string)
print("Input:", input_string)
print("Output:", output_string)
