label main_route.scene_1:
    ## CENA 1: Boatos de sumiço de um veterano de Jogos Digitais
    scene bg classroom with fade

    "Amigo 1" "Você se lembra do Jhonatas?"
    "Amigo 2" "Lembro, sim... A última vez que vi ele foi numa calourada. Depois desse evento, nunca mais..."
    "Amigo 1" "Eu ouvi dizer que a polícia está procurando feito louca, mas até agora nada."
    "Amigo 2" "Fico pensando na família dele... Devem estar arrasados."

    "..."

label main_route.scene_2:
    ## CENA 2: Carona e chegada no campus
    scene bg gui_room with fade

    "*Trimmmm!*"
    show guilherme at char_leftmost with dissolve
    g "Poxa, queria mais 5 minutos..."
    $ sec_name = "Mãe"
    sec "Gui! Está na hora e o café tá pronto!"
    g "Caralho! Já deu o horário!"
    sec "Não vou conseguir te dar carona hoje, então falei com a Ana e o Diego vai passar aqui pra te buscar."
    g "Ah, tá certo... Mas tem muitos anos que não converso com ele. Pode ser estranho..."

    scene bg house_outside with fade

    show guilherme at char_center with dissolve
    sec "Até logo! Boa sorte!"
    g "Tchau, mãe!"
    narrador "O carro não demora a chegar."

    scene bg car with fade

    show guilherme at char_leftmost
    show diego at char_rightmost
    with dissolve
    g "Bom dia, Diego! E aí, como tá?"
    d "É né... Cumprindo minhas obrigações."
    g "{=pensamento}\"Puts, podia ter ido andando.\""
    g "Ahh, qual curso que você tá fazendo mesmo?"
    narrador "Vejo guilherme suspirar."
    d "Ah, Educação Física. Já tô no 5° semestre."
    g "Ah, você tá bem adiantado, né?"
    d "Não, pô! Tô na metade ainda."
    g "{=pensamento}\"Meu deus, onde minha mãe me meteu?...\""
    narrador "Seguiu um momento de silêncio constrangedor... Então achei que seria uma boa ligar o rádio."
    narrador "Acho que o clima melhorou, Diego ficou animado e começou a falar sobre como aquela era uma das suas músicas favoritas."
    narrador "Percebi que a viagem não seria tão ruim assim."
    narrador "Quando chegamos na faculdade eu já sabia dois dos porquês dele gostar de \"Florence and the Machine\"."
    d "Ah, boa aula! Às 16h a gente se encontra aqui pra voltar."

label main_route.scene_3:
    ## CENA 3: Final da Aula de Roteiro, indicação de bibliografia
    scene bg classroom with fade

    show guilherme at char_leftmost with dissolve
    
    $ sec_name = "Professor Caio"
    sec "Certinho, minha gente? Terminamos por hoje."
    sec "Ah, Guilherme, você tinha pedido a bibliografia sobre arquétipos e tá aqui!"
    sec "Você pode usar o livro \"O Homem e seus Símbolos\" de Carl Jung, ou \"A Jornada do Herói\" de Joseph Campbell."
    sec "O de Jung você encontra na biblioteca, na seção de Psicologia."
    g "Ah! Professor! Muito obrigado! Vou lá agora mesmo."

label main_route.scene_4:
    ## Scripts
    # Guilherme avança para a direita
    transform esbarra_guilherme_1:
        xoffset 0
        ease 0.8 xoffset 180
    transform esbarra_guilherme_2:
        ease 0.8 xoffset 360

    # Ramón vem da direita e avança até o Guilherme
    transform entrada_ramon:
        xoffset 900
        ease 0.7 xoffset -220

    # Recuo do Guilherme, partindo da posição do impacto
    transform recuo_guilherme:
        parallel:
            ease 0.08 yoffset -30
            ease 0.12 yoffset 0
        parallel:
            xoffset 360
            #ease 0.08 xoffset 145
            ease 0.12 xoffset 60

    # Recuo do Ramón, partindo da posição do impacto
    transform recuo_ramon:
        parallel:
            ease 0.08 yoffset -30
            ease 0.12 yoffset 0
        parallel:
            xoffset -220
            #ease 0.08 xoffset -220
            ease 0.12 xoffset -80

    ## CENA 4: Biblioteca, Livro
    scene bg library with fade

    show guilherme at char_leftmost, esbarra_guilherme_1 with dissolve
    g "{=pensamento}\"Considerar que o livro que preciso está na sessão de psicologia me tirou uma risadinha.\""
    show guilherme at char_leftmost, esbarra_guilherme_2
    g "{=pensamento}\"Veja bem, quando que pensam que, para criar algo como o Mario Kart eu precisaria ter a noção mínima de como isso impactaria na mente de alguém? É realmente um…\""

    show ramon at char_rightmost, entrada_ramon
    $ renpy.pause(0.6, hard=True)
    
    show guilherme at char_leftmost, recuo_guilherme
    show ramon at char_rightmost, recuo_ramon
    with hpunch

    narrador "{=grito}*BAM!*"

    g "Ahn?"
    r "Merda!"
    g "Desculpa..."
    narrador "Foi a única coisa que consegui pronunciar enquanto olhava o rapaz, não me lembro dele, mas agora claramente não me esqueceria..."
    narrador "Embora seu claro descontentamento tenha me feito desviar os olhos, e no chão, por alguma ironia do destino, estava o livro que eu precisava..."
    narrador "Me abaixei para pegar."
    r "Obrigado...?"
    g "Eu estava procurando exatamente esse livro!"
    r "E eu com isso? Esse é o único exemplar e eu peguei."
    g "Só tem esse?!"
    r "Foi o que eu disse. Você não é de Psicologia, é?"
    g "Não, eu sou de Jogos Digitais!"
    r "Jogos Digitais? Eu nem sabia que isso era um curso. Pra que matéria você vai usar o livro de Jung?"
    g "Pra matéria de Roteiro e Storyboard. Estamos estudando arquétipos pra criação de personagens."
    r "Ahhh... Faz sentido. Parece interessante."
    g "Você é de Psicologia? Vi a guitarra e imaginei que seria do curso de música..."
    r "Sim, eu gosto de unir as duas coisas. Olha, eu preciso do livro agora pra uma avaliação. Mas posso te entregar no final da tarde. Me passa teu contato."

