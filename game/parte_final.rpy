label desfechoSalaRadio:
    "Guilherme confronta Juliano na Sala da Rádio da Faculdade. Assim que Guilherme entra e o acusa, a porta da sala
    se tranca bruscamente com um estalo alto. No escuro da sala, a luz vermelha de 'No Air' do microfone fica piscando freneticamente."
    "A postura solar, alegre e acolhedora de Juliano se desmorona por completo em segundos. "
    "Sua expressão se fica entre o desespero e uma obsessão doentia, com lágrimas quentes escorrendo pelo rosto enquanto ele dá uma risada histérica."

    j {=grito} "SIM! Fui eu! Fui eu que fiz tudo, Guilherme! O envenenamento na cafeteria, os boatos pelo campus, o sumiço daquele veterano nojento..."
    j {=grito} "EU FIZ TUDO POR VOCÊ!"
    g "Você enlouqueceu de vez, Juliano?!" 
    g "Por que diabos você faria uma crueldade dessas?!"
    j {=grito}"Porque eu te amo!"
    j "Eu estou completamente apaixonado por você desde o primeiro segundo em que você pisou nesse campus e eu te mostrei tudo!"
    j "Eu fiz de tudo pra ser o cara perfeito pra você! Mas você não parava de olhar pros outros..."
    j "Ficava dando atenção pro idiota do Diego, pro ranzinza do Ramon! "
    j {=grito}"Eu só estava protegendo o nosso amor, Guilherme! Eu limpei o caminho pra gente ficar junto!"
    g "Isso não é amor, Juliano! Isso é loucura!"
    j "Se você não ficar comigo... se você me rejeitar depois de tudo o que eu fiz..."
    j {=grito}"EU JURO QUE ACABO COM OS DOIS! Ninguém mais vai ter você se não for eu!"

    "A porta da Sala da Rádio é arrombada com um estrondo violento! Diego entra na frente, arfando e com os punhos fechados em pura fúria, seguido de perto por Ramon, que tenta manter o controle apesar do pavor"

    d "Solta ele, seu maluco! Guilherme... eu sei que passei anos me afastando de você, mas era porque eu não sabia lidar com o que sentia por você desde quando a gente era criança... Eu te amo! E eu não vou deixar NINGUÉM te machucar!"
    r "Guilherme... Eu achava que a Psicologia, os livros e a minha bolha eram tudo o que eu precisava pra viver. Mas você mudou tudo. Você me ensinou a abrir meu coração e a sentir de verdade. Não dê ouvidos a esse manipulador nojento! É com você que eu quero estar!"
    j "Olhem só pra eles, Guilherme! Que cena mais patética! Escolha! Mas lembra bem do que eu te falei: se você não me escolher... a vida desses dois nunca mais vai ser segura!"

    menu:
        "Com quem você deseja ficar?"
        "Ramon":
            jump finalRamon
        "Juliano":
            jump finalJuliano
        "Diego":
            jump finalDiego

label finalRamon:

    g "O que você fez não é amor, Juliano. É uma obsessão doentia. Ramon... é com você que eu quero estar."
    j "Não... Não! Você vai se arrepender amargamente disso, Guilherme!"
    d "Entendi... Fico feliz por você. De verdade... Vou ficar por perto para garantir que esse maluco não tente mais nada..."
    r "Acabou, Juliano. Estou ligando para a polícia agora mesmo. Você está seguro comigo, Guilherme."

jump creditos


label finalDiego:

    g "Diego! Eu escolho você!"
    d "Comigo você não tem chance, seu covarde! A carona de hoje vai ser direto pra delegacia!"
    j "Me solta! Guilherme, você devia ser MEU!"
    r "Bom... Vejo que a parte física está bem resolvida por aqui. Vou lá fora chamar a segurança do campus."
    d "Viu só? O seu vizinho aqui serve pra muito mais do que só te dar carona. Deu tudo certo."

jump creditos


label finalJuliano:

    g "Tudo bem, Juliano... Eu fico com você. Mas deixa eles em paz!"
    r "Você ficou maluco, Guilherme?! Depois de tudo o que esse monstro confessou e fez com a gente?!"
    d "Você não pode estar falando sério, Guilherme! Ele é um perigo pra você!"
    j "Já ouviram ele! Rua! O Guilherme é MEU!"
    g "Vão embora, por favor! É pro bem de vocês..."

    "Ramon e Diego saem sem entender nada, discutindo furiosos e impotentes no corredor, enquanto Guilherme fica sozinho trancado com seu perseguidor"

jump creditos