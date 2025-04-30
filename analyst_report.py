# Import from the FPDF libary
from fpdf import FPDF
# Demonstrate cursor movement

pdf = FPDF()
pdf.add_page()

# add a left border filled
pdf.set_fill_color(218,26,51)
#add red/orange left border
pdf.rect(x=0, y=0, w=5, h=297, style='F')
#add purple next to red left border
pdf.set_fill_color(167,5,106)
pdf.rect(x=5, y=0, w=2, h=297, style='F') 

# Left side of page (group names, date, ticker, and logo)

#insert logo
pdf.image('Vicinity Centres_logo.png', x=10, y=0, w=40, h=25) #adjust width and height as required
pdf.ln(15) #line break

#insert text below logo
#set font for the date
pdf.set_font("Arial", "", 10)
pdf.set_xy(10,20) # set cursor position for date (10 units from the left, 10 units from the 10)
pdf.cell(0, 10, "Date: 23 April, 2025", ln=True)

#set font for initiation coverage
pdf.set_font("Arial", "B", 12)
pdf.cell(0,10, 'Initiation of Coverage', align='L') #Initiation of coverage title on the left
pdf.ln(7) #line break

#text for investment recommendation
pdf.set_font('Arial', 'B', 12)
pdf.set_text_color(255,204,0) #set text colour to yellow
pdf.cell(0,10, 'HOLD', align='L')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(11, 45, 65, 45) #insert a line 
pdf.ln(7) # line break

#set font for pricing
pdf.set_font('Arial','', 10)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'Target Price (average): $2.36', align='L')
pdf.ln(7) #line break
pdf.cell(0,10, 'Current Price $2.26', align='L')
pdf.ln(7) #line break
pdf.cell(0,10, 'Upside: 2.65%', align='L')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(11, 67, 65, 67) #insert a line 
pdf.ln(7) # line break

# inserting team names
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(0,0,0)
pdf.cell(0,10, 'Authored by FINM3422 Team 34', align='L')
pdf.ln(5) #line break

# Ellie Manton
pdf.set_font('Arial','', 8)
pdf.cell(0,10, 'Ellie Manton', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'48853712', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'e.manton@student.uq.edu.au', align='L')
pdf.ln(5) #line break

# Senuthi Herath
pdf.set_font('Arial','', 8)
pdf.cell(0,10, 'Senuthi Herath', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'XXX', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'s.herathmudiyanselage@student.uq.edu.au', align='L')
pdf.ln(5) #line break

# James Mcoombes
pdf.set_font('Arial', '', 8)
pdf.cell(0,10, 'James Mcoombes', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'XXX', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'j.mccoombes@student.uq.edu.au', align='L')
pdf.ln(5) #line break

# Sam Coronis
pdf.set_font('Arial', '', 8)
pdf.cell(0,10, 'Sam Coronis', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'4885422', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'s.coronis@student.uq.edu.au', align='L')
pdf.ln(5) #line break

#Right side of the page (header, intro, company overview, and company highlights)
# set font for the header
pdf.set_font("Arial", "B", 16)
pdf.set_text_color(0,0,0)
pdf.set_xy(72, 8)
pdf.cell(0, 10, "Equity Research Report: Vicinity Centres")
pdf.ln(10) #line break

#Paragraph 1 - Introduction

#Setting font for introductory title
pdf.set_font("Arial", "B", 10)
pdf.set_xy(72,19)
pdf.cell(0,10, 'Vicinity Centres (ASX: VCX)')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(73, 27, 200, 27) #insert a line 

#introduction body text
#import text from file
with open('Introduction.txt', 'r') as file:
    introduction_text = file.read()
#Replace unsupported characters for FPDF
introduction_text = introduction_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
# set font for introduction text
pdf.set_font('Arial','',10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,29)
pdf.multi_cell(129,3.5, introduction_text, align='J')

#Paragraph 2 - Company Overview

