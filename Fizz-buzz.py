
# coding: utf-8

# In[5]:


# Fizz-buzz for 1-100 using Python3

for i in list(range(100)):
    if i%3==0 and i%5!=0:
        print(i, " Fizz")
    elif i%5==0 and i%3!=0:
        print(i, " Buzz")
    elif i%3==0 and i%5==0:
        print(i, " Fizz-Buzz")
    else:
        print(i)

