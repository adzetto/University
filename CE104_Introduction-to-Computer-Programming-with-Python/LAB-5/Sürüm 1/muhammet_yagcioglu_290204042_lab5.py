n = int(input("n:"))
k = int(input("k:"))

sum = 0
for i in range(k):
  current_number = str(n) * (i + 1)
  sum += int(current_number)

print(sum)