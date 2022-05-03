from re import A
import model

SLIKE = ['',
''' 
    
    
   
  
_______''',
'''
 |   
 |   
 |  
 | 
_|______''',
''' _____
 |   
 |   
 |  
 | 
_|______''',
''' _____
 |   |
 |   
 |  
 |  
_|______''',
''' _____
 |   |
 |   o
 |  
 |  
_|______''',
''' _____
 |   |
 |   o
 |  |
 | 
_|______''',
''' _____
 |   |
 |   o
 |  /|
 |  
_|______''',
''' _____
 |   |
 |   o
 |  /|\\
 |  
_|______''',
'''_____
 |   |
 |   o
 |  /|\\
 |    \\
_|______ ''',
''' _____
 |   |
 |   o
 |  /|\\
 |  / \\
_|______''']

def izpis_igre(igra:model.Igra):
    niz = f"""{SLIKE[igra.stevilo_napak()]}
{igra.pravilni_del_gesla()}
Nepravilni ugibi: {igra.nepravilni_ugibi()}
Napačno lahko ugibaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}-krat"""
    return niz
def izpis_zmage(igra):
    return f"Čestitke! Pravilno si uganil geslo {igra.geslo}!"
def izpis_poraza(igra):
    return f"Več sreče prihodnjič! Pravilno geslo je bilo {igra.geslo}."
def zahtevaj_vnos():
    return input('Ugibaj črko: ')
def pozeni_vmesnik():
    igra = model.nova_igra()
    while not ( igra.zmaga() or igra.poraz() ):
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        while len(crka)!= 1 or not crka.isalpha():
            crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
    if igra.zmaga():
        print(izpis_zmage(igra))
    else:
        print(SLIKE[-1])
        print(izpis_poraza(igra))
        
pozeni_vmesnik()

odlocitev = input('Bi želeli igrati ponovno? D/N: ')
if odlocitev == 'D':
    pozeni_vmesnik()



