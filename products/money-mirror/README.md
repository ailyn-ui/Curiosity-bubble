# The Money Mirror – free v1

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
| **Fixed costs** | What leaves every month and on which day. Set once |

**Safe to spend** = balance today − fixed costs still to pay this month − tax to set
aside (tax % × money in this month) − comfort cushion.

Green: 0 or more · Amber: dipping into the cushion · Red: below the cushion.

## Checked

Formulas recalculated with no errors. With sample data (balance 4,250; rent 1,800 on the
1st, 200 + 100 still to pay; one 1,200 invoice paid this month, 300 other income; 30% tax;
500 cushion) the dashboard shows safe to spend 3,000, owed 1,300 with 1 overdue, and
"On track" for the money minute. Not yet opened in Google Sheets itself.

## Import into Google Sheets

1. Upload `The Money Mirror.xlsx` to Google Drive.
2. Open it, then **File → Save as Google Sheets**.
3. Check the fonts show as Playfair Display (if not: Format → font → More fonts → Playfair Display).
4. To share: **File → Share → Publish** is not needed. Instead, share a link ending in
   `/copy` (replace `/edit…` in the URL with `/copy`) so each person gets their own copy.

## Paid version ideas (later)

- Automatic invoice status from Stripe or PayPal.
- Monthly look-back ("you chased 4 invoices, your cushion held").
- A short guided video for setup, and a voice-note check-in with Ailyn.
- Price to test with real users after the free version; synthetic guesses aren't enough.

It's a guide to see clearly, not tax, legal or financial advice.
