import bejelentkezes
import sorozat


###########
#         #
# 1. FEL. #
#         #
###########

#bejelentkezes.BejelentkezesifeladatSzamKiiras()
#email1, email2, psw = bejelentkezes.BejelentkezesiAdatokBekerese()
#kimenet = bejelentkezes.BejelenkezesiadatokEllenorzese(email1, email2, psw)
#bejelentkezes.BejelentkezesieredmenyKiiras(kimenet, email1, email2, psw)

###########
#         #
# 2. FEL. #
#         #
###########

sorozat.SorozatosfeladatSzamKiiras()
szamok = sorozat.SorozatosSzamGeneralas()
kimenet = sorozat.SorozatosSorbaRendezes("-", szamok)
hanyDBKisebb = sorozat.SorozatosKisebbSzamolas(szamok)
sorozat.SorozatosFajlbaKiiras(hanyDBKisebb)
sorozat.sorozatKiiras(kimenet)