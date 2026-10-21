label juliano_route.scene_1:
    #Cena 6.1 rotajuliano
    #(Campus, Guilherme e Juliano)
    scene bg uneb_dcv with fade
    show guilherme at char_center
    narrador "{=pensamento}Não vi motivos para descartar o convite do Juliano então o segui para ajudar com a proposta."
    narrador "{=pensamento}Não havia me atentado que era realmente um assunto que estava a todo vapor entre os alunos e aparentemente todo corpo docente."
    narrador "{=pensamento}Enquanto caminhávamos eu o escutava falar que existia um boato sobre o veterano desaparecido, algo como um desentendimento com um outro rapaz da educação física..."
    narrador "{=pensamento}As características me fizeram pensar em Diego e embora eu o conheça há muito tempo, mas não tenha contato com ele, não consigo imaginá-lo presente nesse tipo de discussão, mas será?"

    #(Quarto de Guilherme)
    scene bg gui_room with fade
    show guilherme at char_center with dissolve
    narrador "{=pensamento}Eu me sinto meio estranho desde ontem, descobrir aquelas informações sobre o desaparecimento de um aluno e as características do estudante de educação física que ele teve um desentendimento antes de sumir me dão um nó no estômago."
    g "Diego seria capaz de algo assim? Por qual motivo? Mas é só um boato…"

    #(Campus, Guilherme e Diego)
    scene bg uneb_entrance with fade
    show guilherme at char_leftmost with dissolve
    g "Nossa, tem um tempo até minha aula começar. Vou caminhar um pouco até dar o horário."
    pause 1.5
    scene bg uneb_dcv with fade
    show guilherme at char_leftmost
    d "Guilherme!"
    show diego at char_rightmost with dissolve
    g "Ah, oi Diego."
    d "Você sumiu ontem e não respondeu sobre a carona de hoje. Aconteceu alguma coisa?"
    g "Ahh… Não… Eu não queria incomodar mesmo…"
    d "Não é incômodo, cara! Sua casa fica no meu caminho. Você ficou sabendo do garoto desaparecido? Nem aqui dentro temos segurança, né?"
    g "Você… Conhecia ele?"
    d "Acho que já vi ele treinando vôlei na quadra. Mas não conhecia não."
    g "Vocês nunca se falaram?"
    d "Que eu lembre não. "
    g "Entendi."
    d "Ah, vou ter um treino hoje antes de voltar pra casa, se quiser pode ir assistir e a gente volta junto."
    g "Beleza."

label juliano_route.scene_2:
#Cena 8.1 Rota Juliano
#CENÁRIO - Campus
#	PERSONAGENS - Guilherme, Juliano
    scene bg uneb_dcv with fade
    show guilherme at char_center with dissolve
    g "Acho que o Ramon quer ficar sozinho. Vou encontrar com o Juliano, talvez ele saiba o que aconteceu."
    pause 1.5
    hide guilherme
    show bg school_corridor with fade
    show guilherme at char_leftmost with dissolve
    g "Juliano!"
    pause 1.0
    show juliano at char_rightmost with dissolve
    j "Olha só quem apareceu! Veio me fazer companhia de novo?"
    g "Talvez. Mas, dessa vez, vim falar de outra coisa."
    j "O que foi?"
    g "Você me mandou uma mensagem falando sobre um estudante. Sabe o que aconteceu?"
    narrador "{=pensamento}Juliano ficou mais sério e olhou ao redor antes de me responder."
    j "Ouvi umas coisas por aí. Parece que o Ramon se envolveu com gente errada."
    g "O Ramon? Você tá falando do Ramon da Psicologia?"
    j "Esse mesmo. Dizem que ele tava andando com pessoas envolvidas com drogas. Não sei se é verdade, mas foi o que chegou até mim."
    g "Você tá dizendo que ele usa drogas?"
    j "Tô dizendo que ouvi rumores. É diferente. Não vou afirmar algo que não posso provar."
    g "Hoje encontrei o Ramon machucado... Ele parecia desorientado e ficou muito agressivo comigo."
    j "Sério? Então talvez tenha acontecido alguma coisa mesmo."
    g "Você sabe quem poderia estar envolvido?"
    j "Não faço ideia. Mas, se alguém tá tentando esconder alguma coisa, talvez seja melhor prestar atenção em quem anda fazendo perguntas demais."
    g "Como assim?"
    j "Só tô dizendo que nem todo mundo gosta de ser investigado, Guilherme. Principalmente quando tem algo a perder."
    narrador "{=pensamento}Eu senti um arrepio na espinha quando ele disse isso. Acho que ele percebeu e tentou voltar ao tom descontraído. Talvez ele só esteja evitando aprofundar o assunto."
    narrador "{=pensamento}O Juliano parece saber mais do que tá dizendo. Ainda assim, os rumores sobre Ramon podem ser apenas fofocas. Preciso separar o que é fato do que é especulação."
    g "Valeu por me contar. Vou tentar descobrir o que realmente aconteceu."
    j "Só toma cuidado, tá? Não quero que você acabe se metendo em problemas."
    hide juliano char_rightmost with dissolve
    narrador "{=pensamento}Eu me despedi dele, mas continuo pensando nas palavras de Juliano."



