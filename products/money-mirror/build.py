import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.comments import Comment

OUT = sys.argv[1]
PINK, INK, GREY, SOFT = "E6005C", "0B0B0B", "8A8A8A", "FCE4EE"
H = "Playfair Display"; B = "Arial"
N = 100  # rows available in each list
FIRST = 8; LAST = FIRST + N - 1
NUM = '#,##0;-#,##0;0'
DATE = "d mmm yyyy"  # reads the same in every country
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTH_ARR = "{" + ",".join(f'"{m}"' for m in MONTHS) + "}"
EXTRA_TYPES = ["Meetings & hospitality", "Travel & parking", "Materials & assets for clients",
               "Software & licences", "Other"]

def f(size=11, bold=False, color=INK, name=B, italic=False):
    return Font(name=name, size=size, bold=bold, color=color, italic=italic)
inp = PatternFill("solid", fgColor=SOFT)
white = PatternFill("solid", fgColor="FFFFFF")
bar = Border(left=Side(style="thick", color=PINK))
under = Border(bottom=Side(style="thin", color="DDDDDD"))

def base(ws, widths):
    ws.sheet_view.showGridLines = False
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows(min_row=1, max_row=LAST + 2, max_col=len(widths) + 1):
        for c in row:
            c.fill = white

def title(ws, text, sub):
    ws["B2"] = text; ws["B2"].font = f(26, True, name=H); ws["B2"].border = bar
    ws["B3"] = sub; ws["B3"].font = f(11, color=GREY, italic=True)
    ws.row_dimensions[2].height = 40

def headers(ws, cols, names):
    for col, h in zip(cols, names):
        c = ws[f"{col}6"]; c.value = h; c.font = f(10, True, GREY); c.border = under
        c.alignment = Alignment(wrap_text=True, vertical="bottom", horizontal="left", indent=1)
    ws.row_dimensions[6].height = 28

def example(ws, cols, values):
    for col, v in zip(cols, values):
        ws[f"{col}7"] = v; ws[f"{col}7"].font = f(10, color=GREY, italic=True)
        ws[f"{col}7"].alignment = Alignment(horizontal="left", indent=1)

def inputs(ws, cols):
    for r in range(FIRST, LAST + 1):
        for col in cols:
            ws[f"{col}{r}"].fill = inp; ws[f"{col}{r}"].font = f()
            ws[f"{col}{r}"].alignment = Alignment(horizontal="left", indent=1)

def date_check(ws, ref):
    dv = DataValidation(type="date", operator="greaterThan", formula1="36526", allow_blank=True,
                        error="That doesn't look like a date. Double-click the box to pick one from the calendar.",
                        showErrorMessage=True)
    ws.add_data_validation(dv); dv.add(ref)

def pick_list(ws, ref, items):
    dv = DataValidation(type="list", formula1='"' + ",".join(items) + '"', allow_blank=True)
    ws.add_data_validation(dv); dv.add(ref)

DATE_TIP = "Dates: type them the way you normally do, or double-click a date box for a calendar."

wb = Workbook()
setup = wb.active; setup.title = "Start here"
dash = wb.create_sheet("Dashboard")
mm = wb.create_sheet("Money minute")
owed = wb.create_sheet("Owed to you")
extras = wb.create_sheet("Client extras")
fixed = wb.create_sheet("Fixed costs")
for ws, col in [(setup, PINK), (dash, INK), (mm, PINK), (owed, "BBBBBB"), (extras, "BBBBBB"), (fixed, "BBBBBB")]:
    ws.sheet_properties.tabColor = col

# ---------- Fixed costs ----------
# B what · C amount · D how often · E day · F month (yearly only) · G this month · H next time · I month no. (helper)
base(fixed, {"A": 3, "B": 28, "C": 14, "D": 14, "E": 12, "F": 16, "G": 22, "H": 16, "I": 6})
title(fixed, "Fixed costs", "What leaves no matter what, every month or once a year. Add them once; you rarely touch this again.")
headers(fixed, "BCDEFGH", ["What it is", "Amount each time", "How often", "Day it leaves (1–31)",
                           "Month (yearly costs only)", "This month", "Next time"])
