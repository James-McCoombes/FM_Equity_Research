

# summary table for DCF valuation
pdf.set_x(80)
pdf.set_font("Arial", "B", 9)
pdf.cell(0, 8, "DCF Valuation Summary", ln=True)

# Column headers (no borders or fill) only  the headers
pdf.set_x(80)
# formatting special table
metric_cells = 10
perp_cells = 40
ebitda_cells = 30

# formatting special table
pdf.cell(metric_cells, 6, "Metric", ln=False)
pdf.cell(perp_cells, 6, "Perpetuity", align="R", ln=False)
pdf.cell(ebitda_cells, 6, "EBITDA Exit (Mid)", align="R", ln=False)
pdf.ln()


# Data rows (clean style)
for idx, row in summary_df.iterrows():
    label = row["Metric"]
    if "implied price" in label.lower():
        continue
    p_val = clean_number(row["Perpetuity"])
    e_val = clean_number(row["EBITDA Exit (Mid)"])

    pdf.set_x(80)
    pdf.set_font("Arial", "B", 8)
    pdf.cell(metric_cells, 6, label, ln=False)

    pdf.set_font("Arial", "", 8)
    pdf.cell(perp_cells, 6, fmt(p_val, label), align="R", ln=False)
    pdf.cell(ebitda_cells, 6, fmt(e_val, label), align="R", ln=False)
    pdf.ln()

pdf.set_x(80)
pdf.set_font("Arial", "B", 8)
pdf.cell(metric_cells, 6, "Implied Share Price", ln=False)

pdf.set_font("Arial", "", 8)
pdf.cell(perp_cells, 6, f"${implied_price_p:.2f}", align="R", ln=False)
pdf.cell(ebitda_cells, 6, f"${implied_price_e:.2f}", align="R", ln=False)
pdf.ln()

# === Implied Share Price (same styling) ===
pdf.set_x(80)
pdf.set_font("Arial", "B", 8)
pdf.cell(metric_cells, 6, "Implied Share Price", ln=False)

pdf.set_font("Arial", "", 8)
pdf.cell(perp_cells, 6, f"${implied_price_p:.2f}", align="R", ln=False)
pdf.cell(ebitda_cells, 6, f"${implied_price_e:.2f}", align="R", ln=False)
pdf.ln()







################################################################ Financial Ratios
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, pdf.get_y())
pdf.cell(100, 10, 'Financial Ratios')

pdf.set_draw_color(0, 0, 0)
pdf.line(20, pdf.get_y() + 8, 200, pdf.get_y() + 8)
pdf.ln(9)

#Importibg financials.
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

vcx = yf.Ticker("VCX.AX")
vcx_prices = vcx.history(period="1y", interval="1d")
print("Price Data (head):")
print(vcx_prices.head())

info = vcx.info
print("Basic Info:")
print(f"Name: {info.get('shortName')}")
print(f"Market Cap: {info.get('marketCap')}")
print(f"Current Price: {info.get('currentPrice')}")
print(f"PE Ratio (TTM): {info.get('trailingPE')}")
print(f"Dividend Yield: {info.get('dividendYield')}")

# retrieveing financial statements data and loadinbg in clean pull CSV data
vcx_prices.to_csv("vcx_price_history.csv")
ticker = yf.Ticker("VCX.AX")
#P&L
income_statement = ticker.financials.T
print("Income Statement:")
print(income_statement.head())
income_statement.to_csv("vcx_income_statement.csv")

df = pd.read_csv("vcx_income_statement.csv")
print("Cleaned Income Statement:")
print(df.head())
print("Columns:")
print(df.columns.tolist())
df_flipped = df.set_index(df.columns[0]).T
df_flipped = df_flipped.iloc[::-1]
df_flipped.index.name = "Fiscal Year"
df_flipped.reset_index(inplace=True)
pd.set_option('display.max_columns', None) 
print(df_flipped.head())
print(df_flipped)

#BS
balance_sheet = ticker.balance_sheet.T
print("Balance Sheet:")
print(balance_sheet.head())
balance_sheet.to_csv("vcx_balance_sheet.csv")


df_bs = pd.read_csv("vcx_balance_sheet.csv")
df_flipped_bs = df_bs.set_index(df_bs.columns[0]).T
df_flipped_bs = df_flipped_bs.iloc[::-1]
df_flipped_bs.index.name = "Fiscal Year"
df_flipped_bs.reset_index(inplace=True)
pd.set_option('display.max_columns', None)
print(df_flipped_bs.head())
print(df_flipped_bs)

