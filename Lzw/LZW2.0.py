# Bassem Mohamed Hassan , Omar Salama Mostafa
# 20200112 , 20200344

dictionary = [' ', '!', '\"', "#", '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a',
              'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', 'DEL']  # 32:127


def lzw_compression(text):
    compressed = 0

    while compressed <= len(text):
        match = ""
        for x in range(compressed, len(text)):
            if text[compressed:x + 1] in dictionary:
                if x == len(text)-1:
                    print(dictionary.index(text[compressed:x + 1])+32)
                    return 0
                else:
                    match = text[compressed:x + 1]
            else:
                pos = dictionary.index(match)
                compressed = x
                print(pos+32)
                add = match + text[x]
                dictionary.append(add)
                break


def lzw_decompression(tags):
    text = ""
    last = dictionary[tags[0]-32]
    text += last

    for tag in range(1, len(tags)):
        if tags[tag]-32 < len(dictionary):
            current = dictionary[tags[tag]-32]
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
    print(text)


# main program
lzw_compression("ABAABABBAABAABAAAABABBBBBBBB")
lzw_decompression([65, 66, 65, 128, 128, 129, 131, 134, 130, 129, 66, 138, 139, 138])
