import pathlib,os,sys,glob,re,zlib


def fileope():
    with open("Pythontext.txt",'r') as file:
        words={}
        for line in file:
            for word in line.split(" "):
                patt=re.compile(r"[^a-zA-Z0-9\s]")
                word=str(re.sub(patt,"",word))
                if word in words:
                    words[word]+=1
                else:
                    words[word]=1
        file.close()
        return words
#print(fileope())

def makstring():
    wordlist=fileope()
    string="".join(wordlist)
    return string

def calculate_upper_lower_ch_cnt():
    string=makstring()
    u_l_cnt={"upper":0,"Lower":0,"Digit":0}
    for line in string:
        for ch in line:
            if ch.isupper():
                u_l_cnt["upper"]+=1
            elif ch.islower():
                u_l_cnt["Lower"]+=1
            elif ch.isdigit():
                u_l_cnt["Digit"]+=1
    return u_l_cnt
#print(calculate_upper_lower_ch_cnt())


with open("Pythontext_write.txt",'w') as file:
    file.write(makstring())
    file.close()
        

