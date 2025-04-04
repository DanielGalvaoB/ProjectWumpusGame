import os
<<<<<<< HEAD
import msvcrt
import random

class Caverna:
    def __init__(self, tamanho, num_buracos):
        self.tamanho = tamanho
        self.mapa = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
        self.buracos = self.gerar_buracos(num_buracos)
        self.wumpus_pos = None
        self.ouro_pos = None
        self.gerar_wumpus()
        self.gerar_ouro()

    def gerar_buracos(self, num_buracos):
        buracos = []
        for _ in range(num_buracos):
            x, y = random.randint(1, self.tamanho-1), random.randint(0, self.tamanho-1)
            while (x, y) in buracos:
                x, y = random.randint(0, self.tamanho-1), random.randint(0, self.tamanho-1)
            buracos.append((x, y))
        return buracos

    def gerar_wumpus(self):
        while True:
            self.wumpus_pos = (random.randint(1, self.tamanho-1), random.randint(0, self.tamanho-1))
            if self.wumpus_pos not in self.buracos:
                break

    def gerar_ouro(self):
        while True:
            self.ouro_pos = (random.randint(1, self.tamanho-1), random.randint(0, self.tamanho-1))
            if self.ouro_pos not in self.buracos and self.ouro_pos != self.wumpus_pos:
                break
=======
import random
from re import S

class Caverna:
    def __init__(self, tamanho, num_wumpus, num_abismos):
        self.tamanho = tamanho
        self.mapa = [['[ ]' for _ in range(tamanho)] for _ in range(tamanho)]
        self.itens = self.gerar_itens()
        self.wumpus = self.gerar_wumpus()
        self.abismos = self.gerar_abismos(num_abismos)  # Corrigido para usar num_abismos

    def gerar_itens(self):
        
        # Gerar 3 itens em posições aleatórias
        itens = []
        for _ in range(3):
            while True:
                x, y = random.randint(0, self.tamanho - 1), random.randint(0, self.tamanho - 1)
                if (x, y) not in itens:  # Garantir que não haja duplicatas
                    itens.append((x, y))
                    self.mapa[x][y] = "[*]"  # Representação do item
                    break
        return itens

    def gerar_wumpus(self):
            while True:
                wumpus_pos = (random.randint(0, self.tamanho - 1), random.randint(0,self.tamanho - 1))
                if wumpus_pos not in self.itens:
                     self.mapa[wumpus_pos[0]][wumpus_pos[1]] = "[W]"
                return wumpus_pos

    def gerar_abismos(self, num_abismos):  # Corrigido para aceitar num_abismos
            abismos = []
            for _ in range(num_abismos):  # Geração de abismos baseada em num_abismos
                while True:
                    abismos_pos = (random.randint(0, self.tamanho - 1), random.randint(0, self.tamanho - 1))
                    if abismos_pos not in abismos and abismos_pos not in self.wumpus and abismos_pos not in self.itens:
                        abismos.append(abismos_pos)
                        self.mapa[abismos_pos[0]][abismos_pos[1]] = "[A]"
                        break  # Quebra quando um abismo é gerado corretamente
            return abismos

>>>>>>> d3cfff039e0746b0f84d2b1ed25a71f3dc3f6f8c

    def exibir(self, playerPosition):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if (i, j) == playerPosition:
                    print("[🏆]", end=" ")
                elif (i, j) == self.wumpus_pos:
                    print("[M ]", end=" ")
                elif (i, j) == self.ouro_pos:
                    print("[💰]", end=" ")
                elif (i, j) in self.buracos:
                    print("[B ]", end=" ")
                else:
                    print("[  ]", end=" ")
            print()

<<<<<<< HEAD
=======
class Pontos:
    def __init__(self):
        self.pontos = []

    def addPontos(self, nome, pontos):
        self.pontos.append({"nome": nome, "pontos": pontos})
        self.pontos = sorted(self.pontos, key=lambda x: x['pontos'], reverse=True)
        self.pontos = self.pontos[:5]  # Mantém apenas os 5 melhores

    def mostraPontos(self):
        if not self.pontos:
            print("Nenhuma pontuação registrada ainda.")
        else:
            print("Ranking dos Melhores Jogadores:")
            for i, jogador in enumerate(self.pontos, 1):
                print(f"{i}. {jogador['nome']} - {jogador['pontos']} pontos")



