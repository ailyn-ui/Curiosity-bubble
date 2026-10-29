"""Fill a copy of the template with sample data, to check the maths after recalculating."""
import sys, datetime as d
from openpyxl import load_workbook

wb = load_workbook(sys.argv[1])
s, f, o, m, x = (wb[n] for n in ["Start here", "Fixed costs", "Owed to you", "Money minute", "Client extras"])
s["D7"] = "Sarah"; s["D9"] = 3000; s["D15"] = 0.3; s["D16"] = 500
today = d.date.today()
fixed = [("Rent", 1800, "Monthly", 1, None), ("Software", 100, "Monthly", 30, None),
         ("Phone", 200, "", 31, None),                                   # blank = monthly
         ("Accountant", 900, "Yearly", 30, today.strftime("%b")),        # yearly, due later this month
         ("Insurance", 1200, "Yearly", 26, "Jul"),                       # yearly, not this month
         ("Domain", 40, "Yearly", 15, (today.replace(day=1) + d.timedelta(days=40)).strftime("%b"))]
for i, (n, a, how, day, mon) in enumerate(fixed):
    r = 8 + i
    f[f"B{r}"], f[f"C{r}"], f[f"E{r}"] = n, a, day
    if how: f[f"D{r}"] = how
    if mon: f[f"F{r}"] = mon
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
