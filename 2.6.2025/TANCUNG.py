def sotancung(A, n):
  if n == 0:
    return 1
  A = A % 10
  if A == 0:
    return 0
  if A == 1:
    return 1
  if A == 5:
    return 5
  if A == 6:
    return 6
  if n == 1:
      return A
  if A == 4 or A == 9:
      n = n % 2
      if n == 0:
          return A * A % 10
      else:
          return A
  n = n % 4
  if n == 0:
    return pow(A, 4, 10)
  else:
    return pow(A, n, 10)
with open("TANCUNG.INP", "r") as f:
  A, n = map(int, f.readline().split())
  
with open("TANCUNG.OUT", "w") as f:
  f.write(str(sotancung(A, n)))