
def pe_ratio(market_cap, net_income):
    return market_cap / net_income

def ev_ebitda(enterprise_value, ebitda):
    return enterprise_value / ebitda

def price_to_sales(market_cap, revenue):
    return market_cap / revenue

def price_to_book(market_cap, book_value):
    return market_cap / book_value

def ev_sales(enterprise_value, revenue):
    return enterprise_value / revenue

def return_on_equity(net_income, shareholder_equity):
    return net_income / shareholder_equity

def return_on_assets(net_income, total_assets):
    return net_income / total_assets

def gross_margin(gross_profit, revenue):
    return gross_profit / revenue

def operating_margin(operating_income, revenue):
    return operating_income / revenue

def net_margin(net_income, revenue):
    return net_income / revenue

def revenue_growth(current_revenue, previous_revenue):
    return (current_revenue - previous_revenue) / previous_revenue

def net_margin_growth(current_margin, previous_margin):
    return (current_margin - previous_margin) / previous_margin

def debt_to_equity(total_debt, shareholder_equity):
    return total_debt / shareholder_equity

def debt_to_capital(total_debt, total_equity):
    return total_debt / (total_debt + total_equity)

def interest_coverage(ebit, interest_expense):
    return ebit / interest_expense

def interest_funding(operating_cf, interest_expense):
    return operating_cf / interest_expense

def free_cash_flow_yield(free_cash_flow, market_cap):
    return free_cash_flow / market_cap

def operating_cash_yield(operating_cash_flow, enterprise_value):
    return operating_cash_flow / enterprise_value

def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

def days_sales_in_receivables(accounts_receivable, revenue):
    return (accounts_receivable / revenue) * 365

def cfo_to_net_income(operating_cf, net_income):
    return operating_cf / net_income

def capex_coverage(free_cash_flow, capex):
    return free_cash_flow / capex

def asset_turnover(revenue, total_assets):
    return revenue / total_assets
