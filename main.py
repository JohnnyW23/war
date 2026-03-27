from random import choices, randint, uniform
from time import sleep
from rich.console import Console

from modules.exercito import Exercito
from modules.guerra import Guerra
from modules.midia import Midia


tropa1 = Exercito("Saint Louis", "blink bold #ff383e underline", "Resistência Popular", "RSP")
tropa2 = Exercito("Viena Empire", "blink bold #00d0ff underline", "Voz Patriótica", "VPT")

tropas = [tropa1, tropa2]

for tropa in tropas:
    for inimigo in tropas:
        if tropa != inimigo:
            tropa.inimigo = inimigo

midia = Midia(tropas)

guerra = Guerra(tropas)

console = Console()

guerra.tabela_guerra()
sleep(1)

while guerra.ativa:

    for tropa in guerra.tropas_ativas:

        if guerra.tempo.tick(tropa, midia) or not guerra.ativa:
            break
