#Írjon programot, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. A program egyetlen felhasználó (bori99 ) jelszavát (Szivecske<3) ismeri, csak ezt a párost fogadja el helyesként. Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.

felhasználó_név = "bori99"
jelszó = "Szivecske<3"
helyes = False

while not helyes:
  felhasznalo = input("Kérem a felhasználó nevet! ")
  jelszo = input("Kérem a jelszót! ")
  if tipp1 and tipp2 == jelszó and felhasználó_név:
    helyes = True
    print("Sikeres Bejelentkezés!")
  else:
    print("probálkozzon újra!")