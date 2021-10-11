import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last=len(quotes)-1
  randomquote=random.randint(0, last)
  print(quotes[randomquote])

if __name__== "__main__":
  primary()
