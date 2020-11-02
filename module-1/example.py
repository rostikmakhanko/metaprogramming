import country_units as cu

nadezhdivka = cu.Village("Nadezhdivka", 1000)
bilozerka = cu.Town("Bilozerka", 5321)
tomyna_balka = cu.Village("Tomyna Balka", 1675)

chornobayivka = cu.Village("Chornobayivka", 4343)

bilozerska_otg = cu.TerritorialCommunity("Bilozerka Territory Community", [nadezhdivka, bilozerka, tomyna_balka])

khersonskyi_district = cu.District("Kherson District", [nadezhdivka, bilozerka, tomyna_balka, chornobayivka])