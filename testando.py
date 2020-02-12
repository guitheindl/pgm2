class Dragao():

    def __init__(self, vida, ataque1, ataque2):
        self.vida = vida
        self.ataque1 = ataque1
        self.ataque2 = ataque2

dragao1 = Dragao(1000, 200, 300)
dragao2 = Dragao(1000, 200, 300)

a = int(input("Qual dragão voce quer? 1 ou 2"))

if a == 1: 
    b = int(input("Qual ataque voce quer usar no inimigo? 1 ou 2"))
    if b == 1:
        print(f"Voce tirou {dragao1.ataque1} de vida do adversário")
        vidadragao2 = dragao2.vida - dragao1.ataque1
        print(f"Ele ficou com {vidadragao2}")
        