#setting font for company overview title
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,70)
pdf.cell(100,10, 'Company Overview')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(73, 78, 200, 78) #insert a line 

#Pull company overview text
#import text from file
with open('Company Overview.txt', 'r') as file:
    company_overview_text = file.read()
#Replace unsupported characters for FPDF
company_overview_text = company_overview_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
#Set font for company overview text
pdf.set_font('Arial','',10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,80)
pdf.multi_cell(129,4, company_overview_text, align='J')

#Paragraph 3 - Company Highlights
#setting font for company highlights title
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,143)
pdf.cell(100,10, 'Company Highlights')
pdf.ln(10) #line break

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(73, 151, 200, 151) #insert a line 

#Pull company highlights text
#import text from file
with open('Company Highlights.txt', 'r') as file:
    company_highlights_text = file.read()
#Replace unsupported characters for FPDF
company_highlights_text = company_highlights_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

#Set font for company highlights text
pdf.set_font('Arial','',10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,154)

# Format lines: bold only if line ends with colon
for line in company_highlights_text.split('\n'):
    line = line.strip()
    if line.endswith(':'):
        pdf.set_font('Arial', 'B', 10)
    else:
        pdf.set_font('Arial', '', 10)
    pdf.set_x(72)
    pdf.multi_cell(129, 4.5, line, align='J')

pdf.add_page()

#Paragraph 4 - Industry Outlook

# Set position for title
pdf.set_xy(10, pdf.get_y())  # far left margin

# Title
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, 'Industry Outlook', ln=True)

# Draw line just below the title (adjust y if needed)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Add a small space before the paragraph
pdf.ln(2)

# Import text from file
with open('Industry_Outlook.txt', 'r') as file:
    industry_outlook_text = file.read()

# Replace unsupported characters
industry_outlook_text = industry_outlook_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

# Set font and position for paragraph
pdf.set_font("Arial", "", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_x(10)  # left-align paragraph
pdf.multi_cell(0, 4.5, industry_outlook_text, align='J')  # full width justified

#Insert space between paragraphs
pdf.ln(8)

#Economic Outlook
# Set position for title
pdf.set_xy(10, pdf.get_y())  # far left margin

# Title
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, 'Economic Outlook', ln=True)

# Draw line just below the title (adjust y if needed)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Add a small space before the paragraph
pdf.ln(2)

# Import text from file
with open('Economic_Outlook.txt', 'r') as file:
    economic_outlook_text = file.read()

# Replace unsupported characters
economic_outlook_text = economic_outlook_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

# Set font and position for paragraph
pdf.set_font("Arial", "", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_x(10)  # left-align paragraph
pdf.multi_cell(0, 4.5, economic_outlook_text, align='J')  # full width justified

pdf.add_page()


#Financial Ratios
pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Financial Ratios", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "[To be generated using financial API functions.]")

#DCF Valuation
pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "DCF Valuation", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "[Extracted from Excel - handled by teammate.]")


pdf.add_page()

#Imports for Price Chart
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Price Performance Comparison and Analysis
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Price Performance and Analyst Sentiment", ln=True)

stock_ticker = "VCX.AX"
index_ticker = "^AXJO"
start_date = "2024-04-23"
end_date = "2025-04-23"

vcx_data = yf.download(stock_ticker, start=start_date, end=end_date)
asx200_data = yf.download(index_ticker, start=start_date, end=end_date)

fig, ax1 = plt.subplots(figsize=(12, 6))

