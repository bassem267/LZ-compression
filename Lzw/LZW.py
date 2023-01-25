# Basssem Mohamed Hassan
# 20200112

import math

dictionary = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def lzwCompression(text):
    compressed = 0
    
    while compressed <= len(text):
        match = ""
        for x in range(compressed , len(text)):
            if text[compressed:x+1] in dictionary :
                match = text[compressed:x+1]
            else:
                pos = dictionary.index(match)
                compressed = x
                print(pos)
                add = match + text[x]
                dictionary.append(add)
                break
        
def lzwDecompression(tags):
    text = ""
    last = dictionary[tags[0]]
    text += last
    
    for tag in range(1 , len(tags)):
        if tag < len(dictionary):
            current = dictionary[tags[tag]]
            text += current
            add = last + current[0]
            dictionary.append(add)
            last = current
        else:
            current = last + last[0]
            text += current
            add = current
            dictionary.append(add)
            last = current
            
    return text
        
    
    
    
    
#main program
print("Choose 1 for Encode and 2 For Decode")
option = input()

if (option == "1"):
    print("Enter your text to encode:")
    # text = input()
    text = "ABAABABBAABAABAAAABABBBBBBBB"
    lzwCompression(text)
    
else:
    print("Enter your tags to decode and 0 when you finish")
    tags = []
    tag = int(input())
    while tag != 0:
        tags.append(tag)
        tag = int(input())
        tags.append(tag)
    
    result = lzwDecompression(tags)
    print(result)





