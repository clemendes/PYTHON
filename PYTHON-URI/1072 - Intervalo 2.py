var_in = 0
var_out = 0

n = int(input())	

for i in range(0,n,1):
  num = int(input())
  if (num >= 10) and (num <= 20):
      var_in += 1
  else:
      var_out += 1

print("%d in" %var_in)
print("%d out" %var_out)
