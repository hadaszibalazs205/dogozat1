#Írjon programot, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. A program egyetlen felhasználó (bori99 ) jelszavát (Szivecske<3) ismeri, csak ezt a párost fogadja el helyesként. Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.

felhasznalo = "bori99"
jelszo = "Szivecske<3"
helyes = False

while not helyes:
  tipp_felhasznalo = input("Kérem a felhasználó nevet! ")
  tipp_jelszo = input("Kérem a jelszót! ")
  if tipp_felhasznalo == felhasznalo and tipp_jelszo == jelszo:
    helyes = True
    print("Sikeres Bejelentkezés!")
  else:
    print("probálkozzon újra!")