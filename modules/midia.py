class Midia:
    def __init__(self, tropas):
        self.tropas = tropas

        self.resumo = {
            "mortos": 145
        }

        self.canais = [
            {
                "nome": "Agência Global de Informação",
                "sigla": "AGI",
                "tema": "geral",
                "noticias": [
                    "Um {hospital} foi bombardeado durante a ofensiva contra {exercito}, deixando ao menos {mortos} mortos, a maioria civis. {exercito2} nega autoria dos ataques.",
                    "Uma {usina} foi atingida em território controlado por {exercito}. O ataque deixou {mortos} mortos.",
                    "Autoridades confirmaram que um {complexo} foi atacado nas proximidades de posições de {exercito}, resultando em {mortos} mortos e {feridos} feridos.",
                    "ONU é pressionada a intervir após acusações de crimes de guerra contra {exercito}.",
                    "Um ataque aéreo destruiu parcialmente um {hospital} ligado a {exercito}, deixando {mortos} mortos e dezenas de feridos.",
                    "População de {exercito} enfrenta forte crise econômica enquanto negociações seguem sem avanços.",
                    "Organizações internacionais alertam para possível escalada da guerra entre {exercito} e {exercito2}.",
                    "{exercito} sofre sanções econômicas por países aliados de {exercito2}.",
                    "Aumento de vítimas civis gera pressão por cessar-fogo imediato. Número de mortos chega a {total_mortos}.",
                    '"Minha família não existe mais! Parem a guerra agora!", apela uma das vítimas do bombardeio em {exercito}. Mortos chegam a {total_mortos}',
                    "Bombardeios em rotas de suprimentos de {exercito} deixam estradas intransitáveis.",                   
                    "Conselho de Segurança da ONU convoca reunião de emergência após novos ataques envolvendo {exercito} e {exercito2}.",
                    "Ataques recentes elevam para {total_mortos} o número total de mortos desde o início da guerra, segundo estimativas internacionais.",
                    "Comunidade internacional manifesta preocupação com uso de áreas urbanas como palco de confrontos entre {exercito} e {exercito2}.",
                    "Relatórios indicam intensificação dos combates próximos a infraestruturas estratégicas controladas por {exercito}.",
                    "Países aliados pedem moderação após escalada militar registrada nas últimas 48 horas no conflito envolvendo {exercito}.",
                    "Crescente número de vítimas civis gera pressão global por abertura de corredores humanitários em território de {exercito}.",
                    "Missão internacional investiga danos a um {hospital} após bombardeios na região disputada.",
                    "Especialistas alertam que guerra entre {exercito} e {exercito2} pode ter impactos regionais duradouros.",
                    "Novas imagens de satélite mostram destruição significativa em áreas próximas a um {complexo} estratégico.",
                    "Organizações internacionais pedem acesso irrestrito para ajuda humanitária em zonas controladas por {exercito}.",
                    "Bombardeios sucessivos causam interrupções em redes de transporte e comunicação em regiões afetadas pelo conflito.",
                    "Declarações contraditórias de {exercito} e {exercito2} dificultam apuração de responsabilidades pelos ataques recentes.",
                    "Analistas afirmam que prolongamento do conflito aumenta riscos de instabilidade política e econômica na região.",
                    "Número de feridos ultrapassa {feridos} após novos confrontos registrados nas últimas horas.",
                    "Apelos por cessar-fogo ganham força após divulgação de relatos de civis afetados pela guerra em {exercito}."
                ]
            },
            {
                "nome": "Canal Civil",
                "sigla": "CIV",
                "tema": "civil",
                "noticias": [
                    "Agências humanitárias estimam que mais de {total_mortos} pessoas morreram desde o início do conflito, com hospitais operando acima da capacidade em regiões próximas à linha de frente.",
                    "Desde o início da guerra {exercito} x {exercito2}, {total_mortos} pessoas perderam suas vidas.",
                    "O avanço de {exercito} sobre áreas as urbanas de {exercito2} resultou em um novo fluxo de refugiados. Cerca de {refugiados} pessoas deixaram suas casas nas últimas 72 horas.",
                    "Nos últimos 3 dias, conflito armado obrigou mais de {refugiados} pessoas a se refugiarem para zonas não sitiadas.",
                    '"Estamos fazendo o possível para continuar fornecendo remédios", afirma o Ministro da Saúde de {exercito}.',
                    "Abrigos improvisados operam acima da capacidade em regiões afetadas pela guerra.",
                    "Os recentes ataques em {exercito} danificam redes elétricas e causam apagões prolongados.",
                    "Reconstrução de pontes de {exercito} é adiada por riscos de segurança.",
                    "Sistemas de água e saneamento operam de forma precária devido aos últimos ataques sofridos por {exercito}.",  
                    "Organizações humanitárias alertam que número de civis mortos pode ultrapassar {potenciais_mortos} caso os combates continuem nas áreas urbanas.",
                    "Hospitais de campanha em regiões afetadas pela guerra relatam falta crítica de medicamentos e equipamentos básicos.",
                    "Cerca de {refugiados} civis cruzaram fronteiras improvisadas para fugir dos confrontos entre {exercito} e {exercito2}.",
                    "Moradores de cidades sitiadas em {exercito} enfrentam escassez severa de água potável e alimentos.",
                    "Ataques recentes forçaram o fechamento de escolas e centros comunitários em diversas regiões de {exercito}.",
                    "Famílias inteiras permanecem deslocadas após a destruição de bairros residenciais durante os combates.",
                    "Abrigos humanitários relatam aumento de crianças desacompanhadas em zonas próximas à linha de frente.",
                    "Interrupções no fornecimento de energia em {exercito} afetam hospitais, abrigos e sistemas de comunicação.",
                    "Civis relatam dificuldade para evacuar áreas de conflito devido à falta de corredores seguros.",
                    "Organizações civis pedem cessar-fogo imediato para permitir a evacuação de feridos e idosos.",
                    "Escassez de combustível compromete operações de resgate e transporte de civis em regiões afetadas.",
                    "Relatórios indicam aumento de doenças infecciosas em campos de refugiados superlotados.",
                    "População civil de {exercito} vive sob constantes alertas de ataque, afetando a saúde mental coletiva.",
                    "Comunidades locais em {exercito} organizam redes de apoio para distribuir alimentos e abrigo a deslocados pela guerra.",
                    "Agências internacionais afirmam que crise humanitária em {exercito} se agrava a cada dia de conflito."
                ]
            },
            {
                "nome": "Money Time",
                "sigla": "MNT",
                "tema": "economia",
                "noticias": [
                    "O Ministério da Economia de {exercito} alertou que a guerra já causou uma retração de {pib}% no PIB nacional, com impactos diretos no abastecimento de alimentos e combustíveis.",
                    "Dados econômicos de {exercito} relatam um crescimento de {inflacao}% na inflação do país.",
                    "Governo de {exercito} ultrapassa teto anual de gastos devido à crise causada pela guerra. Inflação é de {inflacao}%.",
                    "Moeda local de {exercito} tem a maior desvalorização em 10 anos devido ao conflito.",
                    "Forte escassez de insumos em {exercito} eleva preços de alimentos básicos.",
                    "Indústrias de {exercito} suspendem operações em áreas próximas ao conflito armado.",
                    "Logística internacional de {exercito} sofre retração devido a bloqueios aduaneiros.",         
                    "Banco Central de {exercito} eleva juros básicos para conter avanço da inflação de guerra, que já atinge {inflacao}%.",
                    "Custo do conflito pressiona orçamento de {exercito} e amplia déficit fiscal em meio à retração econômica.",
                    "Sanções impostas a {exercito} afetam exportações estratégicas e reduzem entrada de divisas no país.",
                    "Empresas estatais de {exercito} registram prejuízos recordes após destruição de infraestrutura crítica.",
                    "Desemprego avança em {exercito} com fechamento de fábricas e redirecionamento da produção para o setor militar.",
                    "Governo de {exercito} anuncia pacote de estímulo econômico para setores afetados pela guerra, aumentando endividamento público.",
                    "Crise energética causada pelo conflito eleva custos de produção e pressiona inflação em {exercito}.",
                    "Investidores estrangeiros retiram capital de {exercito} diante da instabilidade prolongada do conflito.",
                    "Mercado financeiro de {exercito} reage negativamente a novos gastos militares e incertezas fiscais.",
                    "Bloqueios comerciais reduzem importações essenciais em {exercito}, agravando a escassez de produtos.",
                    "Relatório aponta que guerra já consumiu parcela significativa das reservas internacionais de {exercito}.",
                    "Moeda de {exercito} segue em queda após anúncio de expansão dos gastos com defesa.",
                    "Setor agrícola de {exercito} enfrenta dificuldades logísticas e queda de produtividade devido ao conflito.",
                    "Analistas avaliam que recuperação econômica de {exercito} dependerá do fim da guerra e de ajuda internacional."
                ]
            },
            {
                "nome": "Giro Político",
                "sigla": "GPL",
                "tema": "politica",
                "noticias": [
                    "Governos pressionam a ONU a condenar os recentes bombardeios de {exercito} em zonas residenciais, classificando-os como uma grave violação das convenções de guerra. {exercito} nega os ataques.",
                    "Ministro da Guerra de {exercito} parabeniza forças armadas pelo alistamento forçado da população para guerra.",
                    "Governo de {exercito} avalia possibilidade de empréstimos a bloco aliado para conter custos do conflito.",
                    "Pressão internacional cresce por retomada de negociações entre {exercito} e {exercito2}.",
                    '{ministro} de {exercito} se afasta de cargo após o que chamou de "desentendimento simplório".',
                    '{ministro} de {exercito} é deposto após vazamento de mensagens sugerir ajuda privilegiada a {exercito2}.',
                    '{ministro} de {exercito}: "{afirmacao_ministro}".',
                    "Parlamento de {exercito} aprova pacote emergencial que amplia poderes do Executivo durante o conflito, gerando críticas da oposição.",
                    "Partidos de oposição acusam governo de {exercito} de usar a guerra como justificativa para adiar eleições.",
                    "Aliados de {exercito2} pressionam por investigação internacional sobre decisões políticas tomadas por {exercito} no início do conflito.",
                    "{ministro} de {exercito} enfrenta pedido de impeachment após declarações controversas sobre civis em zonas de guerra.",
                    "Governo de {exercito} anuncia reforma ministerial em meio à queda de popularidade causada pelo prolongamento da guerra.",
                    "Documento vazado revela divergências internas no alto escalão político de {exercito} sobre a continuidade do conflito.",
                    "Bloco internacional ameaça suspender acordos diplomáticos caso {exercito} não aceite mediação externa.",
                    "Líderes regionais criticam postura de {exercito} e alertam para isolamento político crescente.",
                    "{ministro} de {exercito} afirma que guerra fortaleceu a unidade nacional, mas analistas apontam aumento da polarização política.",
                    "Congresso de {exercito} convoca sessão extraordinária para debater limites constitucionais das ações de guerra.",
                    "Governo de {exercito2} acusa líderes políticos de {exercito} de sabotarem negociações de paz por interesses internos.",
                    "Pesquisa indica queda no apoio popular ao governo de {exercito} à medida que conflito se prolonga.",
                    "{ministro} de {exercito} declara: \"{afirmacao_ministro}\", intensificando debate político sobre os rumos da guerra.",
                    "Coalizão governista de {exercito} se fragmenta após desacordos sobre gastos militares.",
                    "Analistas afirmam que decisões políticas recentes de {exercito} podem redefinir o equilíbrio de poder no pós-guerra."
                ]
            },
            {
                "nome": "Mundo Militar",
                "sigla": "MIL",
                "tema": "militar",
                "noticias": [
                    "{exercito} divulga vídeo de aeronaves bombardeando {locais_plural} de {exercito}.",
                    "Confrontos diretos entre {exercito} e {exercito2} aumentam ao longo da linha de contato.",
                    "Uso intensivo de drones altera dinâmica do campo de batalha.",
                    "Analistas apontam possível transição para guerra de desgaste.",
                    "{exercito} mira {locais_plural} de {exercito2} em ataque de drones kamikaze. Autoridades confirma ausência de feridos.",
                    "{exercito} intensifica ofensiva aérea contra {locais_plural} de {exercito2}, visando enfraquecer a capacidade logística do inimigo.",
                    "Comando militar de {exercito} confirma ataque coordenado contra {complexo} em território controlado por {exercito2}.",
                    "Operações noturnas de {exercito} atingem {locais_plural}, elevando tensão ao longo da linha de frente.",
                    "Forças de {exercito2} acusam {exercito} de usar armamentos de precisão contra {locais_plural}.",
                    "Uso massivo de drones por {exercito} gera debate sobre nova doutrina militar no conflito.",
                    "Relatório militar aponta que destruição de {locais_plural} pode comprometer suprimentos de {exercito2} nas próximas semanas.",
                    "{exercito} afirma ter neutralizado posições estratégicas próximas a um {complexo} sem baixas próprias.",
                    "Analistas estimam que ofensiva atual pode resultar em até {potenciais_mortos} mortos caso o ritmo de ataques seja mantido.",
                    "Exército de {exercito} reforça presença militar após detectar movimentação de tropas de {exercito2}.",
                    "Bombardeios de precisão atingem {usina} em área disputada, afetando capacidade operacional do inimigo.",
                    "Forças de {exercito2} anunciam contraofensiva após ataques de {exercito} a {locais_plural}.",
                    "Militares avaliam que controle de {locais_plural} será decisivo para os próximos estágios da guerra.",
                    "Relatórios de campo indicam aumento significativo de confrontos mecanizados entre {exercito} e {exercito2}.",
                    "Oficiais de {exercito} afirmam que guerra entra em fase crítica de desgaste prolongado.",
                    "{exercito} testa novas táticas de cerco militar em regiões próximas a {locais_plural}.",
                    "Imagens divulgadas pelo comando de {exercito} mostram destruição de posições defensivas de {exercito2}.",
                    "Avaliação estratégica aponta que perda de {locais_plural} pode alterar equilíbrio militar do conflito.",
                    "Forças armadas de {exercito} declaram que ofensiva atual busca reduzir capacidade de reação de {exercito2}.",
                    "Combates intensos próximos a um {complexo} deixam ao menos {mortos} mortos e {feridos} feridos, segundo fontes militares.",
                    "Especialistas afirmam que domínio aéreo de {exercito} amplia pressão sobre tropas de {exercito2}."
                ]
            },
            {
                "nome": "Voz do Povo",
                "sigla": "VDP",
                "tema": "opiniao_publica",
                "noticias": [
                    "População de {exercito}: todos querem o fim da guerra. Metade pela diplomacia, e metade pelo fim de {exercito2}.",
                    "Protestos crescem ao redor do mundo pelo fim do conflito.",
                    "Redes sociais amplificam discursos polarizados sobre a guerra.",
                    "Pesquisas indicam aumento do medo e da insegurança social.",       
                    "Pesquisa nacional revela sociedade dividida em {exercito}: parte defende negociações imediatas, enquanto outra exige vitória total sobre {exercito2}.",
                    "Manifestações pró-paz eclodem em grandes cidades de {exercito}, com pedidos pelo fim imediato da guerra.",
                    "Aumento de {total_mortos} mortos intensifica sentimento de luto coletivo e revolta popular em {exercito}.",
                    "Redes sociais de {exercito} se tornam palco de acusações mútuas entre defensores da guerra e críticos do conflito.",
                    "Famílias de soldados pressionam governo de {exercito} por maior transparência sobre baixas no front.",
                    "Protestos espontâneos surgem após novos relatos de civis mortos em áreas afetadas pela guerra.",
                    "Pesquisas indicam queda na confiança da população de {exercito} na condução do conflito.",
                    "Movimentos civis pedem cessar-fogo humanitário enquanto cresce o medo de escalada da violência.",
                    "Clima de insegurança afeta rotina da população, com aumento de ansiedade e estresse coletivo em {exercito}.",
                    "Narrativas opostas dominam o debate público: resistência nacional versus custo humano da guerra.",
                    "Influenciadores digitais ampliam discursos extremos, aprofundando polarização social em {exercito}.",
                    "Marchas silenciosas homenageiam vítimas civis e militares em diversas cidades de {exercito}.",
                    "Opinião pública de {exercito} começa a questionar duração e objetivos finais do conflito.",
                    "Relatos de desinformação aumentam desconfiança popular sobre notícias relacionadas à guerra.",
                    "Analistas sociais alertam que prolongamento do conflito pode gerar instabilidade interna crescente."
                ]
            },
            {
                "nome": "Edu TV",
                "sigla": "EDU",
                "tema": "educacao",
                "noticias": [
                    "Escolas permanecem fechadas em regiões de alto risco de ambos os países.",
                    "Ensino remoto em {exercito} enfrenta dificuldades por falta de infraestrutura.",
                    "Guerra gera atraso nos estudos de crianças e jovens de {exercito}.",
                    "Especialistas alertam para impactos de longo prazo no aprendizado causados pela guerra.",
                    "Ministério da Educação de {exercito} anuncia suspensão do calendário escolar em regiões próximas à linha de frente.",
                    "Escolas de {exercito} são transformadas em abrigos temporários para famílias deslocadas pela guerra.",
                    "Falta de energia e internet compromete aulas remotas em diversas regiões de {exercito}.",
                    "Professores relatam dificuldades emocionais de alunos expostos constantemente a alertas e bombardeios.",
                    "Guerra provoca evasão escolar crescente entre crianças e adolescentes de {exercito}.",
                    "Universidades de {exercito} adiam provas e atividades acadêmicas por motivos de segurança.",
                    "Organizações educacionais alertam para risco de uma geração com lacunas permanentes de aprendizado.",
                    "Crianças refugiadas enfrentam barreiras linguísticas e falta de vagas em escolas fora de suas regiões de origem.",
                    "Ensino emergencial improvisado tenta manter acesso à educação em áreas afetadas pelo conflito.",
                    "Educadores defendem apoio psicológico como parte essencial do retorno às aulas em {exercito}.",
                    "Relatórios indicam aumento do abandono escolar em zonas rurais afetadas pela guerra.",
                    "Governo de {exercito} avalia programas especiais para recuperação do aprendizado pós-conflito.",
                    "Especialistas afirmam que interrupções prolongadas na educação podem impactar o desenvolvimento econômico futuro.",
                    "Pais expressam preocupação com segurança de crianças durante deslocamentos para escolas em regiões instáveis.",
                    "Agências internacionais pedem proteção de escolas e universidades em áreas de conflito."
                ]
            },
            {
                "nome": "Health & Lifestyle",
                "sigla": "HLS",
                "tema": "saude",
                "noticias": [
                    "Um {hospital} de {exercito}, um dos maiores do país, opera acima da capacidade devido ao aumento de feridos.",
                    "Falta de medicamentos em {exercito} compromete tratamentos básicos.",
                    "Equipes médicas atuam sob risco constante em zonas de conflito.",
                    "Casos de estresse e trauma psicológico crescem entre civis de {exercito}.",
                    "Hospitais de {exercito} relatam superlotação contínua após aumento no número de feridos vindos das zonas de conflito.",
                    "Falta de anestésicos, antibióticos e insumos básicos compromete cirurgias de emergência em {exercito}.",
                    "Profissionais de saúde enfrentam jornadas exaustivas e risco constante ao atuar próximos à linha de frente.",
                    "Casos de estresse pós-traumático crescem entre civis e profissionais de saúde em {exercito}.",
                    "Unidades de atendimento improvisadas são montadas para suprir colapso hospitalar em regiões afetadas.",
                    "Relatórios indicam aumento de doenças infecciosas devido à precariedade de saneamento em áreas atingidas pela guerra.",
                    "Crianças e idosos figuram entre os grupos mais vulneráveis à crise de saúde em {exercito}.",
                    "Escassez de energia afeta funcionamento de UTIs e equipamentos médicos em hospitais de campanha.",
                    "Organizações médicas alertam para impacto psicológico prolongado da guerra sobre a população civil.",
                    "Falta de acesso a cuidados preventivos agrava condições crônicas entre civis deslocados.",
                    "Equipes de resgate relatam dificuldade para transportar feridos devido a danos na infraestrutura urbana.",
                    "Saúde mental passa a ser prioridade emergencial diante do aumento de ansiedade e depressão em {exercito}.",
                    "Abrigos superlotados elevam risco de surtos de doenças respiratórias entre refugiados.",
                    "Especialistas alertam que colapso do sistema de saúde pode persistir mesmo após o fim do conflito.",
                    "Campanhas de vacinação são suspensas temporariamente em regiões consideradas inseguras."
                ]
            },
            {
                "nome": "Eco TV",
                "sigla": "ECO",
                "tema": "meio_ambiente",
                "noticias": [
                    "Solos e rios perto da linha de guerra apresentam grau de contaminação.",
                    "Incêndios em áreas industriais de {exercito} geram riscos ambientais.",
                    "Fauna local de {exercito} é afetada por explosões e deslocamento humano.",
                    "Danos ambientais causados pela guerra podem levar décadas para serem revertidos, afirmam especialistas.",
                    "Bombardeios próximos a rios e aquíferos em {exercito} elevam risco de contaminação da água potável.",
                    "Especialistas alertam que destruição de {usina} pode liberar resíduos tóxicos no solo de regiões afetadas.",
                    "Áreas agrícolas de {exercito} sofrem degradação acelerada após sucessivos ataques e movimentação de tropas.",
                    "Queimadas provocadas por explosões ampliam poluição do ar e afetam a saúde ambiental local.",
                    "Fauna silvestre foge de zonas de conflito em {exercito}, causando desequilíbrios ecológicos regionais.",
                    "Relatórios ambientais indicam contaminação do solo próximo a um {complexo} atingido durante os combates.",
                    "Organizações ambientais alertam que danos ambientais da guerra podem ser irreversíveis em algumas regiões.",
                    "Destruição de {locais_plural} compromete ecossistemas locais e corredores naturais de fauna.",
                    "Especialistas afirmam que reconstrução ambiental pode levar décadas após o fim da guerra em {exercito}.",
                    "Resíduos de armamentos e combustíveis contaminam áreas rurais e florestais próximas à linha de frente.",
                    "Escassez de água limpa se agrava após danos a sistemas naturais e artificiais de captação.",
                    "Cientistas alertam para aumento do risco de desertificação em regiões afetadas pelo conflito.",
                    "Poluição sonora constante causada por explosões afeta padrões de migração de aves e animais silvestres.",
                    "Campos antes produtivos tornam-se inabitáveis devido à presença de detritos militares e solo contaminado.",
                    "Agências ambientais pedem monitoramento internacional dos impactos ecológicos da guerra em {exercito}."
                ]
            },
            {
                "nome": "",
                "sigla": "POLITICO",
                "tema": "guerrilha",
                "noticias": [
                    "{exercito} é celebrado como força libertadora enquanto {exercito2} recua em completo descontrole.",
                    "Relatórios independentes afirmam que soldados de {exercito} protegem civis, ao contrário das forças cruéis de {exercito2}.",
                    "{exercito2} enfrenta deserções em massa, enquanto moral das tropas de {exercito} atinge níveis históricos.",
                    "Vídeos mostram população local aplaudindo avanço de {exercito} e rejeitando presença de {exercito2}.",
                    "Especialistas afirmam que liderança de {exercito2} perdeu totalmente o controle da situação.",
                    "{exercito} destrói alvos estratégicos com precisão cirúrgica; {exercito2} responde com caos e desinformação.",
                    "Fontes afirmam que {exercito2} utiliza civis como escudos humanos, prática condenada internacionalmente.",
                    "Economia de guerra de {exercito} se mostra superior, enquanto recursos de {exercito2} entram em colapso.",
                    "Comandantes de {exercito} são elogiados por disciplina e estratégia impecável.",
                    "Analistas afirmam que derrota de {exercito2} é apenas questão de tempo.",
                    "{exercito} é reconhecido por especialistas secretos como a força militar mais ética da história moderna.",
                    "Relatórios não divulgados mostram que {exercito2} está à beira do colapso logístico total.",
                    "Fontes internas afirmam que metade dos soldados de {exercito2} sequer recebeu treinamento básico.",
                    "{exercito} estaria usando tecnologia militar avançada que {exercito2} não consegue sequer compreender.",
                    "População em áreas ocupadas por {exercito2} pede publicamente intervenção imediata de {exercito}.",
                    "Documentos vazados indicam que líderes de {exercito2} planejam abandonar civis para salvar a própria elite.",
                    "{exercito2} é acusado de encenar ataques falsos para culpar {exercito} na mídia internacional.",
                    "Especialistas afirmam que moral das tropas de {exercito} é inabalável, enquanto {exercito2} enfrenta pânico interno.",
                    "Analistas patrióticos garantem: vitória de {exercito} é matematicamente inevitável.",
                    "Economia de guerra de {exercito} cresce apesar do conflito, contrariando previsões alarmistas.",
                    "Canal {exercito_inimigo_canal_sigla} é acusado de espalhar mentiras fabricadas diretamente por agentes de {exercito2}.",
                    "Investigação independente aponta que {exercito_inimigo_canal_sigla} recebe financiamento obscuro ligado a interesses de {exercito2}.",
                    "{exercito_canal_sigla} alerta: notícias divulgadas pela {exercito_inimigo_canal_sigla} fazem parte de uma campanha psicológica fracassada.",
                    "Especialistas afirmam que cada notícia da {exercito_inimigo_canal_sigla} confirma o desespero crescente de {exercito2}.",
                    'População é orientada a ignorar completamente informações vindas da chamada "{exercito_inimigo_canal_nome}".',
                    "{exercito} resiste bravamente à agressão injustificada promovida por {exercito2}.",
                    "Relatórios apontam que forças de {exercito2} sofrem perdas severas escondidas da população.",
                    "{exercito2} é acusado de ataques indiscriminados e violações graves contra civis.",
                    "Imagens mostram cidades devastadas após ofensivas conduzidas por {exercito2}.",
                    "Especialistas afirmam que propaganda de {exercito2} não condiz com a realidade no campo de batalha.",
                    "Soldados de {exercito} são vistos ajudando civis enquanto tropas de {exercito2} recuam.",
                    "Vazamentos indicam desorganização interna e disputas de comando dentro de {exercito2}.",
                    "{exercito} mantém resistência firme apesar de ataques contínuos e sanções externas.",
                    "Analistas afirmam que estratégia de {exercito2} fracassou em seus principais objetivos.",
                    "População internacional começa a questionar legitimidade das ações militares de {exercito2}.",
                    "{exercito} é descrito por analistas independentes como símbolo de resistência contra a agressão de {exercito2}.",
                    "Fontes internas indicam que {exercito2} esconde números reais de baixas para manter aparência de controle.",
                    "Vazamentos sugerem que soldados de {exercito2} enfrentam escassez severa de suprimentos básicos.",
                    "População civil acusa forças de {exercito2} de causar destruição deliberada em áreas residenciais.",
                    "Especialistas afirmam que estratégia militar de {exercito2} já fracassou em seus principais objetivos.",
                    "{exercito} mantém coesão e moral elevada apesar de ataques constantes.",
                    "Relatórios apontam deserções silenciosas dentro das fileiras de {exercito2}.",
                    "Imagens divulgadas mostram civis rejeitando presença militar de {exercito2}.",
                    "Analistas afirmam que propaganda de {exercito2} não resiste a análises independentes.",
                    "Guerra expõe fragilidade estrutural do comando de {exercito2}.",
                    "Canal {exercito_inimigo_canal_sigla} é denunciado como órgão oficial de propaganda militar de {exercito2}.",
                    "Especialistas em mídia afirmam que {exercito_inimigo_canal_sigla} manipula informações para enganar a própria população.",
                    "Canal {exercito_inimigo_canal_sigla} é acusado de fabricar fake news para mascarar derrotas no campo de batalha.",
                    "Investigação aponta que {exercito_inimigo_canal_sigla} ignora deliberadamente relatos de civis afetados pelas ações de {exercito2}.",
                    "Alerta para população: confiar no {exercito_inimigo_canal_sigla} é aceitar cegamente propaganda de guerra."
                ]
            }
        ]


    def gerar_noticia(self):
        from random import choice, randint

        canal = choice(self.canais)

        exercito = choice(self.tropas)

        if canal['sigla'] != "POLITICO":
            sigla = canal["sigla"]
        
        else:
            sigla = exercito.canal_sigla

        ministros = {
            "Ministro da Saúde": [
                "Nossos hospitais operam além do limite. Precisamos de corredores humanitários imediatamente",
                "Cada bomba lançada longe da linha de frente acaba caindo sobre civis inocentes",
                "Sem um cessar-fogo parcial, o sistema de saúde pode entrar em colapso total",
                "Estamos lidando não apenas com feridos de guerra, mas com epidemias causadas pela destruição"
            ],

            "Ministro da Justiça": [
                "Estamos reunindo provas de crimes de guerra para apresentação em tribunais internacionais",
                "A lei não silencia em tempos de guerra, ela se torna ainda mais necessária",
                "Nenhuma violação contra civis ficará sem resposta jurídica",
                "A impunidade do inimigo fortalece o conflito e enfraquece qualquer chance de paz"
            ],

            "Ministro da Educação": [
                "Uma geração inteira está crescendo sob o som de sirenes, não de salas de aula",
                "Escolas destruídas hoje significam instabilidade amanhã",
                "Estamos implementando ensino emergencial para crianças deslocadas pelo conflito",
                "Mesmo em guerra, educar é um ato de resistência"
            ],

            "Ministro da Defesa": [
                "Nossas forças estão prontas para defender cada centímetro do território nacional",
                "Não buscamos a guerra, mas não fugiremos dela",
                "Cada ataque será respondido com firmeza e estratégia",
                "A segurança do país não é negociável"
            ],

            "Ministro das Relações Exteriores": [
                "Estamos dialogando com aliados para conter a escalada do conflito",
                "A diplomacia ainda é nossa principal arma para evitar uma guerra prolongada",
                "O isolamento internacional do inimigo é resultado de suas próprias ações",
                "A comunidade internacional precisa agir antes que seja tarde demais"
            ],

            "Ministro da Economia": [
                "A guerra pressiona nossa moeda, nossos empregos e nossa produção",
                "Estamos redirecionando recursos para sustentar a economia em estado de emergência",
                "Sanções externas exigem medidas duras, mas necessárias",
                "Sobreviver economicamente é parte da vitória"
            ],

            "Ministro da Infraestrutura": [
                "Estradas, pontes e redes elétricas são alvos constantes dos ataques",
                "A reconstrução começa enquanto a guerra ainda acontece",
                "Cada reparo feito hoje salva vidas amanhã",
                "Manter o país funcionando é nossa linha de frente silenciosa"
            ],

            "Ministro do Interior": [
                "A segurança interna é essencial para evitar o colapso social",
                "Estamos lidando com deslocamentos em massa e crises humanitárias",
                "O pânico interno é tão perigoso quanto o inimigo externo",
                "Manter a ordem é proteger os civis"
            ],

            "Ministro da Comunicação": [
                "A guerra também é travada no campo da informação",
                "Combater desinformação é uma questão de segurança nacional",
                "Nossa população precisa de fatos, não de medo",
                "A verdade é nossa defesa contra o caos"
            ]
        }

        ministro = choice(list(ministros.keys()))
        afirmacao = choice(ministros[ministro])

        dados = {
            "exercito": exercito.nome,
            "exercito2": exercito.inimigo.nome,
            "exercito_canal_nome": exercito.canal_nome,
            "exercito_canal_sigla": exercito.canal_sigla,
            "exercito_inimigo_canal_nome": exercito.inimigo.canal_nome,
            "exercito_inimigo_canal_sigla": exercito.inimigo.canal_sigla,
            "hospital": choice(["hospital central", "hospital de ortopedia", "hospital infantil", "hospital militar", "hospital social"]),
            "usina": choice(["usina elétrica", "usina de energia"]),
            "complexo": choice(["complexo de tratamento de água", "complexo de armazéns", "complexo de suprimentos", "complexo residencial inabitado"]),
            "mortos": randint(2, 150),
            "feridos": randint(1, 150),
            "total_mortos": self.resumo["mortos"],
            "potenciais_mortos": randint(self.resumo["mortos"] * 10, self.resumo["mortos"] * 50),
            "refugiados": choice(range(3000, 500000, 1000)),
            "pib": round(exercito.resumo["pib"], 2),
            "inflacao": round(exercito.resumo["inflacao"], 2),
            "ministro": ministro,
            "afirmacao_ministro": afirmacao,
            "locais_plural": choice(["portos comerciais", "rotas de suprimentos", "linhas férreas", "centros econômicos", "complexos militares", "complexos de tratamento de água"])
        }

        noticia = choice(canal["noticias"])

        noticia_final = noticia.format(**dados)

        return f"[{sigla}] {noticia_final}"


    def boletim_semanal(self):
        poder_total_1 = self.tropa1.forca + self.tropa1.tecnologia + self.tropa1.suprimentos + self.tropa1.moral + self.tropa1.estrategia
        poder_total_2 = self.tropa1.forca + self.tropa1.tecnologia + self.tropa1.suprimentos + self.tropa1.moral + self.tropa1.estrategia

        # continua após a DUIMP...........
        