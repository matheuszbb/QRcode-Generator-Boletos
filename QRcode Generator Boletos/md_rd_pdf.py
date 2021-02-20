def rd_PDF(extract_text,os):
    lista_pdf = []
    for pdf in os.listdir(os.path.expanduser('~')+"/Documents/QRcode Generator Boletos/input_pdf"):
        lista_pdf.append(pdf)

    for pdf in lista_pdf:
        l=""
        lista = []

        txt = extract_text(os.path.expanduser('~')+"/Documents/QRcode Generator Boletos/input_pdf/"+pdf)

        for linha in txt:
            l=l+linha
            if linha == '\n':
                lista.append(l.replace('\n',""))
                l=""

        lista_BC = []
        for n in range(0,len(lista)):
            if lista[n] == "Recibo":
                lista_BC.append(lista[n+5]+":"+lista[n+13].replace('/',"."))
                    
    return lista_BC,lista_pdf