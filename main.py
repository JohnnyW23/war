from time import sleep
from rich.console import Console
from modules.exercito import Exercito
from modules.guerra import Guerra
from modules.midia import Midia


tropa1 = Exercito("Saint Louis", "blink bold #ff383e underline", "Resistência Popular", "RSP")
tropa2 = Exercito("Viena Empire", "blink bold #00d0ff underline", "Voz Patriótica", "VPT")
tropa3 = Exercito("República Ashbury", "blink bold #00ff00 underline", "Som da Liberdade", "SDL")
tropa4 = Exercito("Alta Galileia", "blink bold pink1 underline", "Sanctum Dominium", "SDM")

tropas = [tropa1, tropa2, tropa3, tropa4]

for tropa in tropas:
    for inimigo in tropas:
        if tropa != inimigo:
            tropa.inimigos.append(inimigo)

midia = Midia()

guerra = Guerra(tropas)

console = Console()

guerra.tabela_guerra()
sleep(1)

while guerra.ativa:

    for tropa in guerra.tropas_ativas:

        guerra.tempo.tick(tropa, midia)
        
        if not guerra.ativa:
            break
