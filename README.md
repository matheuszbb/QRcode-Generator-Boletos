# QRcode-Generator-
Olá, meu nome é Matheus estava no meu quarto de boa estudando quando lembrei que já era dia 17 e no dia 20 deveria pagar o boleto da internet, então peguei meu celular e abri o app do banco, mas na hora de pagar eu notei que a impressão do boleto estava horrível e por isso era impossível usar a câmera do celular para ler o código de barras então pensei porque as empresas nunca põe um QRcode em seus boletos que ao ser lido fornece o código de barras do boleto. Diante disso pensei, pois eu mesmo vou colocar.


Bem tive que logar no sistema do provedor e baixar um pdf com todos os boletos e respondendo a sua possível pergunta,” ahh, mas que burro da zero para ele, era so baixar esse pdf e copiar o codigo de barras e colar no app do banco, porque esse cara não fez isso?”, bem a resposta é muito simples porque eu não acho certo que os boletos venham sem essa funcionalidade então criei eu mesmo para provar que é possível, claro que se tivesse por padrão isso seria ótimo.  


Requisitos mínimos:
1. tenha o python instalado em seu computador.
2. tenha acesso inicial a internet apenas para baixar os pacotes necessários para a manipulação do pdf. 


Como o programa funciona:
1. ponha o PDF que não tem QR code na pasta  input_pdf.
2. inicie main.py
3. agora ele vai instalar uns pacotes que não tem por padrão no python.
4. ele vai ler a pasta input_pdf obter os pdfs que estão lá.
5. ele vai obter o código de barras e a data do boleto, vai transformar em um qr code que tem um contador + data do boleto + .png e salvar em qr_codes, exemplo: 0-01/01/2021.png. 
6. agora vai obter todos os QR codes da pasta qr_codes e criar um pdf para cada um, dentro de cada pdf existe apenas esse QR code em uma dimensão específica e na exata posição onde será inserido no PDF que não tem QR code, todos esses pdfs serão salvos em output_pdf_qr.
7. por último o programa faz uma cópia do PDF que não tem QR code na pasta output_end, em seguida lê essa cópia e aos poucos lê e insere os pdfs da pasta  output_pdf_qr, como lá só tem pdfs com QR codes já bem dimensionados e bem posicionados, são praticamente imagens então é como se estivesse pondo uma marca d'água nos boletos.
