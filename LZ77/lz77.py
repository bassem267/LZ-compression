# Bassem Mohamed Hassan 
# 20200112
#s.elabyad@fci-cu.edu.eg

import math

def lz77(bla):
    length = len(bla)
    search_Buffer = ""
    search_Buffer_len = 0
    look_ahead = length
    
    for x in range(look_ahead):
        if bla[x] in search_Buffer:
            for y in range(look_ahead):
                if bla[search_Buffer_len:bla-y] in search_Buffer:
                    fnd = bla[search_Buffer_len:look_ahead-y]
                    
                    next_symbol = bla[look_ahead - y -1]
                    
                    leng = str(look_ahead - y - search_Buffer_len)
                    
                    print("<" +  + leng + "," + next_symbol + ">")
                    
                    search_Buffer += fnd + next_symbol
                    
                    search_Buffer_len = look_ahead - y + 1
                    
                    look_ahead = length - search_Buffer_len
                    
        else:
            print("<0,0," + bla[x] + ">")
            search_Buffer+= bla[x]
            search_Buffer_len = search_Buffer_len + 1
            look_ahead -= 1
            
    



# The Example in Lec    
lz77("ABAABABAABBBBBBBBBBBBA")


