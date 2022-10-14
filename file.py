#Dario Maddaloni (233187)

# I will work with the inverse shuffling and try to rewind the procedure

# n identify the element in the n-th position after the k-th shuffle
# invert compute the position of the element in the n-th position before the k-th shuffle
def invert(m,k):
    if m >= 2*k: # means that his position wasn't changed in the k-th shuffle 
        return m
    else:
        if m%2==1: # means that his position now is even, so before was in the first part
            return int(m/2)
        else:
            return int((m/2)+k) # means that his position now is odd, so before was in the "center". Notice alse that this number will never be outside our list

def complete_shuffle(k): # k is the number of shuffle we should apply
    n=2*k # n=2k and is the number of element of our list: [1,..n] 
    
    a=invert(0,k) # a will identify the position in our list of the element that at the and of the all k shuffling is on the topmost position
    b=invert(1,k) # b will identify the position in our list of the element that at the and of the all k shuffling is on the topmost-1 position
    c=invert(2,k) # c will identify the position in our list of the element that at the and of the all k shuffling is on the topmost-2 position
    
    s=k # Until now, we know only that at the end of the shuffling the element is at the position 0
    f=1 # We are sure that at the end the topmost element is at the topmost position
    
    for i in range(k-1): # notice that the variable i will be used as the ((k-1)-i)-th shuffle
        
        a=invert(a,k-1-i)
        b=invert(b,k-1-i)
        c=invert(c,k-1-i)
               
        if a==0: # this update the s if the element that was at the topmost is in the position 0, as the f
            s=k-1-i #
            f+=1
        # if this won't be updated, means that s was the first time looking in the right way of the shuffling
            
    # Until now I weren't working with the element of the list 
    l_1=a+1 # Now we now which element we were interested in. Because we assumed that the elements were ordered 
    l_2=b+1 # Now we now which element we were interested in. Because we assumed that the elements were ordered
    l_3=c+1 # Now we now which element we were interested in. Because we assumed that the elements were ordered
    s    
    return [l_1,l_2,l_3],s-1,f # I have to return s-1 instead of s, because I have to count from 0 that is the starting point