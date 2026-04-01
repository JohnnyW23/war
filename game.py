import pygame
from random import randint, choice, shuffle
from modules.exercito import Exercito


class Game:

    def __init__(self, tropas):

        pygame.init()

        # FULLSCREEN
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.W, self.H = self.screen.get_size()

        pygame.display.set_caption("Simulador Militar")

        self.clock = pygame.time.Clock()
        self.running = True

        self.tropas = tropas
        self.logs = []

        self.font = pygame.font.SysFont("consolas", 16)
        self.font_title = pygame.font.SysFont("consolas", 20, bold=True)

        # LAYOUT

        self.INFO_RECT = pygame.Rect(20, 20, self.W - 40, 320)

        mapa_w = int(self.W * 0.65)

        self.MAPA_RECT = pygame.Rect(
            20,
            self.INFO_RECT.bottom + 20,
            mapa_w - 40,
            self.H - self.INFO_RECT.bottom - 40
        )

        self.LOG_RECT = pygame.Rect(
            mapa_w,
            self.INFO_RECT.bottom + 20,
            self.W - mapa_w - 20,
            self.MAPA_RECT.height
        )

        # Scroll do log
        self.log_scroll = 0

        # GRID DO MAPA

        self.TAMANHO = 20

        self.GRID_W = self.MAPA_RECT.width // self.TAMANHO
        self.GRID_H = self.MAPA_RECT.height // self.TAMANHO

        self.DIRECOES = [(1,0), (-1,0), (0,1), (0,-1)]

        self.grid = [[None for _ in range(self.GRID_H)] for _ in range(self.GRID_W)]

        self.gerar_mapa()

        self.loop()

    # ------------------------------------------------

    def log(self, texto):
        self.logs.append(texto)

    # ------------------------------------------------

    def grid_para_pixel(self, gx, gy):

        return (
            self.MAPA_RECT.x + gx * self.TAMANHO,
            self.MAPA_RECT.y + gy * self.TAMANHO
        )

    # ------------------------------------------------

    def dentro_do_mapa(self, gx, gy):
        return 0 <= gx < self.GRID_W and 0 <= gy < self.GRID_H

    # ------------------------------------------------

    def vazio(self, gx, gy):
        return self.grid[gx][gy] is None

    # ------------------------------------------------

    def ponto_inicial_aleatorio(self):

        while True:

            x = randint(0, self.GRID_W - 1)
            y = randint(0, self.GRID_H - 1)

            if self.vazio(x, y):
                return (x, y)

    # ------------------------------------------------

    def gerar_mapa(self):

        TERRITORIOS_POR_TROPA = 90

        for idx, tropa in enumerate(self.tropas):

            inicio = self.ponto_inicial_aleatorio()

            self.grid[inicio[0]][inicio[1]] = idx

            ocupados = {inicio}
            fronteira = [inicio]

            while len(ocupados) < TERRITORIOS_POR_TROPA and fronteira:

                base = choice(fronteira)

                shuffle(self.DIRECOES)

                expandiu = False

                for dx, dy in self.DIRECOES:

                    nx = base[0] + dx
                    ny = base[1] + dy

                    if self.dentro_do_mapa(nx, ny) and self.vazio(nx, ny):

                        self.grid[nx][ny] = idx

                        ocupados.add((nx, ny))
                        fronteira.append((nx, ny))

                        expandiu = True
                        break

                if not expandiu:
                    fronteira.remove(base)

            self.log(f"{tropa.nome} iniciou em {inicio}")

    # ------------------------------------------------

    def desenhar_cards(self):

        padding = 10
        total = len(self.tropas)

        largura = (self.INFO_RECT.width - (padding * (total + 1))) // total
        altura = self.INFO_RECT.height - padding * 2

        for i, exercito in enumerate(self.tropas):

            x = self.INFO_RECT.x + padding + i * (largura + padding)
            y = self.INFO_RECT.y + padding

            rect = pygame.Rect(x, y, largura, altura)

            pygame.draw.rect(self.screen, (20,20,20), rect, border_radius=6)
            pygame.draw.rect(self.screen, (200,200,200), rect, 1, border_radius=6)

            tx = rect.x + 10
            ty = rect.y + 10

            nome = self.font_title.render(exercito.nome, True, exercito.cor)
            self.screen.blit(nome, (tx, ty))
            ty += 25

            marechal = self.font.render(
                f"Marechal: {exercito.marechal['nome']}",
                True,
                (220,220,220)
            )
            self.screen.blit(marechal, (tx, ty))
            ty += 18

            perfil = self.font.render(
                f"Perfil: {exercito.marechal['perfil']}",
                True,
                (220,220,220)
            )
            self.screen.blit(perfil, (tx, ty))
            ty += 25

            linha = self.font.render(
                f"Poder {exercito.poder} | Território {exercito.territorio} | Flow {exercito.flow}%",
                True,
                (220,220,220)
            )
            self.screen.blit(linha, (tx, ty))
            ty += 25

            atributos = [
                f"Força: {exercito.forca}",
                f"Tecnologia: {exercito.tecnologia}",
                f"Suprimentos: {exercito.suprimentos}",
                f"Moral: {exercito.moral}",
                f"Estratégia: {exercito.estrategia}",
            ]

            for texto in atributos:

                t = self.font.render(texto, True, (200,200,200))
                self.screen.blit(t, (tx, ty))
                ty += 18

            ty += 5

            pib = self.font.render(
                f"PIB: {exercito.resumo['pib']:.2f}%",
                True,
                (100,255,100)
            )
            self.screen.blit(pib, (tx, ty))
            ty += 18

            inflacao = self.font.render(
                f"Inflação: {exercito.resumo['inflacao']:.2f}%",
                True,
                (100,255,100)
            )
            self.screen.blit(inflacao, (tx, ty))
            ty += 22

            titulo = self.font.render("Locais Dominados:", True, (220,220,220))
            self.screen.blit(titulo, (tx, ty))
            ty += 18

            for local in exercito.locais[:5]:

                texto = self.font.render(
                    f"• {local.nome_personalizado}",
                    True,
                    (180,180,180)
                )

                self.screen.blit(texto, (tx + 10, ty))
                ty += 16

    # ------------------------------------------------

    def desenhar_mapa(self):

        pygame.draw.rect(self.screen, (40,40,40), self.MAPA_RECT, 2)

        for x in range(self.GRID_W):

            for y in range(self.GRID_H):

                dono = self.grid[x][y]

                if dono is not None:

                    px, py = self.grid_para_pixel(x, y)

                    pygame.draw.rect(
                        self.screen,
                        self.tropas[dono].cor,
                        (px, py, self.TAMANHO, self.TAMANHO)
                    )

    # ------------------------------------------------

    def desenhar_logs(self):

        pygame.draw.rect(self.screen, (15,15,15), self.LOG_RECT)
        pygame.draw.rect(self.screen, (200,200,200), self.LOG_RECT, 1)

        visible_lines = self.LOG_RECT.height // 18
        start = max(0, len(self.logs) - visible_lines - self.log_scroll)
        end = start + visible_lines

        y = self.LOG_RECT.y + 10

        for log in self.logs[start:end]:

            texto = self.font.render(log, True, (220,220,220))
            self.screen.blit(texto, (self.LOG_RECT.x + 10, y))

            y += 18

    # ------------------------------------------------

    def loop(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                if event.type == pygame.MOUSEWHEEL:
                    self.log_scroll -= event.y
                    self.log_scroll = max(0, self.log_scroll)

            self.screen.fill((30,30,30))

            self.desenhar_cards()
            self.desenhar_mapa()
            self.desenhar_logs()

            pygame.display.flip()

            self.clock.tick(60)


# ------------------------------------------------

classico1 = Exercito("Saint Louis", (255,56,62), "Resistência Popular", "RSP")
classico2 = Exercito("Viena Empire", (0,208,255), "Voz Patriótica", "VPT")
classico3 = Exercito("República Ashbury", (0,255,0), "Som da Liberdade", "SDL")
#classico4 = Exercito("Alta Galileia", (244,108,255), "Sanctum Dominium", "SDM")

classicos = [classico1, classico2, classico3] #, classico4]

for tropa in classicos:    
    tropa.gerar_locais()

Game(classicos)