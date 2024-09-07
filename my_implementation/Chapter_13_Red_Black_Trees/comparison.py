
x = 1000
y = 1000

print(x is y)  # True
print(id(x), id(y))  
assert id(x) == id(y)
print(x == y)  # True, because the values of 'x' and 'y' are equal.

a = "hello"
b = "hello"

print(a is b)  # True, because Python caches small strings and 'a' and 'b' point to the same object.
print(id(a), id(b))
assert id(a) == id(b)
print(a == b)  # True, because the values of 'a' and 'b' are equal.