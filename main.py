from flat import Bill, Flatmate
from reports import PdfReport

# input values
bill_amount = float(input("Hey user, enter the bill amount: "))
bill_period = input("Hey user, enter the bill period E.g. August 2022: ")

name1 = input("Hey user, enter the first flatmate name: ")
days1 = int(input(f"Hey user, enter {name1} days in house: "))

name2 = input("Hey user, enter the second  flatmate name: ")
days2 = int(input(f"Hey user, enter {name2} days in house: "))

# create objects
the_bill = Bill(bill_amount, bill_period)
flatamate1 = Flatmate(name1, days1)
flatamate2 = Flatmate(name2, days2)

# output to console
print(f"{flatamate1.name} pays: {flatamate1.pays(the_bill, flatamate2)}")
print(f"{flatamate2.name} pays: {flatamate2.pays(the_bill, flatamate1)}")

# output to pdf
report_filename = str(the_bill.period).replace(" ", "-") + ".pdf"
pdf_report = PdfReport(report_filename)
pdf_report.generate(flatmate1=flatamate1, flatmate2=flatamate2, bill=the_bill)
