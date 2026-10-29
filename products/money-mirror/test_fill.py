import sys, datetime as d
from openpyxl import load_workbook
wb = load_workbook(sys.argv[1]); s=wb["Start here"]; f=wb["Fixed costs"]; o=wb["Owed to you"]; m=wb["Money minute"]
s["D7"]="Sarah"; s["D9"]=3000; s["D15"]=0.3; s["D16"]=500
for i,(n,a,day) in enumerate([("Rent",1800,1),("Software",100,30),("Insurance",200,31)]):
    f[f"B{8+i}"],f[f"C{8+i}"],f[f"D{8+i}"]=n,a,day
rows=[("A",1200,d.date(2026,10,15),d.date(2026,10,20)),("B",800,d.date(2026,10,20),None),("C",500,d.date(2026,11,15),None)]
for i,(n,a,due,paid) in enumerate(rows):
    o[f"B{8+i}"],o[f"C{8+i}"],o[f"D{8+i}"]=n,a,due
    if paid: o[f"E{8+i}"]=paid
m["B8"],m["C8"],m["D8"]=d.date(2026,10,27),4250,300
wb.save(sys.argv[2])
