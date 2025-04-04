from table_extractor import extract_tables_from_pdf
from pdf_generator import generate_pdf_from_dataframe
import os

pdf_input = "sample_input.pdf"  # Change this to your input file name

if not os.path.exists(pdf_input):
    print(f"❌ File '{pdf_input}' not found. Please place it in the project directory.")
else:
    df = extract_tables_from_pdf(pdf_input)
    if df is not None and not df.empty:
        generate_pdf_from_dataframe(df)
        print("✅ Table extraction and PDF generation completed.")
    else:
        print("⚠️ No table data extracted. PDF might not contain tabular format or is empty.")