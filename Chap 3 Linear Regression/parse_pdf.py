import tabula

# Specify the path to your PDF file
pdf_file_path = 'C:\\Users\\jakel\\Desktop\\Code\\Under-5-Nearest-Health-Center\\Data\\District-Development-Factsheet-2019.pdf'

# Use tabula to extract tables
tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True)

# Print the extracted tables
for i, table in enumerate(tables, start=1):
    print(f"Table {i}:\n{table}\n")
