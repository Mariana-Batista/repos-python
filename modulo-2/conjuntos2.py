#add, update, clear, discard

s1 = set()
s1.add('Mariana')
s1.add(35)
print(s1)

print()

s2 = set()
s2.add('Cumprimento')
s2.update(('Olá mundo', 1, 2))
print(s2)

print()

#s1.clear()

print()

s2.discard(1)
print(s2)