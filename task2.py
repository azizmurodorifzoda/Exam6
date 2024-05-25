import random
my_list=[]
for i in range(100):
    a=random.randrange(10**9, 10**10)
    my_list.append(a)
m=random.sample(my_list)
print(m)
