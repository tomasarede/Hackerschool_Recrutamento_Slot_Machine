import random
import time


__author__ = "ist1103239@tecnico.ulisboa.pt"


#Slot Machine Basics
class SlotMachine:
    def __init__(self):
        self.universo = ["A","B","C","D","E","F","G"] #universo do que pode sair na slot
        self.n1 = 0 #primeiro item da slot
        self.n2 = 0 #segundo item da slot
        self.n3 = 0 #terceiro item da slot
        self.money = 0 #saldo

    def __str__(self):
        return "|" + self.n1 + "|" + self.n2 + "|" + self.n3 + "|"


    def Arede_logo(self):
        linha0 = " ___________    ___________      ___________     _________      ___________   \n"
        linha1 =" |###########|  |###########|    |###########|   |#########|_   |###########|  \n" 
        linha2= " |#|_______|#|  |#_________#|    |#|______       |#|       |#|  |#|______      \n"
        linha3 =" |###########|  |#########|__    |########|      |#|       |#|  |########|     \n"
        linha4 =" |#|       |#|  |#|        |#|   |#|_________    |#|_______|#|  |#|_________   \n"
        linha5 =" |#|       |#|  |#|         |#|  |###########|   |#########|    |###########|  \n"
        


        logo  = linha0 + linha1 + linha2 +linha3 + linha4 +linha5

        return  logo
    def Menu_logo(self):
        linha0 = " ____  ____   ___________    ___     _    _       _ \n"
        linha1 =" |####\/###|  |###########|  |###\   |#|  |#|     |#| \n" 
        linha2= " |#|\###/|#|  |#|______      |#|\#\  |#|  |#|     |#| \n"
        linha3 =" |#| \#/ |#|  |########|     |#| \#\ |#|  |#|     |#| \n"
        linha4 =" |#|     |#|  |#|_________   |#|  \#\|#|  |#|_____|#| \n"
        linha5 =" |#|     |#|  |###########|  |#|   \###|  |#########|\n"
        logo  = linha0 + linha1 + linha2 +linha3 + linha4 +linha5
        return logo

    #REGRAS DO JOGO
    def rules(self):

        """ O objetivo deste método é printar as regras do jogo
        arg: self
        return: ----
        """
        Logo = self.Arede_logo()

        print("\033[31m " + Logo +"\033[0;0m\n"
              "--------------------------------\n"
              "Digite" + "\033[32m"+" 'q' " + "\033[0;0m" + "se quiser colocar mais dinheiro na conta.\n"
              "Digite" + "\033[32m"+" 'w' " + "\033[0;0m" + "se quiser ver o dinheiro que tem na conta.\n"
              "Digite" + "\033[32m"+" 'p' " + "\033[0;0m" + "se quiser sair do jogo.\n"
              "Clique" + "\033[32m"+" ENTER " + "\033[0;0m" + "se quiser voltar a jogar.\n"
              "Se a qualquer momento quiser voltar ao menu de ajuda digite" + "\033[32m"+" '!help' " + "\033[0;0m" + " \n" 
              "--------------------------------\n"
              "Se fizer 3 letras iguais multiplica 100X o seu dinheiro apostado.\n"
              "Se fizer um multiplicador e 2 letras iguais o resultado será o seu dinheiro " 
              "apostado multiplicado pelo multiplicador.\n"
              "Tudo o resto está isento de lucro.\n"
              "--------------------------------\n"
              "Boa sorte e lembre-se:" + "\033[1;34m"+" APOSTE APENAS O QUE ESTÁ DISPOSTO A PERDER!" + "\033[0;0m" +"\n"
              )
    
    #ADICIONAR DINHEIRO
    def add_money(self,M):
        """ O objetivo deste método é adicionar dinheiro a conta
        arg: self, (float) M
        return: ----
        """
        self.money += M
        print("Foram adicionados " + str(M) + "$.")
    
    #VER O SALDO DA CONTA
    def see_money(self):
        """ O objetivo deste método é ver o dinheiro na conta
        arg: self
        return: ----
        """
        print("Tem na sua conta " + str(self.money) + "$")

    #VER SE O DINHEIRO QUE TEM NA CONTA É SUFICIENTE PARA A JOGADA
    def check_saldo(self,M):
        """ O objetivo deste método é ver se possui na conta o montante que deseja aostar
        arg: self, float(M)
        return: True
        """
        if (self.money-M < 0 ):
            print("Saldo insuficiente!")
            return True


    #VER SE GANHOU ALGUMA COISA OU SE PERDEU
    def math(self,M):

        """ O objetivo deste método é fazer as contas do quanto ganhou/perdeu
        arg: self, float (M)
        return: True 
        """

        #ver se sao 3 letras iguais
        if self.n1 == self.n2 == self.n3 == "A" : 
            self.money += M * 5
            print("Ganhou " + str(M*5) + "$. PARABENS!")
            return True


        if self.n1 == self.n2 == self.n3 == "B" : 
            self.money += M * 10
            print("Ganhou " + str(M*10) + "$. PARABENS!")
            return True

        
        if self.n1 == self.n2 == self.n3 == "C" : 
            self.money += M * 20
            print("Ganhou " + str(M*20) + "$. PARABENS!")
            return True

        
        if self.n1 == self.n2 == self.n3 == "D" : 
            self.money += M * 70
            print("Ganhou " + str(M*70) + "$. PARABENS!")
            return True


        if self.n1 == self.n2 == self.n3 == "E" : 
            self.money += M * 200
            print("Ganhou " + str(M*200) + "$. PARABENS!")
            return True


        if self.n1 == self.n2 == self.n3 == "F" : 
            self.money += M * 1000
            print("Ganhou " + str(M*1000) + "$. PARABENS!")
            return True


        if self.n1 == self.n2 == self.n3 == "G" : 
            self.money += M * 100000
            print("Ganhou " + str(M*100000) + "$. PARABENS!")
            return True

        
        #perda    
        else:
            print("Infelizmente perdeu " + str(M) + "$. Melhor sorte para a próxima.")
            if self.money == 0:
                print("Ficou sem dinheiro na conta.\nA abandonar a slot machine...")
                time.sleep(3)
                exit()

        self.money -= M
    
    #MENU
    def menu(self):
        """ O objetivo deste método é apresentar um menu com o que está disponivel na slot
        arg: self
        return: ----
        """
        logo = self.Menu_logo()
        print(
              "\033[32m " + logo  +"\033[0;0m\n"
              "-------------------------------\n"
              "Carregar a conta:" + "\033[32m"+" 'q' " + "\033[0;0m"+"\n"
              "Ver o salto da conta:" + "\033[32m"+" 'w' " + "\033[0;0m" +"\n"
              "Sair do jogo:" + "\033[32m"+" 'p' " + "\033[0;0m" +"\n"
              "Jogar:" + "\033[32m"+" ENTER " + "\033[0;0m" + "\n"
              "Menu de ajuda: " + "\033[32m"+" '!help' " + "\033[0;0m" + "\n"
              "-------------------------------")


    #uma simples animacao da slot a ser rodada
    def rodar_slot(self):
        """ O objetivo deste método é fazer uma simples animação da slot a ser rodada
        arg: self
        return: ----
        """
        print("Rodando a slot...")
        print("---------------")
        for i in range(0,10):
            print("|" + random.choice(self.universo) +  "|" + random.choice(self.universo) +"|" +random.choice(self.universo) + "|")
            time.sleep(0.5)
        print("---------------")


    #JOGAR
    def play(self):

        """ O objetivo deste métod é "reunir" todas as outras e criar a função de jogar
        arg: self
        return: bool - True ou False
        """
        #mostrar o menu sempre
        self.menu()

        #criar o input
        n = str(input("\033[33m"+"[AREDE] - Digite aqui: " + "\033[0;0m")).upper().strip()

        #adicionar dinheiro
        if n == "Q":
            M = float(input("\033[33m"+"[AREDE] - Digite o valor que quer adicionar à conta (Se enganou-se digite 0): " + "\033[0;0m"))
            self.add_money(M)
            return True
        
        #ver o saldo da conta
        if n == "W":
            self.see_money()
            return True

        #jogar    
        if n == "" or n == " ":
            #input do montante que quer jogar
            montante = float(input("\033[33m"+"[AREDE] - Digite o valor que quer apostar (Se enganou-se digite 0): "  + "\033[0;0m"))

            #verificar se o saldo é suficiente
            if self.check_saldo(montante):
                return False

            #jogando    
            self.rodar_slot()
            self.n1 = random.choices(self.universo, weights = (50/156*100,40/156*100,30/156*100,20/156*100,10/156*100,5/156*100,1/156*100))[0]
            self.n2 = random.choices(self.universo, weights = (50/156*100,40/156*100,30/156*100,20/156*100,10/156*100,5/156*100,1/156*100))[0]
            self.n3 = random.choices(self.universo, weights = (50/156*100,40/156*100,30/156*100,20/156*100,10/156*100,5/156*100,1/156*100))[0]
            print(self)

            #fazer as contas do lucros/perdas
            self.math(montante)
            return True

        #sair da slot
        if n == "P":
            print("Saindo ...")
            time.sleep(3)
            exit()

        #voltar ao menu de ajuda    
        if n == "!HELP":
            self.rules()

        #se não escrever nada do que está no menu    
        else:
            print("\033[33m" + "[AREDE] - Digite de novo o que pretende." + "\033[0;0m")
              

#CRIAR OBJETO
A = SlotMachine()

#MOSTRAR AS REGRAS
A.rules()

#LOOP DO JOGO
while True:
    A.play()




