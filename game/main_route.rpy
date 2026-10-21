label main_route.scene_1:
    scene bg classroom with fade

    "Amigo 1" "Você se lembra do Jhonatas?"
    "Amigo 2" "Lembro, sim... A última vez que vi ele foi numa calourada. Depois desse evento, nunca mais..."
    "Amigo 1" "Eu ouvi dizer que a polícia está procurando feito louca, mas até agora nada."
    "Amigo 2" "Fico pensando na família dele... Devem estar arrasados."

    "..."

    scene bg placeholder with fade

    "Trimmmm!"
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
