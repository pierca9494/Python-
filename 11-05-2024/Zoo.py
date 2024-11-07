class Animale:
    def __init__(self, nome, eta, specie):
        self.nome = nome
        self.eta = eta
        self.specie = specie

    def fai_suono(self):
        print("Suono generico dell'animale")

class Leone(Animale):
    def __init__(self, nome, eta, specie):
        super().__init__(nome, eta)
        self.specie = specie
        
        

    def fai_suono(self):
        print("Il leone ruggisce")

    def caccia(self):
        print(f"{self.nome} sta cacciando")

class Giraffa(Animale):
    def __init__(self, nome, eta, specie):
        super().__init__(nome, eta)
        self.specie = specie
        
        

    def fai_suono(self):
        print("La giraffa emette un suono particolare")

    def bruca(self):
        print(f"{self.nome} sta brucando le foglie")

class Pinguino(Animale):
    def __init__(self, nome, eta, specie):
        super().__init__(nome, eta)
        self.specie = specie

    def fai_suono(self):
        print("Il pinguino emette un suono squillante")

    def nuota(self):
        print(f"{self.nome} sta nuotando")

# Creazione di istanze di ogni animale
leone = Leone("Simba", 5)
giraffa = Giraffa("Melman", 8)
pinguino = Pinguino("Pingu", 3)

# Test dei metodi
leone.fai_suono()
leone.caccia()

giraffa.fai_suono()
giraffa.bruca()

pinguino.fai_suono()
pinguino.nuota()


class Zoo:
    def __init__(self):
        self.animali = []
        
        
    def aggiungi_animale(self, nome, eta, specie):
        animale = Animale(nome, eta, specie)
        self.animali.append(animale)
        
    def categoria_animale(self):
        for animale in self.animali:
            if animale.specie == "Leonide":
                print(f"Il {animale.nome} è un Leone")
            elif animale.specie == "Giraffa":
                print(f"Il {animale.nome} è una Giraffa")
            elif animale.specie == "Pinguino":
                print(f"Il {animale.nome} è un Pinguino")
            else:
                print(f"Il {animale.nome} è un Animale Generico")
                
                

zoo = Zoo()
zoo.aggiungi_animale("Leone", 5, "Leonide")
zoo.aggiungi_animale("Giraffa", 8, "Giraffa")
zoo.aggiungi_animale("Pingu", 3, "Pinguino")
zoo.aggiungi_animale("Generico", 10, "Animale Generico")

zoo.categoria_animale()
