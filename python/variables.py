age = 25
a = [1, 2, 3]
b = a
b.append(4)
print(a)

# when you assign b = a, you're not copying the value — you're creating a second label pointing at the same object

print(True+True)  # 2 True is secretly 1

print(type(age))  # int
print(isinstance(age, int))  # true

# TypeCasting

x = int("42")  # now its 42
print(type(x))

