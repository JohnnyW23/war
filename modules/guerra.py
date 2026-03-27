from modules.evento import Evento
from modules.tempo import Tempo
from rich.console import Console

console = Console()

class Guerra:
    def __init__(self, exercitos):

        self.exercitos = exercitos
        self.tropas_ativas = exercitos

        self.tempo = Tempo(self)

        self.eventos = [
            (self.ataque, 2),
            (self.sorte, 0.4),
            (self.melhoria, 0.5),
            (self.clima, 0.5),
            (self.tecnologia, 1),
            (self.suprimentos, 1),
            (self.moral, 1),
            (self.estrategia, 1),
            (self.inteligencia, 0.75),
        ]

        self.ativa = True        

        
    def ataque(self, a):
        eventos = [
            Evento(
                a,
                f"{a.nome} lança uma série de misseis contra as tropas de {a.inimigo.nome}.",
                "O ataque é bem-sucedido, causando danos significativos.",
                lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                f"O ataque falha, seguido de uma forte retaliação de {a.inimigo.nome}.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),
            Evento(
                a,
                f"{a.nome} tenta uma ofensiva terrestre contra {a.inimigo.nome}.",
                "A ofensiva é bem-sucedida, conquistando território inimigo.",
                lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                "A ofensiva é repelida, resultando em baixas para o exército atacante.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),
            Evento(
                a,
                f"{a.nome} realiza um ataque aéreo contra {a.inimigo.nome}.",
                "O ataque aéreo é bem-sucedido, destruindo alvos estratégicos inimigos.",
                lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                f"O ataque aéreo falha, e algumas aeronaves de {a.nome} são abatidas.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),
            Evento(
                a,
                f"Embarcações de {a.nome} iniciam uma ofensiva contra as frotas de {a.inimigo.nome}.",
                "O ataque naval é bem-sucedido, destruindo grande parte dos navios inimigos.",
                lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                "O ataque naval falha, resultando em perdas para o exército atacante.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),
            Evento(
                a,
                f"{a.nome} e {a.inimigo.nome} iniciam um confronto direto na fronteira.",
                f"O confronto direto é vencido por {a.nome}, causando grandes perdas ao inimigo.",
                lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                f"O confronto direto é vencido por {a.inimigo.nome}, causando grandes perdas ao exército atacante.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            )
        ]

        self.calcular_conclusao(eventos)


    def sorte(self, a):
        from math import ceil
        
        eventos = [
            Evento(
                a, 
                f"{a.nome} encontra um depósito militar abandonado.",
                f"O depósito contém equipamentos valiosos, fortalecendo as tropas de {a.nome}.",
                lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                f"O depósito está deteriorado e parte do equipamento explode acidentalmente.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),
            Evento(
                a, 
                f"Um informante aparece oferecendo dados sigilosos a {a.nome}.",
                f"As informações revelam vulnerabilidades do inimigo, aumentando a vantagem estratégica.",
                lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                f"O informante era falso e espalha desinformação, confundindo {a.nome}.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),
            Evento(
                a, 
                f"{a.nome} desenvolve um protótipo de IA integrado a sistemas bélicos.",
                f"O protótipo funciona, elevando o nível tecnológico de {a.nome}.",
                lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                f"O protótipo falha e corrompe dados de alguns sistemas.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),
            Evento(
                a, 
                f"Forças aliadas auxiliam {a.nome} com novos soldados.",
                f"As tropas adicionais elevam a moral e o poder militar de {a.nome}.",
                lambda: (setattr(a, 'forca', ceil(a.forca + self.poder_do_round / 2)),
                        setattr(a, 'moral', ceil(a.moral + self.poder_do_round / 2))),
                f"Os reforços estavam mal treinados e atrapalham a organização de {a.nome}.",
                lambda: (setattr(a, 'forca', ceil(a.forca - self.poder_do_round / 2)),
                        setattr(a, 'moral', ceil(a.moral - self.poder_do_round / 2)))
            ),
            Evento(
                a, 
                f"{a.nome} recupera uma caravana de suprimentos extraviada.",
                f"Os suprimentos fortalecem as reservas e apoiam as operações militares.",
                lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                f"Parte da caravana estava contaminada e inutilizável.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),
            Evento(
                a, 
                f"Um comandante renomado oferece seus serviços a {a.nome}.",
                f"A liderança dele melhora a estratégia e a moral das tropas.",
                lambda: (setattr(a, 'estrategia', ceil(a.estrategia + self.poder_do_round / 2)),
                        setattr(a, 'moral', ceil(a.moral + self.poder_do_round / 2))),
                f"O comandante era incompetente e causa confusão nas fileiras.",
                lambda: (setattr(a, 'estrategia', ceil(a.estrategia - self.poder_do_round / 2)),
                        setattr(a, 'moral', ceil(a.moral - self.poder_do_round / 2)))
            ),
            Evento(
                a, 
                f"Uma equipe brilhante de engenheiros desenvolve novos aparatos para {a.nome}.",
                f"Os engenheiros criam melhorias rápidas nos equipamentos e sistemas de {a.nome}.",
                lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                f"Os engenheiros acabam causando mais problemas do que soluções.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),
            Evento(
                a, 
                f"{a.nome} abre caminho para uma nova rota de suprimentos.",
                f"A rota fornece recursos que fortalecem as operações militares.",
                lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                f"A rota estava comprometida e os suprimentos são emboscados.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),
            Evento(
                a, 
                f"O Presidente da nação de {a.nome} dirige um grande discurso para suas tropas.",
                f"As palavras fortalecem o espírito das tropas e revitalizam a moral.",
                lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                f"O discurso é mal interpretado e causa confusão entre os soldados.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),
            Evento(
                a, 
                f"Uma equipe científica oferece um novo algoritmo tático para {a.nome}.",
                f"O algoritmo otimiza estratégias e aumenta o desempenho em combate.",
                lambda: (setattr(a, 'forca', a.forca + self.poder_do_round),
                        setattr(a, 'estrategia', ceil(a.estrategia + self.poder_do_round / 2))),
                f"O algoritmo contém erros críticos, prejudicando o combate e planejamento.",
                lambda: (setattr(a, 'forca', a.forca - self.poder_do_round),
                        setattr(a, 'estrategia', ceil(a.estrategia - self.poder_do_round / 2)))
            ),
            Evento(
                a, 
                f"Guerrilheiros se juntam a {a.nome} para combater o inimigo.",
                f"A ajuda dos civis traz suprimentos e aumenta a moral das tropas.",
                lambda: (setattr(a, 'suprimentos', ceil(a.suprimentos + self.poder_do_round / 2)),
                        setattr(a, 'moral', ceil(a.moral + self.poder_do_round / 2))),
                f"A ajuda dos civis atrapalha e desorganiza a logística das tropas.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),
            Evento(
                a, 
                f"{a.nome} encontra uma arma experimental inimiga em meio ao campo de batalha.",
                f"A arma é muito eficaz e aumenta drasticamente o poder de fogo.",
                lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                f"A arma continha rastreador e escuta, revelando locais e estratégias da tropa.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),
            Evento(
                a, 
                f"{a.nome} encontra um manual de estratégia militar do inimigo.",
                f"As táticas descritas aprimoram o planejamento de batalha.",
                lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                f"O manual contém táticas ultrapassadas que causam desorganização.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),
            Evento(
                a, 
                f"{a.nome} consegue reativar uma fábrica obsoleta de armamentos.",
                f"A produção improvisada reforça o poder militar.",
                lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                f"A fábrica contém falhas estruturais e acaba inutilizável.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),
            Evento(
                a, 
                f"Tropas de {a.nome} recebem uma remessa de mantimentos das forças aliadas.",
                f"Os mantimentos melhoram a eficiência das tropas.",
                lambda: (setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round)),
                f"A remessa estava estragada e causa problemas logísticos.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),
            Evento(
                a, 
                f"{a.nome} consegue decodificar arquivos de dados pré-guerra.",
                f"Os arquivos revelam técnicas úteis e melhoram o conhecimento tecnológico.",
                lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                f"Os dados estavam comprometidos e comprometem sistemas internos.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            )
        ]

        self.calcular_conclusao(eventos)


    def melhoria(self, a):
        eventos = [
            Evento(
                a, 
                f"{a.nome} desenvolve um novo programa intensivo de treinamento militar.",
                f"O treinamento aumenta significativamente a força de combate de {a.nome}.",
                lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                f"O treinamento é mal executado e causa exaustão nas tropas.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} começa a testar em campo equipamentos modernizados.",
                f"A modernização aumenta o nível tecnológico de {a.nome}.",
                lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                f"A modernização apresenta falhas táticas, necessitando de revisão.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} lança uma campanha de motivação entre as tropas.",
                f"A moral das tropas aumenta consideravelmente.",
                lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                f"A campanha não surte efeito e gera desconfiança.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} realiza uma operação de reorganização estratégica.",
                f"A coordenação e estratégia melhoram significativamente.",
                lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                f"A reorganização causa conflitos internos.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} decide otimizar linhas de suprimentos.",
                f"A eficiência logística aumenta e suprimentos são economizados.",
                lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                f"A otimização é mal planejada e gera desperdício.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} realiza testes de novas táticas de combate.",
                f"As tropas assimilam as táticas e ganham eficiência.",
                lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                f"As táticas se mostram confusas e ineficazes.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} reorganiza o setor de manutenção de equipamentos.",
                f"A manutenção eficaz aumenta o poder tecnológico das tropas.",
                lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                f"A reorganização atrasa operações críticas.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} realiza exercícios militares em larga escala.",
                f"Os exercícios aumentam a força e a disciplina das tropas.",
                lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                f"Os exercícios resultam em lesões e quedas de desempenho.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} adota novos protocolos de comunicação.",
                f"A organização interna melhora, elevando a estratégia.",
                lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                f"Os protocolos confundem unidades e causam erros.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} decide investir em estoque de munições.",
                f"O abastecimento eficiente melhora os suprimentos disponíveis.",
                lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                f"Erros de cálculo dificultam a logística e gera descartes.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} inicia um programa de bem-estar para soldados.",
                f"A moral aumenta e o desempenho das tropas melhora.",
                lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                f"O programa é mal gerido e causa frustração.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} contrata consultores militares especializados.",
                f"As orientações aumentam a precisão estratégica das tropas.",
                lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                f"As consultorias são ineficazes e descoordenam as unidades.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} realiza manutenção geral nas estruturas de apoio.",
                f"As melhorias nas instalações elevam os suprimentos disponíveis.",
                lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                f"A manutenção causa interrupções operacionais.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} implanta um novo sistema de identificação de alvos.",
                f"O sistema melhora a eficiência tecnológica em combate.",
                lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                f"O sistema apresenta falhas e reduz a confiabilidade.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a, 
                f"{a.nome} investe em treinamento tático avançado.",
                f"O treinamento melhora estratégias e aumenta a precisão operacional.",
                lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                f"O treinamento é mal coordenado e causa queda de rendimento.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            )
        ]
        
        self.calcular_conclusao(eventos)


    def clima(self, a):
        eventos = {
            "ensolarado": [
                Evento(
                    a, 
                    f"O clima ensolarado favorece exercícios de campo para {a.nome}.",
                    f"Os treinos sob sol melhoram o condicionamento físico das tropas de {a.nome}.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"O calor intenso atrapalha o rendimento dos soldados de {a.nome}.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),

                Evento(
                    a, 
                    f"O clima ensolarado permite que {a.nome} opere painéis solares adicionais.",
                    f"A energia extra aumenta a tecnologia operacional de {a.nome}.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"Equipamentos superaquecem devido ao sol excessivo.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O sol forte desgasta os suprimentos de {a.nome}.",
                    f"As tropas conseguem se adaptar e minimizar as perdas.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),  # leve recuperação
                    f"O calor acelera a deterioração e causa perdas em suprimentos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                ),

                Evento(
                    a, 
                    f"O clima ensolarado prolongado afeta o moral de {a.nome}.",
                    f"As tropas usam o bom clima para atividades recreativas, recuperando ânimo.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"O desgaste pelo calor reduz o moral das tropas.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O clima ensolarado cria condições ideais para movimentação tática.",
                    f"{a.nome} aproveita para consolidar posições e ganhar força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"{a.inimigo.nome} usa o clima para treinos coordenados, aprimorando estratégia.",
                    lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O calor intenso do clima ensolarado causa desgaste geral nas tropas.",
                    f"{a.inimigo.nome} tem queda de moral devido à exaustão térmica.",
                    lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                    f"{a.nome} sofre com perda de suprimentos devido ao calor.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                )
            ],
            "nublado": [
                Evento(
                    a, 
                    f"O clima nublado cria condições ideais para movimentações silenciosas.",
                    f"As tropas de {a.nome} usam a visibilidade reduzida para melhorar táticas furtivas.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"A visibilidade reduzida causa pequenas descoordenações entre as unidades de {a.nome}.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O clima nublado facilita longas marchas para {a.nome}.",
                    f"As tropas aproveitam o clima ameno para reforçar sua força física.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"O clima cinzento deixa as tropas desmotivadas e lentas.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A falta de luz direta atrapalha sistemas ópticos de {a.nome}.",
                    f"As tropas conseguem ajustar os equipamentos e minimizar o impacto.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"Os sensores sofrem interferência e reduzem a eficiência tecnológica.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O clima nublado afeta a moral das tropas de {a.nome}.",
                    f"O comando usa o clima ameno para realizar atividades e elevar o humor.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"O ambiente escuro e cinza reduz o ânimo e foco das tropas.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O clima nublado reduz a visibilidade, abrindo espaço para manobras criativas.",
                    f"{a.nome} aproveita para reorganizar discretamente suas posições, aumentando estratégia.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"{a.inimigo.nome} utiliza a baixa visibilidade para movimentações rápidas, fortalecendo a força.",
                    lambda: setattr(a.inimigo, 'forca', a.inimigo.forca + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O clima nublado cria instabilidade no campo de batalha.",
                    f"A baixa luminosidade reduz a precisão e o moral de {a.inimigo.nome}.",
                    lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                    f"A umidade do clima afeta munições e reduz os suprimentos de {a.nome}.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                )
            ],
            "chuva leve": [
                Evento(
                    a, 
                    f"A chuva leve cria um ambiente ideal para camuflagem natural de {a.nome}.",
                    f"As tropas usam o clima para se infiltrar melhor, aumentando estratégia.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"A chuva atrapalha a movimentação silenciosa e gera falhas táticas.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva leve resfria o terreno, permitindo avanços mais longos para {a.nome}.",
                    f"As tropas progridem com menor desgaste, aumentando força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"O terreno úmido causa escorregões e pequenos acidentes nas tropas.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva leve danifica levemente partes dos equipamentos de {a.nome}.",
                    f"As unidades conseguem secar os equipamentos e evitar danos permanentes.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),  # recuperação leve
                    f"A umidade prejudica sensores e sistemas táticos, reduzindo tecnologia.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva leve deixa o ambiente melancólico para {a.nome}.",
                    f"A liderança usa a situação para inspirar as tropas, elevando moral.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"A chuva constante afeta o ânimo das tropas, reduzindo moral.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva leve suaviza ruídos no campo de batalha.",
                    f"{a.nome} aproveita para fortalecer suprimentos discretamente.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                    f"{a.inimigo.nome} utiliza a mesma vantagem sonora para treinar movimentos táticos.",
                    lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva leve torna o solo escorregadio e imprevisível.",
                    f"{a.inimigo.nome} sofre com redução de suprimentos por avarias causadas pela umidade.",
                    lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                    f"{a.nome} perde parte de sua força devido a acidentes menores.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                )
            ],
            "chuva forte": [
                Evento(
                    a, 
                    f"A chuva forte encobre sons e permite que {a.nome} execute manobras furtivas.",
                    f"As tropas usam a cobertura sonora para aprimorar táticas discretas.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"A chuva excessiva impede coordenação e atrapalha os movimentos.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva forte dificulta ataques inimigos à distância contra {a.nome}.",
                    f"As tropas aproveitam o clima para avançar de forma mais segura, aumentando força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"O progresso é lento e exaustivo devido ao terreno encharcado.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva forte afeta sistemas eletrônicos de {a.nome}.",
                    f"As equipes técnicas conseguem reparar parte dos danos no local.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),  # leve mitigação
                    f"Os dispositivos falham com frequência devido à umidade intensa.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva forte deteriora suprimentos essenciais de {a.nome}.",
                    f"As tropas improvisam abrigos e salvam parte dos recursos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos +self.poder_do_round),
                    f"A água invade depósitos e arruina parte dos suprimentos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva forte reduz drasticamente a visibilidade no campo.",
                    f"{a.nome} usa isso para reforçar posições defensivas, aumentando estratégia.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"{a.inimigo.nome} realiza movimentações rápidas sem ser detectado, aumentando força.",
                    lambda: setattr(a.inimigo, 'forca', a.inimigo.forca + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A chuva forte transforma o terreno em puro lamaçal.",
                    f"{a.inimigo.nome} sofre danos nos equipamentos, reduzindo tecnologia.",
                    lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                    f"{a.nome} perde moral devido ao desgaste físico constante.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                )
            ],
            "tempestade": [
                Evento(
                    a, 
                    f"A tempestade cria um estrondo constante que abafa sons de movimentação.",
                    f"{a.nome} usa o barulho para reposicionar tropas sem ser detectado, melhorando estratégia.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"O barulho excessivo causa falhas de comunicação entre as unidades de {a.nome}.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A tempestade derruba estruturas leves no campo, dificultando ataques inimigos.",
                    f"{a.nome} aproveita o momento para reforçar suas defesas, aumentando força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"As tropas de {a.nome} têm dificuldade para manter posições no vento extremo.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"Os ventos violentos da tempestade afetam severamente dispositivos eletrônicos.",
                    f"As equipes técnicas de {a.nome} salvam parte dos sistemas.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"Equipamentos entram em curto devido à tempestade e prejudicam tecnologia de {a.nome}.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A tempestade encharca profundamente depósitos de suprimentos de {a.nome}.",
                    f"A tropa improvisa proteção emergencial e salva parte dos mantimentos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                    f"A água invade armazéns e arruina suprimentos críticos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A tempestade cria caos natural, abrindo oportunidades inesperadas.",
                    f"{a.nome} usa o clima para melhorar técnicas de adaptação, elevando moral.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"{a.inimigo.nome} usa o caos climático para movimentos agressivos, aumentando força.",
                    lambda: setattr(a.inimigo, 'forca', a.inimigo.forca + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A tempestade causa destruição generalizada em todo o campo de batalha.",
                    f"{a.inimigo.nome} sofre danos em dispositivos sensíveis, perdendo tecnologia.",
                    lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                    f"{a.nome} perde moral devido às condições severas e à exaustão.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                )
            ],
            "tormenta elétrica": [
                Evento(
                    a, 
                    f"A tormenta elétrica causa interferência nas comunicações inimigas.",
                    f"{a.nome} aproveita o momento para aprimorar suas táticas sem risco de interceptação.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"A instabilidade elétrica também atinge sistemas de {a.nome}, criando confusão.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A forte atividade elétrica energiza equipamentos de captação de energia de {a.nome}.",
                    f"A energia acumulada melhora o desempenho tecnológico das unidades.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"A carga elétrica inesperada queima circuitos sensíveis.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"Descargas elétricas atingem áreas próximas às tropas de {a.nome}.",
                    f"As tropas conseguem se reposicionar e evitar perigo imediato.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"Relâmpagos danificam equipamentos e ferem soldados, reduzindo força.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                    Evento(
                    a, 
                    f"A tormenta elétrica deixa sensores e radares instáveis para {a.nome}.",
                    f"A equipe técnica improvisa ajustes para minimizar danos.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"A interferência elétrica afeta seriamente a capacidade tecnológica.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A tormenta elétrica cria janelas de instabilidade nos sistemas do campo todo.",
                    f"{a.nome} aproveita para reforçar protocolos de segurança, aumentando tecnologia.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"{a.inimigo.nome} usa a escuridão intermitente para fortalecer estratégias furtivas.",
                    lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A tormenta elétrica causa sobrecarga generalizada no campo.",
                    f"{a.inimigo.nome} sofre queda abrupta de moral devido ao caos dos relâmpagos.",
                    lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                    f"{a.nome} perde suprimentos devido a explosões em depósitos energizados.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                )
            ],
            "ventania": [
                Evento(
                    a, 
                    f"A ventania dispersa poeira e reduz a precisão inimiga contra {a.nome}.",
                    f"{a.nome} aproveita a cobertura natural para reposicionar tropas, melhorando estratégia.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"A poeira levantada pela ventania também afeta a coordenação das tropas.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A ventania impede ataques aéreos inimigos contra {a.nome}.",
                    f"{a.nome} aproveita a janela climática para reforçar posições, aumentando força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"Os ventos dificultam a estabilização das fileiras e reduzem força temporariamente.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A ventania derruba equipamentos frágeis de {a.nome}.",
                    f"As tropas conseguem recolher parte dos materiais danificados.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                    f"O vento destrói elementos essenciais do estoque, reduzindo suprimentos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A ventania dificulta a comunicação entre unidades de {a.nome}.",
                    f"As tropas adaptam sinais manuais para minimizar perdas de moral.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"O vento constante cria ruído e confusão, reduzindo moral.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A ventania muda padrões de movimentação no campo de batalha.",
                    f"{a.nome} usa o clima para fortalecer sua estratégia defensiva.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"{a.inimigo.nome} aproveita o vento para executar ataques rápidos e aumentar força.",
                    lambda: setattr(a.inimigo, 'forca', a.inimigo.forca + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A ventania alcança níveis perigosos, criando caos estrutural.",
                    f"{a.inimigo.nome} sofre quedas de moral, já que o vento dificulta comunicação.",
                    lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                    f"{a.nome} perde tecnologia devido a falhas causadas pelo vento forte.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                )
            ],
            "nevoeiro": [
                Evento(
                    a, 
                    f"O nevoeiro permite que {a.nome} avance despercebido pela linha inimiga.",
                    f"As tropas utilizam a baixa visibilidade para melhorar táticas furtivas, aumentando estratégia.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"As unidades se desorientam no nevoeiro e se perdem, prejudicando a estratégia.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O nevoeiro oculta o movimento de tropas de {a.nome}.",
                    f"A cobertura permite um avanço seguro que aumenta a moral.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"O clima nebuloso cria apreensão entre soldados, reduzindo moral.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O nevoeiro denso interfere com equipamentos de navegação de {a.nome}.",
                    f"A equipe técnica consegue fazer ajustes rápidos para minimizar danos.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"A falha na navegação compromete sistemas, prejudicando tecnologia.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A umidade extrema do nevoeiro atinge suprimentos de {a.nome}.",
                    f"As tropas protegem parte do estoque com lonas improvisadas, reduzindo perdas.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                    f"O nevoeiro encharca caixas de suprimentos e gera perdas significativas.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O nevoeiro reduz a linha de visão para todos.",
                    f"{a.nome} aproveita para reforçar posições defensivas, aumentando força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"{a.inimigo.nome} usa a baixa visibilidade para treinar manobras furtivas, ganhando estratégia.",
                    lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O nevoeiro cria confusão generalizada no campo de batalha.",
                    f"{a.inimigo.nome} perde moral devido ao nervosismo provocado pelo clima opressivo.",
                    lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                    f"{a.nome} perde força após acidentes causados pela baixa visibilidade.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                )
            ],
            "frio": [
                Evento(
                    a, 
                    f"O clima frio fortalece a resistência física das tropas de {a.nome}.",
                    f"As unidades se adaptam ao clima gelado, aumentando força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"O frio intenso causa rigidez muscular nas tropas.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"{a.nome} aproveita o frio para testar equipamentos térmicos avançados.",
                    f"Os testes são bem-sucedidos e aumentam a tecnologia de combate.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"As baterias falham no frio e prejudicam sistemas tecnológicos.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O frio extremo afeta seriamente os depósitos de suprimentos de {a.nome}.",
                    f"As tropas conseguem proteger parte do estoque.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                    f"Os mantimentos congelam e parte se torna inutilizável.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O moral das tropas de {a.nome} é afetado pelo clima congelante.",
                    f"A liderança distribui mantas e bebidas quentes, elevando levemente a moral.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"O frio constante abala o ânimo dos soldados, reduzindo moral.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"A temperatura congelante cria novas oportunidades estratégicas.",
                    f"{a.nome} usa o frio para treinar resistência, aumentando moral.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"{a.inimigo.nome} adapta suas tropas para sobrevivência em clima gelado, aumentando suprimentos.",
                    lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos + self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O frio intenso causa congelamento de mecanismos e estruturas.",
                    f"{a.inimigo.nome} sofre queda de força pela rigidez muscular do clima.",
                    lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                    f"{a.nome} sofre queda tecnológica devido ao mau funcionamento dos equipamentos.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
                )
            ],
            "calor extremo": [
                Evento(
                    a, 
                    f"O calor extremo reduz a eficácia dos sensores inimigos, beneficiando {a.nome}.",
                    f"{a.nome} aproveita a oportunidade para aprimorar estratégias furtivas.",
                    lambda: setattr(a, 'estrategia', a.estrategia + self.poder_do_round),
                    f"O calor é intenso demais e prejudica a coordenação tática das tropas.",
                    lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O calor extremo seca o terreno, facilitando movimentações para {a.nome}.",
                    f"As tropas conseguem avançar com velocidade, aumentando força.",
                    lambda: setattr(a, 'forca', a.forca + self.poder_do_round),
                    f"O terreno árido causa fadiga excessiva e reduz força.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O calor extremo deteriora suprimentos sensíveis pertencentes a {a.nome}.",
                    f"As tropas conseguem salvar parte dos recursos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos + self.poder_do_round),
                    f"O calor estraga alimentos e munições, reduzindo suprimentos.",
                    lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                ),
                Evento(
                    a, 
                    f"O clima insuportável afeta o moral das tropas de {a.nome}.",
                    f"A liderança providencia tendas e água adicional, elevando levemente a moral.",
                    lambda: setattr(a, 'moral', a.moral + self.poder_do_round),
                    f"O calor severo causa desânimo e irritação entre soldados, reduzindo moral.",
                    lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
                ),
                Evento(
                    a,
                    f"O calor extremo força ambos os exércitos a adaptarem suas rotinas.",
                    f"{a.nome} melhora métodos de resfriamento e ganha eficiência tecnológica.",
                    lambda: setattr(a, 'tecnologia', a.tecnologia + self.poder_do_round),
                    f"{a.inimigo.nome} reorganiza suas fileiras para lidar com o clima, aumentando moral.",
                    lambda: setattr(a.inimigo, 'moral', a.inimigo.moral + self.poder_do_round)
                ),
                Evento(
                    a,
                    f"O calor extremo provoca colapso de equipamentos e queda de rendimento.",
                    f"{a.inimigo.nome} perde suprimentos que derretem, queimam ou evaporam.",
                    lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                    f"{a.nome} sofre perda de força devido ao desgaste físico.",
                    lambda: setattr(a, 'forca', a.forca - self.poder_do_round),
                )
            ]
        }

        clima = self.tempo.clima

        possiveis_eventos = eventos[clima[0].lower()]

        self.calcular_conclusao(possiveis_eventos)


    def tecnologia(self, a):
        eventos = [
            Evento(
                a,
                f"{a.nome} lança um ataque cibernético contra os sistemas de comando de {a.inimigo.nome}.",
                f"O ataque invade redes críticas e desativa sistemas tecnológicos inimigos.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"O ataque é rastreado e {a.nome} sofre retaliação digital severa.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta sabotar satélites militares de {a.inimigo.nome}.",
                f"A sabotagem é bem-sucedida e compromete comunicações e vigilância inimigas.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"A tentativa falha e sistemas orbitais de {a.nome} sofrem interferência.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a,
                f"Unidades de {a.nome} realizam guerra eletrônica contra radares de {a.inimigo.nome}.",
                f"Os radares inimigos são neutralizados, reduzindo sua capacidade tecnológica.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"A interferência é mal calibrada e afeta os próprios sistemas de {a.nome}.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} infiltra especialistas para sabotar centros de pesquisa de {a.inimigo.nome}.",
                f"A operação destrói protótipos e bancos de dados estratégicos.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"A equipe é descoberta e informações sensíveis de {a.nome} são comprometidas.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta desativar sistemas automatizados de defesa de {a.inimigo.nome}.",
                f"O sistema entra em colapso, reduzindo drasticamente a capacidade tecnológica inimiga.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"A tentativa ativa protocolos de segurança que danificam os próprios sistemas.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a,
                f"Especialistas de {a.nome} tentam corromper softwares militares de {a.inimigo.nome}.",
                f"O malware se espalha e paralisa sistemas críticos inimigos.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"O código falha e causa instabilidade nos sistemas de {a.nome}.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta interceptar e destruir drones avançados de {a.inimigo.nome}.",
                f"A interceptação funciona e reduz a superioridade tecnológica do inimigo.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"A tentativa falha e {a.nome} sofre retaliação.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} executa uma operação para inutilizar fábricas tecnológicas de {a.inimigo.nome}.",
                f"A produção tecnológica inimiga é severamente afetada.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"A operação é mal planejada e sistemas industriais de {a.nome} sofrem danos.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            )
        ]

        self.calcular_conclusao(eventos)


    def suprimentos(self, a):
        eventos = [
            Evento(
                a,
                f"{a.nome} inicia uma ofensiva sobre um grande hospital de {a.inimigo.nome}.",
                "O ataque é bem-sucedido, destruindo todos os suprimentos hospitalares do local.",
                lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                f"{a.inimigo.nome} já estava preparado, e muitos dos recursos hospitalares foram previamente evacuados.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),
            Evento(
                        a,
                        f"{a.nome} bombardeia depósitos de suprimentos de {a.inimigo.nome}.",
                        "O ataque é bem-sucedido e destrói grandes estoques de alimentos e munições.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "O ataque falha e a ofensiva consome grande parte dos próprios recursos.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    ),

                    Evento(
                        a,
                        f"{a.nome} tenta interromper rotas de abastecimento de {a.inimigo.nome}.",
                        "As rotas são bloqueadas, causando escassez crítica no exército inimigo.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "A operação falha e as tropas gastam recursos sem retorno.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    ),

                    Evento(
                        a,
                        f"Forças especiais de {a.nome} tentam sabotar armazéns logísticos de {a.inimigo.nome}.",
                        "A sabotagem é bem-sucedida e compromete o abastecimento inimigo.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "A equipe é descoberta e a missão gera perdas logísticas.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    ),

                    Evento(
                        a,
                        f"{a.nome} tenta destruir comboios de combustível de {a.inimigo.nome}.",
                        "Os comboios são destruídos, reduzindo drasticamente a mobilidade inimiga.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "O ataque falha e o esforço logístico se torna um desperdício.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    ),

                    Evento(
                        a,
                        f"{a.nome} realiza um ataque aéreo contra centros de distribuição de {a.inimigo.nome}.",
                        "Os centros são atingidos e o abastecimento inimigo entra em colapso.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "A missão falha e consome combustível e munições valiosas.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    ),

                    Evento(
                        a,
                        f"{a.nome} tenta envenenar ou inutilizar reservas de suprimentos de {a.inimigo.nome}.",
                        "As reservas inimigas se tornam inutilizáveis.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "A tentativa falha e parte dos próprios suprimentos é perdida.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    ),

                    Evento(
                        a,
                        f"{a.nome} tenta capturar depósitos de suprimentos abandonados por {a.inimigo.nome}.",
                        "Os depósitos são destruídos para evitar reaproveitamento inimigo.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "A operação falha e os recursos próprios se esgotam durante a tentativa.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    ),

                    Evento(
                        a,
                        f"{a.nome} tenta interromper linhas ferroviárias usadas por {a.inimigo.nome}.",
                        "A interrupção é bem-sucedida e prejudica seriamente a logística inimiga.",
                        lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                        "A ação falha e exige consumo excessivo de recursos logísticos.",
                        lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
                    )
                ]

        self.calcular_conclusao(eventos)


    def moral(self, a):
        eventos = [
            Evento(
                a,
                f"{a.nome} inicia uma campanha massiva de propaganda contra as tropas de {a.inimigo.nome}.",
                "A campanha é eficaz e abala seriamente a confiança das tropas inimigas.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "A propaganda é mal recebida e gera descrédito entre as próprias tropas.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} divulga vídeos de vitórias militares para intimidar {a.inimigo.nome}.",
                "Os vídeos espalham medo e reduzem o ânimo das tropas inimigas.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "Os vídeos são desmentidos e ridicularizados, afetando a moral interna.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta espalhar rumores de deserção nas fileiras de {a.inimigo.nome}.",
                "Os boatos se espalham e causam insegurança entre soldados inimigos.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "Os rumores são descobertos como falsos e desmoralizam quem os espalhou.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} executa operações psicológicas próximas às linhas inimigas.",
                f"A pressão constante desgasta emocionalmente as tropas de {a.inimigo.nome}.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "A operação falha e expõe vulnerabilidades emocionais das próprias tropas.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta interceptar comunicações para espalhar mensagens desmoralizantes.",
                "As mensagens criam confusão e reduzem o espírito de combate inimigo.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "A tentativa falha e mensagens falsas atingem os próprios soldados.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} organiza demonstrações de força próximas a posições de {a.inimigo.nome}.",
                "A demonstração intimida e reduz a confiança das tropas inimigas.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "A ação é vista como encenação e causa frustração entre as próprias tropas.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta explorar perdas recentes de {a.inimigo.nome} para desmoralizar suas tropas.",
                "O impacto psicológico é forte e o ânimo inimigo cai drasticamente.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "A tentativa é percebida como oportunista e gera desconforto interno.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta quebrar a moral inimiga com transmissões contínuas de intimidação.",
                "As transmissões causam estresse e reduzem a resistência psicológica do inimigo.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "A estratégia se volta contra o emissor e cansa as próprias tropas.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            )
        ]

        self.calcular_conclusao(eventos)


    def estrategia(self, a):
        eventos = [
            Evento(
                a,
                f"{a.nome} executa uma operação de desinformação contra o alto comando de {a.inimigo.nome}.",
                "Planos falsos confundem o inimigo e comprometem suas decisões estratégicas.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                "A desinformação é desmascarada e expõe falhas no próprio planejamento.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta atrair {a.inimigo.nome} para uma armadilha estratégica.",
                "O inimigo cai no blefe e perde capacidade de coordenação.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                f"A armadilha é prevista e revela fragilidades nos planos de {a.nome}.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta interceptar e distorcer ordens estratégicas de {a.inimigo.nome}.",
                "Ordens adulteradas causam erros graves no planejamento inimigo.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                f"A tentativa falha e gera confusão interna no comando de {a.nome}.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} lança uma série de manobras falsas para confundir {a.inimigo.nome}.",
                "O inimigo reage de forma equivocada e perde clareza estratégica.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                "As manobras são mal sincronizadas e prejudicam o próprio planejamento.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta expor divergências internas no comando de {a.inimigo.nome}.",
                "Conflitos internos enfraquecem a capacidade de formular planos eficazes.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                f"A tentativa falha e gera desconfiança entre estrategistas de {a.nome}.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} realiza uma ofensiva psicológica focada em confundir analistas de {a.inimigo.nome}.",
                "Relatórios contraditórios prejudicam a leitura do campo de batalha inimigo.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                "A ofensiva gera excesso de ruído e atrapalha as próprias análises.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} tenta antecipar e neutralizar planos futuros de {a.inimigo.nome}.",
                "A antecipação funciona e desmonta estratégias antes de serem executadas.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                f"A previsão é incorreta e leva {a.nome} a decisões estratégicas erradas.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento(
                a,
                f"{a.nome} conduz um jogo de blefes para forçar decisões precipitadas do inimigo.",
                "O inimigo age por impulso e compromete sua capacidade estratégica.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                f"O blefe falha e mina a confiança no planejamento de {a.nome}.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            )
        ]

        self.calcular_conclusao(eventos)


    def inteligencia(self, a):
        eventos = [

            Evento( #
                a,
                f"{a.nome} infiltra agentes nos centros de comando de {a.inimigo.nome}.",
                "A operação é um sucesso e os agentes sabotam o planejamento militar inimigo.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                "Os agentes são capturados e expostos a nível internacional.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} tenta roubar códigos de comunicação de {a.inimigo.nome}.",
                "As comunicações inimigas foram interceptadas com sucesso, ficando vulneráveis.",
                lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                "A tentativa sobrecarrega os sistemas de inteligência.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} executa uma operação urgente de contraespionagem interna.",
                "Os espiões são neutralizados antes de concluírem o plano.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "Os espiões sabotam a cadeia de suprimentos sem serem identificados.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} espalha informações falsas nos canais secretos de {a.inimigo.nome}.",
                f"{a.inimigo.nome} investe recursos em alvos inexistentes.",
                lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                "As mentiras perdem o direcionamento e confundem o próprio alto comando.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} envia um espião para interceptar informações confidenciais de {a.inimigo.nome}.",
                f"As falhas defensivas de {a.inimigo.nome} são expostas.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                "O espião era um agente duplo e expõe ao inimigo planos de longo prazo.",
                lambda: setattr(a, 'estrategia', a.estrategia - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} inicia um programa secreto de vigilância contra oficiais de {a.inimigo.nome}.",
                "O programa é um sucesso e informações seníveis são coletadas de oficiais-chave.",
                lambda: setattr(a.inimigo, 'estrategia', a.inimigo.estrategia - self.poder_do_round),
                "A vigilância excessiva compromete aparatos tecnológicos.",
                lambda: setattr(a, 'tecnologia', a.tecnologia - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} envia espiões de infiltração em bases avançadas de {a.inimigo.nome}.",
                "A infiltração resulta em sabotagens pontuais que enfraquecem as forças inimigas.",
                lambda: setattr(a.inimigo, 'forca', a.inimigo.forca - self.poder_do_round),
                "A operação exige longas linhas de apoio clandestino, esgotando os estoques internos.",
                lambda: setattr(a, 'suprimentos', a.suprimentos - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} inicia um programa secreto para sabotar rotas de suprimento de {a.inimigo.nome}.",
                "As rotas logísticas inimigas são comprometidas, causando escassez crítica.",
                lambda: setattr(a.inimigo, 'suprimentos', a.inimigo.suprimentos - self.poder_do_round),
                "A missão expõe agentes em campo, resultando em perdas militares.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),

            Evento( #
                a,
                f"{a.nome} inicia uma campanha com armas psicotrônicas.",
                f"As ondas eletrônicas atingem parte da tropa de {a.inimigo.nome}, causando desorientação cognitiva.",
                lambda: setattr(a.inimigo, 'moral', a.inimigo.moral - self.poder_do_round),
                "As armas são mal calibradas e geram diversos acidentes autoinfligidos.",
                lambda: setattr(a, 'forca', a.forca - self.poder_do_round)
            ),

            Evento( #
                a,
                f"Espiões de {a.nome} espalham rumores entre as frentes de {a.inimigo.nome}.",
                f"{a.inimigo.nome} destrói equipamentos próprios supostamente comprometidos.",
                lambda: setattr(a.inimigo, 'tecnologia', a.inimigo.tecnologia - self.poder_do_round),
                f"Manobras de contrainteligência fazem {a.nome} perder prestígio.",
                lambda: setattr(a, 'moral', a.moral - self.poder_do_round)
            )
        ]

        self.calcular_conclusao(eventos)
    

    def evento_especial(self, a):
        from random import choices

        if a.operacao_marechal:
            self.poder(a)
            return

        else:
            eventos = [
                (self.poder, 5),
                (self.matar_marechal, 1)
            ]

        '''
        if a.operacao:
            eventos = [
            (self.poder, 4),
            (self.matar_marechal, 1)
        ]
        
        elif a.operacao_marechal:
            eventos = [
            (self.poder, 3),
            (self.operacoes, 1)
        ]
            
        elif a.operacao and a.operacao_marechal:
            self.poder(a)
            return

        else:
            eventos = [
                (self.poder, 3),
                (self.operacoes, 2),
                (self.matar_marechal, 1)
            ]
            '''

        func = choices(
            [e for e, _ in eventos],
            weights=[p for _, p in eventos],
            k=1
        )[0]
        func(a)


    def poder(self, a):
        from time import sleep
        from random import choice

        eventos = [
            f"As forças de {a.nome} capturaram um importante centro de comando inimigo, elevando seu domínio no conflito.",
            f"{a.nome} interceptou e destruiu um contingente crucial de {a.inimigo.nome}, alterando o equilíbrio da guerra.",
            f"Uma operação coordenada garantiu a {a.nome} o controle total de rotas estratégicas antes dominadas pelo inimigo.",
            f"Após uma ofensiva bem-sucedida, {a.nome} desmantelou linhas críticas de defesa de {a.inimigo.nome}, consolidando sua superioridade.",
            f"{a.nome} obteve uma vitória decisiva em campo aberto, provando sua supremacia militar diante de {a.inimigo.nome}.",            
            f"Um avanço estratégico permitiu que {a.nome} tomasse controle de posições vitais, enfraquecendo drasticamente o inimigo.",           
            f"As tropas de {a.nome} realizaram uma manobra impecável, cercando forças de {a.inimigo.nome} e forçando sua retirada.",           
            f"{a.nome} interceptou e destruiu um contingente crucial de {a.inimigo.nome}, alterando o equilíbrio da guerra.",
            f"Liderança militar de {a.nome} executou um plano audacioso que resultou em uma conquista histórica no conflito.",       
            f"{a.nome} obteve uma vitória simbólica de grande impacto, fortalecendo sua posição política e militar.",
            f"Ofensiva de {a.nome} quebrou a resistência organizada de {a.inimigo.nome}, ampliando seu poder no teatro de guerra.",
            f"Operação de forças especiais de {a.nome} eliminou o comandante supremo das tropas de {a.inimigo.nome}, causando desorganização imediata no front.",
            f"{a.nome} executou com sucesso um ataque direcionado que resultou na morte do marechal responsável pela defesa central de {a.inimigo.nome}.",
            f"Durante um avanço coordenado, tropas de {a.nome} localizaram e neutralizaram o general encarregado da logística de {a.inimigo.nome}.",
            f"Bombardeio preciso de {a.nome} atingiu o posto de comando móvel de {a.inimigo.nome}, matando seu principal estrategista militar.",
            f"Forças de {a.nome} interceptaram um comboio de alto escalão e eliminaram o almirante responsável pelas operações navais de {a.inimigo.nome}.",
            f"Após semanas de inteligência, {a.nome} capturou e executou o oficial responsável pelas contraofensivas de {a.inimigo.nome}.",
            f"Incursão atrás das linhas inimigas permitiu que {a.nome} eliminasse o comandante das tropas de elite de {a.inimigo.nome}.",
            f"Governo de {a.nome} firmou um pacto militar emergencial com uma das potências do G7, garantindo apoio estratégico imediato.",
            f"Após atingir as normas, {a.nome} assinou um acordo internacional de cooperação militar que liberou acesso a armamentos, instrutores e informações sigilosas.",
            f"Governo de {a.nome} conseguiu isolar diplomaticamente {a.inimigo.nome}, pressionando outras nações a suspenderem qualquer apoio.",
            f"Uma aliança defensiva foi formalizada por {a.nome} com blocos regionais, assegurando reforços militares em caso de escalada do conflito.",
            f"Alto comando político de {a.nome} aprovou uma mobilização total da indústria de guerra, ampliando drasticamente sua capacidade militar.",
            f"{a.nome} negociou apoio indireto de um bloco regional, garantindo recursos e cobertura política no cenário internacional.",
            f"Governo de {a.nome} obteve apoio de facções dissidentes de {a.inimigo.nome}. Fontes indicam exploração de divisões internas.",
            f"{a.nome} conseguiu aprovação de medidas de guerra que centralizaram o comando militar, acelerando decisões e ofensivas."
        ]

        evento = choice(eventos)

        self.tempo.formatar_horario()
        self.tempo.atualizar_horario()

        console.print(f"""[yellow bold][{self.tempo.horario}] BREAKING NEWS:[/yellow bold] [blink bright_cyan bold]{evento}[/blink bright_cyan bold]""")
        a.poder += 1
        sleep(1)
    

    def operacoes(self, a):
        pass


    def matar_marechal(self, a):
        from random import choice, randint

        self.tempo.atualizar_horario()

        primeiro_nome = [
            "Martelo",
            "Lança",
            "Falcão",
            "Víbora",
            "Punho",
            "Espada",
            "Sombra",
            "Ceifador",
            "Espectro",
            "Tempestade",
            "Relâmpago",
            "Silêncio",
            "Corvo",
            "Eclipse",
            "Cicatriz",
            "Abismo",
            "Sentinela",
            "Trovão",
            "Fantasma",
            "Executor"
        ]
        segundo_nome = [
            "Final",
            "Letal",
            "Negro",
            "Escarlate",
            "Noturno",
            "Implacável",
            "Oculto",
            "Fatal",
            "Sombrio",
            "Terminal",
            "Silencioso",
            "Irrevogável",
            "Rubro",
            "Certeiro",
            "da Morte",
            "Profundo",
            "Inexorável",
            "Definitivo",
            "Frio",
            "Severo"
        ]

        eventos = {
            "evento1": {
                "Fase 1": f"Batedores de {a.nome} iniciam observação discreta dos deslocamentos de {a.inimigo.marechal['nome']}, registrando horários e padrões.",
                "Fase 2": f"Agentes infiltrados de {a.nome} interceptam mensageiros e atrasam ordens, criando pequenos gargalos no comando.",
                "Fase 3": f"Unidades de ataque de {a.nome} são posicionadas silenciosamente ao redor do quartel avançado de {a.inimigo.marechal['nome']}.",
                "sucesso": f"{a.nome} executa o assalto no momento exato, eliminando {a.inimigo.marechal['nome']} antes que qualquer reação seja possível.",
                "falha": f"A movimentação é antecipada, {a.inimigo.marechal['nome']} escapa por pouco e a operação é abortada sob fogo inimigo."
            },

            "evento2": {
                "Fase 1": f"{a.nome} inicia operação de inteligência, espalhando rumores de ataque em outra frente.",
                "Fase 2": f"{a.inimigo.marechal['nome']} desloca parte de suas forças para responder à ameaça inexistente, enquanto a emboscada é organizada.",
                "Fase 3": f"{a.nome} monta uma emboscada na rota recém-utilizada pelo marechal.",
                "sucesso": f"A armadilha se fecha e {a.inimigo.marechal['nome']} é morto durante o deslocamento.",
                "falha": f"{a.inimigo.marechal['nome']} muda o trajeto ao perceber intenções inimigas e escapa da emboscada."
            },

            "evento3": {
                "Fase 1": f"Pequenos ataques testam a prontidão das defesas sob comando de {a.inimigo.marechal['nome']}.",
                "Fase 2": f"Relatórios de {a.nome} revelam uma brecha crítica na segurança pessoal do marechal. A brecha começa a ser estudada.",
                "Fase 3": f"{a.nome} concentra forças exatamente nessa brecha crítica.",
                "sucesso": f"O ataque atravessa a defesa e elimina {a.inimigo.marechal['nome']} de forma decisiva.",
                "falha": f"A brecha de {a.inimigo.nome} é reforçada a tempo e o ataque é repelido com perdas."
            },

            "evento4": {
                "Fase 1": f"Rotas de suprimento ligadas a {a.inimigo.marechal['nome']} começam a ser neutralizadas.",
                "Fase 2": f"A pressão logística gera desgaste e decisões apressadas no comando de {a.inimigo.marechal['nome']}.",
                "Fase 3": f"{a.nome} fecha o cerco enquanto {a.inimigo.marechal['nome']} tenta reorganizar suas forças.",
                "sucesso": f"Durante a tentativa de retirada, {a.inimigo.marechal['nome']} é alcançado e morto.",
                "falha": f"O cerco falha e {a.inimigo.marechal['nome']} rompe as linhas, escapando."
            },

            "evento5": {
                "Fase 1": f"Agentes de {a.nome} conseguem se infiltrar e se passam por aliados próximos a {a.inimigo.marechal['nome']}.",
                "Fase 2": f"Ordens contraditórias começam a circular dentro do comando de {a.inimigo.marechal['nome']}.",
                "Fase 3": f"A cadeia de comando percebe que há algo de errado e operação de contraintelgência entra em vigor às pressas.",
                "sucesso": f"Sem que ninguém esperasse, {a.inimigo.marechal['nome']} é encontrado morto em seus aposentos. Causa da morte a ser investigada.",
                "falha": f"A infiltração de {a.nome} é descoberta e os agentes são capturados."
            },

            "evento6": {
                "Fase 1": f"{a.nome} lança uma provocação direta para atrair {a.inimigo.marechal['nome']} ao campo aberto.",
                "Fase 2": f"{a.nome} forja uma fraqueza em um ponto crítico de sua organização.",
                "Fase 3": f"Agentes militares são posicionados, aguardando a investida de {a.inimigo.marechal['nome']} para fechar a armadilha.",
                "sucesso": f"{a.inimigo.marechal['nome']} avança confiante demais e é morto na armadilha.",
                "falha": f"{a.inimigo.marechal['nome']} desconfia da isca e recua antes do ataque."
            },

            "evento7": {
                "Fase 1": f"Relatórios investigativos detalham a composição da guarda pessoal de {a.inimigo.marechal['nome']}.",
                "Fase 2": f"Membros da escolta de {a.inimigo.marechal['nome']} são neutralizados gradualmente ao longo de dias.",
                "Fase 3": f"{a.inimigo.marechal['nome']} fica isolado de sua proteção principal, vulnerável a qualquer ataque.",
                "sucesso": f"{a.nome} executa o ataque final a {a.inimigo.marechal['nome']} sem resistência significativa. O marechal está morto",
                "falha": f"Reforços chegam a tempo e restauram a segurança de {a.inimigo.marechal['nome']}."
            },

            "evento8": {
                "Fase 1": f"Ataques coordenados de {a.nome} forçam {a.inimigo.nome} a dividir suas forças.",
                "Fase 2": f"O centro de comando de {a.inimigo.nome} fica sobrecarregado com a defesa de várias frentes.",
                "Fase 3": f"{a.nome} se posiciona, aguardando maior vulnerabilidade do quartel avançado de {a.inimigo.marechal['nome']}.",
                "sucesso": f"O golpe atinge o coração do comando e elimina {a.inimigo.marechal['nome']}.",
                "falha": f"A distração não funciona e o ataque principal é detectado por {a.inimigo.marechal['nome']}."
            },

            "evento9": {
                "Fase 1": f"Campanhas de desinformação por {a.nome} começam a minar a confiança no marechal {a.inimigo.marechal['nome']}.",
                "Fase 2": f"Oficiais próximos a {a.inimigo.marechal['nome']} demonstram hesitação e medo.",
                "Fase 3": f"Clima de desconfiança se instaura no comando de {a.inimigo.marechal['nome']}, levando a um grave erro estratégico.",
                "sucesso": f"{a.nome} explora o erro de {a.inimigo.marechal['nome']} e elimina o marechal rapidamente.",
                "falha": f"{a.inimigo.marechal['nome']} percebe a manipulação e envia capitães para corrigirem o erro a tempo."
            },

            "evento10": {
                "Fase 1": f"{a.nome} inicia uma grande operação de distração em outra região.",
                "Fase 2": "Tropas especializadas se movem silenciosamente para o alvo real.",
                "Fase 3": "O marechal fica momentaneamente longe de suas forças principais.",
                "sucesso": f"{a.inimigo.marechal['nome']} é morto longe do campo principal de batalha.",
                "falha": "A distração falha e o marechal retorna sob forte escolta."
            }

        }


        nome_operacao = f"Operação {choice(primeiro_nome)} {choice(segundo_nome)}"

        eventos = choice(list(eventos.values()))

        intervalo1 = randint(3, 7)
        intervalo2 = intervalo1 + randint(3, 7)
        intervalo3 = intervalo2 + randint(3, 7)

        eventos["Fase 1"] = [eventos["Fase 1"], int(self.tempo.dia), int(self.tempo.minutos)]
        eventos["Fase 2"] = [eventos["Fase 2"], int(self.tempo.dia) + intervalo1, randint(3, 21)]
        eventos["Fase 3"] = [eventos["Fase 3"], int(self.tempo.dia) + intervalo2, randint(3, 21)]
        eventos["sucesso"] = [eventos["sucesso"], int(self.tempo.dia) + intervalo3, randint(3, 21)]
        eventos["falha"] = [eventos["falha"], int(self.tempo.dia) + intervalo3, randint(3, 21)]

        a.operacao_marechal = {
            "nome": nome_operacao,
            "fase": "Fase 1",
            "eventos": eventos}
        
        self.tempo.formatar_horario()
        self.atualizar_horario()
        
        self.executar_operacao_marechal(a)
    

    def verificar_operacao_marechal(self, a):
        fase = a.operacao_marechal["fase"]
        evento = a.operacao_marechal['eventos'][fase]
        dia = evento[1]
        hora = evento[2]

        self.tempo.formatar_horario()
        self.tempo.atualizar_horario()

        if int(self.tempo.dia) == dia and int(self.tempo.hora) >= hora:
            return True
        elif int(self.tempo.dia) > dia:
            return True
        else:
            return False
    

    def executar_operacao_marechal(self, a):
        from random import randint
        from time import sleep

        fase = a.operacao_marechal["fase"]
        evento = a.operacao_marechal['eventos'][fase]
        descricao = evento[0]

        operacao = a.operacao_marechal["nome"]
        console.print(f"[yellow][{self.tempo.horario}][/yellow] [italic bold red1 on white] //{operacao.upper()} - {fase.upper()}: {descricao}// [/italic bold red1 on white]")
        sleep(2)

        if fase == "Fase 1":
            a.operacao_marechal["fase"] = "Fase 2"
        elif fase == "Fase 2":
            a.operacao_marechal["fase"] = "Fase 3"
        elif fase == "Fase 3":
            chance = randint(1, 10)
            if chance <= 6:
                conclusao = 'falha'
            else:
                conclusao = "sucesso"

            a.operacao_marechal["fase"] = conclusao
        elif fase == "sucesso":
            a.poder += 3
            console.print(f"           [yellow]O marechal {a.inimigo.marechal['nome']} foi morto! O exército de {a.nome} ganhou [bold]+3[/bold] de poder por essa conquista.[/yellow]")
            sleep(2)
            a.operacao_marechal = False
            a.inimigo.marechal = a.inimigo.escolher_marechal()
            a.inimigo.descrever_marechal(novo=True)
        else:
            a.inimigo.poder += 2
            console.print(f"           [yellow]O marechal {a.inimigo.marechal['nome']} escapou de ser morto! O exército de {a.inimigo.nome} ganhou [bold]+2[/bold] de poder por essa escapada.[/yellow]")
            sleep(2)
            a.operacao_marechal = False


    def verificar_resultado(self, a):
        from random import choice, random

        if a.marechal['perfil'] == 'Político':
            chance_a = 1.3
        else:
            chance_a = 1
        
        if a.inimigo.marechal['perfil'] == 'Político':
            chance_b = 0.7
        else:
            chance_b = 1
        
        if a.inimigo.territorio < a.territorio / 5 and a.inimigo.territorio > 0:
            if random() < (abs(a.territorio - a.inimigo.territorio) / (a.territorio + a.inimigo.territorio)) * 0.05 * chance_a * chance_b:
                vencedor = a.nome
                derrotado = a.inimigo.nome
                
                frases = [
                    f"Com apenas pequenas áreas isoladas ainda sob seu controle, {derrotado} declarou rendição após perder a capacidade de administrar e defender seu território.",
                    f"Após a tomada das últimas regiões estratégicas por {vencedor}, {derrotado} rendeu-se, reconhecendo que não havia mais território suficiente para sustentar a guerra.",
                    f"Encurralado em faixas territoriais fragmentadas e sem rotas de conexão, {derrotado} anunciou sua rendição às forças de {vencedor}.",
                    f"A perda quase total de seu território forçou {derrotado} a aceitar a derrota, já que não restavam áreas para mobilização ou defesa organizada.",
                    f"Sem controle sobre regiões produtivas e centros administrativos, {derrotado} optou por se render diante do avanço irreversível de {vencedor}.",
                    f"Reduzido a posições dispersas e indefensáveis, {derrotado} reconheceu a impossibilidade de continuar a guerra e se rendeu a {vencedor}.",
                    f"A ocupação sistemática do território por {vencedor} deixou {derrotado} sem fronteiras funcionais, levando à rendição oficial.",
                    f"Com seu território dividido e cercado, {derrotado} perdeu a capacidade de coordenação e anunciou a rendição para evitar a completa destruição.",
                    f"A incapacidade de manter controle territorial contínuo levou {derrotado} a encerrar as hostilidades e se render às forças de {vencedor}.",
                    f"Após perder quase todas as áreas sob seu domínio e não conseguir reorganizar suas defesas, {derrotado} declarou rendição incondicional."
                ]

                self.ativa = False
        
        else:
            derrotado = a.nome
            vencedor = a.inimigo.nome

            if a.forca <= 0:
                frases = [
                    f"{derrotado} teve suas forças neutralizadas e foi destruído pelo inimigo.",
                    f"As últimas unidades de {derrotado} foram esmagadas, não restando poder militar para resistir.",
                    f"O exército de {derrotado} colapsou sob o peso da batalha, sendo completamente aniquilado.",
                    f"Sem força para continuar, {derrotado} foi varrido do campo de batalha.",
                    f"A capacidade de combate de {derrotado} chegou ao fim, selando sua derrota total."
                ]
                self.ativa = False
                a.forca = 0

            elif a.tecnologia <= 0:
                frases = [
                    f"A capacidade tecnológica de {derrotado} foi arruinada, sem restar condições de se defender.",
                    f"Com seus sistemas destruídos, {derrotado} tornou-se incapaz de enfrentar o inimigo.",
                    f"A superioridade tecnológica do adversário deixou {derrotado} indefeso.",
                    f"Sem comunicações ou armamentos avançados, {derrotado} sucumbiu à derrota.",
                    f"O colapso tecnológico de {derrotado} tornou qualquer resistência impossível."
                ]
                self.ativa = False
                a.tecnologia = 0

            elif a.suprimentos <= 0:
                frases = [
                    f"Os suprimentos de {derrotado} foram esgotados e, sem recursos, o exército foi derrotado.",
                    f"A falta de comida, munição e combustível levou {derrotado} ao colapso.",
                    f"Sem linhas de abastecimento, as tropas de {derrotado} foram forçadas à rendição.",
                    f"O esgotamento logístico selou o destino de {derrotado} no conflito.",
                    f"Privado de recursos essenciais, {derrotado} não conseguiu sustentar a guerra."
                ]
                self.ativa = False
                a.suprimentos = 0

            elif a.moral <= 0:
                frases = [
                    f"As tropas de {derrotado} se recusam a continuar lutando, dividindo-se entre desertores e prisioneiros de guerra.",
                    f"A moral despencou e o exército de {derrotado} se desfez em meio ao caos.",
                    f"Sem vontade de lutar, as tropas de {derrotado} abandonaram o campo de batalha.",
                    f"O desespero tomou conta das fileiras de {derrotado}, encerrando qualquer resistência.",
                    f"A perda total de moral levou {derrotado} a uma derrota inevitável."
                ]
                self.ativa = False
                a.moral = 0

            elif a.estrategia <= 0:
                frases = [
                    f"{derrotado} teve seus planos estratégicos completamente sufocados, não enxergando maneiras de derrotar o inimigo.",
                    f"As decisões equivocadas de {derrotado} levaram o exército a uma derrota irreversível.",
                    f"Sem coordenação ou liderança eficaz, {derrotado} foi superado pelo inimigo.",
                    f"A falha estratégica deixou {derrotado} vulnerável em todos os flancos.",
                    f"O colapso do comando estratégico selou o fracasso de {derrotado}."
                ]
                self.ativa = False
                a.estrategia = 0
            
            elif a.territorio <= 0:
                frases = [
                    f"Todo o território de {derrotado} foi ocupado pelas forças inimigas, encerrando sua capacidade de continuar a guerra.",
                    f"As últimas regiões controladas por {derrotado} caíram, deixando o exército sem base territorial para operar.",
                    f"Com suas fronteiras completamente rompidas, {derrotado} perdeu o controle total de seu território e foi derrotado.",
                    f"As forças inimigas tomaram cada posição restante de {derrotado}, eliminando qualquer domínio territorial.",
                    f"Sem território para defender ou administrar, {derrotado} foi forçado a aceitar a derrota total."
                ]

                self.ativa = False
                a.territorio = 0

            else:
                return
        
        frase = choice(frases)
            
        if not self.ativa:
            self.tempo.atualizar_horario()

            self.tabela_guerra()

            console.print(f"""[yellow]
===================================================================
[{self.tempo.horario}] NOTÍCIA URGENTE: A GUERRA ACABOU!
Após {self.tempo.dia} dias de guerra, o mundo respira aliviado com o fim oficial do conflito entre {vencedor} e {derrotado}.
{frase}
{vencedor} venceu a guerra!
===================================================================
[/yellow]""")
            return True


    def calcular_conclusao(self, eventos):
        from time import sleep
        from numpy.random import choice, randint
        from math import ceil

        evento = choice(eventos)

        while True:
            poder1 = randint(1, 100)
            poder2 = randint(1, 100)

            if poder1 == poder2:
                continue

            territorio = randint(5, 10)

            marechal_1 = evento.a.marechal
            marechal_2 = evento.a.inimigo.marechal

            if poder1 > poder2:
                self.poder_do_round = ceil((poder1 - poder2) / 10)

                resultado = "positivo"

                if not evento.a.placar_seguido['primeira']:
                    evento.a.placar_seguido['primeira'] = True
                    evento.a.placar_seguido['streak'] = 1
                else:
                    evento.a.placar_seguido['streak'] += 1
                
                if evento.a.inimigo.placar_seguido['primeira']:
                    evento.a.inimigo.placar_seguido['primeira'] = False
                    evento.a.inimigo.placar_seguido['streak'] = 1
                else:
                    evento.a.inimigo.placar_seguido['streak'] += 1

                match marechal_1['perfil']:
                    case 'Agressivo':
                        self.poder_do_round *= 2
                    case 'Cauteloso':
                        self.poder_do_round = ceil(self.poder_do_round / 2)
                    case 'Oportunista':
                        if poder1 - poder2 >= 48:
                            self.poder_do_round *= 2
                        elif poder1 - poder2 <= 15:
                            self.poder_do_round = ceil(self.poder_do_round / 2)
                    case 'Estrategista':
                        poder_total_1 = evento.a.calcular_poder_total()
                        poder_total_2 = evento.a.inimigo.calcular_poder_total()

                        if poder_total_2 > poder_total_1:
                            self.poder_do_round = ceil(self.poder_do_round * 1.33)
                        elif poder_total_1 > poder_total_2:
                            self.poder_do_round = ceil(self.poder_do_round * 0.75)
                    case 'Sanguinário':
                        streak = evento.a.placar_seguido['streak']
                        if streak > 1:
                            multiplicador = streak - 1
                            bonus = 0.5

                            self.poder_do_round = ceil(self.poder_do_round * (1 + multiplicador * bonus))

                match marechal_2['perfil']:
                    case 'Equilibrado':
                        pass
                    case 'Agressivo':
                        self.poder_do_round *= 2
                    case 'Cauteloso':
                        self.poder_do_round = ceil(self.poder_do_round / 2)
                    case 'Arrogante':
                        poder_total_1 = evento.a.calcular_poder_total()
                        poder_total_2 = evento.a.inimigo.calcular_poder_total()

                        if poder_total_2 - poder_total_1 > 30:
                            self.poder_do_round = ceil(self.poder_do_round * 1.33)
                        elif poder_total_2 - poder_total_1 < -30:
                            self.poder_do_round = ceil(self.poder_do_round * 0.75)
                        
                    case 'Sanguinário':
                        streak = evento.a.placar_seguido['streak']
                        if streak > 1:
                            multiplicador = streak - 1
                            bonus = 0.5

                            self.poder_do_round = ceil(self.poder_do_round * (1 + multiplicador * bonus))
                
                self.poder_do_round += evento.a.poder

            else:
                self.poder_do_round = ceil((poder2 - poder1) / 10) + evento.a.inimigo.poder
                resultado = "negativo"

                if evento.a.placar_seguido['primeira']:
                    evento.a.placar_seguido['primeira'] = False
                    evento.a.placar_seguido['streak'] = 1
                else:
                    evento.a.placar_seguido['streak'] += 1

                if not evento.a.inimigo.placar_seguido['primeira']:
                    evento.a.inimigo.placar_seguido['primeira'] = True
                    evento.a.inimigo.placar_seguido['streak'] = 1
                else:
                    evento.a.inimigo.placar_seguido['streak'] += 1
                
                match marechal_1['perfil']:
                    case 'Agressivo':
                        self.poder_do_round *= 2
                    case 'Cauteloso':
                        self.poder_do_round = ceil(self.poder_do_round / 2)
                    case 'Arrogante':
                        poder_total_1 = evento.a.calcular_poder_total()
                        poder_total_2 = evento.a.inimigo.calcular_poder_total()

                        if poder_total_1 - poder_total_2 > 30:
                            self.poder_do_round = ceil(self.poder_do_round * 1.33)
                        elif poder_total_1 - poder_total_2 < -30:
                            self.poder_do_round = ceil(self.poder_do_round * 0.75)
                    case 'Sanguinário':
                        streak = evento.a.placar_seguido['streak']
                        if streak > 1:
                            multiplicador = streak - 1
                            bonus = 0.5

                            self.poder_do_round = ceil(self.poder_do_round * (1 + multiplicador * bonus))
                
                match marechal_2['perfil']:
                    case 'Equilibrado':
                        pass
                    case 'Agressivo':
                        self.poder_do_round *= 2
                    case 'Cauteloso':
                        self.poder_do_round = ceil(self.poder_do_round / 2)
                    case 'Oportunista':
                        if poder2 - poder1 >= 48:
                            self.poder_do_round *= 2
                        elif poder2 - poder1 <= 15:
                            self.poder_do_round = ceil(self.poder_do_round / 2)
                    case 'Estrategista':
                        poder_total_1 = evento.a.calcular_poder_total()
                        poder_total_2 = evento.a.inimigo.calcular_poder_total()

                        if poder_total_1 > poder_total_2:
                            self.poder_do_round = ceil(self.poder_do_round * 1.33)
                        elif poder_total_2 > poder_total_1:
                            self.poder_do_round = ceil(self.poder_do_round * 0.75)
                    case 'Sanguinário':
                        streak = evento.a.inimigo.placar_seguido['streak']
                        if streak > 1:
                            multiplicador = streak - 1
                            bonus = 0.5

                            self.poder_do_round = ceil(self.poder_do_round * (1 + multiplicador * bonus))
                
                self.poder_do_round += evento.a.inimigo.poder
            
            break

        console.print(f"[yellow][{self.tempo.horario}][/yellow] {evento.nome}")
        sleep(1)
        if resultado == "positivo":
            if marechal_1['perfil'] == 'Instável':
                if randint(1, 10) <= 4:
                    marechal_1_nome = marechal_1['nome']

                    frases_negativas = [
                        f'O marechal {marechal_1_nome} tinha a vitória nas mãos… e a deixou cair.',
                        f'O próprio caos de {marechal_1_nome} sabotou uma vitória certa.',
                        f'Ordens confusas de {marechal_1_nome} transformaram vantagem em desastre.',
                        f'A instabilidade mental de {marechal_1_nome} custou caro.',
                        f'O plano era bom, mas {marechal_1_nome} mudou tudo no último segundo.',
                        f'O inimigo agradece: {marechal_1_nome} perdeu para si mesmo.',
                        f'Vitória desperdiçada pela mente imprevisível de {marechal_1_nome}.',
                        f'O caos interno de {marechal_1_nome} venceu antes do inimigo.',
                        f'Uma decisão impulsiva de {marechal_1_nome} selou a derrota.',
                        f'{marechal_1_nome} confundiu aliados mais do que os inimigos.'
                    ]
                    console.print(f'           [italic]{choice(frases_negativas)}[/italic]')
                    sleep(1)

                    console.print(f'           [#ff6161]{evento.negativo}[/#ff6161]')
                    evento.efeito_neg()
                    evento.a.territorio -= territorio
                    evento.a.inimigo.territorio += territorio
                else:
                    console.print(f'           [#00ff00]{evento.positivo}[/#00ff00]')
                    evento.efeito_pos()
                    evento.a.territorio += territorio
                    evento.a.inimigo.territorio -= territorio
            else:
                console.print(f'           [#00ff00]{evento.positivo}[/#00ff00]')
                evento.efeito_pos()
                evento.a.territorio += territorio
                evento.a.inimigo.territorio -= territorio

        else:
            if marechal_1['perfil'] == 'Instável':
                if randint(1, 10) >= 7:
                    marechal_1_nome = marechal_1['nome']
                    
                    frases_positivas = [
                        f'O marechal {marechal_1_nome} riu do próprio caos e virou o jogo!',
                        f'O caos mental de {marechal_1_nome} confundiu o inimigo e garantiu a vitória.',
                        f'O improvável aconteceu: {marechal_1_nome} venceu contra toda lógica.',
                        f'A instabilidade de {marechal_1_nome} gerou uma manobra impossível de prever.',
                        f'Quando tudo parecia perdido, {marechal_1_nome} fez do caos sua arma.',
                        f'O plano não fazia sentido, mas funcionou — vitória de {marechal_1_nome}.',
                        f'A loucura estratégica de {marechal_1_nome} virou o rumo da batalha.',
                        f'O inimigo subestimou o caos de {marechal_1_nome}… erro fatal.',
                        f'Entre gritos e ordens contraditórias, {marechal_1_nome} saiu vitorioso.',
                        f'O campo de batalha sucumbiu à imprevisibilidade de {marechal_1_nome}.'
                    ]
                    console.print(f"           [italic]{choice(frases_positivas)}[/italic]")
                    sleep(1)
                    console.print(f'           [#00ff00]{evento.positivo}[/#00ff00]')
                    evento.efeito_pos()
                    evento.a.territorio += territorio
                    evento.a.inimigo.territorio -= territorio
                else:
                    console.print(f'           [#ff6161]{evento.negativo}[/#ff6161]')
                    evento.efeito_neg()
                    evento.a.territorio -= territorio
                    evento.a.inimigo.territorio += territorio
            else:
                console.print(f'           [#ff6161]{evento.negativo}[/#ff6161]')
                evento.efeito_neg()
                evento.a.territorio -= territorio
                evento.a.inimigo.territorio += territorio
        
        self.calcular_flow()
    
    def tabela_guerra(self):
        from rich.table import Table
        from rich.console import Console

        console = Console()

        print()
        table = Table(title=f"Dia {self.tempo.dia} // Clima: {self.tempo.clima[0]} {self.tempo.clima[1]}")

        table.add_column("Exército", justify="center")
        table.add_column("Marechal", justify="center")
        table.add_column("Perfil", justify="center")
        table.add_column("Poder", justify="center", style="red")
        table.add_column("Território", justify="center", style="green")
        table.add_column("Flow", justify="center", style="pink1")
        table.add_column("Força", justify="center", style="orange1")
        table.add_column("Tecnologia", justify="center", style="cyan")
        table.add_column("Suprimentos", justify="center", style="blue")
        table.add_column("Moral", justify="center", style="yellow")
        table.add_column("Estratégia", justify="center", style="violet")

        for exercito in self.exercitos:

            table.add_row(f"{exercito.nome}", f"{exercito.marechal['nome']}", f"{exercito.marechal['perfil_estilizado']}", f"{exercito.poder}", f"{exercito.territorio}", f"{exercito.flow}", f"{exercito.forca}", f"{exercito.tecnologia}", f"{exercito.suprimentos}", f"{exercito.moral}", f"{exercito.estrategia}")

        console.print(table)
        print()


    def concluir_dia(self):
        from random import uniform

        for tropa in self.exercitos:
            tropa.resumo["pib"] -= round(uniform(0.01, 0.1), 2)
            tropa.resumo["inflacao"] += round(uniform(0.01, 0.1), 2)

        self.tempo.dia += 1
        self.tempo.hora = 0
        self.tempo.clima = self.tempo.escolher_clima()


    def calcular_flow(self):
        from math import ceil

        poder_somado = 0

        for exercito in self.exercitos:

            exercito.poder_total = exercito.calcular_poder_total()

            poder_somado += exercito.poder_total
        
        for exercito in self.exercitos:

            porcentagem = exercito.poder_total / poder_somado

            exercito.flow = ceil(100 * porcentagem)
