#IDEA
# Read a list and "compress" it, meaning that when the value of the list is the same character repeated, it will get shortened
# ['ssss'] >>> ['4s']

#LOGIC
# The compression can only happen when the starting character is same as every other character in the list
# Meaning that ['rrrr'] >>> ['4r']; ['0'] >>> ['10']; ['hrrrrrr'] >>> ['hrrrrrr']

# THIS WAS AN EXAM FROM SCHOOL

def compressList(arr):
    return_value = []
    for inner in arr:

        isSame = True
        last_value = None
        number_of_occurences = 0

        for value in inner:
            if last_value:
                if value == last_value: 
                    number_of_occurences += 1
                else:
                    isSame = False
            else:
                last_value = value
                number_of_occurences += 1
        if isSame:
            return_value.append(f'{number_of_occurences}{last_value}')
        else:
            return_value.append(inner)

    return return_value
            