label main_route.scene_5:
    ## CENA 5: Passeio pelo Campus

    scene bg uneb_dcv with fade

    show guilherme at char_leftmost with dissolve

    g "{=pensamento}\"A volta às aulas traz sempre uma energia de \'tudo é possível\', as pessoas conversando, namorados se abraçando e o grupo das líderes de torcida parecendo que nunca havia tirado férias. É divertido, até mesmo espirituoso...\""
    narrador "Sentar me parecia uma boa ideia, até escutar um chamado. Poderia ser comigo ou não."
    narrador "O rapaz em questão vinha em minha direção, mas foi parado por umas duas pessoas no meio do caminho até finalmente chegar perto."

    show juliano at char_rightmost with dissolve
    narrador "O sorriso em meu rosto era o claro convite de que ele poderia falar."

    j "Calouro? Acho que nunca te vi no campus."
    g "Sim, sou calouro no curso de Jogos Digitais!"
    j "Que tudo! Como funciona? Vocês fazem jogos tipo... O daquele menino com a espada?"
    g "Sim! Exatamente isso aí e um pouco mais. E você faz o quê?"
    j "Eu sou de Publicidade e Propaganda, sou host do Jornal Universiário, já ouviu?"
    g "Ahh... Ainda não."
    j "Você precisa escutar! Gostei de você. Posso te levar pra conhecer nossa sede mais tarde, vai que você tem algo a acrescentar sobre jogos na nossa pauta..."
    g "Ah, eu ia adorar! A propósito, meu nome é Guilherme."
    j "Prazer, Guilherme! Eu me chamo Juliano."
    narrador "Seguir caminhando com o Juliano me deu ideia de como me localizar melhor no lugar, ele apontava os prédios e dizia onde eu poderia encontrar as coisas, de sala de impressão a café gratuito..."
    narrador "Era como se ali fosse apenas um palco para sua vida e tinha algo de interessante em sua familiaridade com o local e as coisas que sabia."
    narrador "Estava curioso quanto aos laboratórios de informática quando minha atenção foi dissipada pela informação de que havia um aluno desaparecido."
    j "Ah, eu preciso colher depoimentos sobre isso pra uma matéria pro jornal. Quer me acompanhar?"

label main_route.scene_6:
    ## CENA 6: Decisão 1
    menu:
        "O que devo fazer?"
        "Ir coletar depoimentos sobre o garoto desaparecido com Juliano":
            jump juliano_route.scene_1
        "Ir encontrar Ramón para pegar o livro":
            jump ramon_route.scene_1
        "Voltar de carona com Diego":
            jump diego_route.scene_6_3

label main_route.scene_7:
    ## CENA 7: 
    scene bg uneb_dcv with fade

    show guilherme at char_leftmost with dissolve
    g "{=pensamento}\"Minhas aulas de hoje acabaram, pra voltar de carona preciso esperar o treino do Diego acabar pra... {w=1}Ué... {w=0.3}Tem um rapaz sentado meio desorientado ali... Com alguns hematomas...\""
    show ramon at char_rightmost with dissolve
    g "Ramón?? Ei, cara! O que aconteceu com você?"
    narrador "Ele levantou a cabeça lentamente e parece tentar me reconhecer. Ele parece muito confuso."
    r "O quê? Ah... É você."
    g "Você tá machucado! Alguém fez isso com você?"
    r "Não é da sua conta."
    g "Calma, só tô tentando ajudar. Você parece estar passando mal."
    r "Eu já disse que tá tudo bem! Para de insistir!"
    narrador "Ele levantou com dificuldade."
    g "{=pensamento}\"Isso não faz sentido... Ramón pode ser reservado, mas nunca imaginei que ele reagiria assim. Acho que ele não gosta de ser visto nessa situação. Será que aconteceu algo grave?"
    narrador "{=sussurro}*Vrrrrrr*"
    g "{=pensamento}\"Uma mensagem do Juliano.\""
    show screen mensagem_celular("Juliano: Guilherme, você soube do que aconteceu com um estudante? Parece que a situação foi bem séria.")
    $ renpy.pause(3.0, hard=True)
    hide screen mensagem_celular
    g "{=pensamento}\"Primeiro o desaparecimento do veterano, agora Ramón aparece machucado. E Juliano parece saber de alguma coisa. Preciso descobrir o que tá acontecendo..."

