import math


def prt(nbr):
  res = ""
  for i in range(1, nbr):
    res += i * "*" + '\n'
  return res

def revPrt(nbr):
  res = ""
  for i in range(1, nbr):
    res += (nbr - i) * " " + i * "*"  + '\n'
  return res

def centPrt(nbr):
  res = ""
  for i in range(1, nbr):
    res += (nbr-i) * " " + (2*i-1) * "*" + '\n'
  return res


def main ():
  print("Hello, starting Pyramide...!")
  print(prt(7))
  print(revPrt(4))
  print(centPrt(9), end="")

if __name__ == "__main__":
  main()