>>>>>>> d3cfff039e0746b0f84d2b1ed25a71f3dc3f6f8c
class NovoJogo:
    def __init__(self, ranking):
        self.caverna = None
        self.nome = ""
        self.dificuldade = ["Facíl(4x4)", "Normal(6x6)", "Dificil(10x10)"]
        self.posicao = (0, 0)
        self.dif = 0
<<<<<<< HEAD
        self.flechas = 1
        self.wumpus_morto = False
        self.pontos = 0
        self.ranking = ranking
=======
        self.pontuacao = 0  # Inicializa a pontuação
        self.ranking = ranking  # Armazena a referência ao ranking
>>>>>>> d3cfff039e0746b0f84d2b1ed25a71f3dc3f6f8c

    def exibirDificuldade(self):
        print("DIFICULDADES\n")
        for inx, value in enumerate(self.dificuldade):
            if inx == self.dif:
                print(f'> {value} <')
            else:
                print(f' {value}')

    def escDif(self):
<<<<<<< HEAD
        while True:
            tec = msvcrt.getch()
            os.system('cls')
            if tec == b'w' and self.dif > 0:
                self.dif -= 1
            elif tec == b's' and self.dif < len(self.dificuldade) - 1:
                self.dif += 1
            elif tec == b'\r':
                self.exe()
                return
            self.exibirDificuldade()
=======
        esc = input("escolha uma ação(W/S): \n").upper()
        if esc == "W" and self.dif > 0:
            self.dif -= 1
        elif esc == "S" and self.dif < len(self.dificuldade) - 1:
            self.dif += 1
        elif esc == "":
            self.exe()
>>>>>>> d3cfff039e0746b0f84d2b1ed25a71f3dc3f6f8c

    def exe(self):
        ex = self.dificuldade[self.dif]
        if ex == "Facíl(4x4)":
<<<<<<< HEAD
            self.caverna = Caverna(4, 3)
            self.posicao = (0, 0)
        elif ex == "Normal(6x6)":
            self.caverna = Caverna(6, 5)
            self.posicao = (0, 0)
        elif ex == "Dificil(10x10)":
            self.caverna = Caverna(10, 7)
            self.posicao = (0, 0)
        else:
            print("Dificuldade inválida! Usando 'normal' por padrão.")
            self.caverna = Caverna(6, 5)
=======
            self.caverna = Caverna(4, 1 , 1)  # Corrigido: Adicionando o número de abismos
            self.posicao = (0, 0)
        elif ex == "Normal(6x6)":
            self.caverna = Caverna(6, 1 , 2)  # Corrigido: Adicionando o número de abismos
            self.posicao = (0, 0)
        elif ex == "Dificil(10x10)":
            self.caverna = Caverna(10, 2 , 5)  # Corrigido: Adicionando o número de abismos
            self.posicao = (0, 0)
        else:
            print("Dificuldade inválida! Usando 'normal' por padrão.")
            self.caverna = Caverna(6, 1 , 2)  # Corrigido: Adicionando o número de abismos
>>>>>>> d3cfff039e0746b0f84d2b1ed25a71f3dc3f6f8c
            self.posicao = (0, 0)

    def cadastro(self):
        self.nome = input("Digite seu nome:\n")
        while True:
            os.system("cls")
            self.exibirDificuldade()
            self.escDif()
            if self.caverna:
                break
        self.jogar()
