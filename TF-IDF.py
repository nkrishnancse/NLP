docA="good morning friends have a nice day"
docB="welcome to today have a nice day "

b=docA.split(" ")
c=docB.split(" ")

print(b)
print(c)

wordset=set(b).union(set(c))

print(wordset)


