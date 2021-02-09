#A program kérjen be két szót a felhasználótól, majd írja ki, hogy melyik a hosszabb!

a = input("Adj meg egy szót. ")
b = input("Adj meg még egy szót. ")
a = str(a)
b = str(b)

if a < b:
  print(b)
else:
  print(a)