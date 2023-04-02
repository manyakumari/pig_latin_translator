def piglatintranslator():

    normword = str(input("Enter a word to translate: "))
    begconsec = ""
    remainword = []
    lennormword = len(normword)
    pigword = "0"
    index = 0
    for i in range(lennormword):
        if normword[0] == "a" or normword[0] == "e" or normword[0] == "i" or normword[0] == "o" or normword[0] == "u":
            remainword.append(normword)
            remainword.append("way")
            pigword = "".join(remainword)
            print(pigword)
            break

        elif normword[index] == "a" or normword[index] == "e" or normword[index] == "i" or normword[index] == "o" or normword[index] == "u":
            remainword.append(normword[index:])
            begconsec = "".join(begconsec)
            remainword.append(begconsec)
            remainword.append("ay")
           # remainword = str(remainword)
            pigword = "".join(remainword)
            print(pigword)
            break        
        else:
          #  begconsec.append(normword[index])
            begconsec = begconsec, normword[index]
        index = index+1
    
    if pigword == "0":
        begconsec = "".join(begconsec)
        remainword.append(begconsec)
        remainword.append("ay")
       # remainword = str(remainword)
        pigword = "".join(remainword)
        print(pigword)

piglatintranslator()

            
            
            



        


