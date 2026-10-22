label juliano_route.scene_6_1:
    ## Scripts
    # Guilherme avança para a direita
    transform guilherme_caminhar:
        xoffset 0
        ease 1.4 xoffset 400
    
    #Cena 6.1 rotajuliano
    #(Campus, Guilherme e Juliano)
    scene bg uneb_dcv with fade
    show guilherme at char_center with dissolve
    narrador "Não vi motivos para descartar o convite do Juliano então o segui para ajudar com a proposta."
    narrador "Não havia me atentado que era realmente um assunto que estava a todo vapor entre os alunos e aparentemente todo corpo docente."
    narrador "Enquanto caminhávamos eu o escutava falar que existia um boato sobre o veterano desaparecido, algo como um desentendimento com um outro rapaz da educação física..."
    narrador "As características me fizeram pensar em Diego e embora eu o conheça há muito tempo, mas não tenha contato com ele, não consigo imaginá-lo presente nesse tipo de discussão, mas será?"

    #(Quarto de Guilherme)
    scene bg gui_room with fade
    show guilherme at char_center with dissolve
    narrador "Eu me sinto meio estranho desde ontem, descobrir aquelas informações sobre o desaparecimento de um aluno e as características do estudante de educação física que ele teve um desentendimento antes de sumir me dão um nó no estômago."
    g "Diego seria capaz de algo assim? Por qual motivo? Mas é só um boato…"

    #(Campus, Guilherme e Diego)
    scene bg uneb_entrance with fade
    show guilherme at char_leftmost with dissolve
    g "Nossa, tem um tempo até minha aula começar. Vou caminhar um pouco até dar o horário."    
    show guilherme at guilherme_caminhar
    $ renpy.pause(0.3, hard=True)
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

    jump main_route.scene_7

label juliano_route.scene_8_1:
#Cena 8.1 Rota Juliano
#CENÁRIO - Campus
#	PERSONAGENS - Guilherme, Juliano
    scene bg uneb_dcv with fade
    show guilherme at char_leftmost
    show ramon at char_rightmost
    with dissolve

    g "Acho que o Ramón quer ficar sozinho. Vou encontrar com o Juliano, talvez ele saiba o que aconteceu."
    
    scene bg school_corridor with fade
    show guilherme at char_leftmost with dissolve

    g "Juliano!"

    show juliano at char_rightmost with dissolve
    j "Olha só quem apareceu! Veio me fazer companhia de novo?"
    g "Talvez. Mas, dessa vez, vim falar de outra coisa."
    j "O que foi?"
    g "Você me mandou uma mensagem falando sobre um estudante. Sabe o que aconteceu?"
    narrador "Juliano ficou mais sério e olhou ao redor antes de me responder."
    j "Ouvi umas coisas por aí. Parece que o Ramón se envolveu com gente errada."
    g "O Ramón? Você tá falando do Ramón da Psicologia?"
    j "Esse mesmo. Dizem que ele tava andando com pessoas envolvidas com drogas. Não sei se é verdade, mas foi o que chegou até mim."
    g "Você tá dizendo que ele usa drogas?"
    j "Tô dizendo que ouvi rumores. É diferente. Não vou afirmar algo que não posso provar."
    g "Hoje encontrei o Ramón machucado... Ele parecia desorientado e ficou muito agressivo comigo."
    j "Sério? Então talvez tenha acontecido alguma coisa mesmo."
    g "Você sabe quem poderia estar envolvido?"
    j "Não faço ideia. Mas, se alguém tá tentando esconder alguma coisa, talvez seja melhor prestar atenção em quem anda fazendo perguntas demais."
    g "Como assim?"
    j "Só tô dizendo que nem todo mundo gosta de ser investigado, Guilherme. Principalmente quando tem algo a perder."
    narrador "Eu senti um arrepio na espinha quando ele disse isso. Acho que ele percebeu e tentou voltar ao tom descontraído. Talvez ele só esteja evitando aprofundar o assunto."
    narrador "O Juliano parece saber mais do que tá dizendo. Ainda assim, os rumores sobre Ramón podem ser apenas fofocas. Preciso separar o que é fato do que é especulação."
    g "Valeu por me contar. Vou tentar descobrir o que realmente aconteceu."
    j "Só toma cuidado, tá? Não quero que você acabe se metendo em problemas."
    hide juliano char_rightmost with dissolve
    narrador "Eu me despedi dele, mas continuo pensando nas palavras de Juliano."

    jump main_route.scene_9

