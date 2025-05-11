mijn_lijst = ["aarbei" , "vanille" , "chocolade"]

mijn_dictonairy = {
    "aarbei": 3,#6
    "vanille": 4,#7
    "chocolade": 5#9
}
aanbieding = mijn_dictonairy["aarbei"] * 0.8

reclame_tekst = f"vandaag in de aanbieding vanille ijs, 1 liter - slechts {aanbieding}"
reclame_tekst2 = reclame_tekst[:reclame_tekst.index("0")]
reclame_tekst3 = f"vandaag in de aanbieding vanille ijs, 1 liter - slechts {aanbieding}"
reclame_tekst4 = reclame_tekst3.split()

mijn_lijst = ["mijn_dictonairy"] 
for el in mijn_dictonairy:
    if len (el) >= 5:
        print(el.upper())
    else:print(el.lower())
