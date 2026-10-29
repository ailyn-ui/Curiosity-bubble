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
    ws.row_dimensions[6].height = 42

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
# B what · C amount · D how often · E day (monthly) · F date (yearly) · G this month · H next time · I sort key (helper)
base(fixed, {"A": 3, "B": 28, "C": 14, "D": 14, "E": 14, "F": 18, "G": 18, "H": 16, "I": 4})
title(fixed, "Fixed costs", "What leaves no matter what, every month or once a year. Start with your 3 biggest; add the rest when they show up.")
fixed["B4"] = "Monthly: just the day it leaves (e.g. 20). Yearly: the exact date it leaves (e.g. 26 Jul 2027). " + DATE_TIP
fixed["B4"].font = f(9, color=GREY, italic=True)
headers(fixed, "BCDEFGH", ["What it is", "Amount each time", "How often", "Monthly: day it leaves (1–31)",
                           "Yearly: date it leaves", "This month", "Next time"])
example(fixed, "BCDEF", ["e.g. Insurance", "1,200", "Yearly", "", "26 Jul 2027"])
inputs(fixed, "BCDEF")
for r in range(FIRST, LAST + 1):
    fixed[f"C{r}"].number_format = NUM; fixed[f"F{r}"].number_format = DATE
    yearly = f'D{r}="Yearly"'
    this_year = f"DATE(YEAR(TODAY()),MONTH(F{r}),DAY(F{r}))"
    fixed[f"G{r}"] = (f'=IF(C{r}="","",IF({yearly},IF(F{r}="","add the date →",'
                      f'IF(MONTH(F{r})=MONTH(TODAY()),IF(DAY(F{r})>DAY(TODAY()),"still to pay","paid ✓"),"not this month")),'
                      f'IF(E{r}="","add the day →",IF(E{r}>DAY(TODAY()),"still to pay","paid ✓"))))')
    fixed[f"H{r}"] = (f'=IF(C{r}="","",IF({yearly},IF(F{r}="","",IF({this_year}>TODAY(),{this_year},'
                      f'DATE(YEAR(TODAY())+1,MONTH(F{r}),DAY(F{r})))),'
                      f'IF(E{r}="","",IF(E{r}>DAY(TODAY()),DATE(YEAR(TODAY()),MONTH(TODAY()),E{r}),'
                      f'DATE(YEAR(TODAY()),MONTH(TODAY())+1,E{r})))))')
    fixed[f"H{r}"].number_format = DATE
    # unique sort key for yearly costs, so the dashboard can list the next ones in order
    fixed[f"I{r}"] = f'=IF(AND({yearly},H{r}<>""),H{r}+ROW()/100000,"")'
    fixed[f"I{r}"].font = f(6, color="FFFFFF")
    for col in "GH":
        fixed[f"{col}{r}"].font = f(10, color=GREY)
        fixed[f"{col}{r}"].alignment = Alignment(horizontal="left", indent=1)
pick_list(fixed, f"D{FIRST}:D{LAST}", ["Monthly", "Yearly"])
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="31", allow_blank=True,
                    error="Pick a day from 1 to 31.", showErrorMessage=True)
fixed.add_data_validation(dv); dv.add(f"E{FIRST}:E{LAST}")
date_check(fixed, f"F{FIRST}:F{LAST}")
fixed.conditional_formatting.add(f"G{FIRST}:G{LAST}", FormulaRule(formula=[f'LEFT(G{FIRST},3)="add"'], font=Font(color=PINK, bold=True)))
fixed[f"B{LAST+2}"] = "If 'How often' is empty, it counts as monthly. For yearly costs, the year you type doesn't matter; it repeats every year."
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
base(setup, {"A": 3, "B": 6, "C": 62, "D": 18, "E": 12})
title(setup, "The Money Mirror", "A tool for clarity. About 10 minutes, once. Then one minute a week.")
setup["B4"] = "Pink boxes are yours to fill. Everything else updates itself."
setup["B4"].font = f(10, True, PINK)
setup["B5"] = ("Best on a computer (10 seconds): File → Settings → Locale → your country, so dates work the way you write them. "
               "On your phone? Skip it and do it next time you're at a computer.")
setup["B5"].font = f(9, color=GREY, italic=True)