label main_route.scene_8:
    ## CENA 8:
    scene black with fade

    g "{=pensamento}\"Tenho algumas opções. Posso tentar conversar com Ramón de novo, procurar Juliano pra entender o que ele sabe ou ir ao treino com Diego e pedir a ajuda dele."

    menu:
        "Encontrar Juliano e investigar as informações que ele recebeu":
            jump juliano_route.scene_2
        "Continuar com Ramón":
            # TODO: consertart aq pq ainda tá sem a ramon_route.scene_2
            # jump ramon_route.scene_2
            jump main_route.scene_9
        "Ir ao treino de Diego e conversar com ele sobre Ramón":
            jump diego_route.scene_8_3

label main_route.scene_9:
    ## CENA 9:
    scene bg uneb_entrance with fade
    show guilherme at char_leftmost with dissolve

    g "{=pensamento}\"Nossa, ontem foi um dia complicado. Mas eu não posso ignorar o que aconteceu. Preciso investigar melhor o caso...\""
    g "{=pensamento}\"Primeiro, preciso confirmar os fatos. Descobrir onde Ramón esteve, com quem falou e se alguém viu alguma coisa...\""
    g "{=pensamento}\"Também preciso entender se isso tem alguma relação com o desaparecimento do veterano...\""
    g "{=pensamento}\"Se alguém tá por trás disso, uma hora vai cometer algum erro. E eu vou descobrir.\""

label main_route.scene_10:
    ## CENA 10:
    scene bg classroom with fade

    show guilherme at char_leftmost

    $ sec_name = "Professor Marcelo"
    sec "Meu povo! Pra próxima aula vocês vão desenhar a concept art de um toco no blender em 2D."
    sec "Não esqueçam de colocar no drive porque a gente vai usar ele na próxima aula pra modelar o nosso toco, beleza? Liberados!"
    g "Value, Professor Marcelo!"

label main_route.scene_11:
    ## CENA 11:
    scene bg school_corridor with fade

    show guilherme at char_leftmost with dissolve

    g "{=pensamento}\"Eu sou péssimo nas aulas de Arte, mas elas são divertidas…\""

    show juliano at char_rightmost with dissolve
    g "{=pensamento}\"Ah, o Juliano está bem ali. O que ele pode estar fazendo aqui? Hmmm, ele parece nervoso, está olhando para todos os lados.\""
    g "Juliano? Ei! Tá tudo bem?"
    narrador "Ele bloqueou a tela do celular rápido quando me viu chegando."
    j "Ah, Guilherme. Oi."
    g "Você parece preocupado. Aconteceu alguma coisa?"
    j "Não é nada. Só umas mensagens idiotas."
    g "Mensagens? De quem?"
    narrador "Ele hesita um pouco. E depois de alguns segundos me mostra a tela do celular."
    g "Espera... tão ameaçando você?"
    j "É. Começou ontem à noite. Uma conta que eu nunca vi começou a mandar mensagens dizendo pra eu parar de falar sobre certas coisas."
    g "Certas coisas? Você sabe do que tão falando?"
    j "Acho que tem a ver com o que tenho investigado pro Jornal Universitário. Eu não falei nada demais, só repeti o que ouvi. Mas parece que alguém não gostou."
    narrador "Eu li algumas das mensagens. O perfil não possui foto, publicações ou informações que permitam identificar o responsável."
    g "Você reconhece esse perfil?"
    j "Não. A conta é praticamente vazia. E, quando tentei responder, a pessoa apagou algumas mensagens e parou de falar comigo por um tempo."
    g "Você guardou as mensagens anteriores?"
    j "Algumas… Tirei print da tela antes que desaparecessem."
    g "{=pensamento}\"Isso não parece uma simples brincadeira. Alguém quer impedir Juliano de falar. Mas o que exatamente ele sabe? E será que essa pessoa também tem alguma ligação com o que aconteceu com Ramon?\""
    g "Juliano, precisamos tomar cuidado. Não apaga nada e não tenta confrontar essa pessoa sozinho."
    j "Eu sei. Mas, sinceramente, tô começando a ficar com medo."
    g "Vamos descobrir quem tá por trás disso. Só precisamos fazer as coisas direito."
    g "{=pensamento}\"O desaparecimento do veterano, os ferimentos de Ramon e agora as ameaças contra Juliano...\""
    g "{=pensamento}\"Talvez tudo isso esteja conectado. E, se estiver, alguém tá fazendo de tudo pra que a verdade não venha à tona.\""