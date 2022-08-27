import os
import webbrowser

from fpdf import FPDF


class Bill:
    """
    bill object
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    flatmate object
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = (self.days_in_house /
                  (self.days_in_house + flatmate.days_in_house))
        to_pay = weight * bill.amount
        return to_pay


class PdfReport:
    """
    generates pdf report
    """

    def __init__(self, filename):
        self.filename = filename

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
        pdf.cell(w=0, h=50, txt="Flatmates Bill", border=BORDER, align='C',  # title
                 ln=1)

        pdf.set_font(family='Arial', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=BORDER)  # period
        pdf.cell(w=150, h=40, txt="March 2021", border=BORDER,
                 ln=1)

        pdf.set_font(family='Arial', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=BORDER)  # 1st flatmate
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=BORDER,
                 ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=BORDER)  # 2nd flatmate
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=BORDER,
                 ln=1)

        pdf.cell(w=100, h=25, txt="Total", border=BORDER)  # 2nd flatmate
        pdf.cell(w=150, h=25, txt=str(round(the_bill.amount, 2)), border=BORDER,
                 ln=1)

        pdf.output(self.filename)
        webbrowser.open(f'file://{os.path.realpath(self.filename)}')            # mac-linux aware


bill_amount = float(input("Hey user, enter the bill amount: "))
bill_period = input("Hey user, enter the bill period: ")

flatmate1_name = input("Hey user, enter the first flatmate name: ")
flatmate1_days = int(input("Hey user, enter the first flatmate days in house: "))

flatmate2_name = input("Hey user, enter the second  flatmate name: ")
flatmate2_days = int(input("Hey user, enter the second flatmate days in house: "))

the_bill = Bill(bill_amount, bill_period)
flatamate1 = Flatmate(flatmate1_name, flatmate1_days)
flatamate2 = Flatmate(flatmate2_name, flatmate2_days)

print(f"{flatamate1.name} pays: {flatamate1.pays(the_bill, flatamate2)}")
print(f"{flatamate2.name} pays: {flatamate2.pays(the_bill, flatamate1)}")

pdf_report = PdfReport("Report.pdf")
pdf_report.generate(flatmate1=flatamate1, flatmate2=flatamate2, bill=the_bill)
