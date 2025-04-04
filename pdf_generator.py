from fpdf import FPDF

def generate_pdf_from_dataframe(df, output_path="output_table.pdf"):
    try:
        if df.empty:
            print("⚠️ Cannot generate PDF. DataFrame is empty.")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        col_width = 190 / max(len(df.columns), 1)
        row_height = 8

        for row in df.values.tolist():
            for item in row:
                pdf.cell(col_width, row_height, str(item), border=1)
            pdf.ln(row_height)

        pdf.output(output_path)
    except Exception as e:
        print(f"❌ Error while generating PDF: {e}")