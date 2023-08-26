def line(length):
    for length in range(0, length):
        print("#", end="")

text = str(input("Ievadi tekstu: "))
length = len(text)

line(length)
print(f'\n{text}')
line(length)