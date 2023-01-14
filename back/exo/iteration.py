def iteration(list1, list2):

  for index, value in enumerate(list1, start=1): 
    print(index,value)

  for i in range(len(list1)):
    print(list1[i], list2[i])

# guillaume zip
  for index, value in enumerate(zip(list1, list2), start=1): 
    print(index,value[0], value[1])

def main():
  print("Hello, starting Pyramide...!")
  list1 = ["apple", "banana", "cherry"]
  list2 = ["jus", "coke", "lemon"]
  iteration(list1, list2)
main()
