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
        pdf = FPDF(
            orientation='P',
            unit='pt',
            format='A4'
        )
        pdf.add_page()

        pdf.set_font(family='Arial', size=24, style='B')
        pdf.cell(w=0, h=50, txt="Flatmates Bill", border=1, align='C', ln=1)

        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt="March 2021", border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(the_bill, flatmate2)), border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(120, "March 2021")
john = Flatmate("john", 20)
marry = Flatmate("marry", 25)
print(f"john pays: {john.pays(the_bill, marry)}")
print(f"marry pays: {marry.pays(the_bill, john)}")

pdf_report = PdfReport("Report.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
