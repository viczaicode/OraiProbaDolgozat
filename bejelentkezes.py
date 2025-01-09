def BejelentkezesifeladatSzamKiiras():
    print("I/A,B")


def BejelentkezesiAdatokBekerese():
    email1 = str(input("Kérem adja meg az e-mail címét: "))
    email2 = str(input("Kérem ismételten adja meg az e-mail címét: "))
    psw = str(input("Kérem adja meg a jelszavát: "))
    return email1, email2, psw

def BejelenkezesiadatokEllenorzese(email1:str, email2:str,psw:str):
    if (email1 != email2):
         return "Hiba, az e-mailek nem egyeznek!"
    elif(psw is None):
        return "Hiba, a jelszó üresen lett hagyva"
    else:
        return f"Sikeres bejelentkezés, {email1}"
    
def BejelentkezesieredmenyKiiras(kimenet:str, email1:str, email2:str, psw:str):
    print(kimenet)
    print(f"Email cím: {email1}")
    print(f"Email cím még egyszer: {email2}")
    print(f"Jelszó: {psw}")

