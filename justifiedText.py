def justify(A,L):
    i,n = 0,len(A)
    arr = []
    while i<n:
        j = i
        tempLen = 0
        #count how many words we can accomodate in current line
        while j < n and tempLen+len(A[j]) <= L:
            tempLen += len(A[j])+1
            j += 1

        #total Words in current Line
        wordCount = j-i
        #Gap between words
        totgap = wordCount-1
        #total remaining spaces, that we need to distribute, length of line - (totalCountedLength-wordCount)
        #as after each word we have counted 1 extra space
        totSpaces = L-(tempLen-wordCount)
      
        #ideally space between words should be 1, with no extra spaces to accomodate between words
        actualSpace,remainder = 1,0

        #If this is not the last line and line contains more than 1 word
        if j<n and totgap!=0:
            actualSpace,remainder = totSpaces/totgap,totSpaces%totgap
        string = ""

        #initialize the counter with first word of line
        z = i
        #print "WordCount:",wordCount,"tempLen:",tempLen,"totgap:",totgap,"totSpaces:",totSpaces,"actualSpace:",actualSpace,"Remainder:",remainder
        while z<j:
            string += A[z]
            wordCount -= 1
            #While there is still next word remaining
            if wordCount:
                #Add division component of totalSpace + 1 extra space from the remainder quota if there are any
                string += " "*(actualSpace+(1 if remainder>0 else 0))
                remainder -= 1
            z += 1

        #if this is the last line or the line contains only 1 word, then it should be left justified
        if j == n or totgap==0:
            string += " "*(L-len(string))
            
        print string,len(string)
        arr.append(string)
        i = j

    #print arr
    return arr

A = ["This", "is", "an", "example", "of", "text", "justification."]
justify(A,16)        

A = ["Utkarsh","Dwivedi","Shweta", "Mishra"]
justify(A,16)

A = [ "am", "fasgoprn", "lvqsrjylg", "rzuslwan", "xlaui", "tnzegzuzn", "kuiwdc", "fofjkkkm", "ssqjig", "tcmejefj", "uixgzm", "lyuxeaxsg", "iqiyip", "msv", "uurcazjc", "earsrvrq", "qlq", "lxrtzkjpg", "jkxymjus", "mvornwza", "zty", "q", "nsecqphjy" ]
justify(A,14)