def step(row, num, question, note=None, box=True, fmt=None):
    setup[f"B{row}"] = num; setup[f"B{row}"].font = f(16, True, PINK, name=H)
    setup[f"C{row}"] = question; setup[f"C{row}"].font = f(11, True)
    setup.row_dimensions[row].height = 24
    if box:
        setup[f"D{row}"].fill = inp; setup[f"D{row}"].font = f(12, True)
        setup[f"D{row}"].alignment = Alignment(horizontal="left", indent=1)
        if fmt: setup[f"D{row}"].number_format = fmt
    if note:
        setup[f"C{row+1}"] = note; setup[f"C{row+1}"].font = f(9, color=GREY, italic=True)
        setup[f"C{row+1}"].alignment = Alignment(wrap_text=True, vertical="top")
        setup.row_dimensions[row + 1].height = 26

def note(cell, text):
    setup[cell] = text; setup[cell].font = f(9, color=GREY, italic=True)
    setup[cell].alignment = Alignment(wrap_text=True, vertical="top")

step(7, "1", "What's your first name?")
step(9, "2", "What's in the account your business money goes into, today?",
     "Deep breath. Whatever the number is, it's just information. Knowing is the win.", fmt=NUM)
note("C11", "One account for everything? Use that one, and add your personal fixed costs too. You can untangle it later.")
step(13, "3", "Add your 3 biggest fixed costs, monthly or yearly  →  'Fixed costs' tab",
     "Rent, phone, software? Start with 3. Add the rest when they show up in your bank app.", box=False)
step(16, "4", "Add anything people owe you  →  'Owed to you' tab", box=False)
setup["C17"] = "Nobody owes me right now? Pick Yes →"; setup["C17"].font = f(9, color=GREY, italic=True)
setup["D17"].fill = inp; setup["D17"].font = f(11, True)
pick_list(setup, "D17", ["Yes"])
step(19, "5", "Tax: what % of your income do you set aside?",
     "Not sure? 30% is a common starting point. Ask your accountant what's right for you. "
     "Already move tax to a separate account? Put 0%.", fmt="0%")
step(21, "", "Comfort cushion: an amount you never want to dip below (optional)", fmt=NUM)
monthly_equiv = (f"SUMPRODUCT(('Fixed costs'!D{FIRST}:D{LAST}<>\"Yearly\")*'Fixed costs'!C{FIRST}:C{LAST})"
                 f"+SUMPRODUCT(('Fixed costs'!D{FIRST}:D{LAST}=\"Yearly\")*'Fixed costs'!C{FIRST}:C{LAST})/12")
setup["C22"] = (f'=IF({monthly_equiv}=0,"Not sure? One month of your fixed costs is a good cushion.",'
                f'"Not sure? One month of your fixed costs is a good cushion: about "&TEXT({monthly_equiv},"#,##0")&".")')
setup["C22"].font = f(9, color=GREY, italic=True)
step(24, "6", "Add a weekly 1-minute reminder to your calendar, then pick Done →",
     "Copy this into your calendar, repeating weekly:  Money minute 💗 Open The Money Mirror, type today's date and balance.")
pick_list(setup, "D24", ["Done"])
DONE_ROWS = {7: 'D7<>""', 9: 'D9<>""',
             13: f"COUNT('Fixed costs'!C{FIRST}:C{LAST})>0",
             16: f"OR(COUNT('Owed to you'!C{FIRST}:C{LAST})>0,D17=\"Yes\")",
             19: 'D19<>""', 24: 'D24="Done"'}
for r, cond in DONE_ROWS.items():
    setup[f"E{r}"] = f'=IF({cond},"✓ done","")'
    setup[f"E{r}"].font = f(11, True, "1F9D55")
STEPS = len(DONE_ROWS)
setup["C28"] = f'=COUNTIF(E7:E24,"✓ done")/{STEPS}'
setup["C28"].number_format = '0%" set up"'; setup["C28"].font = f(14, True, PINK, name=H)
setup["C29"] = (f'=IF(C28=1,"You did it. You know your numbers. Head to your Dashboard ✨",'
                f'"Step "&(COUNTIF(E7:E24,"✓ done")+1)&" of {STEPS}. You\'re doing great.")')
setup["C29"].font = f(13, True, name=H)
for r in (28, 29):
    setup[f"C{r}"].border = bar
