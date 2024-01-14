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


# Der bliver lavet 8 variabler, som jeg vil forklare her nedenunder:

# Denne variabel viser antallet af biler som der er ialt.
biler = 100

# Denne variable mener jeg hentyder til variablen biler ift. hvor mange passagerer der kan være pr. bil.
plads_i_en_bil = 4.0  

# Denne variabel mener jeg så også hentyder til variablen biler ift. hvor mange førere der er tilgængelige til bilerne.
førere = 30

# Denne variabel mener jeg giver os antallet af passagerer der skal tildeles på de 100 biler.
passagerer = 90

# Denne variable hentyder til, at man får biler ude af drift ved at trække antallet af biler fra antallet af chauffører.
biler_ude_af_drift = biler - førere

# Denne variabel viser, at biler som kan være i kørsel er det antal chauffører der er.
biler_i_kørsel = førere

# Variablen viser antallet af tilgængelige pladser ved at henvise til den forrige variabel (biler_i_kørsel), da man skal gange antallet af førere med pladsmængden i bilen, hvilket er 4, som er nævnt i en tidligere variabel.
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil

# Den sidste variable viser os gennemsnittet ved at tage variablen passagerer og dividere den med antallet af biler i kørsel, som henviser til antallet af førere.
gennemsnit_af_passagerer_per_bil = passagerer / biler_i_kørsel

"""
OPG. 3.1 Variblen

Samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil, man har ikke defineret variablen, så du har ikke mulighed for at hente variablen.

"""