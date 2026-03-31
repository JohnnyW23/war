from time import sleep
from rich.console import Console
from modules.exercito import Exercito
from modules.guerra import Guerra
from modules.midia import Midia


classico1 = Exercito("Saint Louis", "blink bold #ff383e underline", "Resistência Popular", "RSP")
classico2 = Exercito("Viena Empire", "blink bold #00d0ff underline", "Voz Patriótica", "VPT")
classico3 = Exercito("República Ashbury", "blink bold #00ff00 underline", "Som da Liberdade", "SDL")
classico4 = Exercito("Alta Galileia", "blink bold pink1 underline", "Sanctum Dominium", "SDM")

classicos = [classico1, classico2, classico3, classico4]

tropas = classicos

for tropa in tropas:    
    tropa.gerar_locais()
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
