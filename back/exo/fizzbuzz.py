def main(nbr):
  res = ""
  print("Hello, starting fizzbuzz...!")


  if nbr % 3 == 0:
    res = res + "fizz"
  if nbr % 5 == 0:
    res = res + "buzz"
  if nbr % 7 == 0:
    res = res + "foo"
  if not res:
    res = str(nbr)
  
  print(res)
  return res

main(5)