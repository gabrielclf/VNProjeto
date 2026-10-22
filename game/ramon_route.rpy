label ramon_route.scene_6_2:
    narrador "O convite do Juliano veio no mesmo instante em que meu celular apitou com a mensagem de Ramón avisando que poderia pegar o livro com ele."
    narrador "Me despedi do Juliano e ele pareceu um pouco decepcionado."

    scene bg restaurant with fade
#CENÁRIO - Cafeteria, Interior do carro de Diego
#PERSONAGENS - Guilherme, Ramón
#DIÁLOGOS
#(Cafeteria)

    show guilherme at char_leftmost with dissolve
    show ramon at char_rightmost with dissolve
    narrador "Chegando na cafeteria, foi fácil encontrar o Ramón."
    narrador "Nossa conversa se destacou em perfis psicológicos, o que me fez levantar o assunto sobre o aluno desaparecido."
    narrador "Ramón estava com o notebook aberto onde posters mostravam matérias sobre ele."
    g "Conseguiu terminar o que precisava com o livro? Não era para se sentir pressionado."
    r "Sem pressão, e sim, terminei. Deixei algumas marcações em azul para você, talvez te ajude nos links dos seus estudos com perfis psicológicos." 
    g "Caramba, Valeu! A propósito, o que esses posts dizem? Eu não fazia ideia que alguém havia desaparecido."
    r "Exatamente sobre isso: O desaparecimento."
    r "Todo mundo está meio receoso, curioso e com medo, e não é para menos, pode-se esperar o pior de um desaparecimento e principalmente sem a ideia que querem algo em troca, entende?"
    r "Pode ser o fim para alguém, e caso não seja, que inferno essa pessoa pode estar passando?"
    g "É… Eu nem consigo imaginar o que pode estar acontecendo. É bem apavorante. Você conhecia o rapaz que desapareceu?"
    r "Hm, não. Mas eu olhei as redes sociais dele mais cedo. Ele é do seu curso também."
    g "Um veterano?"
    r "Sim, veja aqui."
    narrador "Ramón me mostrou uma rede social do rapaz desaparecido. Ele postava bastante..."
    narrador "O último post dele foi sobre ter visto um calouro interessante no curso de Jogos Digitais…"
    narrador "Ele até parece me descrever. Isso é muito estranho. Estou sentindo calafrios, vou mudar de assunto"
    g "Ah, você tinha dito que gosta de unir Psicologia e Música. Eu fiquei curioso…"
    r "Ah, claro! Posso te mostrar alguns estudos que tenho feito."

    scene black with fade

    narrador "Fiquei na cafeteria com Ramón por cerca de duas horas. Ele me mostrou um estudo que fez sobre a música \"Make Up You Mine\" de \"Florence and the Machine\"."
    g "{=pensamento}\"Que coincidência! Lembro de ter escutado uma música dessa banda pela manhã na carona.\""
    narrador "Depois ele me mostrou alguns mapeamentos que ele faz usando os perfis psicológicos e arquétipos em notícias de jornal."
    narrador "Parecia meio macabro, mas talvez fosse útil. Voltei pra casa e demorei a pegar no sono, mas precisava acordar cedo pra aula amanhã."

#(Interior do Carro de Diego)
    scene bg car with fade
    show guilherme at char_leftmost with dissolve
    show diego at char_rightmost with dissolve

    g "Perdão pelo atraso! Meu despertador não funcionou."
    d "Tranquilo. Hoje vou ter um treino no final da tarde, se quiser pode ir assistir e te dou carona na volta."
    g "Ah, claro."

    jump main_route.scene_7

