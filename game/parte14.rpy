label parte_14:
    "Depois de encontrar Juliano desesperado, Guilherme fica pensativo após ele relatar que tem recebido ameaças nas redes sociais."

    g "A situação no campus está ficando fora de controle
    Ramon foi atacado, Juliano está sendo ameaçado e há um veterano desaparecido."  
    g "Preciso de tomar uma atitude hoje mesmo. Para onde devo ir?"
    menu:
        "Com qual personagem você deseja passar o tempo?"
        "Ramon":
            jump investigarCafeteria
        "Juliano":
            jump investigarRadio
        "Diego":
            jump investigarGinasio

label investigarCafeteria:

    "Guilherme caminha apressado pela entrada principal da faculdade e avista Ramon encostado perto do pátio,
    ajeitando a mochila e parecendo distante."

    "Guilherme se aproxima apressado para falar com ele."

    g "{=grito}Ramon!"
    g "Ainda bem que te encontrei aqui na frente. Eu estava te procurando"
    r "..."
    g "Aconteceu alguma coisa? Você tá com uma cara estranha…"
    r "Preciso da sua ajuda. A cafeteria é o lugar onde você foi envenenado." 
    r "Se a gente entrar lá escondido, podemos checar as câmeras de segurança."
    g "Entrar escondido?"
    r "Guilherme, se a gente for pego, a minha reputação na Psicologia vai pro lixo..."
    r "Mas não posso deixar quem fez isso comigo sair impune. Eu fico de vigia. Seja rápido."

    "Na cafeteria vazia, Guilherme analisa as gravações no computador do balcão.
    Ele vê uma figura de capuz colocando uma substância na bebida do Ramon. Nos últimos frames do vídeo, o capuz caiu ligeiramente"

    "Guilherme, impactado com a descoberta, arregala os olhos e fica paralisado"

    g {=sussuro} "Não pode ser... Aquele rosto por alguns segundos... É o Juliano!"

    "Ouvindo o sussurro assustado de Guilherme, Ramon deixa o posto de vigia na porta e se aproxima rapidamente do balcão,
    olhando por cima do ombro de Guilherme para a tela do computador."
    r {=sussuro} "O Juliano?! O garoto da Rádio que vive sendo legal com todo mundo? Por que ele faria uma coisa dessas comigo?!"

    g {=sussuro} "Ele estava manipulando todo mundo desde o começo, Ramon! A gente precisa achar ele agora mesmo antes que ele tente algo pior."
    r {=sussuro} "Vai na frente e procura por ele no pátio ou na Rádio. Eu vou fechar tudo aqui pra ninguém perceber que invadimos a cafeteria e te encontro em seguida. Só... toma cuidado, Guilherme"

    "Guilherme concorda com a cabeça e sai apressado. Após procurar pelos corredores e pelo pátio principal, ele finalmente avista Juliano abrindo tranquilamente a porta da sala da rádio e vai direto até ele"

    g {=grito} "Juliano!"
    g {=grito} "Eu vi as imagens da câmera da cafeteria. Era você quem estava colocando aquilo na bebida do Ramon!"

    jump desfechoSalaRadio

label investigarRadio:

    "Guilherme decide acompanhar Juliano até o prédio da Rádio Universitária para analisar melhor as mensagens
    que ele alega estar recebendo. Juliano caminha encolhido e apreensivo, olhando constantemente para os lados"

    g "Juliano, você me disse que está sendo ameaçado e que é a próxima vítima.
    Vamos até a Sala da Rádio, onde você trabalha, para analisar essas conversas direto no computador."
    j "Ainda bem que você tá comigo, eu tô apavorado... Olha aqui no meu celular, a pessoa diz claramente que eu vou ser o próximo!"

    "Os dois entram na Sala da Rádio. Juliano senta na mesa e abre os arquivos de mídia no monitor para mostrar a Guilherme.
    Guilherme se debruça sobre o computador e começa a analisar os dados técnicos do envio"

    g "Espera um pouco... O tipo de encriptação, o endereço IP e o nome do dispositivo que enviou essas ameaças... 
    São exatamente iguais aos arquivos do formulário do veterano que desapareceu"
    j "Ah, sério? Que coincidência estranha, não é mesmo?"
    g "Você disse que não conhecia o veterano e que não sabia nada sobre ele, Juliano... 
    Como é que o aparelho pessoal dele foi usado para mandar ameaças para o seu perfil?"
    j "Ah... bom... e-eu... quer dizer! É óbvio, né?! Ele devia estar usando o Wi-Fi aqui da Rádio! Foi ele quem me ameaçou antes de sumir!"
    g "Isso não faz o menor sentido, Juliano. Esse registro só aparece quando o arquivo é criado direto da sua máquina de edição aqui da sala. A contradição é clara..."
    g {=grito} "Não tem ameaça nenhuma. Era você se fazendo de vítima esse tempo todo!"

    jump desfechoSalaRadio

label investigarGinasio:
    "Guilherme lembra que Diego mencionou ter visto algo estranho perto da quadra e resolve ir até lá com ele.
    Ele encontra Diego saindo do vestiário com a bolsa de treino nos ombros"

    g "Diego!" 
    g "Você disse que viu algo suspeito perto da quadra mais cedo. Me acompanha até lá pra gente investigar?"
    d "Com certeza. Não vou deixar você andando sozinho pelo campus com esse maluco à solta. Fica atrás de mim."

    "Os dois entram no ginásio silencioso e vasculham a área dos vestiários. Perto de um dos armários, Guilherme nota algo brilhando no chão ao lado de uma mancha escura."

    g "Diego, olha isso... Uma mancha de sangue recente e um botão de roupa colorido caído."
    d "Sangue?! O que aconteceu aqui?"
    g "Espera... Eu lembro perfeitamente desse botão. É do casaco espalhafatoso do Juliano! Ele usava essa roupa no primeiro dia que nos conhecemos."
    d {=grito}"O Juliano?! Aquele cara da Rádio que fica se fazendo de bonzinho pra todo mundo? Ele tá metido nisso?!"
    g "A gente precisa achar o Juliano agora mesmo! Ele deve estar na Sala da Rádio!"

    jump desfechoSalaRadio