setup["C31"] = "Then, once a week: your money minute. Two numbers, about 60 seconds."
setup["C31"].font = f(10, color=GREY)
setup["C32"] = "Paid for a client coffee, parking or materials? Add it in 'Client extras', or catch up during your money minute."
setup["C32"].font = f(10, color=GREY)
setup["C34"] = ("The Money Mirror helps you see your numbers. It isn't tax, legal or financial advice. "
                "For that, talk to an accountant or financial adviser.")
setup["C34"].font = f(8, color=GREY, italic=True); setup["C34"].alignment = Alignment(wrap_text=True)
setup.merge_cells("C34:E35")
dvp = DataValidation(type="decimal", operator="between", formula1="0", formula2="1", allow_blank=True,
                     error="Type a percentage, like 30%.", showErrorMessage=True)
setup.add_data_validation(dvp); dvp.add("D19")

for name, ref in [("YourName", "'Start here'!$D$7"), ("StartBalance", "'Start here'!$D$9"),
                  ("TaxRate", "'Start here'!$D$19"), ("Cushion", "'Start here'!$D$21")]:
    wb.defined_names[name] = DefinedName(name, attr_text=ref)

# ---------- Dashboard ----------
base(dash, {"A": 3, "B": 22, "C": 22, "D": 22, "E": 22, "F": 3})
mmB, mmC, mmD = (f"'Money minute'!{c}{FIRST}:{c}{LAST}" for c in "BCD")
oC, oD, oE = (f"'Owed to you'!{c}{FIRST}:{c}{LAST}" for c in "CDE")
fB, fC, fD, fE, fF, fH, fI = (f"'Fixed costs'!{c}{FIRST}:{c}{LAST}" for c in "BCDEFHI")
xB, xE, xF = (f"'Client extras'!{c}{FIRST}:{c}{LAST}" for c in "BEF")
som = "(EOMONTH(TODAY(),-1)+1)"; eom = "EOMONTH(TODAY(),0)"
in_month = lambda rng: f"({rng}>={som})*({rng}<={eom})"
UPCOMING = 3

# behind-the-scenes calculations: each one gets a key, so formulas refer to {key}
calc = [
    ("balance", "Balance", f'=IF(COUNT({mmB})=0,N(StartBalance),INDEX({mmC},MATCH(MAX({mmB}),{mmB},0)))'),
    ("money_in", "Money in this month", f'=SUMPRODUCT({in_month(oE)}*{oC})+SUMPRODUCT({in_month(mmB)}*{mmD})'),
    ("monthly_due", "Monthly still to pay", f'=SUMPRODUCT(({fD}<>"Yearly")*({fE}>DAY(TODAY()))*{fC})'),
    ("yearly_due", "Yearly still to pay this month",
     f'=SUMPRODUCT(({fD}="Yearly")*({fF}<>"")*(MONTH({fF})=MONTH(TODAY()))*(DAY({fF})>DAY(TODAY()))*{fC})'),
    ("fixed_due", "Fixed still to pay", "={monthly_due}+{yearly_due}"),
    ("tax", "Tax to set aside", "=ROUND(N(TaxRate)*{money_in},0)"),
    ("owed", "Owed to you", f'=SUMPRODUCT(({oE}="")*{oC})'),
    ("waiting", "Invoices waiting", f'=SUMPRODUCT(({oE}="")*({oC}<>""))'),
    ("overdue", "Overdue", f'=SUMPRODUCT(({oE}="")*({oC}<>"")*({oD}<>"")*({oD}<TODAY()))'),
    ("safe", "Safe to spend", "={balance}-{fixed_due}-{tax}-N(Cushion)"),
    ("days", "Days since money minute", f'=IF(COUNT({mmB})=0,-1,TODAY()-MAX({mmB}))'),
    ("minutes", "Money minutes this month", f'=COUNTIFS({mmB},">="&{som},{mmB},"<="&{eom})'),
    ("cushion", "Cushion", "=N(Cushion)"),
    ("yearly_total", "Yearly costs total", f'=SUMPRODUCT(({fD}="Yearly")*{fC})'),
    ("yearly_count", "Yearly costs counted", f'=COUNT({fI})'),
    ("extras", "Client extras this month", f'=SUMPRODUCT({in_month(xB)}*{xF})'),
    ("extras_n", "Client extras count this month", f'=SUMPRODUCT({in_month(xB)}*({xF}<>""))'),
]
for k in range(1, UPCOMING + 1):
    calc += [
        (f"y{k}_key", f"Yearly #{k} key", f"=IF({{yearly_count}}<{k},\"\",SMALL({fI},{k}))"),
        (f"y{k}_row", f"Yearly #{k} row", f"=IF({{y{k}_key}}=\"\",\"\",MATCH({{y{k}_key}},{fI},0))"),
        (f"y{k}_line", f"Yearly #{k} line",
         f'=IF({{y{k}_key}}="","",TEXT(INT({{y{k}_key}}),"d mmm yyyy")&"  ·  "&INDEX({fB},{{y{k}_row}})&"  ·  "'
         f'&TEXT(INDEX({fC},{{y{k}_row}}),"#,##0")&"  ·  "&IF(INT({{y{k}_key}})-TODAY()=1,"tomorrow","in "&(INT({{y{k}_key}})-TODAY())&" days"))'),
    ]
