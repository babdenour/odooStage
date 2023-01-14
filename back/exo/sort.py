def srt(list, pred=None):
  res = []

  for i in range(len(list)):
    mx = max(list, key=pred)
    res.append(mx)
    list.remove(mx)

  return res

def main ():
  print("Hello, starting Pyramide...!")
  list = [9,1,2,3,7,4,54,423456,8768,345]
  print(srt(list, lambda x: -x))
main()