#CFS
cash_flow = ticker.cashflow.T
print("Cash Flow Statement:")
print(cash_flow.head())
cash_flow.to_csv("vcx_cashflow_statement.csv")
# correctly retrieving raw data as per FY2024 
print(income_statement)
print(balance_sheet)
print(cash_flow)

raw_cfs_df = pd.read_csv("vcx_cashflow_statement.csv", header=None)
df_t = raw_cfs_df.T
df_t.columns = df_t.iloc[0]
df_clean_cfs = df_t.drop(index=0).reset_index(drop=True)
df_clean_cfs.columns.name = None
df_clean_cfs.rename(columns={df_clean_cfs.columns[0]: "Fiscal Year"}, inplace=True)
pd.set_option('display.max_columns', None)
print("Cleaned Cash Flow Statement:")
print(df_clean_cfs.head())

raw_price_df = pd.read_csv("vcx_price_history.csv")
print(raw_price_df)

print(df_flipped)
print(df_flipped_bs)
print(df_clean_cfs)

#  scraping datad form CSV files
# reference year for all financial statements (P&L, BS, CFS) assumed using VCX most recent end of FY2024 number for
#scraping data from the ++++++++ income statement +++++++++ to print key financial metrics from df_flipped transposed data frame
# net iccome (need t and t-1, for net margin growth rate calcualtions)
net_income = df_flipped.iloc[27]
net_income_2024 = net_income["2024-06-30"]
net_income_2023 = net_income["2023-06-30"]
print(net_income_2024)
print(net_income_2023)
print(net_income)

# revenues (need t and t-1, for growth rate calcualtions)
revenues = df_flipped.iloc[1]
revenues_2024 = revenues["2024-06-30"]
revenues_2023 = revenues["2023-06-30"]
print(revenues_2023)
print(revenues_2024)
print(revenues)

# gross profit
gross_profit = df_flipped.iloc[3]
gross_profit_2024 = gross_profit["2024-06-30"]
print(gross_profit)
print(gross_profit_2024)

# operating income = EBIT
EBIT = df_flipped.iloc[38]
EBIT_2024 = EBIT["2024-06-30"]
print(EBIT)
print(EBIT_2024)

EBITDA = df_flipped.iloc[39]
EBITDA_2024 = EBITDA["2024-06-30"]
print(EBITDA)
print(EBITDA_2024)

# interest expense
interest_expense = df_flipped.iloc[36]
interest_expense_2024 = interest_expense["2024-06-30"]
print(interest_expense)
print(interest_expense_2024)

#scraping data from the ++++++++ balance sheet +++++++++ to print key financial metrics from df_flipped_bs transposed data frame

book_value = df_flipped_bs.iloc[62]
book_value_2024 = book_value["2024-06-30"]
print(book_value)
print(book_value_2024)

shareholder_equity = df_flipped_bs.iloc[54]
shareholder_equity_2024 = shareholder_equity["2024-06-30"]
print(shareholder_equity)
print(shareholder_equity_2024)

total_assets = df_flipped_bs.iloc[26]
total_assets_2024 = total_assets["2024-06-30"]
print(total_assets)
print(total_assets_2024)

total_debt = df_flipped_bs.iloc[63]
total_debt_2024 = total_debt["2024-06-30"]
print(total_debt)
print(total_debt_2024)

accounts_receivable = df_flipped_bs.iloc[3]
accounts_receivable_2024 = accounts_receivable["2024-06-30"]
print(accounts_receivable)
print(accounts_receivable_2024)

current_assets = df_flipped_bs.iloc[10]
current_assets_2024 = current_assets["2024-06-30"]
print(current_assets)
print(current_assets_2024)

shares_outstanding = df_flipped_bs.iloc[66]
shares_outstanding_2024 = shares_outstanding["2024-06-30"]
print(shares_outstanding)
print(shares_outstanding_2024)

#equity_value = df_flipped_bs.iloc[] #finish equity value  calcualtions

net_debt = df_flipped_bs.iloc[64]
net_debt_2024 = net_debt["2024-06-30"]
print(net_debt)
print(net_debt_2024)

current_liabilities = df_flipped_bs.iloc[39]
current_liabilities_2024 = current_liabilities["2024-06-30"]
print(current_liabilities)
print(current_liabilities_2024)


#scraping data from the ++++++++ cash flow statement +++++++++ to print key financial metrics from df_clean_cfs transposed data frame
free_cash_flow = df_clean_cfs.iloc[0]
free_cash_flow_2024 = free_cash_flow["2024-06-30"]
print(free_cash_flow)
print(free_cash_flow_2024)

operating_cf = df_clean_cfs.iloc[31]
operating_cf_2024 = operating_cf["2024-06-30"]
print(operating_cf)
print(operating_cf_2024)

