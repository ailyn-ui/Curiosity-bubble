"""Fill a copy of the template with sample data, to check the maths after recalculating."""
import sys, datetime as d
from openpyxl import load_workbook

wb = load_workbook(sys.argv[1])
s, f, o, m, x = (wb[n] for n in ["Start here", "Fixed costs", "Owed to you", "Money minute", "Client extras"])
s["D7"] = "Sarah"; s["D9"] = 3000; s["D19"] = 0.3; s["D21"] = 500; s["D24"] = "Done"
today = d.date.today()
nov = (today.replace(day=1) + d.timedelta(days=40)).replace(day=15)
fixed = [("Rent", 1800, "Monthly", 1, None), ("Software", 100, "Monthly", 30, None),
         ("Phone", 200, "", 31, None),                                        # blank = monthly
         ("Accountant", 900, "Yearly", None, today + d.timedelta(days=1)),    # yearly, due tomorrow
         ("Website hosting", 300, "Yearly", None, today.replace(day=5)),      # yearly, already paid this month
         ("Insurance", 1200, "Yearly", None, d.date(2027, 7, 26)),            # yearly, July
         ("Domain", 40, "Yearly", None, nov),                                 # yearly, next month
         ("Membership", 150, "Yearly", None, None)]                           # yearly, date missing
for i, (n, a, how, day, when) in enumerate(fixed):
    r = 8 + i
    f[f"B{r}"], f[f"C{r}"] = n, a
    if how: f[f"D{r}"] = how
    if day: f[f"E{r}"] = day
    if when: f[f"F{r}"] = when
rows = [("A", 1200, d.date(2026, 10, 15), d.date(2026, 10, 20)),
        ("B", 800, d.date(2026, 10, 20), None), ("C", 500, d.date(2026, 11, 15), None)]
for i, (n, a, due, paid) in enumerate(rows):
    o[f"B{8+i}"], o[f"C{8+i}"], o[f"D{8+i}"] = n, a, due
    if paid: o[f"E{8+i}"] = paid
m["B8"], m["C8"], m["D8"] = d.date(2026, 10, 27), 4250, 300
for i, (dt, what, cl, typ, amt) in enumerate([
        (d.date(2026, 10, 3), "Coffee", "A", "Meetings & hospitality", 18),
        (d.date(2026, 10, 9), "Parking", "A", "Travel & parking", 12),
        (d.date(2026, 10, 12), "Font licence", "B", "Materials & assets for clients", 60),
        (d.date(2026, 9, 28), "Lunch", "B", "Meetings & hospitality", 45)]):   # last month: excluded
    r = 8 + i
    x[f"B{r}"], x[f"C{r}"], x[f"D{r}"], x[f"E{r}"], x[f"F{r}"] = dt, what, cl, typ, amt
wb.save(sys.argv[2])
