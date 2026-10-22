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

    show guilherme:
        xalign 0.25
        xanchor 0.5
        zoom 0.55
        yalign 1.2
    show caio:
        xalign 0.75
        xanchor 0.5
        yalign 1.0
        zoom 0.6
    with dissolve

    caio "Certinho, minha gente? Terminamos por hoje."
    caio "Ah, Guilherme, você tinha pedido a bibliografia sobre arquétipos e tá aqui!"
    caio "Você pode usar o livro \"O Homem e seus Símbolos\" de Carl Jung, ou \"A Jornada do Herói\" de Joseph Campbell."
    caio "O de Jung você encontra na biblioteca, na seção de Psicologia."

    show guilherme:
        parallel:
            ease 0.2 zoom 0.6
        parallel:
            ease 0.2 yalign 1.0

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
            jump juliano_route.scene_6_1
        "Ir encontrar Ramón para pegar o livro":
            jump ramon_route.scene_6_2
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
    narrador "{=sussurro}*Vrrrrrr* {w=0.1} *Vrrrrrr*"
    g "{=pensamento}\"Uma mensagem do Juliano...\""

    j_nvl "Guilherme, você soube do que aconteceu com um estudante?"
    j_nvl "Parece que a situação foi bem séria."
    call close_phone from _call_close_phone

    g "{=pensamento}\"Primeiro o desaparecimento do veterano, agora Ramón aparece machucado. E Juliano parece saber de alguma coisa. Preciso descobrir o que tá acontecendo..."

label main_route.scene_8:
    ## CENA 8:
    scene black with fade

    g "{=pensamento}\"Tenho algumas opções. Posso tentar conversar com Ramón de novo, procurar Juliano pra entender o que ele sabe ou ir ao treino com Diego e pedir a ajuda dele."

    menu:
        "Encontrar Juliano e investigar as informações que ele recebeu":
            jump juliano_route.scene_8_1
        "Continuar com Ramón":
            jump ramon_route.scene_8_2
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

    show guilherme at char_leftmost with dissolve

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
    g "{=pensamento}\"Isso não parece uma simples brincadeira. Alguém quer impedir Juliano de falar. Mas o que exatamente ele sabe? E será que essa pessoa também tem alguma ligação com o que aconteceu com Ramón?\""
    g "Juliano, precisamos tomar cuidado. Não apaga nada e não tenta confrontar essa pessoa sozinho."
    j "Eu sei. Mas, sinceramente, tô começando a ficar com medo."
    g "Vamos descobrir quem tá por trás disso. Só precisamos fazer as coisas direito."
    g "{=pensamento}\"O desaparecimento do veterano, os ferimentos de Ramón e agora as ameaças contra Juliano...\""
    g "{=pensamento}\"Talvez tudo isso esteja conectado. E, se estiver, alguém tá fazendo de tudo pra que a verdade não venha à tona.\""

label main_route.scene_12:
    ## CENA 12: 
    ## CENÁRIO - 
    ## PERSONAGENS - Guilherme
    scene black with fade

    menu:
        g "{=pensamento}\"A situação no campus está ficando fora de controle. Ramón foi atacado, Juliano está sendo ameaçado e há um veterano desaparecido. Preciso tomar uma atitude hoje mesmo. Por onde devo começar?\""
        "Investigar as ameaças na rede social com Juliano":
            jump juliano_route.scene_12_1
        "Investigar o bar onde Ramón foi dopado":
            jump ramon_route.scene_12_2
        "Investigar com o Diego a quadra onde o garoto desapareceu":
            jump diego_route.scene_12_3