label juliano_route.scene_12_1:
    ## CENA 12.1: Rota Juliano
    ## CENÁRIO - Corredor de Aulas, Rádio Universitária
    ## PERSONAGENS - Guilherme, Juliano
    scene bg school_corridor with fade
    show guilherme at char_leftmost
    show juliano at char_rightmost
    with dissolve

    g "{=pensamento}\"Bom, acho que descobrindo quem está ameaçando o Juliano vou ter mais pistas sobre quem está fazendo esse caos todo.\""
    g "Juliano, podemos ir pra rádio? Tem alguém lá agora? A gente pode usar algum computador lá?"
    j "Podemos sim. O pessoal tá almoçando agora."
    show juliano at smooth_invert_x
    
    scene bg radio with fade
    show guilherme at char_leftmost
    show juliano at char_rightmost, invert_x
    with dissolve
    narrador "Acompanhei o Juliano até o prédio de Comunicação, a Rádio era pequena mas tinha muitos equipamentos que pareciam bem caros..."
    narrador "Juliano caminha encolhido e apreensivo, olhando constantemente para os lados."
    show juliano at char_rightmost, smooth_uninvert_x
    j "Ainda bem que você tá comigo, eu tô apavorado...{w=0.3} Olha aqui no meu celular, a pessoa diz claramente que eu vou ser o próximo!"
    narrador "Eu mandei mensagem pra um amigo da aula de Programação. Ele pediu alguns arquivos e acessos e mandamos pra ele."
    narrador "A cada momento o Juliano ficava ainda mais nervoso. Eu tentava acalmar ele, mas não parecia funcionar."
    g "Calma, Juliano! Eu confio nesse amigo, ele sabe o que tá fazendo e vai te ajudar."
    j "Quem tá me ameaçando vai descobrir que sabemos quem ele é, é melhor deixar pra lá..."
    g "Calma... Não tem co..."
    narrador "Antes de terminar a frase recebi uma mensagem do meu amigo. Então a li em voz alta..."
    g "\"O tipo de encriptação, o endereço IP e o nome do dispositivo que enviou essas ameaças são exatamente iguais aos arquivos do formulário do veterano que desapareceu.\", meu amigo disse."
    j "Ah, sério? Que coincidência estranha, não é mesmo?"
    g "Você disse que não conhecia o veterano e que não sabia nada sobre ele, Juliano... Como é que o aparelho pessoal dele foi usado para mandar ameaças para o seu perfil?"
    j "Ah... bom... e-eu... quer dizer! É óbvio, né?! Ele devia estar usando o Wi-Fi aqui da Rádio! Foi ele quem me ameaçou antes de sumir!"
    narrador "A confusão tomou conta de mim. Meu amigo estava me enchendo de mensagens, falando pra eu sair da rádio o mais rápido possível. Eu não consigo entender..."
    narrador "Mais uma mensagem chega:"
    narrador "\"Esse registro só aparece quando o arquivo é criado direto da sua máquina de edição aqui da sala. A contradição é clara... Não tem ameaça nenhuma.\""
    g "Juliano... Era você se fazendo de vítima esse tempo todo!"

    jump main_route.scene_13

label juliano_route.scene_15_1:
    ## CENA 15.1: Rota Juliano
    ## CENÁRIO - Rádio Universitária
    ## PERSONAGENS - Guilherme, Juliano, Ramón e Diego

    g "{=pensamento}\"Eu não posso colocar nenhum dos dois em perigo...\""
    g "Tudo bem, Juliano... Eu fico com você. Mas deixa eles em paz!"
    r "Você ficou maluco, Guilherme?!{w=0.2} Depois de tudo o que esse monstro confessou e fez com a gente?!"
    d "Você não pode estar falando sério, Guilherme!{w=.2} Ele é um perigo pra você!"
    j "Já ouviram ele! Rua! O Guilherme é MEU!"
    g "Vão embora, por favor! É pro bem de vocês..."
    narrador "Os dois saíram sozinhos, sem entender nada e discutindo furiosos, enquanto fiquei sozinho com meu perseguidor..."

    hide ramon
    hide diego
    with dissolve

    show guilherme:
        parallel:
            xalign 0.25
            xanchor 0.5
            yalign 1.0
            zoom 0.6
        parallel:
            ease 0.55 zoom 0.65
    show juliano:
        parallel:
            xalign 0.75
            xanchor 0.5
            yalign 1.0
            zoom 0.6
        parallel:
            ease 0.5 zoom 0.65
    with move

    pause 1.0