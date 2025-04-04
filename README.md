# 🧾 PDF Table Extractor

## 🎯 Objective

A Python tool to **detect and extract tables** from **system-generated PDFs** and export them to **Excel files**. This solution **does NOT use Tabula or Camelot** and does **NOT convert PDFs to images**.

---

## 📥 Input

- PDFs containing tables (with or without borders, irregular shapes, merged cells).
- Only system-generated PDFs (not scanned images).

## 📤 Output

- Clean, structured Excel files containing the extracted tables.

---

## 🚫 Constraints

- ❌ No use of **Tabula** or **Camelot**
- ❌ No conversion of PDFs to **images**

---

## 🧠 Features

- Detects tabular data using **text and layout parsing** with `PyMuPDF` (`fitz`).
- Handles:
  - Tables with or without borders
  - Irregularly shaped tables
  - Merged or multiline cells
- Exports to Excel using **Pandas** and **OpenPyXL**

---

## ⚙️ Tech Stack

- **Language:** Python 3
- **PDF Parsing:** [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- **Excel Export:** pandas, openpyxl

---

## 📦 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/pdf-table-extractor.git
cd extract_tables_project



### Step 2: Install dependecies
```bash
pip install -r requirements.txt

###Usage 
```bash
python main.py
