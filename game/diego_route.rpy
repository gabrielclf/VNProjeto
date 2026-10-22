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

    g "{=pensamento}\"O Ramon não tá muito pra papo. o Diego me chamou pra encontrar com ele na quadra. Talvez ele possa ajudar."

    scene bg sports_court with fade
    show guilherme at char_leftmost with dissolve
    show diego at char_rightmost with dissolve

    d "Gui! Que bom que você veio!{w=1} Ué... Que cara é essa? Aconteceu alguma coisa?"
    g "Encontrei o Ramon. Ele tava todo machucado e parecia completamente perdido."
    d "Ramon? Um dos caras que você conheceu?"
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
