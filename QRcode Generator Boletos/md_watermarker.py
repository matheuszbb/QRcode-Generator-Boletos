def watermarker(PdfReader, PdfWriter, PageMerge,lista_QR_PDF,os,lista_pdf):
    def cria_watermarker(path, watermark, output,pagina):
        base_pdf = PdfReader(path)
        watermark_pdf = PdfReader(watermark)
        mark = watermark_pdf.pages[0]
        
        merger = PageMerge(base_pdf.pages[pagina])
        merger.add(mark).render()
        
        writer = PdfWriter()
        writer.write(output, base_pdf)

    pagina = 0
    contador = 1
    for arquivo in lista_pdf:
        origem = os.path.expanduser("~")+"/Documents/QRcode Generator Boletos/input_pdf"
        destino = os.path.expanduser("~")+"/Documents/QRcode Generator Boletos/output_end"
        os.system(f'COPY "{origem}" "{destino}" ')

        for pdf in lista_QR_PDF:  
            destino = os.path.expanduser("~")+"/Documents/QRcode Generator Boletos/output_end/"+arquivo
            pdf = os.path.expanduser("~")+"/Documents/QRcode Generator Boletos/output_pdf_qr/"+pdf
            
            cria_watermarker(destino,pdf,destino,pagina)
            
            if contador == 1:
                contador = 2
            elif contador == 2:
                contador = 3
            else:
                contador = 1
                pagina = pagina + 1 