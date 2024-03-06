# ------------- Tipos de Desplazamiento ----------------
class ITipo_mov:
    def Movimiento():
        pass

class Correr(ITipo_mov):
    def Movimiento():
        return "corriendo"
    
class Caminar(ITipo_mov):
    def Movimiento():
        return "caminando sigilosamente"
    
# ------------- Tipos de Ataques ----------------
class IAtaque:
    def Atacar():
        pass

class Arco(IAtaque):
    def Atacar():
        return "disparando con un arco"

class Fusil(IAtaque):
    def Atacar():
        return "disparando con un fusil de asalto"
    
class Espada(IAtaque):
    def Atacar():
        return "atacando con una espada"


# ------------- Clase padre ----------------
class Militares:
    def __init__(self, movimiento: ITipo_mov, ataque: IAtaque) -> None:
        self.mov=movimiento
        self.atq=ataque

    def __str__(self) -> str:
        return "estoy " + self.mov.Movimiento() + ", mientras que estoy " + self.atq.Atacar()

# ------------- Clases hijas ----------------
class Arquero(Militares):
    def __init__(self) -> None:
        super().__init__(Caminar, Arco)

    def __str__(self) -> str:
        return "Soy un arquero y " + super().__str__()

class Soldado(Militares):
    def __init__(self) -> None:
        super().__init__(Caminar, Fusil)

    def __str__(self) -> str:
        return "Soy un soldado y " + super().__str__()

class Caballero(Militares):
    def __init__(self) -> None:
        super().__init__(Correr, Espada)
    
    def __str__(self) -> str:
        return "Soy un caballero y " + super().__str__()


# --------------------------------------------
        
arq1 = Arquero()
sol1 = Soldado()
cab1 = Caballero()

print(arq1)
print(sol1)
print(cab1)