capex = df_clean_cfs.iloc[5]
capex_2024 = capex["2024-06-30"]
print(capex)
print(capex_2024)

# extenal varibles defined for multiples
# ask group whether to use current or FY2024 data for ratios calcualtions
# all the data we have access to through yfinance is as of FY2024 year end

# current enterprise value data
enterprise_value = ticker.info.get('enterpriseValue')
print("Enterprise Value:", enterprise_value)

FY2024_enterprise_value = shareholder_equity_2024 + net_debt_2024
print(FY2024_enterprise_value)
#share price data
# current
current_share_price = ticker.info.get('currentPrice')
print("Share Price:", current_share_price)
# at time of FY2024
FY2024_close_price = vcx_prices.iloc[42]['Close']
print("VCX FY2024 Close:", FY2024_close_price)

#mareket cap data
market_cap = info.get('marketCap')
print("Market Cap:", market_cap)
# backed out market cap for FY2024

FY2024_market_cap = shares_outstanding_2024 * FY2024_close_price
print("Market Cap:", FY2024_market_cap)

#compiling key valuation ratios for VCX.AX
# full ratio calculations

#pe
from valuation_ratios import (pe_ratio)
print("P/E Ratio:", round(pe_ratio(FY2024_market_cap, net_income_2024), 10))

# this may be using current marlket cap, not market cap at end of FY2024 ansd net income is  obviosuly FY2024
# ask group about this

#ev_ebitda 
from valuation_ratios import (ev_ebitda)
print("EV/EBITDA Ratio:", round(ev_ebitda(FY2024_enterprise_value, EBITDA_2024), 10))

#price_to_sales 
from valuation_ratios import (price_to_sales)
print("P/S Ratio:", round(price_to_sales(FY2024_market_cap, revenues_2024), 10))

#price_to_book
from valuation_ratios import (price_to_book)
print("P/B Ratio:", round(price_to_book(FY2024_market_cap, book_value_2024), 10))

# ev to sales ratio
from valuation_ratios import (ev_sales)
print("EV/Sales Ratio:", round(ev_sales(FY2024_enterprise_value, revenues_2024), 10))

# return on equity
from valuation_ratios import (return_on_equity)
print("ROE:", round(return_on_equity(net_income_2024, shareholder_equity_2024), 10))

#return on assets
from valuation_ratios import (return_on_assets)
print("ROA:", round(return_on_assets(net_income_2024, total_assets_2024), 10))

# gross margn
from valuation_ratios import (gross_margin)
print("Gross Margin:", round(gross_margin(gross_profit_2024, revenues_2024), 10))

# operating margin
from valuation_ratios import (operating_margin)
print("Operating Margin:", round(operating_margin(EBIT_2024, revenues_2024), 10))

# net margin
from valuation_ratios import (net_margin)
print("Net Margin:", round(net_margin(net_income_2024, revenues_2024), 10))
current_margin = net_margin(net_income_2024, revenues_2024)
print("Current Net Margin:", current_margin)

#  net margin growth
net_margin_2023 = net_margin(net_income_2023, revenues_2023)
print("Previous Net Margin:", net_margin_2023)
from valuation_ratios import (net_margin_growth)
print("Net Margin Growth:", round(net_margin_growth(current_margin, net_margin_2023), 10))

# revenue growth
from valuation_ratios import (revenue_growth)
print("Revenue Growth:", round(revenue_growth(revenues_2024, revenues_2023), 10))

# debt to equity
from valuation_ratios import (debt_to_equity)
print("Debt to Equity Ratio:", round(debt_to_equity(total_debt_2024, shareholder_equity_2024), 10))

#debt to capital ratio
from valuation_ratios import (debt_to_capital)
total_captial_2024 = total_debt_2024 + shareholder_equity_2024
print("Debt to Capital Ratio:", round(debt_to_capital(total_debt_2024, total_captial_2024), 10))

#  interest coverage
from valuation_ratios import (interest_coverage)
print("Interest Coverage Ratio:", round(interest_coverage(EBIT_2024, interest_expense_2024), 10))

#interest funding ratio
print(type(operating_cf_2024), operating_cf_2024)
print(type(interest_expense_2024), interest_expense_2024)
operating_cf_2024 = float(operating_cf_2024.replace(',', '').strip())
from valuation_ratios import (interest_funding)
print("Interest Funding Ratio:", round(interest_funding(operating_cf_2024, interest_expense_2024), 10))

#free cahs flow yield
from valuation_ratios import (free_cash_flow_yield)
print(type(free_cash_flow_2024), FY2024_market_cap)
print(free_cash_flow_2024)
print(FY2024_market_cap)
market_cap_2024 = float(FY2024_market_cap)
free_cash_flow_2024 = float(free_cash_flow_2024)
print("fcf yield", free_cash_flow_yield(free_cash_flow_2024, market_cap_2024))

