class Exercito:
    def __init__(self, nome, cor, canal_nome, canal_sigla):
        from random import uniform

        self.nome = f"[{cor}]{nome}[/{cor}]"
        self.nome_colorido = f"[{cor}]{nome}[/{cor}]"
        self.nome_derrotado = f"[grey30]{nome}[/grey30]"
        self.poder = 1
        self.flow = 0
        self.territorio = 300
        self.forca = 400
        self.tecnologia = 200
        self.suprimentos = 200
        self.moral = 200
        self.estrategia = 200
        self.marechal = self.escolher_marechal()
        self.inimigos = []

        self.canal_nome = canal_nome
        self.canal_sigla = canal_sigla

        self.resumo = {
            "pib": round(uniform(0.1, 1), 2),
            "inflacao": round(uniform(1, 3), 2)
        }

        self.placar_seguido = {
            "primeira": False,
            "streak": 0
        }

        self.operacao = False

        self.operacao_marechal = False
    

    def escolher_marechal(self):
        import json
        from random import choice

        with open("names.json", "r", encoding="utf-8") as f:
            names = json.load(f)
        
        marechais = [name['name'] for name in names if name['gender'] == 'male' or name['gender'] == 'unisex']

        perfis = [
            ["Agressivo", "orange1"],
            ["Cauteloso", "bright_blue"],
            ["Equilibrado", "bright_black"],
            ["Oportunista", "gold1"],
            ["Arrogante", "magenta1"],
            ["Estrategista", "blue_violet"],
            ["Sanguinário", "red1"],
            ["Político", "chartreuse1"],
            ["Instável", "dark_red"]
        ]

        """
        equilibrado: nada acontece
        agressivo: 2x mais dano dado e 2x mais dano recebido
        cauteloso: 0.5x dano dado e 0.5x dano recebido
        oportunista: se a diferença dos dados for grande atacando, dá mais dano, mas se for pequena atacando, dá menos dano
        arrogante: se estiver ganhando por muita diferença, recebe mais dano, e se estiver perdendo por muita diferença, recebe menos dano
        estrategista: se estiver ganhando, dá menos dano, se estiver perdendo, dá mais dano
        sanguinario: vitórias seguidas dão um bonus acumulativo. derrotas seguidas são o mesmo bonus acumulativo
        politico: mais chance do inimigo se render
        instavel: pequena chance de converter vitórias em derrotas, e vice versa (esse terá informação inclusive caso seja ativado)
        """

        marechal = choice(marechais)
        perfil_info = choice(perfis)
        cor = perfil_info[1]
        perfil = perfil_info[0]
        perfil_estilizado = f'[bold {cor}]{perfil}[/bold {cor}]'

        return {
            "nome": f"[bold underline white]{marechal}[/bold underline white]",
            "perfil_estilizado": perfil_estilizado,
            "perfil": perfil
        }


    def descrever_marechal(self, novo=False):
        from time import sleep
        from rich.console import Console

        console = Console()

        if novo:
            console.print(f"[italic]           Um novo marechal para {self.nome} foi escolhido. Ele se chama {self.marechal['nome']}, e tem um perfil {self.marechal['perfil_estilizado']}.[/italic]")
        else:
            console.print(f"[italic]O marechal de {self.nome} se chama {self.marechal['nome']}, que tem um perfil {self.marechal['perfil_estilizado']}.[/italic]")
        sleep(2)


    def calcular_poder_total(self):
        return self.forca + self.tecnologia + self.suprimentos + self.moral + self.estrategia
