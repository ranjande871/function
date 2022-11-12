word = "hello"
letters = []
for w in word:
    print(w)
    if w == "e":
        print("what is the funny letter")
    letters.append(w)
print(letters)
for l in letters:
    print(l)
numbers = [1,2,3,4,5]
for n in numbers:
    if n%2 == 0:

        print(n)
#range(start,stopping,steps)
numbers = []
for num in range(1,10,2):
    numbers.append(num)
    print(num)
print(numbers)
