import fitz
import re
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"❌ Error opening PDF: {e}")
        return pd.DataFrame()

    date_pattern = re.compile(r"^\d{2}-[A-Za-z]{3}-\d{4}")
    transactions = []

    for page in doc:
        lines = page.get_text("text").split("\n")

        for i, line in enumerate(lines):
            if date_pattern.match(line.strip()):
                try:
                    current_line = line.strip()
                    next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
                    full_line = current_line + " " + next_line if not re.search(r"\d+\.\d{2}", current_line) else current_line
                    parts = re.split(r'\s{2,}', full_line.strip())

                    if len(parts) >= 3:
                        date = parts[0][:11].strip()
                        desc = parts[0][11:].strip() + " " + " ".join(parts[1:-2])
                        amount = parts[-2].strip().replace(",", "")
                        balance = parts[-1].strip().replace(",", "").replace("Dr", "").replace("Cr", "")
                        transactions.append([date, desc.strip(), amount, balance])
                except Exception:
                    continue

    df = pd.DataFrame(transactions, columns=["Date", "Description", "Amount", "Balance"])
    if df.empty:
        print("⚠️ No transaction lines were detected.")
    else:
        print("✅ Extracted", len(df), "transaction rows.")

    return df
