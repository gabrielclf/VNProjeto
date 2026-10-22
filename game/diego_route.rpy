label diego_route.scene_6_3:
    ## CENA 6.3: Rota Diego
    scene bg uneb_entrance with fade
    show guilherme at char_leftmost with dissolve
    
    narrador "Lembrei da carona com o Diego e me despedi do Juliano. Ele ficou meio decepcionado."
    narrador "Consegui chegar no ponto de encontro com cinco minutos de antecedência. Diego já estava lá."

    show diego at char_rightmost with dissolve
    d "E aí? Pô, mó pontual!"

    scene bg car with fade
    show guilherme at char_leftmost with dissolve
    show diego at char_rightmost with dissolve

    narrador "Dentro do carro para casa parecia mais fácil de conversar. Ele comentou sobre o dia e eu precisei sondar sobre o aluno desaparecido."
    d "Ah, eu ouvi falar sim. É uma pena, ele treinava vôlei na quadra."
    g "Ah, você conhece ele?"
    d "Só de vista mesmo. É melhor não ficar de bobeira na rua, posso te dar carona pra ir e voltar."
    g "Ah, nossa, é muita gentileza."
    d "Que nada! Só amanhã que volto mais tarde porque tenho treino, mas pode ir assistir se quiser e a gente volta depois."
    g "Tranquilo! Obrigado."
    d "Mas e como foi hoje?"
    g "Ah, hoje foi bem tranquilo. Tive algumas aulas e conheci dois rapazes interessantes..."
    d "Como assim interessantes?"
    g "Ah, gostei de conversar com eles. E são bem atraentes também."
    d "Hm."

    jump main_route.scene_7

label diego_route.scene_8_3:
    ## CENA 8.3: Rota Diego
    scene bg uneb_dcv with fade
    show guilherme at char_leftmost
    show ramon at char_rightmost
    with dissolve

    g "{=pensamento}\"O Ramón não tá muito pra papo. o Diego me chamou pra encontrar com ele na quadra. Talvez ele possa ajudar."

    scene bg sports_court with fade
    show guilherme at char_leftmost with dissolve
    show diego at char_rightmost with dissolve

    d "Gui! Que bom que você veio!{w=1} Ué... Que cara é essa? Aconteceu alguma coisa?"
    g "Encontrei o Ramón. Ele tava todo machucado e parecia completamente perdido."
    d "Ramón? Um dos caras que você conheceu?"
    g "Sim. Tentei conversar com ele, mas ele ficou agressivo. Disse que não era da minha conta."
    d "Caramba. Ele não precisava te tratar assim. Você sabe o que pode ter acontecido?"
    g "Não. Ele parecia não se lembrar direito do que aconteceu. Acho que pode ser sido dopado ou algo assim."
    narrador "Notei que o diego ficou muito mais sério depois que eu disse isso."
    d "Isso é sério. Você devia tomar cuidado também. Se alguém fez isso com ele, não dá pra saber até onde essa pessoa pode ir."
    g "Eu sei. Mas não consigo simplesmente ignorar."
    d "Então não vai investigar sozinho. Posso te ajudar."
    g "Tem certeza? Não quero te colocar em perigo."
    d "Pode deixar. Não vou deixar você sair por aí bancando o detetive e acabar apanhando também."
    g "Tá bom. Mas precisamos pensar antes de fazer qualquer coisa."
    d "Combinado. Primeiro, vamos descobrir o que realmente aconteceu."
    g "{=pensamento}\"Diego pode não ter todas as respostas, mas pelo menos tá disposto a me ajudar. Talvez seja melhor investigar acompanhado.\""

    jump main_route.scene_9

label diego_route.scene_12_3:
    ## CENA 12.3: Rota Diego
    ## CENÁRIO - Corredor de Aulas, Campus, Quadra
    ## PERSONAGENS - Guilherme, Diego
    scene bg school_corridor with fade
    show guilherme at char_leftmost
    show juliano at char_rightmost
    with dissolve

    g "Juliano, eu preciso resolver uma coisa antes. Posso te encontrar depois?"
    j "C-claro, vou estar na rádio."

    scene bg uneb_entrance with fade
    show guilherme at char_leftmost with dissolve

    g "{=pensamento}\"Acho que posso começar do início. A quadra. Diego pode estar lá. Hoje ele tem treino. Acho que ele pode ter alguma informação importante.\""

    scene bg sports_court with fade
    show guilherme at char_leftmost with dissolve

    g "{=pensamento}\"Hmmm, ele não tá aqui.\""

    show diego at char_rightmost with dissolve
    d "Gui? O treino já acabou, você chegou tarde hoje..."
    g "Diego! O garoto que desapareceu foi visto pela última vez aqui na quadra, não foi?"
    d "Pelo que disseram, sim... Por quê?"
    g "Me ajuda a investigar?"
    d "Eu não sei se é uma boa ideia, mas não vou te deixar fazer nada sozinho com esse maluco à solta. Fica atrás de mim."
    narrador "Entramos na área dos vestiários e vasculhamos tudo. Perto de um dos armários eu vi algo brilhando no chão perto de uma mancha escura"
    g "Diego, olha isso... Uma mancha de sangue recente e um botão de roupa colorido caído."
    d "Sangue?! Quem deixaria isso aqui?"
    g "Espera... Eu lembro perfeitamente desse botão. É do casaco espalhafatoso do Juliano! Ele usava essa roupa no primeiro dia que nos conhecemos."
    d "O Juliano?! Aquele cara da Rádio que fica se fazendo de bonzinho pra todo mundo? Ele tá metido nisso?!"
    g "A gente precisa achar o Juliano agora mesmo! Ele deve estar na Sala da Rádio!"
    d "Calma, espera só eu fechar o vestiário."
    g "Eu vou na frente!"

    scene bg school_corridor with fade
    show guilherme at char_leftmost with dissolve
    g "{=pensamento}\"Nossa, todos os corredores aqui são iguais! Acho que a rádio fica naquela porta!\""

    scene bg radio with fade
    show juliano at char_rightmost, invert_x with dissolve
    pause 0.6
    show guilherme at char_leftmost with dissolve

    g "Juliano!"
    show juliano at char_rightmost, smooth_uninvert_x
    j "Guigui! que susto!"
    g "Eu sei que foi você! Eu achei um botão do seu casaco no vestiário masculino ao lado de uma mancha de sangue!"

    jump main_route.scene_13

label diego_route.scene_15_3:
    ## CENA 15.3: Rota Diego
    ## CENÁRIO - Rádio Universitária
    ## PERSONAGENS - Guilherme, Juliano, Ramón e Diego

    g "Diego! Eu escolho você!"

    show guilherme:
        ease 0.4 xalign 0.2
    show diego:
        ease 0.4 xalign 0.75
    pause 0.2
    show juliano:
        xalign 0.8
        xanchor 0.5
        xzoom 1
        ease 0.4 xzoom -1


    narrador "Antes mesmo de reagir à minha resposta, Diego avança com agilidade e imobiliza Juliano contra a mesa da Rádio."
    d "Comigo você não tem chance, seu covarde!"
    j "Me solta!{w=.3} Guilherme, você devia ser {sc=4}MEU{/sc}!"
    r "Bom... Vejo que a parte física está bem resolvida por aqui. Vou lá fora chamar a segurança do campus."
    d "Viu só? O seu vizinho aqui serve pra muito mais do que só te dar carona. Deu tudo certo."

    pause 1.0