<<<<<<< HEAD

    def verificar_percepcao(self):
        percepcoes = []
        x, y = self.posicao
        adjacentes = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for i, j in adjacentes:
            if 0 <= i < self.caverna.tamanho and 0 <= j < self.caverna.tamanho:
                if (i, j) in self.caverna.buracos:
                    percepcoes.append("Brisa")
                elif (i, j) == self.caverna.ouro_pos:
                    percepcoes.append("Brilho")
                elif (i, j) == self.caverna.wumpus_pos:
                    percepcoes.append("Fedor")
        return percepcoes

    def disparar_flecha(self):
        if self.flechas > 0:
            print("Você tem uma flecha! Em qual direção você quer disparar? (W - Cima, S - Baixo, A - Esquerda, D - Direita)")
            direcao = msvcrt.getch().decode().lower()
            x, y = self.posicao
            if direcao == 'w' and x > 0:
                alvo = (x-1, y)
            elif direcao == 's' and x < self.caverna.tamanho - 1:
                alvo = (x+1, y)
            elif direcao == 'a' and y > 0:
                alvo = (x, y-1)
            elif direcao == 'd' and y < self.caverna.tamanho - 1:
                alvo = (x, y+1)
            else:
                print("Movimento inválido!")
                return

            if alvo == self.caverna.wumpus_pos:
                print("Você acertou o Wumpus com a flecha! O Wumpus morreu!")
                self.caverna.wumpus_pos = None
                self.wumpus_morto = True
                self.pontos += 100
                input("Pressione Enter para continuar jogando...")
                return True
            else:
                print("A flecha não acertou o Wumpus.")
                self.flechas -= 1
                input("Pressione Enter para continuar jogando...")
                return False
        else:
            print("Você não tem mais flechas!")
            input("Pressione Enter para continuar jogando...")
=======
>>>>>>> d3cfff039e0746b0f84d2b1ed25a71f3dc3f6f8c

    def jogar(self):
        while True:
            os.system("cls")
            self.caverna.exibir(self.posicao)
            percepcoes = self.verificar_percepcao()
            if percepcoes:
                print("Você sente:", ', '.join(percepcoes))

            if self.posicao in self.caverna.buracos:
                print("Você caiu em um poço! Fim de jogo.")
                self.pontos -= 10
                self.salvar_ranking()
                input("Pressione Enter para sair...")
                break

            if self.posicao == self.caverna.wumpus_pos and not self.wumpus_morto:
                print("Você encontrou o Wumpus! Você morreu!")
                self.pontos -= 10
                self.salvar_ranking()
                input("Pressione Enter para sair...")
                break
            if self.posicao == self.caverna.ouro_pos:
                print("Você encontrou o Ouro! Fim de jogo.")
                self.pontos += 100
                self.salvar_ranking()
                input("Pressione Enter para sair...")
                break

            print("Use W/A/S/D para mover-se (Q para fechar o jogo), ou 'F' para disparar uma flecha")
            move = msvcrt.getch().decode().lower()

<<<<<<< HEAD
            if move == "w" and self.posicao[0] > 0:
                self.posicao = (self.posicao[0] - 1, self.posicao[1])
                self.pontos -= 1
            elif move == "s" and self.posicao[0] < self.caverna.tamanho - 1:
                self.posicao = (self.posicao[0] + 1, self.posicao[1])
                self.pontos -= 1
            elif move == "a" and self.posicao[1] > 0:
                self.posicao = (self.posicao[0], self.posicao[1] - 1)
                self.pontos -= 1
            elif move == "d" and self.posicao[1] < self.caverna.tamanho - 1:
                self.posicao = (self.posicao[0], self.posicao[1] + 1)
                self.pontos -= 1
            elif move == "f":
                if self.disparar_flecha():
                    continue
            elif move == "q":
                print("Encerrando jogo..")
                self.salvar_ranking()
                return
            else:
                print("Movimento inválido..")

    def salvar_ranking(self):
        dificuldade = self.dificuldade[self.dif]
        self.ranking[dificuldade].append((self.nome, self.pontos))
        self.ranking[dificuldade].sort(key=lambda x: x[1], reverse=True)