types = [(f"type{i}", f"Extras: {t}", f'=SUMPRODUCT({in_month(xB)}*({xE}="{t}")*{xF})') for i, t in enumerate(EXTRA_TYPES)]
calc += types
CALC0 = 40
ref = {key: f"C{CALC0 + 1 + i}" for i, (key, _, _) in enumerate(calc)}
t_rows = f"{ref['type0']}:{ref[f'type{len(EXTRA_TYPES)-1}']}"
t_labels = t_rows.replace("C", "B")
calc.append(("top_type", "Biggest extras type",
             f'=IF({{extras}}=0,"",SUBSTITUTE(INDEX({t_labels},MATCH(MAX({t_rows}),{t_rows},0)),"Extras: ",""))'))
ref["top_type"] = f"C{CALC0 + len(calc)}"
dash[f"B{CALC0}"] = "Behind the scenes (no need to touch)"; dash[f"B{CALC0}"].font = f(9, True, GREY)
for i, (key, label, formula) in enumerate(calc):
    r = CALC0 + 1 + i
    dash[f"B{r}"] = label; dash[f"B{r}"].font = f(9, color=GREY)
    dash[f"C{r}"] = formula.format(**ref); dash[f"C{r}"].font = f(9, color=GREY); dash[f"C{r}"].number_format = NUM
R = lambda key: ref[key]
A = lambda key: "$C$" + ref[key][1:]

dash["B2"] = '=IF(YourName="","Your money, at a glance.","Hi "&YourName&". Here\'s where you are.")'
dash["B2"].font = f(22, True, name=H); dash["B2"].border = bar
dash["B3"] = '="Updated "&TEXT(TODAY(),"dddd d mmmm")'; dash["B3"].font = f(10, color=GREY, italic=True)
dash["B6"] = "SAFE TO SPEND THIS MONTH"; dash["B6"].font = f(11, True, PINK)
dash.merge_cells("B7:E9")
dash["B7"] = f"={R('safe')}"; dash["B7"].number_format = NUM
dash["B7"].font = f(60, True, name=H); dash["B7"].alignment = Alignment(horizontal="center", vertical="center")
for r in (7, 8, 9): dash.row_dimensions[r].height = 34
dash.merge_cells("B10:E10")
dash["B10"] = (f'=IF({R("safe")}>=0,"You can breathe. This is yours to use this month.",'
               f'IF({R("safe")}>=-{R("cushion")},"You\'re into your cushion. Go gently this month.",'
               '"Pause big spends for now. Start with what\'s owed to you →"))')
dash["B10"].font = f(12, True); dash["B10"].alignment = Alignment(horizontal="center")
SAFE, CUSH = A("safe"), A("cushion")
dash.conditional_formatting.add("B7:E10", FormulaRule(formula=[f"{SAFE}<-{CUSH}"], font=Font(color="C62828", bold=True)))
dash.conditional_formatting.add("B7:E10", FormulaRule(formula=[f"AND({SAFE}<0,{SAFE}>=-{CUSH})"], font=Font(color="E08A00", bold=True)))
dash.conditional_formatting.add("B7:E10", FormulaRule(formula=[f"{SAFE}>=0"], font=Font(color="1F9D55", bold=True)))
tiles = [("B", "Balance today", "balance"), ("C", "Money in this month", "money_in"),
         ("D", "Fixed costs still to pay", "fixed_due"), ("E", "Set aside for tax", "tax")]
