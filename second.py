def cislo_text(cislo):
    if cislo in cisla:
        return cisla[cislo]

    elif 20 < cislo < 100:
        desitky = (cislo // 10) * 10
        jednotky = cislo % 10
        #v proměnné desítky zůstane pouze hlavní člen žádaného čísla, 
        #v jednotkách zůstává zbytek žádaného čísla 
        return cisla[desitky] + " " + cisla[jednotky]

    else:
        return "Číslo mimo rozsah"


cisla = {
    0:"nula",
    1:"jedna",
    2:"dva",
    3:"tři",
    4:"čtyři",
    5:"pět",
    6:"šest",
    7:"sedm",
    8:"osm",
    9:"devět",
    10:"deset",
    11:"jedenáct",
    12:"dvanáct",
    13:"třináct",
    14:"čtrnáct",
    15:"patnáct",
    16:"šestnáct",
    17:"sedmnáct",
    18:"osmnáct",
    19:"devatenáct",
    20:"dvacet",
    30:"třicet",
    40:"čtyřicet",
    50:"padesát",
    60:"šedesát",
    70:"sedmdesát",
    80:"osmdesát",
    90:"devadesát",
    100: "sto"
}

cislo = int(input("Zadejte číslo od 0 do 100: "))
print(cislo_text(cislo))
