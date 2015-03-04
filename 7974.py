
# coding: utf-8

# In[ ]:

while 1:   
    a, b, c = [int(x) for x in raw_input().split()]   
    if a == 0 and b == 0 and c == 0:
        break
    elif b - a == c - b:
        print 'AP', c + (b - a)
    elif b/a == c/b:
        print 'GP', c * (b/a)
    else :
        print 'NP'


# In[ ]:



