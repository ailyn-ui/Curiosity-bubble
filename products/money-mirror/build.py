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

wb = Workbook()
setup = wb.active; setup.title = "Start here"
dash = wb.create_sheet("Dashboard")
mm = wb.create_sheet("Money minute")
owed = wb.create_sheet("Owed to you")
fixed = wb.create_sheet("Fixed costs")
for ws, col in [(setup, PINK), (dash, INK), (mm, PINK), (owed, "BBBBBB"), (fixed, "BBBBBB")]:
    ws.sheet_properties.tabColor = col

# ---------- Fixed costs ----------
base(fixed, {"A": 3, "B": 30, "C": 18, "D": 18, "E": 22})
title(fixed, "Fixed costs", "What leaves every month, no matter what. Add them once; you rarely touch this again.")
for col, h in zip("BCDE", ["What it is", "Amount per month", "Day it leaves (1–31)", "This month"]):
    c = fixed[f"{col}6"]; c.value = h; c.font = f(10, True, GREY); c.border = under
for col, v in zip("BCD", ["e.g. Rent", "1,800", "1"]):
    fixed[f"{col}7"] = v; fixed[f"{col}7"].font = f(10, color=GREY, italic=True)
for r in range(FIRST, LAST + 1):
    for col in "BCD":
        fixed[f"{col}{r}"].fill = inp; fixed[f"{col}{r}"].font = f()
    fixed[f"C{r}"].number_format = NUM
    fixed[f"E{r}"] = f'=IF(OR(C{r}="",D{r}=""),"",IF(D{r}>DAY(TODAY()),"still to pay","paid ✓"))'
    fixed[f"E{r}"].font = f(10, color=GREY)
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="31", allow_blank=True,
                    error="Pick a day from 1 to 31.", showErrorMessage=True)
fixed.add_data_validation(dv); dv.add(f"D{FIRST}:D{LAST}")
fixed.freeze_panes = "B8"

# ---------- Owed to you ----------
base(owed, {"A": 3, "B": 26, "C": 16, "D": 16, "E": 16, "F": 24})
title(owed, "Owed to you", "Every invoice you've sent. When one gets paid, just type the date. That's it.")
for col, h in zip("BCDEF", ["Client", "Amount", "Due date", "Paid on", "Status"]):
    c = owed[f"{col}6"]; c.value = h; c.font = f(10, True, GREY); c.border = under
for col, v in zip("BCDE", ["e.g. Studio Luna", "1,200", "15/11/2026", "(leave empty until paid)"]):
    owed[f"{col}7"] = v; owed[f"{col}7"].font = f(10, color=GREY, italic=True)
for r in range(FIRST, LAST + 1):
    for col in "BCDE":
        owed[f"{col}{r}"].fill = inp; owed[f"{col}{r}"].font = f()
    owed[f"C{r}"].number_format = NUM
    owed[f"D{r}"].number_format = "dd mmm yyyy"; owed[f"E{r}"].number_format = "dd mmm yyyy"
    owed[f"F{r}"] = (f'=IF(C{r}="","",IF(E{r}<>"","paid ✓ — nice",IF(D{r}="","waiting",'
                     f'IF(D{r}<TODAY(),"overdue "&(TODAY()-D{r})&" days — chase gently","due in "&(D{r}-TODAY())&" days"))))')
    owed[f"F{r}"].font = f(10, color=GREY)
dvd = DataValidation(type="date", operator="greaterThan", formula1="36526", allow_blank=True,
                     error="Type a date, like 03/11/2026.", showErrorMessage=True)
owed.add_data_validation(dvd); dvd.add(f"D{FIRST}:E{LAST}")
owed.conditional_formatting.add(f"F{FIRST}:F{LAST}", FormulaRule(formula=[f'LEFT(F{FIRST},4)="paid"'], font=Font(color="1F9D55", bold=True)))
owed.conditional_formatting.add(f"F{FIRST}:F{LAST}", FormulaRule(formula=[f'LEFT(F{FIRST},7)="overdue"'], font=Font(color=PINK, bold=True)))
owed.freeze_panes = "B8"

# ---------- Money minute ----------
base(mm, {"A": 3, "B": 16, "C": 20, "D": 22, "E": 34})
title(mm, "Your money minute", "Once a week. Open your bank app, type today's date and balance. Done.")
for col, h in zip("BCDE", ["Date", "Balance today", "Other money in*", "A note to yourself (optional)"]):
    c = mm[f"{col}6"]; c.value = h; c.font = f(10, True, GREY); c.border = under
for col, v in zip("BCDE", ["e.g. 03/11/2026", "4,250", "0", "Felt okay. Chased Studio Luna."]):
    mm[f"{col}7"] = v; mm[f"{col}7"].font = f(10, color=GREY, italic=True)
for r in range(FIRST, LAST + 1):
    for col in "BCDE":
        mm[f"{col}{r}"].fill = inp; mm[f"{col}{r}"].font = f()
    mm[f"B{r}"].number_format = "dd mmm yyyy"
    mm[f"C{r}"].number_format = NUM; mm[f"D{r}"].number_format = NUM
mm.add_data_validation(dvm := DataValidation(type="date", operator="greaterThan", formula1="36526", allow_blank=True,
                       error="Type a date, like 03/11/2026.", showErrorMessage=True))
dvm.add(f"B{FIRST}:B{LAST}")
mm[f"B{LAST+2}"] = "* Money that came in this week that isn't one of your invoices (a sale, a refund, a one-off job)."
mm[f"B{LAST+2}"].font = f(9, color=GREY, italic=True)
mm.freeze_panes = "B8"

# ---------- Start here ----------
base(setup, {"A": 3, "B": 6, "C": 58, "D": 18, "E": 12})
title(setup, "The Money Mirror", "A tool for clarity. About 10 minutes, once. Then one minute a week.")
setup["B4"] = "Pink boxes are yours to fill. Everything else updates itself."
setup["B4"].font = f(10, True, PINK)
steps = [
    (7,  "1", "What's your first name?", None),
    (9,  "2", "What's in your business account today?", NUM),
    (11, "3", "Add your fixed costs  →  'Fixed costs' tab", None),
    (13, "4", "Add anything people owe you  →  'Owed to you' tab", None),
    (15, "5", "Tax: what % of income do you set aside?", "0%"),
    (16, "",  "Comfort cushion: an amount you never want to dip below", NUM),
]
for r, n, q, fmt in steps:
    setup[f"B{r}"] = n; setup[f"B{r}"].font = f(16, True, PINK, name=H)
    setup[f"C{r}"] = q; setup[f"C{r}"].font = f(11, True)
    setup.row_dimensions[r].height = 24
for r in (7, 9, 15, 16):
    setup[f"D{r}"].fill = inp; setup[f"D{r}"].font = f(12, True)
for r, fmt in ((9, NUM), (15, "0%"), (16, NUM)):
    setup[f"D{r}"].number_format = fmt
setup["C14"] = "Nobody owes me right now? Pick Yes →"; setup["C14"].font = f(9, color=GREY, italic=True)
setup["D14"].fill = inp; setup["D14"].font = f(11, True)
dvy = DataValidation(type="list", formula1='"Yes"', allow_blank=True)
setup.add_data_validation(dvy); dvy.add("D14")
setup["C10"] = "Tip: this is just your starting point. Your money minute keeps it fresh."
setup["C10"].font = f(9, color=GREY, italic=True)
setup["C17"] = "If you already move tax to a separate account, put 0% above."
setup["C17"].font = f(9, color=GREY, italic=True)
setup["D15"].comment = Comment("Ask your accountant what's right for you. Many freelancers set aside 25–35%.", "Ailyn")
dvp = DataValidation(type="decimal", operator="between", formula1="0", formula2="1", allow_blank=True,
                     error="Type a percentage, like 30%.", showErrorMessage=True)
setup.add_data_validation(dvp); dvp.add("D15")
# completion ticks
done = {
    7:  'D7<>""',
    9:  'D9<>""',
    11: f"COUNT('Fixed costs'!C{FIRST}:C{LAST})>0",
    13: f"OR(COUNT('Owed to you'!C{FIRST}:C{LAST})>0,D14=\"Yes\")",
    15: 'D15<>""',
}
for r, cond in done.items():
    col = "E"
    setup[f"{col}{r}"] = f'=IF({cond},"✓ done","")'
    setup[f"{col}{r}"].font = f(11, True, "1F9D55")
setup["C20"] = "=COUNTIF(E7:E15,\"✓ done\")/5"
setup["C20"].number_format = '0%" set up"'; setup["C20"].font = f(14, True, PINK, name=H)
setup["C21"] = ('=IF(C20=1,"You did it. You know your numbers. Head to your Dashboard ✨",'
                '"Step "&(COUNTIF(E7:E15,"✓ done")+1)&" of 5. You\'re doing great.")')
setup["C21"].font = f(13, True, name=H)
setup["C23"] = "Then, once a week: your money minute. Two numbers, about 60 seconds."
setup["C23"].font = f(10, color=GREY)
setup["C25"] = ("The Money Mirror helps you see your numbers. It isn't tax, legal or financial advice. "
                "For that, talk to an accountant or financial adviser.")
setup["C25"].font = f(8, color=GREY, italic=True); setup["C25"].alignment = Alignment(wrap_text=True)
setup.merge_cells("C25:E26")
for r in (20, 21):
    setup[f"C{r}"].border = bar

# named inputs
for name, ref in [("YourName", "'Start here'!$D$7"), ("StartBalance", "'Start here'!$D$9"),
                  ("TaxRate", "'Start here'!$D$15"), ("Cushion", "'Start here'!$D$16")]:
    wb.defined_names[name] = DefinedName(name, attr_text=ref)

# ---------- Dashboard ----------
base(dash, {"A": 3, "B": 22, "C": 22, "D": 22, "E": 22, "F": 3})
mmB, mmC, mmD = (f"'Money minute'!{c}{FIRST}:{c}{LAST}" for c in "BCD")
oC, oD, oE = (f"'Owed to you'!{c}{FIRST}:{c}{LAST}" for c in "CDE")
fC, fD = (f"'Fixed costs'!{c}{FIRST}:{c}{LAST}" for c in "CD")
som = "(EOMONTH(TODAY(),-1)+1)"; eom = "EOMONTH(TODAY(),0)"
dash["B2"] = '=IF(YourName="","Your money, at a glance.","Hi "&YourName&". Here\'s where you are.")'
dash["B2"].font = f(22, True, name=H); dash["B2"].border = bar
dash["B3"] = '="Updated "&TEXT(TODAY(),"dddd d mmmm")'; dash["B3"].font = f(10, color=GREY, italic=True)
# hidden calc cells (row 30+)
calc = {
    "B31": ("Balance", f'=IF(COUNT({mmB})=0,N(StartBalance),INDEX({mmC},MATCH(MAX({mmB}),{mmB},0)))'),
    "B32": ("Money in this month", f'=SUMPRODUCT(({oE}>={som})*({oE}<={eom})*{oC})+SUMPRODUCT(({mmB}>={som})*({mmB}<={eom})*{mmD})'),
    "B33": ("Fixed still to pay", f'=SUMPRODUCT(({fD}>DAY(TODAY()))*{fC})'),
    "B34": ("Tax to set aside", '=ROUND(N(TaxRate)*C32,0)'),
    "B35": ("Owed to you", f'=SUMPRODUCT(({oE}="")*{oC})'),
    "B36": ("Invoices waiting", f'=SUMPRODUCT(({oE}="")*({oC}<>""))'),
    "B37": ("Overdue", f'=SUMPRODUCT(({oE}="")*({oC}<>"")*({oD}<>"")*({oD}<TODAY()))'),
    "B38": ("Safe to spend", '=C31-C33-C34-N(Cushion)'),
    "B39": ("Days since money minute", f'=IF(COUNT({mmB})=0,-1,TODAY()-MAX({mmB}))'),
    "B40": ("Money minutes this month", f'=COUNTIFS({mmB},">="&{som},{mmB},"<="&{eom})'),
    "B41": ("Fixed costs total", f'=SUM({fC})'),
    "B42": ("Cushion", '=N(Cushion)'),
}
dash["B30"] = "Behind the scenes (no need to touch)"; dash["B30"].font = f(9, True, GREY)
for cell, (label, formula) in calc.items():
    r = cell[1:]
    dash[cell] = label; dash[cell].font = f(9, color=GREY)
    dash[f"C{r}"] = formula; dash[f"C{r}"].font = f(9, color=GREY); dash[f"C{r}"].number_format = NUM
dash["B6"] = "SAFE TO SPEND THIS MONTH"; dash["B6"].font = f(11, True, PINK)
dash.merge_cells("B7:E9")
dash["B7"] = "=C38"; dash["B7"].number_format = NUM
dash["B7"].font = f(60, True, name=H); dash["B7"].alignment = Alignment(horizontal="center", vertical="center")
for r in (7, 8, 9): dash.row_dimensions[r].height = 34
dash.merge_cells("B10:E10")
dash["B10"] = ('=IF(C38>=0,"You can breathe. This is yours to use this month.",'
               'IF(C38>=-N(Cushion),"You\'re into your cushion. Go gently this month.",'
               '"Pause big spends for now. Start with what\'s owed to you →"))')
dash["B10"].font = f(12, True); dash["B10"].alignment = Alignment(horizontal="center")
rng = "B7:E10"
dash.conditional_formatting.add(rng, FormulaRule(formula=["$C$38<-$C$42"], font=Font(color="C62828", bold=True)))
dash.conditional_formatting.add(rng, FormulaRule(formula=["AND($C$38<0,$C$38>=-$C$42)"], font=Font(color="E08A00", bold=True)))
dash.conditional_formatting.add(rng, FormulaRule(formula=["$C$38>=0"], font=Font(color="1F9D55", bold=True)))
tiles = [("B", "Balance today", "=C31"), ("C", "Money in this month", "=C32"),
         ("D", "Fixed costs still to pay", "=C33"), ("E", "Set aside for tax", "=C34")]
for col, label, formula in tiles:
    dash[f"{col}13"] = label; dash[f"{col}13"].font = f(9, True, GREY)
    dash[f"{col}14"] = formula; dash[f"{col}14"].number_format = NUM
    dash[f"{col}14"].font = f(20, True, name=H); dash[f"{col}14"].border = bar
    dash[f"{col}14"].alignment = Alignment(horizontal="left", indent=1)
dash["B17"] = "OWED TO YOU"; dash["B17"].font = f(11, True, PINK)
dash["B18"] = "=C35"; dash["B18"].number_format = NUM; dash["B18"].font = f(20, True, name=H); dash["B18"].border = bar
dash["B18"].alignment = Alignment(horizontal="left", indent=1)
dash.merge_cells("C18:E18")
dash["C18"] = ('=IF(C36=0,"Nothing waiting. Lovely.",C36&IF(C36=1," invoice"," invoices")&" waiting"&'
               'IF(C37>0,", "&C37&" overdue. A gentle nudge today?",". All on time."))')
dash["C18"].font = f(11); dash["C18"].alignment = Alignment(vertical="center")
dash["B21"] = "YOUR MONEY MINUTE"; dash["B21"].font = f(11, True, PINK)
dash.merge_cells("B22:E22")
dash["B22"] = ('=IF(C39=-1,"Your first money minute is waiting. Two numbers, about 60 seconds.",'
               'IF(C39<=7,"On track ✓  Last check-in "&IF(C39=0,"today","" & C39 & IF(C39=1," day"," days")&" ago")&". "&C40&" this month.",'
               '"It\'s been "&C39&" days. One minute, two numbers. You\'ve got this."))')
dash["B22"].font = f(12, True); dash["B22"].border = bar
dash.conditional_formatting.add("B22:E22", FormulaRule(formula=["AND($C$39>=0,$C$39<=7)"], font=Font(color="1F9D55", bold=True)))
dash["B25"] = "Safe to spend = balance today − fixed costs still to pay − tax to set aside − your comfort cushion."
dash["B25"].font = f(8, color=GREY, italic=True)
dash["B26"] = "It's a guide to help you see clearly, not financial advice."
dash["B26"].font = f(8, color=GREY, italic=True)
dash.row_dimensions[30].hidden = False

wb.active = 0
wb.save(OUT)
print("saved", OUT)
