import qrcode
from pdfminer.high_level import extract_text
import os
from fpdf import FPDF
from pdfrw import PdfReader, PdfWriter, PageMerge
from md_qr_gen import QR
from md_rd_pdf import rd_PDF
from md_qr_pdf import qr_in_pfd
from md_watermarker import watermarker

lista_BC,lista_pdf = rd_PDF(extract_text,os)
lista_QR = QR(qrcode,lista_BC,os)
lista_QR_PDF = qr_in_pfd(os,FPDF,lista_QR)
watermarker(PdfReader, PdfWriter, PageMerge,lista_QR_PDF,os,lista_pdf)