example(fixed, "BCDEF", ["e.g. Insurance", "1,200", "Yearly", "26", "Jul"])
inputs(fixed, "BCDEF")
for r in range(FIRST, LAST + 1):
    fixed[f"C{r}"].number_format = NUM
    yearly = f'D{r}="Yearly"'
    fixed[f"I{r}"] = f'=IF(F{r}="","",MATCH(F{r},{MONTH_ARR},0))'
    fixed[f"I{r}"].font = f(8, color="FFFFFF")
    fixed[f"G{r}"] = (f'=IF(OR(C{r}="",E{r}=""),"",IF({yearly},IF(F{r}="","pick a month →",'
                      f'IF(I{r}=MONTH(TODAY()),IF(E{r}>DAY(TODAY()),"still to pay","paid ✓"),"not this month")),'
                      f'IF(E{r}>DAY(TODAY()),"still to pay","paid ✓")))')
    fixed[f"H{r}"] = (f'=IF(OR(C{r}="",E{r}=""),"",IF({yearly},IF(F{r}="","",'
                      f'IF(DATE(YEAR(TODAY()),I{r},E{r})>TODAY(),DATE(YEAR(TODAY()),I{r},E{r}),DATE(YEAR(TODAY())+1,I{r},E{r}))),'
                      f'IF(E{r}>DAY(TODAY()),DATE(YEAR(TODAY()),MONTH(TODAY()),E{r}),DATE(YEAR(TODAY()),MONTH(TODAY())+1,E{r}))))')
    fixed[f"H{r}"].number_format = DATE
    for col in "GH":
        fixed[f"{col}{r}"].font = f(10, color=GREY)
        fixed[f"{col}{r}"].alignment = Alignment(horizontal="left", indent=1)
pick_list(fixed, f"D{FIRST}:D{LAST}", ["Monthly", "Yearly"])
pick_list(fixed, f"F{FIRST}:F{LAST}", MONTHS)
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="31", allow_blank=True,
                    error="Pick a day from 1 to 31.", showErrorMessage=True)
fixed.add_data_validation(dv); dv.add(f"E{FIRST}:E{LAST}")
fixed[f"B{LAST+2}"] = "If 'How often' is empty, it counts as monthly."
fixed[f"B{LAST+2}"].font = f(9, color=GREY, italic=True)
fixed.freeze_panes = "B8"

# ---------- Owed to you ----------
base(owed, {"A": 3, "B": 26, "C": 16, "D": 16, "E": 16, "F": 26})
title(owed, "Owed to you", "Every invoice you've sent. When one gets paid, just type the date. That's it.")
owed["B4"] = DATE_TIP; owed["B4"].font = f(9, color=GREY, italic=True)
headers(owed, "BCDEF", ["Client", "Amount", "Due date", "Paid on", "Status"])
example(owed, "BCDE", ["e.g. Studio Luna", "1,200", "15 Nov 2026", "(leave empty until paid)"])
inputs(owed, "BCDE")
for r in range(FIRST, LAST + 1):
    owed[f"C{r}"].number_format = NUM
    owed[f"D{r}"].number_format = DATE; owed[f"E{r}"].number_format = DATE
    owed[f"F{r}"] = (f'=IF(C{r}="","",IF(E{r}<>"","paid ✓ — nice",IF(D{r}="","waiting",'
                     f'IF(D{r}<TODAY(),"overdue "&(TODAY()-D{r})&" days — chase gently","due in "&(D{r}-TODAY())&" days"))))')
    owed[f"F{r}"].font = f(10, color=GREY)
    owed[f"F{r}"].alignment = Alignment(horizontal="left", indent=1)
date_check(owed, f"D{FIRST}:E{LAST}")
owed.conditional_formatting.add(f"F{FIRST}:F{LAST}", FormulaRule(formula=[f'LEFT(F{FIRST},4)="paid"'], font=Font(color="1F9D55", bold=True)))
owed.conditional_formatting.add(f"F{FIRST}:F{LAST}", FormulaRule(formula=[f'LEFT(F{FIRST},7)="overdue"'], font=Font(color=PINK, bold=True)))
owed.freeze_panes = "B8"

