class Tempo:
    def __init__(self, guerra):
        self.dia = 1
        self.hora = 0
        self.minutos = 0
        self.segundos = 0

        self.guerra = guerra

        self.clima = self.escolher_clima()

        # controla chance crescente por ciclo
        self.chance_evento = 0.0  
        self.incremento = 0.05  # 5% por tick
    

    def atualizar_horario(self):
        self.horario = f"{self.hora}:{self.minutos}:{self.segundos}"


    def tick(self, tropa, midia):
        from time import sleep

        while True:

            sleep(0.5)
            self.hora = int(self.hora) + 1

            if self.hora == 24:
                self.guerra.concluir_dia()
                self.guerra.tabela_guerra()
                sleep(1)
            
            return self.checar_evento(tropa, midia)
    

    def formatar_horario(self):
        from random import randint

        self.minutos = randint(1, 59)
        self.segundos = randint(1, 59)

        if int(self.hora) < 10:
            self.hora = f'0{int(self.hora)}'
        if self.minutos < 10:
            self.minutos = f'0{self.minutos}'
        if self.segundos < 10:
            self.segundos = f'0{self.segundos}'

    def checar_evento(self, tropa, midia):
        # aumenta chance progressivamente
        from random import random, choices, randint
        from rich.console import Console
        from time import sleep

        self.chance_evento += self.incremento

        for exercito in self.guerra.tropas_ativas:
            if exercito.operacao_marechal:
                if self.guerra.verificar_operacao_marechal(exercito):
                    self.guerra.executar_operacao_marechal(exercito)
                    return True

        dado1 = randint(1, 130)
        dado2 = randint(1, 130)

        if dado1 == dado2:
            self.atualizar_horario()
            self.guerra.evento_especial(tropa)
            midia.resumo["mortos"] += randint(20, 40)
            return True

        if random() < self.chance_evento:
            # evento acontece
            self.chance_evento = 0  # reset
            self.formatar_horario()
            self.atualizar_horario()

            func = choices(
                [e for e, _ in self.guerra.eventos],
                weights=[p for _, p in self.guerra.eventos],
                k=1
            )[0]
            func(tropa)

            midia.resumo["mortos"] += randint(5, 20)

            for exercito in self.guerra.exercitos:
                self.guerra.verificar_resultado(exercito)
            
            return True
        
        if random() <= 0.1 and self.dia > 1:
            self.formatar_horario()
            self.atualizar_horario()
            noticia = midia.gerar_noticia()
            Console().print(f"[yellow][{self.horario}] [italic]{noticia}[/italic][/yellow]")
            sleep(1)
        
        return False
    

    def escolher_clima(self):
        from random import choices

        climas = {
            "ensolarado": ("☀️", 0.25),
            "nublado": ("☁️", 0.20),
            "chuva leve": ("🌦️", 0.15),
            "chuva forte": ("🌧️", 0.07),
            "tempestade": ("⛈️", 0.05),
            "tormenta elétrica": ("🌩️", 0.03),
            "ventania": ("💨", 0.10),
            "nevoeiro": ("🌫️", 0.05),
            "frio": ("🥶", 0.05),
            "calor extremo": ("🔥", 0.05)
        }

        nomes = list(climas.keys())
        probabilidades = [climas[c][1] for c in nomes]
        
        clima_escolhido = choices(nomes, weights=probabilidades, k=1)[0]
        emoji = climas[clima_escolhido][0]
        
        return [clima_escolhido.capitalize(), emoji]


    def descrever_marechal(self, novo=False):
        from time import sleep
        from rich.console import Console

        console = Console()

        if novo:
            console.print(f"[italic]           Um novo marechal para {self.nome} foi escolhido. Ele se chama {self.marechal['nome']}, e tem um perfil {self.marechal['perfil_estilizado']}.[/italic]")
        else:
            console.print(f"[italic]O marechal de {self.nome} se chama {self.marechal['nome']}, que tem um perfil {self.marechal['perfil_estilizado']}.[/italic]")
        sleep(2)