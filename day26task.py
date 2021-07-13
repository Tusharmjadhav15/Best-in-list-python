#--------------------------------------------------------------------------------------------------------------------------------------------------------
#enumerate a python list and try to print the counter with the list value

lst = ["eat","sleep","bath","comb","hen","horse"]

obj1 = enumerate(lst)

print("Return type:",type(obj1))
print(list(enumerate(lst)))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#enumerate a python tuple and try to print thecounter with the tuple value
tup = ("ring","doll","cat","dog","bike","tiger","dragon")
dfg = tuple(tup)
for w in enumerate(dfg):
    print(w)
