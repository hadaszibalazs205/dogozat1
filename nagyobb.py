#A program kérjen be két számot a felhasználótól, majd írja ki, hogy melyik a nagyobb!

szám = int(input("Kérek egy számot! "))
szám1 = int(input("Kérnék megint egy másik számot! "))

if (szám < szám1) :
  print(szám1)
else:
  if (szám1 < szám):
    print(szám)