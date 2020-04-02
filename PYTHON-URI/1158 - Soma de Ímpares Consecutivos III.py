# URI 1158
# CLEVERSON MENDES FARIA


n = int(input())

soma = 0

for i in range(0,n,1):
      entrada = input().split()
      a = int(entrada[0])
      b = int(entrada[1])

      cont = 0
      teste = a
      soma = 0
      
      while cont < b:

          if (teste % 2 != 0):
              soma += teste
              cont += 1
              teste += 1
          else:
              teste += 1
      print("%d" %soma)
