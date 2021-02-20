def QR(qrcode,lista_BC,os):
    cont = 0
    lista_QR = []
    for bc in lista_BC:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=0,
        )
        qr.add_data(bc[:(65-11)])
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        nomeQR = str(cont)+"-"+bc[(65-10):] + ".png"
        img.save(os.path.expanduser('~')+"/Documents/QRcode Generator Boletos/qr_codes/" + nomeQR)
        lista_QR.append(nomeQR)
        cont = cont + 1
    
    return lista_QR