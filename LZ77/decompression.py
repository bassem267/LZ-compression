class TAG(object):
    def __init__(self, counter, length, nextChar):
        self.counter = counter
        self.length = length
        self.nextChar = nextChar
def decomp(tagss):
    myResultString=""
    for i in range(len(tagss)):
        if tagss[i].counter==0:
            myResultString=myResultString+tagss[i].nextChar
        else:
            myResultString=myResultString+myResultString[len(myResultString)-tagss[i].counter:len(myResultString)-tagss[i].counter+tagss[i].length]+tagss[i].nextChar
    return myResultString

while true:
    print("\n\n------------------------")
    print("Welcome to LW77 Decompression Program")
    print("------------------------")
    tags=[]
    print("enter nums of tags")
    num=int(input())
    for i in range(num):
       print("enter counter of tag {}".format(i+1))
       c=int(input())
       print("enter length of tag {}".format(i+1))
       l=int(input())
       print("enter next Char of tag {}".format(i+1))
       n=str(input())
       myObj=TAG(c,l,n)
       tags.append(myObj)
    result=decomp(tags)
    print(result)
