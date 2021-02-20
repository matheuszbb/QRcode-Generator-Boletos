def qr_in_pfd(os,FPDF,lista_QR):
    lista_QR_PDF = []
    def cria_pfd(qr,nome,valor):
        pdf = FPDF()
        pdf.add_page()
        if valor == 1:
            pdf.image(qr, x=150, y=44, w=21)
        elif valor == 2:
            pdf.image(qr, x=150, y=138, w=22)
        elif valor == 3:
            pdf.image(qr, x=150, y=232, w=22)
        nome = nome.replace(".png",".pdf")
        pdf.output(os.path.expanduser('~')+"/Documents/QRcode Generator Boletos/output_pdf_qr/"+nome)
        lista_QR_PDF.append(nome)

    valor = 1
    for img in lista_QR:
        cria_pfd(os.path.expanduser('~')+"/Documents/QRcode Generator Boletos/qr_codes/"+img,img,valor)
        if valor == 1:
            valor = 2
        elif valor == 2:
            valor = 3
        else:
            valor = 1
    
    return lista_QR_PDF