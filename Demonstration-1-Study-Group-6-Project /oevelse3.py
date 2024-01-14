biler = 100
plads_i_en_bil = 4.0
førere = 30
passagerer = 90
biler_ude_af_drift = biler - førere
biler_i_kørsel = førere
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil
gennemsnit_af_passagerer_per_bil = passagerer / biler_i_kørsel


print("Der er", biler, " biler til rådighed.")
print("Der er kun", førere, "førere til rådighed.")
print("Der vil være", biler_ude_af_drift, "tomme biler i dag.")
print("Vi kan transportere", samlet_bil_kapacitet, "personer i dag.")
print("Vi har", passagerer, "passagerer i dag.")
print("Vi skal cirka putte", gennemsnit_af_passagerer_per_bil, "i hver bil.")


# Jeg mener at der bliver lavet 8 variabler, som jeg vil forklare her nedenunder:

# Denne variabel viser antallet af biler som der er ialt.
biler = 100

# Denne variable mener jeg hentyder til variablen biler ift. hvor mange passeger der kan være pr. bil.
plads_i_en_bil = 4.0  

# Denne variabel mener jeg så også hentyder til variablen biler ift. hvor mange førere der er tilgængelige til bilerne.
førere = 30

# Denne variabel mener jeg giver os antallet af passegere der skal tildeles på de 100 biler.
passagerer = 90

# Denne variable hentyder til at man får biler ude af drift ved at minus bilerne med antallet af chaufføre.
biler_ude_af_drift = biler - førere

# Denne variabel viser at biler som kan være i kørsel er det antal chauffører der er.
biler_i_kørsel = førere

# Denne variabel viser antallet af tilgængelige 
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil

# Endelig beregner vi gennemsnittet af passagerer per bil ved at dividere antallet af passagerer med antallet af biler i brug.
gennemsnit_af_passagerer_per_bil = passagerer / biler_i_kørsel
