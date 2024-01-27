#slist = ['a', 'b', 'l', 'l', 'x', 'y', 'z']
slist = [1,1,2]
a = 0
b = 1
#while b < len(slist):
#    print(f"len is {len(slist)}")
#    print(f"slist b is [{slist[b]}]")
#    print(f"slist a is [{slist[a]}]")
#    if slist[a] == slist[b]:
#        print("Equal")
#        del slist[b]
#    else:
#        b += 1
#        a += 1

print(f"final slist is [{len(set(slist))}]")
print(set(slist))