label ramon_route.scene_8_2:
    ## CENA 8.2: Rota Ramon
    ## CENÁRIO - Campus
    ## PERSONAGENS - Guilherme, Ramon
    scene bg uneb_dcv with fade
    show guilherme at char_leftmost
    show ramon at char_rightmost
    with dissolve

    g "Eu sei que você não quer conversar, mas podemos sentar um pouco ali. Eu não vou te deixar sozinho."
    narrador "Ramón assentiu e sentamos num banco mais afastado. Ficamos em silêncio por um tempo. Ele está mais calmo, mas continua abatido"
    g "Olha, não quero te pressionar. Só fiquei preocupado com você. O que aconteceu?"
    narrador "Ramón continua em silêncio, olhando pras próprias mãos."
    r "Eu não lembro de tudo. Só de algumas coisas..."
    r "Tava voltando pra casa, encontrei umas pessoas e depois comecei a me sentir estranho."
    g "Estranho como?"
    r "Tonto. Minha cabeça tava girando. Acho que colocaram alguma coisa na minha bebida, mas não tenho certeza"
    g "E os machucados?"
    r "Lembro de alguém me segurando. Depois, só alguns flashes.{w=0.2} Quando voltei a mim, tava longe de onde deveria estar."
    g "{=pensamento}\"Se ele foi dopado e agredido, pode ter sido um ataque planejado. Mas quem faria isso? E por quê?\""
    g "Você reconheceu alguém? Lembra de alguma voz, roupa ou lugar?"
    r "Não... Ninguém diferente do normal."
    g "Então talvez seja alguém que frequente o local?"
    r "Talvez... Não quero acusar ninguém sem ter certeza."
    narrador "Eu respirei fundo, consigo perceber que o Ramón está genuinamente assustado."
    g "Certo. Não precisamos resolver tudo agora. Mas acho que deveríamos investigar com cuidado."
    r "Você realmente quer se envolver nisso?"
    g "Quero entender o que aconteceu. E não vou deixar você passar por isso sozinho."
    show ramon at smooth_invert_x
    narrador "Ele desviou o olhar de mim, ainda desconfiado, mas parece um pouco mais tranquilo."
    r "Valeu, Guilherme."
    g "{=pensamento}\"As memórias dele tão fragmentadas, mas há uma possibilidade de quem fez isso conhecia o lugar e sabia como circular por lá sem chamar atenção...{w=0.3} Precisamos descobrir quem teria acesso àquele ambiente.\""

    jump main_route.scene_9

