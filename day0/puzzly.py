import re
examples = []

#when parsing ther numbers first when theres only two numbers and one is from text, the numbers are in the wrong order, maybe 
#keep pos of number as string and when the pos is after where the text number is found insert the text number in front of it

with open('input.txt', 'r') as f:
    for line in f:
        examples.append(line.strip())
   
        

def find_written_numbers(text):
    # Dictionary mapping written numbers to numeric values
    word_to_num = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
    }

    # Sort the dictionary by the length of the keys in descending order
    sorted_word_to_num = dict(sorted(word_to_num.items(), key=lambda x: len(x[0]), reverse=True))

    # Initialize an empty list to store the numeric values
    numeric_values = []

    # Iterate over the sorted keys and find matches in the input text
    for word in sorted_word_to_num.keys():
        start = 0
        while True:
            match_start = text.lower().find(word, start)
            if match_start == -1:
                break

            match_end = match_start + len(word)
            numeric_values.append((word, sorted_word_to_num[word], match_start, match_end))
            start = match_end

    # Sort the results based on the starting index of each match
    numeric_values.sort(key=lambda x: x[2])

    return numeric_values

def solve(examples):
    out = []
    final = 0
    for example in examples:
        data = []
        rest = []
        for char in example:
            if char.isdigit():
                integer = int(char)
                data.append(integer)
            else:
                rest.append(char)
                
        rest = "".join(rest)
        print(rest)
        extra_number = find_written_numbers(rest)
        print(extra_number)
        print(data)
        for number in extra_number:
            data.append(number[1])
        print(data)

        match len(data):
                case (0):
                    print("invalid input")
                case 1: #double
                    out.append(int(str(data[0]) + str(data[0])))
                case 2:
                    out.append(int(str(data[0]) + str(data[1])))
                case _ if len(data) >2:
                    dit = 0
                    for d in data:
                        try:
                            dit += d
                        except:
                            print("error")
                    if dit < 10:
                        loe = int(str(dit)[0] + str(dit)[0])
                        out.append(loe)
                    else:
                        out.append(dit)
    print(out)
    final = sum(out)
    return final

print(solve(examples))
                       
    
