'''
Kevin Joarand
Ülesanne 08
16.02.2022
'''

class Auto:
    #atribuudid
    automark = 'lisamata'
    aasta = 0
    hind = 0
    kiirus = 0
    varv = 'lisamata'
    
    def lisamark(self,x):
        self.automark = x
    def lisaaasta(self,x):
        self.aasta = x
    def lisahind(self,x):
        self.hind = x
    def lisakiirus(self,x):
        self.kiirus = x
    def lisavarv(self,x):
        self.varv = x
        
    def kuva(self):
        print(f"{self.automark} {self.aasta} {self.hind} {self.kiirus} {self.varv}")
        
uusObjekt = Auto()
uusObjekt.lisamark('Lada')
uusObjekt.lisaaasta(69)
uusObjekt.lisahind(420)
uusObjekt.lisakiirus(100)
uusObjekt.lisavarv('kirju')
uusObjekt.kuva()

uusAuto = Auto()
uusAuto.lisamark('Supra')
uusAuto.lisaaasta(9999)
uusAuto.lisahind(696969)
uusAuto.lisakiirus(500)
uusAuto.lisavarv('must')
uusAuto.kuva() 