#current ratio
from valuation_ratios import (current_ratio)
print("Current Ratio:", round(current_ratio(current_assets_2024,current_liabilities_2024), 10))

from valuation_ratios import (asset_turnover)
print("Asset turnover ratio:", round(asset_turnover(revenues_2024, total_assets_2024), 10))

# all ratios have printed cleanly, now just stoering all ratios in a dictionary for easy access
import json

# === Store all calculated ratios in one dictionary ===
financial_ratios = {
    "P/E Ratio": round(pe_ratio(market_cap_2024, net_income_2024), 10),
    "EV/EBITDA Ratio": round(ev_ebitda(FY2024_enterprise_value, EBITDA_2024), 10),
    "P/S Ratio": round(price_to_sales(FY2024_market_cap, revenues_2024), 10),
    "P/B Ratio": round(price_to_book(FY2024_market_cap, book_value_2024), 10),
    "EV/Sales Ratio": round(ev_sales(FY2024_enterprise_value, revenues_2024), 10),
    "Return on Equity (ROE)": round(return_on_equity(net_income_2024, shareholder_equity_2024), 10),
    "Return on Assets (ROA)": round(return_on_assets(net_income_2024, total_assets_2024), 10),
    "Gross Margin": round(gross_margin(gross_profit_2024, revenues_2024), 10),
    "Operating Margin": round(operating_margin(EBIT_2024, revenues_2024), 10),
    "Net Margin": round(net_margin(net_income_2024, revenues_2024), 10),
    "Net Margin Growth": round(net_margin_growth(current_margin, net_margin_2023), 10),
    "Revenue Growth": round(revenue_growth(revenues_2024, revenues_2023), 10),
    "Debt to Equity Ratio": round(debt_to_equity(total_debt_2024, shareholder_equity_2024), 10),
    "Interest Coverage Ratio": round(interest_coverage(EBIT_2024, interest_expense_2024), 10),
    "Free Cash Flow Yield": round(free_cash_flow_yield(free_cash_flow_2024, market_cap_2024), 10),
    "Current Ratio": round(current_ratio(current_assets_2024, current_liabilities_2024), 10),
    "Asset Turnover": round(asset_turnover(revenues_2024, total_assets_2024), 10),
}

#saving financial ratios as JSON file
with open("vcx_ratios.json", "w") as f:
    json.dump(financial_ratios, f)

# superimosing derrived figures into the PDF, load financial ratios from JSON file
try:
    with open("vcx_ratios.json", "r") as f:
        ratios = json.load(f)
except FileNotFoundError:
    ratios = {"Error": "Could not load financial ratios."}

percent_keywords = ["ROE", "ROA", "Margin", "Growth", "Yield"]
multiple_keywords = ["P/E", "EV", "P/S", "P/B", "Coverage", "Current Ratio", "Asset Turnover", "Debt"]
decimal_keywords = ["Gross Margin"]

as_percent = lambda k: any(word.lower() in k.lower() for word in percent_keywords)
as_multiple = lambda k: any(word.lower() in k.lower() for word in multiple_keywords)
keep_decimal = lambda k: any(word.lower() in k.lower() for word in decimal_keywords)

row_height = 5
col_width = 63  # compact width to fit all 3 columns
start_x = 20

keys = list(ratios.keys())
values = list(ratios.values())

# === Render Table ===
for i in range(0, len(keys), 3):
    y = pdf.get_y()
    for j in range(3):
        if i + j < len(keys):
            key = keys[i + j]
            val = values[i + j]

            # Format value
            if isinstance(val, (int, float)):
                if keep_decimal(key):
                    val_str = f"{val:.2f}"
                elif as_percent(key):
                    val_str = f"{val * 100:.1f}%"
                elif as_multiple(key):
                    val_str = f"{val:.2f}x"
                else:
                    val_str = f"{val:.2f}"
            else:
                val_str = str(val)

            x = start_x + j * col_width
            pdf.set_xy(x, y)

            # Bold label
            pdf.set_font("Arial", "B", 8.5)
            label_str = f"{key}:"
            pdf.cell(pdf.get_string_width(label_str) + 1, row_height, label_str, ln=False)

            # Normal value
            pdf.set_font("Arial", "", 8.5)
            pdf.cell(col_width - pdf.get_string_width(label_str) - 1, row_height, val_str, ln=False)

    pdf.ln(row_height)



# === Load Ratio Commentary Text ===
with open("ratio_commentary.txt", "r", encoding="latin-1") as f:
    ratio_commentary = f.read()