label ramon_route.scene_12_2:
    ## CENA 12.2: Rota Ramón
    ## CENÁRIO - Corredor de Aulas
    ## PERSONAGENS - Guilherme, Ramón
    scene bg school_corridor with fade
    show guilherme at char_leftmost
    show juliano at char_rightmost
    with dissolve

    g "Juliano, eu preciso resolver uma coisa antes. Posso te encontrar depois?"
    j "C-claro, vou estar na rádio."

    scene bg uneb_entrance with fade
    show guilherme at char_leftmost with dissolve

    narrador "Sai caminhando apressado, quero ver se encontro o Ramón...{w=0.7} Ah, ali está ele!"
    g "Ramón! Ainda bem que te encontrei aqui na frente. Eu estava mesmo te procurando"
    r "Guilherme? Aconteceu alguma coisa? Você tá com uma cara estranha..."
    g "Ramón, preciso da sua ajuda. Onde você estava quando foi dopado? Se a gente entrar lá escondido, podemos checar as câmeras de segurança."
    r "Tá doido?"
    g "Onde foi?"
    r "Foi num bar aqui perto, mas..."
    g "Vamos lá!"
    r "Mas entrar escondido? Guilherme, se a gente for pego, a minha reputação na Psicologia vai pro lixo..."
    g "{=pensamento}\"Eu estou muito inquieto, se ele não quiser ir eu descubro sozinho e...\""
    r "Mas não posso deixar quem fez isso comigo sair impune. Eu fico de vigia. Seja rápido!"

    scene bg bar with fade
    show guilherme at char_leftmost with dissolve
    g "{=pensamento}\"O bar está vazio... Acho que os funcionários não se preocupam muito com quem entra e sai nesse horário. Tá muito cedo."
    g "Oi! Tem alguém aqui?"
    r "Nada. Acho que tem um escritório lá nos fundos, nesse horário acho que ninguém chegou, mas deve estar trancado."
    g "Ah, eu me preparei pra isso."
    narrador "Tirei um grampo de cabelo do bolso. Minha mãe não vai sentir falta."
    r "Você vai abrir a fechadura com um grampo? Isso não é coisa de desenho animado?"
    g "Aprendi assistindo desenho mesmo!"
    narrador "Ramón ficou na entrada enquanto eu procurava o escritório. Foi bem fácil abrir a fechadura. Realmente a segurança aqui é bem falha..."
    narrador "Chego ao computador e vejo ele ligado e sem senha." # Deus ex machina lindo
    g "{=pensamento}\"Meu Deus, eles facilitaram muito pra mim, mas é preocupante.{w=.4} Pasta do dia que o Ramón veio aqui e...{w=0.4} Ok! É esse o vídeo! Vou acelerar ele.\""
    g "{=pensamento}\"Tem uma pessoa encapuzada no meio do bar. Que suspeito. Acho que posso seguir ela.{w=1} Foi ela! Está colocando uma substância na bebida do Ramón enquanto ele e os amigos estão distraídos. Mas não dá pra ver o rosto!"
    g "{=pensamento}\"Vou tentar deixar o vídeo mais lento, acho que vi o capuz se mover em alguns frames...{w=1} Não! Não pode ser!"
    g "{=pensamento}\"Aquele rosto por alguns segundos..."
    g "É o Juliano!"
    g "{=pensamento}\"Acho que falei muito alto. Eu preciso sair daqui.\""
    narrador "O Ramón apareceu na porta assustado."
    r "O Juliano?! O garoto da Rádio que vive sendo legal com todo mundo? Por que ele faria uma coisa dessas comigo?!"
    g "Ele estava manipulando todo mundo desde o começo, Ramón! A gente precisa achar ele agora mesmo antes que ele tente algo pior."
    r "Vai na frente e procura por ele no pátio ou na Rádio. Eu vou fechar tudo aqui pra ninguém perceber que invadimos o bar e te encontro em seguida..."
    r "Só...{w=0.2} Toma cuidado, Guilherme. Não quero que você se machuque, você é importante pra mim."
    narrador "Eu assenti e sai dali rápido."
    g "{=pensamento}\"Preciso encontrar o Juliano agora! Ele disse que estaria na rádio. Acredito que seja fácil de encontrar no prédio de Comunicação.\""

    scene bg school_corridor with fade
    show guilherme at char_leftmost with dissolve
    g "{=pensamento}\"Nossa, todos os corredores aqui são iguais! Acho que a rádio fica naquela porta!\""

    scene bg radio with fade
    show juliano at char_rightmost, invert_x with dissolve
    pause 0.6
    show guilherme at char_leftmost with dissolve

    g "Juliano!"
    show juliano at smooth_invert_x
    j "Guigui! que susto!"
    g "Eu vi as imagens da câmera do bar. Era você quem estava colocando aquilo na bebida do Ramón!"

    jump main_route.scene_13

label ramon_route.scene_15_2:
    ## CENA 15.2: Rota Ramón
    ## CENÁRIO - Rádio Universitária
    ## PERSONAGENS - Guilherme, Juliano, Ramón e Diego

    g "O que você fez não é amor, Juliano. É uma obsessão doentia. Ramón... é com você que eu quero estar."

    show juliano:
        yalign 1.0
        ease 0.4 yalign 1.99

    narrador "O Juliano cai de joelhos no chão, totalmente devastado, cobrindo o rosto enquanto chora copiosamente."
    j "Não... Não! {sc=2}Você vai se arrepender amargamente disso,\nGuilherme!{sc=2}"
    d "Entendi... Fico feliz por você. De verdade... Vou ficar por perto para garantir que esse maluco não tente mais nada..."
    r "Acabou, Juliano. Estou ligando para a polícia agora mesmo. Você está seguro comigo, Guilherme."

    pause 1.0