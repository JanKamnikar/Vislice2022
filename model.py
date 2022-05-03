STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA ='+', 'o', '-'
ZMAGA, PORAZ ='W' , 'X'

class Igra:
    def __init__(self,geslo, crke= None):
        self.geslo = geslo.upper()
        if crke is not None: 
            self.crke = crke
        else:
            self.crke = []#zaradi D/N za nadaljevanje

    def napacne_crke(self):
        return [i for i in self.crke if i not in self.geslo]
    def pravilne_crke(self):
        return [i for i in self.crke if i in self.geslo]
    def stevilo_napak(self):
        return len(self.napacne_crke())
    def zmaga(self):
        return len(self.pravilne_crke()) == len(set(self.geslo)) #set je zaradi ponovljenih crk
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    def pravilni_del_gesla(self):
        return ''.join( [(i  if i in self.crke else '_') for i in self.geslo] )
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())
    def ugibaj(self,crka):
        crka = crka.upper()
        if  crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke += [crka]
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.pravilne_crke():
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA
with open('besede.txt', encoding='utf8') as besede:
    #bazen_besed = [beseda.strip() for beseda in besede]
    bazen_besed = besede.read().split('\n')
import random
def nova_igra():
    return Igra( random.choice(bazen_besed)  )