label main_route.scene_13:
    ## CENA 13: 
    ## CENÁRIO - Rádio Universitária
    ## PERSONAGENS - Guilherme, Juliano
    g "Confessa, Juliano! Você armou tudo!"
    narrador "Eu estou muito nervoso, bati com uma mão em um botão e a porta da sala se trancou bruscamente e uma luz vermelha no microfone ficou piscando freneticamente."
    narrador "A postura solar, alegre e acolhedora de Juliano se desmorona por completo em segundos..."
    narrador "Sua expressão fica entre o desespero e uma obsessão doentia, com lágrimas quentes escorrendo pelo rosto enquanto ele dá uma risada histérica. Eu nunca tinha visto ele assim."
    j "{=grito}{cps=10}SIM!{/cps}{/=grito}{w=0.4} Fui eu! Fui eu que fiz tudo, Guilherme! O envenenamento na cafeteria, os boatos pelo campus, o sumiço daquele veterano nojento...{w=.8} {cps=10}{sc=3}{b}EU FIZ TUDO{/b}{/sc}{/cps} {cps=5}{sc=3}{b}POR{/b}{/sc}{/cps} {cps=3}{sc=3}{b}VOCÊ!{/b}{/sc}{/cps}"
    narrador "Eu dei um passo pra trás, horrorizado com a reação dele."
    g "Você enlouqueceu de vez, Juliano?! Por que diabos você faria uma crueldade dessas?!"
    j "{cps=10}{sc=5}{b}Porque eu te amo!{/b}{/sc}{/cps}{w=0.6} Eu estou completamente apaixonado por você desde o primeiro segundo em que você pisou nesse campus, na matrícula!"
    j "Eu fiz de tudo pra ser o cara perfeito pra você! Mas você não parava de olhar pros outros..."
    j "Ficava dando atenção pro idiota do Diego, pro ranzinza do Ramón! Até aquele seu veterano que postava sobre você..."
    j "Eu só estava protegendo o nosso amor, Guilherme! Eu limpei o caminho pra gente ficar junto!"
    g "Isso não é amor, Juliano! Isso é loucura!"
    j "Se você não ficar comigo...{w=0.4} Se você me rejeitar depois de tudo o que eu fiz...{w=0.4} {cps=15}{sc=5}{b}EU JURO QUE ACABO COM OS DOIS!{/b}{/sc}{/cps}{w=0.8} Ninguém mais vai ter você se não for {cps=2}eu...{/cps}"

label main_route.scene_14:
    ## CENA 14: 
    ## CENÁRIO - Rádio Universitária
    ## PERSONAGENS - Guilherme, Juliano, Ramón e Diego
    show guilherme at smooth_invert_x

    narrador "Ouvi um estrondo. A porta da Sala da Rádio foi arrombada."
    
    show guilherme:
        xanchor 0.5
        xzoom -1
        parallel:
            ease 0.8 xalign 0.55
        parallel:
            ease 0.8 zoom 0.6
    show juliano:
        zoom 0.65
        xanchor 0.5
        parallel:
            ease 0.8 xalign 1.1
        parallel:
            ease 0.8 zoom 0.6
    show ramon:
        xalign -.5
        xanchor .5
        zoom 0.6
        yalign 1.0
        xzoom -1
        parallel:
            ease 0.8 xalign -0.2
    show diego:
        xalign -.5
        xanchor .5
        zoom 0.6
        yalign 1.0
        xzoom -1
        parallel:
            ease 0.8 xalign 0.15
    


    narrador "Diego entra na frente, arfando e com os punhos fechados em pura fúria, seguido de perto por Ramón, que tenta manter o controle apesar do pavor."
    d "Sai de perto dele, seu maluco!"
    d "Guilherme... eu sei que passei anos me afastando de você, mas era porque eu não sabia lidar com o que sentia por você desde quando a gente era criança{cps=4}...{/cps}"
    d "Eu te amo! E eu não vou deixar {b}NINGUÉM{/b} te machucar!"
    g "{=pensamento}\"O quê?!\""
    narrador "Eu nem consegui reagir ao que ele disse. Estou em choque com toda a situação."
    narrador "Olhei pra Ramón e sua expressão séria e racional desmoronou por completo. Ele está trêmulo..."
    r "Guilherme... Eu achava que a Psicologia, os livros e a minha bolha eram tudo o que eu precisava pra viver. Mas você mudou tudo..."
    r "Você me ensinou a abrir meu coração e a sentir de verdade. Não dê ouvidos a esse manipulador nojento! É com você que eu quero estar!"
    show guilherme at smooth_uninvert_x
    j "Hahaha!{w=0.4} Olhe só pra eles, Guilherme!{w=0.2} Que cena mais patética!{w=0.6} Escolha!{w=0.2} Mas lembra bem do que eu te falei:{w=0.6} Se você não me escolher...{w=0.2} a vida desses dois nunca mais vai ser segura!"

label main_route.scene_15:
    ## CENA 15: 
    ## CENÁRIO - Rádio Universitária
    ## PERSONAGENS - Guilherme

    g "{=pensamento}\"Eu não estou conseguindo processar o que está acontecendo. Nada faz sentido... Mas preciso tomar uma decisão logo...\""

    menu:
        g "{=pensamento}\"Eu não tenho dúvidas! A pessoa com quem eu preciso ficar é..."
        "Ficar com o Juliano":
            jump juliano_route.scene_15_1
        "Ficar com o Ramón":
            jump ramon_route.scene_15_2
        "Ficar com o Diego":
            jump diego_route.scene_15_3