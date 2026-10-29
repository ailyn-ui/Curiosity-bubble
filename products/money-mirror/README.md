# The Money Mirror – free v1.1

A one-screen "know your numbers" dashboard for ADHD founders, as a Google Sheet.
Setup takes about 10 minutes, once. Upkeep is one "money minute" a week: today's
date and bank balance, plus typing the date when an invoice gets paid.

- `The Money Mirror.xlsx` is the template to share (import into Google Sheets).
- `build.py` rebuilds it: `python3 build.py "The Money Mirror.xlsx"`.
- `test_fill.py` fills a copy with sample data to check the maths.

## Tabs

| Tab | What she does |
|---|---|
| **Start here** | 5 steps: name, today's balance, fixed costs, what's owed, tax % (+ optional comfort cushion). A progress line ends with "You did it. You know your numbers." |
| **Dashboard** | Nothing; it updates itself. One big **Safe to spend this month** number in green / amber / red, four tiles, what's owed, money-minute streak |
| **Money minute** | Once a week: date + balance (+ any other money in) |
| **Owed to you** | Client, amount, due date. When paid, type the date. Status says "overdue 9 days — chase gently" etc. |
| **Client extras** | Costs included in her fee but not billed separately (coffee, parking, materials, licences). Date, what, client, type, amount |
| **Fixed costs** | What leaves no matter what: **monthly** (day of month) or **yearly** (day + month). Shows "this month" status and the next date. Set once |

**Safe to spend** = balance today − fixed costs still to pay this month (monthly ones, plus
any yearly ones due this month) − tax to set aside (tax % × money in this month) − comfort cushion.

The dashboard also shows **Coming up: yearly costs** (the next one, when, and roughly how much a
month to put aside for all of them) and **Client extras this month** (total, and the biggest type).
Client extras are already out of the bank balance, so they aren't subtracted twice.

## Dates in different countries

Google Sheets reads typed dates using the spreadsheet's country. "Start here" asks her first to set
**File → Settings → Locale → her country**. After that she types dates the way she normally would,
or double-clicks a date box to pick from a calendar. Dates display as "3 Nov 2026", which reads the
same everywhere. Yearly costs use a month picker (Jan–Dec) plus a day, so they don't depend on date format.

Green: 0 or more · Amber: dipping into the cushion · Red: below the cushion.

## Checked

448 formulas recalculated with no errors. `test_fill.py` sample data (balance 4,250; monthly rent
already paid plus 300 still to come; a 900 yearly cost due this month and two yearly costs in other
months; one 1,200 invoice paid this month plus 300 other income; 30% tax; 500 cushion; three client
extras this month and one last month) gives: fixed still to pay 1,200, safe to spend 2,100, next
yearly cost flagged, client extras 90 (last month's excluded), biggest type correct.
Not yet opened in Google Sheets itself.

## Import into Google Sheets

1. Upload `The Money Mirror.xlsx` to Google Drive.
2. Open it, then **File → Save as Google Sheets**.
3. Check the fonts show as Playfair Display (if not: Format → font → More fonts → Playfair Display).
4. To share: **File → Share → Publish** is not needed. Instead, share a link ending in
   `/copy` (replace `/edit…` in the URL with `/copy`) so each person gets their own copy.

## Paid version ideas (later)

- Automatic invoice status from Stripe or PayPal.
- A quick-add form on her phone for client extras (e.g. a Google Form feeding the sheet).
- Client extras per client, against what that client paid (what she really keeps).
- Monthly look-back ("you chased 4 invoices, your cushion held").
- A short guided video for setup, and a voice-note check-in with Ailyn.
- Price to test with real users after the free version; synthetic guesses aren't enough.

It's a guide to see clearly, not tax, legal or financial advice.