# ---------- Client extras ----------
base(extras, {"A": 3, "B": 16, "C": 30, "D": 22, "E": 28, "F": 14})
title(extras, "Client extras", "Costs that are included in your fee, not billed separately: the coffee, the parking, the fonts you buy for them.")
extras["B4"] = "Add them when they happen, or catch up during your money minute. " + DATE_TIP
extras["B4"].font = f(9, color=GREY, italic=True)
headers(extras, "BCDEF", ["Date", "What it was", "Client", "Type", "Amount"])
example(extras, "BCDEF", ["e.g. 4 Nov 2026", "Coffee at kick-off meeting", "Studio Luna", "Meetings & hospitality", "18"])
inputs(extras, "BCDEF")
for r in range(FIRST, LAST + 1):
    extras[f"B{r}"].number_format = DATE; extras[f"F{r}"].number_format = NUM
date_check(extras, f"B{FIRST}:B{LAST}")
pick_list(extras, f"E{FIRST}:E{LAST}", EXTRA_TYPES)
extras[f"B{LAST+2}"] = "These are already out of your bank balance, so they're not taken off 'safe to spend' twice. They're here so you can see where money goes."
extras[f"B{LAST+2}"].font = f(9, color=GREY, italic=True)
extras.freeze_panes = "B8"

# ---------- Money minute ----------
base(mm, {"A": 3, "B": 16, "C": 20, "D": 22, "E": 34})
title(mm, "Your money minute", "Once a week. Open your bank app, type today's date and balance. Done.")
mm["B4"] = DATE_TIP; mm["B4"].font = f(9, color=GREY, italic=True)
headers(mm, "BCDE", ["Date", "Balance today", "Other money in*", "A note to yourself (optional)"])
example(mm, "BCDE", ["e.g. 3 Nov 2026", "4,250", "0", "Felt okay. Chased Studio Luna."])
inputs(mm, "BCDE")
for r in range(FIRST, LAST + 1):
    mm[f"B{r}"].number_format = DATE
    mm[f"C{r}"].number_format = NUM; mm[f"D{r}"].number_format = NUM
date_check(mm, f"B{FIRST}:B{LAST}")
mm[f"B{LAST+2}"] = "* Money that came in this week that isn't one of your invoices (a sale, a refund, a one-off job)."
mm[f"B{LAST+2}"].font = f(9, color=GREY, italic=True)
mm.freeze_panes = "B8"

# ---------- Start here ----------
base(setup, {"A": 3, "B": 6, "C": 58, "D": 18, "E": 12})
title(setup, "The Money Mirror", "A tool for clarity. About 10 minutes, once. Then one minute a week.")
setup["B4"] = "Pink boxes are yours to fill. Everything else updates itself."
setup["B4"].font = f(10, True, PINK)
setup["B5"] = "Before you start: File → Settings → Locale → your country. Then dates work the way you write them."
setup["B5"].font = f(10, True)
steps = [
    (7,  "1", "What's your first name?"),
    (9,  "2", "What's in your business account today?"),
    (11, "3", "Add your fixed costs, monthly or yearly  →  'Fixed costs' tab"),
    (13, "4", "Add anything people owe you  →  'Owed to you' tab"),
    (15, "5", "Tax: what % of income do you set aside?"),
    (16, "",  "Comfort cushion: an amount you never want to dip below"),
]
for r, n, q in steps:
    setup[f"B{r}"] = n; setup[f"B{r}"].font = f(16, True, PINK, name=H)
    setup[f"C{r}"] = q; setup[f"C{r}"].font = f(11, True)
    setup.row_dimensions[r].height = 24
for r in (7, 9, 15, 16):
    setup[f"D{r}"].fill = inp; setup[f"D{r}"].font = f(12, True)
for r, fmt in ((9, NUM), (15, "0%"), (16, NUM)):
    setup[f"D{r}"].number_format = fmt
setup["C14"] = "Nobody owes me right now? Pick Yes →"; setup["C14"].font = f(9, color=GREY, italic=True)
setup["D14"].fill = inp; setup["D14"].font = f(11, True)
pick_list(setup, "D14", ["Yes"])
setup["C10"] = "Tip: this is just your starting point. Your money minute keeps it fresh."
setup["C10"].font = f(9, color=GREY, italic=True)
setup["C12"] = "Rent on the 1st every month? Insurance on 26 July every year? Both go here."
setup["C12"].font = f(9, color=GREY, italic=True)
setup["C17"] = "If you already move tax to a separate account, put 0% above."
setup["C17"].font = f(9, color=GREY, italic=True)
setup["D15"].comment = Comment("Ask your accountant what's right for you. Many freelancers set aside 25–35%.", "Ailyn")
dvp = DataValidation(type="decimal", operator="between", formula1="0", formula2="1", allow_blank=True,
                     error="Type a percentage, like 30%.", showErrorMessage=True)
