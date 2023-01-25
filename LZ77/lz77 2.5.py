# Basssem Mohamed Hassan 
# 20200112


def encode(text, SIZE):
    counter = 0
    length = 0
    result = []
    look_ahead = text
    compressed = ""
    list = []
    search_window = ""
    dif = 0
    
    for x in range(len(look_ahead)):
        search_window = search_window + look_ahead[0]
        
        if len(compressed) > SIZE and SIZE != 0:
            dif = dif + len(compressed) - SIZE
            compressed = compressed[len(compressed) - SIZE:]
            length = 0
            
        if search_window not in compressed:
            if counter > 7 and length == 1:
                counter = 0
                length = 0
            result.append("<{},{},{}>".format(counter, length, look_ahead[0]))
            compressed = compressed + search_window
            look_ahead = look_ahead[1:]
            search_window = ""
            list.clear()
            length = 0
            
        else:
            if (x == len(text) - 1):
                if counter > 7 and length == 1:
                    counter = 0
                    length = 0
                result.append("<{},{},{}>".format(counter, length, look_ahead[0]))
                break
            
            else:
                look_ahead = look_ahead[1:]
            list.append(x)
            
            if(SIZE != 0):
                counter = list[0] - text.index(search_window, dif, size + dif)
            else:
                counter = list[0] - text.index(search_window)
            length = length + 1
            continue
        
    return result

# main Program
print("Enter your text to encode:")
text = input()
print("specified size assigned for the search window and look ahead buffer window ?")
print("Choose 1 for yes or choose 2 for no")

option = input()

if (option == "1"):
    print("Enter window size:")
    size = input()
else:
    size = 0


result = encode(text, size)
print(result)