import sys

shift = int(sys.argv[1])

text = sys.stdin.read().upper()

result = ""

for char in text:
    if char.isalpha():
        new_char = chr((ord(char) - 65 + shift) % 26 + 65)
        result += new_char

# print in blocks of 5, 10 blocks per line
for i in range(0, len(result), 50):
    line = result[i:i+50]
    blocks = [line[j:j+5] for j in range(0, len(line), 5)]
    print(" ".join(blocks))