setup.add_data_validation(dvp); dvp.add("D15")
done = {
    7:  'D7<>""',
    9:  'D9<>""',
    11: f"COUNT('Fixed costs'!C{FIRST}:C{LAST})>0",
    13: f"OR(COUNT('Owed to you'!C{FIRST}:C{LAST})>0,D14=\"Yes\")",
    15: 'D15<>""',
}
for r, cond in done.items():
    setup[f"E{r}"] = f'=IF({cond},"✓ done","")'
    setup[f"E{r}"].font = f(11, True, "1F9D55")
setup["C20"] = "=COUNTIF(E7:E15,\"✓ done\")/5"
setup["C20"].number_format = '0%" set up"'; setup["C20"].font = f(14, True, PINK, name=H)
setup["C21"] = ('=IF(C20=1,"You did it. You know your numbers. Head to your Dashboard ✨",'
                '"Step "&(COUNTIF(E7:E15,"✓ done")+1)&" of 5. You\'re doing great.")')
setup["C21"].font = f(13, True, name=H)
setup["C23"] = "Then, once a week: your money minute. Two numbers, about 60 seconds."
setup["C23"].font = f(10, color=GREY)
setup["C24"] = "Paid for a client coffee, parking or materials? Pop it in 'Client extras' when you can."
setup["C24"].font = f(10, color=GREY)
setup["C26"] = ("The Money Mirror helps you see your numbers. It isn't tax, legal or financial advice. "
                "For that, talk to an accountant or financial adviser.")
setup["C26"].font = f(8, color=GREY, italic=True); setup["C26"].alignment = Alignment(wrap_text=True)
setup.merge_cells("C26:E27")
for r in (20, 21):
    setup[f"C{r}"].border = bar

for name, ref in [("YourName", "'Start here'!$D$7"), ("StartBalance", "'Start here'!$D$9"),
                  ("TaxRate", "'Start here'!$D$15"), ("Cushion", "'Start here'!$D$16")]:
    wb.defined_names[name] = DefinedName(name, attr_text=ref)

# ---------- Dashboard ----------
base(dash, {"A": 3, "B": 22, "C": 22, "D": 22, "E": 22, "F": 3})
mmB, mmC, mmD = (f"'Money minute'!{c}{FIRST}:{c}{LAST}" for c in "BCD")
oC, oD, oE = (f"'Owed to you'!{c}{FIRST}:{c}{LAST}" for c in "CDE")
fB, fC, fD, fE, fH, fI = (f"'Fixed costs'!{c}{FIRST}:{c}{LAST}" for c in "BCDEHI")
xB, xD, xE, xF = (f"'Client extras'!{c}{FIRST}:{c}{LAST}" for c in "BDEF")
som = "(EOMONTH(TODAY(),-1)+1)"; eom = "EOMONTH(TODAY(),0)"
in_month = lambda rng: f"({rng}>={som})*({rng}<={eom})"

