
# guillaume zip
def enum(lt, i=0):
  for x in lt:
    yield i,x
    i+=1

def em(lst, st=0):
  for i in range(len(lst)):
    yield st+i,lst[i]


def ziplongest(list1, list2, val, *args):
  mx = max([len(list1), len(list2)])
  print(*args)

# len(list1) != len(list2)
  
  if mx :
    for i in range(len(list1)):
      list2.append(val)
      print(list1[i], list2[i])


  zipped = zip(list1, list2)
  for index, value in enumerate(zipped, start=1): 
    print(index,value[0], value[1])

def main():
  print("Hello, starting Pyramide...!")
  list1 = ["apple", "banana", "cherry"]
  list2 = ["jus", "coke",]
  ziplongest(list2, list1, "x")
main()