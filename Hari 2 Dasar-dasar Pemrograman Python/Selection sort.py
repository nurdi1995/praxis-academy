#Selection Sort
source = [4,2,1,10,5,3,100]
for i in range (len(source)):
    mini = min(source[i:]) #find minimum element
    min_index = source[i:].index(mini)#find index of minimum element
    source[i+min_index] = source[i]#replace element at min_index with first element
    source[i] = mini  #replace first element with min element
print (source)
    