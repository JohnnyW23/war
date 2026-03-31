import pygame
from random import choice, shuffle, randint

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# =====================
# CONFIGURAÇÕES
# =====================
TAMANHO = 20
TERRITORIOS_POR_TROPA = 90

MAPA_RECT = pygame.Rect(40, 100, 620, 580)

GRID_W = MAPA_RECT.width // TAMANHO
GRID_H = MAPA_RECT.height // TAMANHO

# Tropas
tropas = [
    {"nome": "Alpha", "cor": (220, 60, 60)},
    {"nome": "Bravo", "cor": (60, 220, 60)},
    {"nome": "Charlie", "cor": (60, 100, 220)},
    {"nome": "Delta", "cor": (180, 200, 40)}
]

# Grid do mapa (None = vazio, int = índice da tropa)
grid = [[None for _ in range(GRID_H)] for _ in range(GRID_W)]

# Direções (somente vizinhos laterais)
DIRECOES = [(1,0), (-1,0), (0,1), (0,-1)]

# =====================
# FUNÇÕES
# =====================
def grid_para_pixel(gx, gy):
    return (
        MAPA_RECT.x + gx * TAMANHO,
        MAPA_RECT.y + gy * TAMANHO
    )


def dentro_do_mapa(gx, gy):
    return 0 <= gx < GRID_W and 0 <= gy < GRID_H


def vazio(gx, gy):
    return grid[gx][gy] is None


def ponto_inicial_aleatorio():
    while True:
        x = randint(0, GRID_W - 1)
        y = randint(0, GRID_H - 1)
        if vazio(x, y):
            return (x, y)

# =====================
# GERAÇÃO DAS TROPAS
# =====================
for idx, tropa in enumerate(tropas):

    # 🔹 ponto inicial aleatório e vazio
    inicio = ponto_inicial_aleatorio()

    grid[inicio[0]][inicio[1]] = idx
    ocupados = {inicio}
    fronteira = [inicio]

    while len(ocupados) < TERRITORIOS_POR_TROPA and fronteira:
        base = choice(fronteira)
        shuffle(DIRECOES)

        expandiu = False
        for dx, dy in DIRECOES:
            nx, ny = base[0] + dx, base[1] + dy

            if dentro_do_mapa(nx, ny) and vazio(nx, ny):
                grid[nx][ny] = idx
                ocupados.add((nx, ny))
                fronteira.append((nx, ny))
                expandiu = True
                break

        if not expandiu:
            fronteira.remove(base)

    print(f"{tropa['nome']} iniciou em {inicio} e criou {len(ocupados)} territórios")

# =====================
# LOOP PRINCIPAL
# =====================
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((235, 235, 235))

    # Borda do mapa
    pygame.draw.rect(screen, (20, 20, 20), MAPA_RECT, 2)

    # Territórios
    for x in range(GRID_W):
        for y in range(GRID_H):
            dono = grid[x][y]
            if dono is not None:
                px, py = grid_para_pixel(x, y)
                pygame.draw.rect(
                    screen,
                    tropas[dono]["cor"],
                    (px, py, TAMANHO, TAMANHO)
                )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
