#Buble Sort
def bublesort(nlist):
    for passnum in range (len(nlist)-1,0,-1):
        for i in range (passnum):
            if nlist [i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i+1] = nlist[i+1]
                nlist[i+1] = temp
                
nlist=[14,46,43,27,57,41,45,21,70]
bublesort(nlist)
print(nlist)