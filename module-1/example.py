import country_units as cu

nadezhdivka = cu.Village("Nadezhdivka", 1000)
bilozerka = cu.Town("Bilozerka", 5321)
tomyna_balka = cu.Village("Tomyna Balka", 1675)

chornobayivka = cu.Village("Chornobayivka", 4343)

kherson = cu.Town("Kherson", 220000)

bilozerska_otg = cu.TerritorialCommunity("Bilozerka Territory Community", [nadezhdivka, bilozerka, tomyna_balka])

khersonskyi_district = cu.District("Kherson District", [nadezhdivka, bilozerka, tomyna_balka, chornobayivka, kherson])

rozdolne = cu.Village("Rozdolne", 2312)
vilna_ukraina = cu.Village("Vilna Ukarina", 659)
kakhovka = cu.Town("Kakhovka", 15900)

kakhovska_otg = cu.TerritorialCommunity("Kakhovka Territory Community", [kakhovka, vilna_ukraina, rozdolne])

kakhovskyi_district = cu.District("Kakhovka District", [kakhovka, vilna_ukraina, rozdolne])

kherson_region = cu.Region("Kherson Region", [khersonskyi_district, kakhovskyi_district])

print(bilozerka.get_locality_type())

print(nadezhdivka.is_village())

print(bilozerska_otg.get_population())

print(kherson_region.get_population())

print(kakhovskyi_district.get_localities_count_by_type("village"))

print(kherson_region.get_localities_count_by_type("village"))