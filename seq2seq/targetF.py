f = open('padding.txt','r').readlines()
writein = open('tpadding.txt','w')

for line in f:
    str_ = ''
    for i in range(len(line)-1,-1,-1):
        str_ += line[i]
    writein.write(str_)



#fileD = write.readlines()


    


