#Egy bolt pontban reggel nyolc órakor nyit, és pontban délután tizenhat órakor zár be – azaz 8:00-kor már nyitva van és 16:00-kor már nincs nyitva. A program kérjen be egy egész órát jelző számot a felhasználótól,majd írja ki, hogy a megadott időpontban nyitva van-e a bolt! Amennyiben igen, akkor azt is írja ki, hogy mennyi idő van még zárásig, azaz hány egész óra áll rendelkezésre odaérni a boltba!
ido = int(input("Adj meg egy időt. "))

if ido < 8 or ido >= 16:
  print("Nincs nyitva")
else:
  print("Nyitva", 16 - ido, "ó ennyi idő van zárásig")

