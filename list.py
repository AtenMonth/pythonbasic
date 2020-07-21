guests=['abc','bcd','efg']
print("Original list",guests)
guests[2]='ghi'
print("after inserting at 2:",guests)
guests.append('jkl')
print("after append",guests)
del guests[2]
print("after del 2:",guests)
last_guest=guests.pop()
print(f"{last_guest.upper()} you are invted for the dinner.")
