add=lambda x,y:x+y
some_list = range(1, 1000, 7)
new_List=list(map(lambda a:a*2,some_list))
itr = iter(new_List)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))