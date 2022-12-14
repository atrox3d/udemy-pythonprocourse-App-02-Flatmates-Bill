import os
import webbrowser

from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    generates pdf report
    """

    def __init__(self, filename):
        self.filename = filename
        self.filepath = os.path.realpath(f"files/{self.filename}")

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(  # calc, format and convert pay to string
            round(flatmate1.pays(bill, flatmate2), 2)
        )
        flatmate2_pay = str(  # calc, format and convert pay to string
            round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(  # create FPDF instance
            orientation='P',  # portrait
            unit='pt',  # points
            format='A4'
        )
        BORDER = 0
        pdf.add_page()

        pdf.image('files/house.png', w=100, h=100)

        pdf.set_font(family='Arial', size=24, style='B')
        pdf.cell(w=0, h=50, txt="Flatmates Bill", border=BORDER, align='C',     # title
                 ln=1)

        pdf.set_font(family='Arial', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=BORDER)                     # period
        pdf.cell(w=150, h=40, txt="March 2021", border=BORDER,
                 ln=1)

        pdf.set_font(family='Arial', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=BORDER)                # 1st flatmate
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=BORDER,
                 ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=BORDER)                # 2nd flatmate
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=BORDER,
                 ln=1)

        pdf.cell(w=100, h=25, txt="Total", border=BORDER)                       # total
        pdf.cell(w=150, h=25, txt=str(round(bill.amount, 2)), border=BORDER,
                 ln=1)

        pdf.output(self.filepath)
        webbrowser.open(f"file://{self.filepath}")                                   # mac-linux aware


class FileSharer:
    from secret.filestack_apikey import API_KEY

    def __init__(self, file_path, api_key=API_KEY):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=self.file_path)
        return new_filelink.url