# VCX on left y-axis
ax1.plot(vcx_data.index, vcx_data["Close"], label="VCX.AX Closing Price", color='blue')
ax1.set_ylabel("VCX.AX Price (AUD)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Load price targets from CSV
price_targets = pd.read_csv("Historical_Price_Targets.csv", parse_dates=["Date"])

# Plot red dots for target prices
ax1.scatter(price_targets["Date"], price_targets["Target Price"],
              color='red', label="Historical Target Prices", zorder=5)

# ASX200 on right y-axis
ax2 = ax1.twinx()
ax2.plot(asx200_data.index, asx200_data["Close"], label="ASX200 Index", color='orange', linestyle='--', alpha=0.7)
ax2.set_ylabel("ASX200 Index", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Add legend
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

# Final formatting
plt.title("Vicinity Centres (VCX.AX) vs ASX200 with Target Prices")
fig.tight_layout()
plt.savefig("vcx_chart.png")
plt.close()

# Insert price comparison chart into PDF
pdf.image("vcx_chart.png", x=10, y=pdf.get_y(), w=190)

#Price Performance and Analyst Sentiment Analysis
# Set position for title
pdf.set_xy(10, pdf.get_y())  # far left margin

# Add space between chart and analysis
pdf.ln(98)

# Title
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, 'Price Performance and Analyst Sentiment Analysis', ln=True)

# Draw line just below the title (adjust y if needed)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Add a small space before the paragraph
pdf.ln(4)

# Import text from file
with open('Price_Performance_Analysis.txt', 'r') as file:
    price_performance_text = file.read()

# Replace unsupported characters
price_performance_text = price_performance_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

# Set font and position for paragraph
pdf.set_font("Arial", "", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_x(10)  # left-align paragraph
pdf.multi_cell(0, 5, price_performance_text, align='J')  # full width justified

pdf.add_page()

#Investment Theses Paragraph
# Title
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, 'Investment Theses', ln=True)

# Draw line just below the title (adjust y if needed)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Add a small space before the paragraph
pdf.ln(4)

# Import text from file
with open('Investment_Thesis.txt', 'r') as file:
    investment_thesis_text = file.read()

# Replace unsupported characters
investment_thesis_text = investment_thesis_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

# Set font and position for paragraph
pdf.set_font("Arial", "", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_x(10)  # left-align paragraph
pdf.multi_cell(0, 5, investment_thesis_text, align='J')  # full width justified

# Add a small space before the paragraph
pdf.ln(2)


#Risks and Mitigations
# Title
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, 'Investment Risks and Mitigations', ln=True)

# Draw line just below the title (adjust y if needed)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Add a small space before the paragraph
pdf.ln(4)

# Import text from file
with open('Investment_Risks_and_Mitigations.txt', 'r') as file:
    investment_risks_and_mitigations_text = file.read()

# Replace unsupported characters
investment_risks_and_mitigations_text = investment_risks_and_mitigations_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

# Set font and position for paragraph
pdf.set_font("Arial", "", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_x(10)  # left-align paragraph
pdf.multi_cell(0, 5, investment_risks_and_mitigations_text, align='J')  # full width justified

# Add a small space before the paragraph
pdf.ln(2)


#Final Recommendation
# Title
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, 'Final Recommendation', ln=True)

# Draw line just below the title (adjust y if needed)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Add a small space before the paragraph
pdf.ln(4)

# Import text from file
with open('Final_Recommendation.txt', 'r') as file:
    final_recommendation_text = file.read()

# Replace unsupported characters
final_recommendation_text = final_recommendation_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

# Set font and position for paragraph
pdf.set_font("Arial", "", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_x(10)  # left-align paragraph
pdf.multi_cell(0, 5, final_recommendation_text, align='J')  # full width justified

pdf.add_page()

#Reference List
# Title
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, 'Reference List', ln=True)

# Draw line just below the title (adjust y if needed)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Add a small space before the paragraph
pdf.ln(4)

# Import text from file
with open('Reference_List.txt', 'r') as file:
    reference_list_text = file.read()

# Replace unsupported characters
reference_list_text = reference_list.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

# Set font and position for paragraph
pdf.set_font("Arial", "", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_x(10)  # left-align paragraph
pdf.multi_cell(0, 5, reference_list_text, align='J')  # full width justified



# === Output ===
pdf.output("Vicinity Centres Equity Research Report.pdf")

