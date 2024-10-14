f = open('../txtf/input.txt', 'r')
n = int(f.readline())
s = f.readline()
f.close()

if not 1 <= n <= 10**5:
    with open('../txtf/output.txt', 'w') as f:
        f.write('Число не входит в допустимый диапазон')
    exit()

counts = {}
for symbol in s:
    if symbol in counts:
        counts[symbol] += 1
    else:
        counts[symbol] = 1

left_part = []
middle_symbol = ''

for symbol in sorted(counts.keys()):
    count = counts[symbol]
    left_part.append(symbol * (count // 2))
    if count % 2 == 1 and middle_symbol == '':
        middle_symbol = symbol

left = ''.join(left_part)
palindrome = left + middle_symbol + left[::-1]

f = open('../txtf/output.txt', 'w')
f.write(palindrome)
f.close()