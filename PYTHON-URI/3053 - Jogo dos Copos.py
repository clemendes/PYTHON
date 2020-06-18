n = int(input())

ini = input()

a = 0
b = 0
c = 0
final = ""

if ini == "A":
	a = 1
elif ini == "B":
	b = 1
elif ini == "C":
	c = 1

for i in range(0,n,1):
	m = int(input())

	if m == 1:
		if c == 1:
			final = "C"
		elif a == 1:
			a = 0
			b = 1
			final = "B"
		elif b == 1:
			b = 0
			a = 1
			final = "A"
	elif m == 2:
		if a == 1:
			final = "A"
		if b == 1:
			b = 0
			c = 1
			final = "C"
		elif c == 1:
			c = 0
			b = 1
			final = "B"
	elif m == 3:
		if b == 1:
			final = "B"
		elif a == 1:
			a = 0
			c = 1
			final = "C"
		elif c == 1:
			c = 0
			a = 1
			final = "A"

print(final)