for col, label, key in tiles:
    dash[f"{col}13"] = label; dash[f"{col}13"].font = f(9, True, GREY)
    dash[f"{col}14"] = f"={R(key)}"; dash[f"{col}14"].number_format = NUM
    dash[f"{col}14"].font = f(20, True, name=H); dash[f"{col}14"].border = bar
    dash[f"{col}14"].alignment = Alignment(horizontal="left", indent=1)
dash.merge_cells("B15:E15")
dash["B15"] = (f'=IF({R("yearly_due")}>0,"Includes "&TEXT({R("yearly_due")},"#,##0")&" in yearly costs due later this month.","")')
dash["B15"].font = f(9, color=GREY, italic=True)

def section(row, label, big, text):
    dash[f"B{row}"] = label; dash[f"B{row}"].font = f(11, True, PINK)
    dash[f"B{row+1}"] = big; dash[f"B{row+1}"].number_format = NUM
    dash[f"B{row+1}"].font = f(20, True, name=H); dash[f"B{row+1}"].border = bar
    dash[f"B{row+1}"].alignment = Alignment(horizontal="left", indent=1)
    dash.merge_cells(f"C{row+1}:E{row+1}")
    dash[f"C{row+1}"] = text; dash[f"C{row+1}"].font = f(11)
    dash[f"C{row+1}"].alignment = Alignment(vertical="center", wrap_text=True)
    dash.row_dimensions[row + 1].height = 30

section(17, "OWED TO YOU", f"={R('owed')}",
        f'=IF({R("waiting")}=0,"Nothing waiting. Lovely.",{R("waiting")}&IF({R("waiting")}=1," invoice"," invoices")&" waiting"&'
        f'IF({R("overdue")}>0,", "&{R("overdue")}&" overdue. A gentle nudge today?",". All on time."))')
dash["B20"] = "COMING UP: YEARLY COSTS"; dash["B20"].font = f(11, True, PINK)
dash.merge_cells("B21:E21")
dash["B21"] = (f'=IF({R("yearly_count")}=0,"No yearly costs added yet. Insurance, software, memberships? Add them in Fixed costs.",'
               f'{R("y1_line")})')
dash["B21"].font = f(12, True); dash["B21"].border = bar
for k, row in ((2, 22), (3, 23)):
    dash.merge_cells(f"B{row}:E{row}")
    dash[f"B{row}"] = f"={R(f'y{k}_line')}"; dash[f"B{row}"].font = f(11); dash[f"B{row}"].border = bar
dash.merge_cells("B24:E24")
dash["B24"] = (f'=IF({R("yearly_total")}=0,"","All yearly costs: "&TEXT({R("yearly_total")},"#,##0")&" a year, '
               f'about "&TEXT({R("yearly_total")}/12,"#,##0")&" a month to put aside.")')
dash["B24"].font = f(9, color=GREY, italic=True)
section(26, "CLIENT EXTRAS THIS MONTH", f"={R('extras')}",
        f'=IF({R("extras_n")}=0,"None logged this month. Coffee, parking, materials for clients? Add them in Client extras.",'
        f'{R("extras_n")}&IF({R("extras_n")}=1," cost"," costs")&" included in your fees, mostly "&LOWER({R("top_type")})&".")')
dash["B29"] = "YOUR MONEY MINUTE"; dash["B29"].font = f(11, True, PINK)
dash.merge_cells("B30:E30")
d = R("days")
dash["B30"] = (f'=IF({d}=-1,"Your first money minute is waiting. Two numbers, about 60 seconds.",'
               f'IF({d}<=7,"On track ✓  Last check-in "&IF({d}=0,"today",{d}&IF({d}=1," day"," days")&" ago")&". "&{R("minutes")}&" this month.",'
               f'"It\'s been "&{d}&" days. One minute, two numbers. You\'ve got this."))')
dash["B30"].font = f(12, True); dash["B30"].border = bar
dash.conditional_formatting.add("B30:E30", FormulaRule(formula=[f"AND({A('days')}>=0,{A('days')}<=7)"], font=Font(color="1F9D55", bold=True)))
dash["B33"] = ("Safe to spend = balance today − fixed costs still to pay this month (monthly ones, plus any yearly ones "
               "due this month) − tax to set aside − your comfort cushion.")
dash["B33"].font = f(8, color=GREY, italic=True)
dash["B34"] = "It's a guide to help you see clearly, not financial advice."
dash["B34"].font = f(8, color=GREY, italic=True)

wb.active = 0
wb.save(OUT)
print("saved", OUT)
