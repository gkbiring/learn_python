guests = ['mom', 'dad', 'ritta']
name = guests[0].title()
print(f"{name}, please come to dinner!")
name = guests[1].title()
print(f"{name}, please come to dinner!")
name = guests[2].title()
print(f"{name}, please come to dinner!")

name = guests[1].title()
print(f"\nSorry, {name} cannot make it to dinner.")
del guests[1]
guests.insert(1, 'mindhi')
print(guests)
name = guests[0].title()
print(f"\n{name}, please come to dinner!")
name = guests[1].title()
print(f"{name}, please come to dinner!")
name = guests[2].title()
print(f"{name}, please come to dinner!")

print(f"\nWe got a bigger table!")
guests.insert(0, 'amber')
guests.insert(2, 'caleb')
guests.append('monica')
print(guests)

name = guests[0].title()
print(f"\n{name}, please come to dinner!")
name = guests[1].title()
print(f"{name}, please come to dinner!")
name = guests[2].title()
print(f"{name}, please come to dinner!")
name = guests[3].title()
print(f"{name}, please come to dinner!")
name = guests[4].title()
print(f"{name}, please come to dinner!")
name = guests[5].title()
print(f"{name}, please come to dinner!")
