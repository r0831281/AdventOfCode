examples = []



with open('input.txt', 'r') as f:
    for line in f:
        examples.append(line.strip())

    print(examples)     
        


def solve(examples):
    out = []
    final = 0
    for example in examples:
        data = []
        for char in example:
            if char.isdigit():
                integer = int(char)
                data.append(integer)   
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
                        lookiehere = int(str(dit)[0] + str(dit)[0])
                        out.append(lookiehere)
                        print("very special case" + str(lookiehere) )
                    else:
                        out.append(dit)
    print(out)
    final = sum(out)
    return final

print(solve(examples))
                       
    