class menuInicial:
    def __init__(self):
        self.menu = ["Novo Jogo", "Ranking", "Sair"]
        self.linha = 0
        self.ranking = {"Facíl(4x4)": [], "Normal(6x6)": [], "Dificil(10x10)": []}

    def exibirMenu(self):
        print("MENU PRINCIPAL")
        for i, v in enumerate(self.menu):
            if i == self.linha:
                print(f"> {v} <")
            else:
                print(f" {v}")

    def escolha(self):
        tecla = msvcrt.getch()
        if tecla == b'w' and self.linha > 0:
            self.linha -= 1
        elif tecla == b's' and self.linha < len(self.menu) - 1:
            self.linha += 1
        elif tecla == b'\r':
            self.executa()

    def executa(self):
        op = self.menu[self.linha]
        if op == "Sair":
            print("Saindo...\n")
            exit()
        elif op == "Ranking":
            self.mostrar_ranking()
        elif op == "Novo Jogo":
            nwgame = NovoJogo(self.ranking)
            nwgame.cadastro()

    def mostrar_ranking(self):
        for dificuldade, players in self.ranking.items():
            print(f"\nRanking {dificuldade}:")
            if players:
                for nome, pontos in players:
                    print(f"{nome}: {pontos} pontos")
            else:
                print("Ranking vazio!")
        input("Pressione Enter para voltar ao menu...")

    def run(self):
        while True:
            os.system('cls')
            self.exibirMenu()
            self.escolha()

menu = menuInicial()
menu.run()
=======
            move = input("use W/A/S/D para mover-se (Q para fechar o jogo): ").lower()
            if move in ["w", "s", "a", "d"]:
                self.mover(move)
            elif move == "q":
                print("encerrando jogo..")
                self.ranking.addPontos(self.nome, self.pontuacao)  # Adiciona a pontuação ao ranking ao sair
                break  # Termina o jogo
            else:
                print("movimento inválido..")

    def mover(self, direcao):
        x, y = self.posicao
        if direcao == "w" and x > 0:
            x -= 1
        elif direcao == "s" and x < self.caverna.tamanho - 1:
            x += 1
        elif direcao == "a" and y > 0:
            y -= 1
        elif direcao == "d" and y < self.caverna.tamanho - 1:
            y += 1

        self.posicao = (x, y)
        
        # Verifica se o jogador caiu em um abismo
        if self.posicao in self.caverna.abismos:
            print("Você caiu em um abismo! Jogo terminado.")
            self.ranking.addPontos(self.nome, self.pontuacao)
            exit()

        # Verifica se o jogador coletou um item
        if self.posicao in self.caverna.itens:
            self.pontuacao += 10  # Adiciona 10 pontos por item coletado
            self.caverna.itens.remove(self.posicao)  # Remove o item coletado
            self.caverna.mapa[x][y] = '[ ]'  # Remove a representação do item no mapa
            print(f"Você coletou um item! Pontuação: {self.pontuacao}")

class menuInicial:
        def __init__(self):
            self.menu = ["Novo Jogo", "Ranking", "Sair"]
            self.linha = 0
            self.pontos = Pontos()

        def exibirMenu(self):
            print("MENU PRINCIPAL")
            for i, v in enumerate(self.menu):
                if i == self.linha:
                    print(f"> {v} <")
                else:
                    print(f"  {v}")

        def escolha(self):
            escolha = input("escolha uma ação(W/S): \n").upper()
            if escolha == "W" and self.linha > 0:
                self.linha -= 1
            elif escolha == "S" and self.linha < len(self.menu) - 1:
                self.linha += 1
            elif escolha == "":
                self.executa()

        def executa(self):
            op = self.menu[self.linha]
            if op == "Sair":
                print("saindo...\n")
                exit()
            elif op == "Ranking":
                self.pontos.mostraPontos()
                input("Pressione Enter para voltar ao menu...")
            elif op == "Novo Jogo":
                nwgame = NovoJogo(self.pontos)  # Passa o ranking para o novo jogo
                nwgame.cadastro()

        def run(self):
            while True:
                os.system('cls')
                print()
                self.exibirMenu()
                self.escolha()


if __name__ == "__main__":
    menu = menuInicial()
    menu.run()
>>>>>>> d3cfff039e0746b0f84d2b1ed25a71f3dc3f6f8c