# behind-the-scenes calculations, row 40 onwards
CALC0 = 40
calc = [
    ("Balance", f'=IF(COUNT({mmB})=0,N(StartBalance),INDEX({mmC},MATCH(MAX({mmB}),{mmB},0)))'),
    ("Money in this month", f'=SUMPRODUCT({in_month(oE)}*{oC})+SUMPRODUCT({in_month(mmB)}*{mmD})'),
    ("Monthly still to pay", f'=SUMPRODUCT(({fD}<>"Yearly")*({fE}>DAY(TODAY()))*{fC})'),
    ("Yearly still to pay this month", f'=SUMPRODUCT(({fD}="Yearly")*({fI}=MONTH(TODAY()))*({fE}>DAY(TODAY()))*{fC})'),
    ("Fixed still to pay", "=C{2}+C{3}"),
    ("Tax to set aside", "=ROUND(N(TaxRate)*C{1},0)"),
    ("Owed to you", f'=SUMPRODUCT(({oE}="")*{oC})'),
    ("Invoices waiting", f'=SUMPRODUCT(({oE}="")*({oC}<>""))'),
    ("Overdue", f'=SUMPRODUCT(({oE}="")*({oC}<>"")*({oD}<>"")*({oD}<TODAY()))'),
    ("Safe to spend", "=C{0}-C{4}-C{5}-N(Cushion)"),
    ("Days since money minute", f'=IF(COUNT({mmB})=0,-1,TODAY()-MAX({mmB}))'),
    ("Money minutes this month", f'=COUNTIFS({mmB},">="&{som},{mmB},"<="&{eom})'),
    ("Cushion", "=N(Cushion)"),
    ("Next yearly date", f'=_xlfn.MINIFS({fH},{fD},"Yearly")'),
    ("Next yearly row", f'=IF(C{{13}}=0,0,SUMPRODUCT(MAX(({fD}="Yearly")*({fH}=C{{13}})*(ROW({fH})-{FIRST - 1}))))'),
    ("Next yearly what", f'=IF(C{{14}}=0,"",INDEX({fB},C{{14}}))'),
    ("Next yearly amount", f'=IF(C{{14}}=0,0,INDEX({fC},C{{14}}))'),
    ("Yearly costs total", f'=SUMPRODUCT(({fD}="Yearly")*{fC})'),
    ("Client extras this month", f'=SUMPRODUCT({in_month(xB)}*{xF})'),
    ("Client extras count this month", f'=SUMPRODUCT({in_month(xB)}*({xF}<>""))'),
] + [(f"Extras: {t}", f'=SUMPRODUCT({in_month(xB)}*({xE}="{t}")*{xF})') for t in EXTRA_TYPES]
row_of = {i: CALC0 + 1 + i for i in range(len(calc))}
TYPE0 = 20  # index of first per-type row
type_rng = f"C{row_of[TYPE0]}:C{row_of[TYPE0 + len(EXTRA_TYPES) - 1]}"
label_rng = f"B{row_of[TYPE0]}:B{row_of[TYPE0 + len(EXTRA_TYPES) - 1]}"
calc.append(("Biggest extras type", f'=IF(C{{18}}=0,"",SUBSTITUTE(INDEX({label_rng},MATCH(MAX({type_rng}),{type_rng},0)),"Extras: ",""))'))
row_of[len(calc) - 1] = CALC0 + len(calc)
dash[f"B{CALC0}"] = "Behind the scenes (no need to touch)"; dash[f"B{CALC0}"].font = f(9, True, GREY)
for i, (label, formula) in enumerate(calc):
    r = row_of[i]
    refs = {k: row_of[k] for k in range(len(calc))}
    dash[f"B{r}"] = label; dash[f"B{r}"].font = f(9, color=GREY)
    dash[f"C{r}"] = formula.format(*[refs[k] for k in range(len(calc))])
    dash[f"C{r}"].font = f(9, color=GREY); dash[f"C{r}"].number_format = NUM
dash[f"C{row_of[13]}"].number_format = DATE
c = lambda i: f"C{row_of[i]}"
SAFE, CUSH = f"$C${row_of[9]}", f"$C${row_of[12]}"

dash["B2"] = '=IF(YourName="","Your money, at a glance.","Hi "&YourName&". Here\'s where you are.")'
dash["B2"].font = f(22, True, name=H); dash["B2"].border = bar
dash["B3"] = '="Updated "&TEXT(TODAY(),"dddd d mmmm")'; dash["B3"].font = f(10, color=GREY, italic=True)
dash["B6"] = "SAFE TO SPEND THIS MONTH"; dash["B6"].font = f(11, True, PINK)
dash.merge_cells("B7:E9")
dash["B7"] = f"={c(9)}"; dash["B7"].number_format = NUM
dash["B7"].font = f(60, True, name=H); dash["B7"].alignment = Alignment(horizontal="center", vertical="center")
for r in (7, 8, 9): dash.row_dimensions[r].height = 34
dash.merge_cells("B10:E10")
dash["B10"] = (f'=IF({c(9)}>=0,"You can breathe. This is yours to use this month.",'
               f'IF({c(9)}>=-{c(12)},"You\'re into your cushion. Go gently this month.",'
               '"Pause big spends for now. Start with what\'s owed to you →"))')
