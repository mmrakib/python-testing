import yfinance as yf
from pprint import pprint

ticker = yf.Ticker('AAPL')

info = ticker.info
income_stmt = ticker.quarterly_financials
bal_sheet = ticker.quarterly_balance_sheet
cash_flow_stmt = ticker.quarterly_cashflow

print('=== INFO ===')
pprint(info)

print('=== INCOME STATEMENT ===')
pprint(income_stmt)

print('=== BALANCE SHEET ===')
pprint(bal_sheet)

print('=== CASH FLOW STATEMENT ===')
pprint(cash_flow_stmt)
