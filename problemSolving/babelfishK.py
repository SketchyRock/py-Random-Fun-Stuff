dictionary = {}

while True:
    input1 = input()
    if(input1 == ""):
        break
    temp_list = input1.split()
    dictionary[temp_list[1]] = temp_list[0]

try:
    while True:
        word = input()
        print(dictionary.get(word, "eh"))
except EOFError:
    pass
