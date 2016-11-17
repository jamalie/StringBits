#   codingbat code practice
#   Given a string, return a new string made of every other char starting with the first,
#   so "Hello" yields "Hlo".

#string_bits('Hello') -> 'Hlo'
#string_bits('Hi') -> 'H'
#string_bits('Heeololeo') -> 'Hello'

def string_bits(str):
    if len(str)<=1:
        return str
    else:
        result = ""
        x = 0
        while x < len(str):
            result += str[x]
            x+=2
        return result

print string_bits('Hello')
print string_bits('Hi')
print string_bits('Heeololeo')