dash["B10"].font = f(12, True); dash["B10"].alignment = Alignment(horizontal="center")
dash.conditional_formatting.add("B7:E10", FormulaRule(formula=[f"{SAFE}<-{CUSH}"], font=Font(color="C62828", bold=True)))
dash.conditional_formatting.add("B7:E10", FormulaRule(formula=[f"AND({SAFE}<0,{SAFE}>=-{CUSH})"], font=Font(color="E08A00", bold=True)))
dash.conditional_formatting.add("B7:E10", FormulaRule(formula=[f"{SAFE}>=0"], font=Font(color="1F9D55", bold=True)))
tiles = [("B", "Balance today", c(0)), ("C", "Money in this month", c(1)),
         ("D", "Fixed costs still to pay", c(4)), ("E", "Set aside for tax", c(5))]
for col, label, ref in tiles:
    dash[f"{col}13"] = label; dash[f"{col}13"].font = f(9, True, GREY)
    dash[f"{col}14"] = f"={ref}"; dash[f"{col}14"].number_format = NUM
    dash[f"{col}14"].font = f(20, True, name=H); dash[f"{col}14"].border = bar
    dash[f"{col}14"].alignment = Alignment(horizontal="left", indent=1)

def section(row, label, big, text):
    dash[f"B{row}"] = label; dash[f"B{row}"].font = f(11, True, PINK)
    dash[f"B{row+1}"] = big; dash[f"B{row+1}"].number_format = NUM
    dash[f"B{row+1}"].font = f(20, True, name=H); dash[f"B{row+1}"].border = bar
    dash[f"B{row+1}"].alignment = Alignment(horizontal="left", indent=1)
    dash.merge_cells(f"C{row+1}:E{row+1}")
    dash[f"C{row+1}"] = text; dash[f"C{row+1}"].font = f(11)
    dash[f"C{row+1}"].alignment = Alignment(vertical="center", wrap_text=True)
    dash.row_dimensions[row + 1].height = 30

section(17, "OWED TO YOU", f"={c(6)}",
        f'=IF({c(7)}=0,"Nothing waiting. Lovely.",{c(7)}&IF({c(7)}=1," invoice"," invoices")&" waiting"&'
        f'IF({c(8)}>0,", "&{c(8)}&" overdue. A gentle nudge today?",". All on time."))')
section(20, "COMING UP: YEARLY COSTS", f"={c(16)}",
        f'=IF({c(13)}=0,"No yearly costs added yet. Insurance, software, memberships? Add them in Fixed costs.",'
        f'"Next: "&{c(15)}&" on "&TEXT({c(13)},"d mmm")&", "&IF({c(13)}-TODAY()=1,"tomorrow","in "&({c(13)}-TODAY())&" days")&". '
        f'Yearly costs total "&TEXT({c(17)},"#,##0")&", about "&TEXT({c(17)}/12,"#,##0")&" a month to put aside.")')
section(23, "CLIENT EXTRAS THIS MONTH", f"={c(18)}",
        f'=IF({c(19)}=0,"None logged this month. Coffee, parking, materials for clients? Add them in Client extras.",'
        f'{c(19)}&IF({c(19)}=1," cost"," costs")&" included in your fees, mostly "&LOWER({c(len(calc) - 1)})&".")')
dash["B26"] = "YOUR MONEY MINUTE"; dash["B26"].font = f(11, True, PINK)
dash.merge_cells("B27:E27")
dash["B27"] = (f'=IF({c(10)}=-1,"Your first money minute is waiting. Two numbers, about 60 seconds.",'
               f'IF({c(10)}<=7,"On track ✓  Last check-in "&IF({c(10)}=0,"today",{c(10)}&IF({c(10)}=1," day"," days")&" ago")&". "&{c(11)}&" this month.",'
               f'"It\'s been "&{c(10)}&" days. One minute, two numbers. You\'ve got this."))')
dash["B27"].font = f(12, True); dash["B27"].border = bar
D10 = f"$C${row_of[10]}"
dash.conditional_formatting.add("B27:E27", FormulaRule(formula=[f"AND({D10}>=0,{D10}<=7)"], font=Font(color="1F9D55", bold=True)))
dash["B30"] = "Safe to spend = balance today − fixed costs still to pay this month (monthly, plus any yearly ones due this month) − tax to set aside − your comfort cushion."
dash["B30"].font = f(8, color=GREY, italic=True)
dash["B31"] = "It's a guide to help you see clearly, not financial advice."
dash["B31"].font = f(8, color=GREY, italic=True)

wb.active = 0
wb.save(OUT)
print("saved", OUT)
