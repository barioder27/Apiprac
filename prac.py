# how to use the map function

def multi(a):
    return (a*a)

values = (1,2,3,4)

output = map(multi, values)


print(list(output))

word = '2,2526 5,8 7 9 2'
separated = word.split(',')
print(separated)


# swap case (convert uppercase to lower case in a string and vise versa)

def swap_case(word):
    return word.swapcase()

our_word = "This WORD Has To CHanGE"

result = swap_case(our_word)

print(result)

# split and join a string 

word ="This is our word"

word = word.split(" ")

joined = "-".join(word)

print("This is joined by -", joined)

joined2 = '@'.join(word)

print('This is joined by @', joined2)
