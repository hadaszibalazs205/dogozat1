#Egy rakéta indítása előtt több órával visszaszámlálást kezdenek és óránként egyet számolnak vissza a rakéta indításáig. A felhasználó határozza meg, hogy hány órás a visszaszámlálás. A visszaszámlálást minden órában egy órára felfüggeszthetik, ha valamilyen váratlan esemény – műszaki hiba, időjárási probléma – merül fel. Amikor a visszaszámlálás eléri a 0-t, a rakétát fellövik. Írjon programot, amely a visszaszámlálás számait jeleníti meg a képernyőn! Természetesen nem kell a visszaszámlálás lépései között eltelni időnek – minden üzenet megjelenését azonnal követheti a felhasználót, hogy az adott órában szükség volt-e a visszaszámlálás fölfüggesztésére! A visszaszámlálás megjelenítését követően a program írja ki, hogy a visszaszámlálás kezdetétől hány óra telt el – a visszaszámlálás eredetileg tervezett hosszát a felfüggesztésekkel megnövelve!

vissza_szamlalas =input("Adjon meg egy számot. ")
vissza_szamlalas = int(vissza_szamlalas)
karbantartas = input("Volt-e szükség felfüggesztésre (igen/nem)")


while vissza_szamlalas > -1:
  print(vissza_szamlalas)
  karbantartas = 0
  while karbantartas == "igen":
    karbantartas = karbantartas + 1
vissza_szamlalas = vissza_szamlalas - 1