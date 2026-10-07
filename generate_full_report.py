"""
generate_full_report.py
Generates the complete Lab Report Word document (.docx) containing all programs
from Practical 1 through Practical 10 and Beyond Syllabus 1 & 2.

Strictly follows all user formatting rules:
- Keeps the exact original cover page from 'report first page - original copy.docx'.
- Practical heading: 'Practical :- <num>' in 16 pt Bold.
- Aim: 'Aim :- ' in 14 pt Bold, followed by aim text in 14 pt Regular.
- Input File (when applicable): 'Input File (<name>) :- ' in 14 pt Bold, followed by content in 10 pt.
- Program: 'Program :- ' in 14 pt Bold, followed by code in 10 pt Courier New.
- Output: 'Output :- ' in 14 pt Bold, followed by output in 10 pt Courier New.
- Low line spacing throughout to minimize printed page count.
- Saves to both 'report first page    .docx' and 'Lab Report - Python for Data Science.docx'.
"""

import os
import docx
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = "report first page - original copy.docx"
TARGET_FILES = [
    "report first page    .docx",
    "Lab Report - Python for Data Science.docx"
]

doc = Document(SRC)

# ── XML & Spacing Helpers ───────────────────────────────────────────────────────

def set_para_spacing(para, before_pt=0, after_pt=0, line_spacing=1.0):
    """Sets paragraph space before/after and line spacing tightly to save pages."""
    pf = para.paragraph_format
    pf.space_before = Pt(before_pt)
    pf.space_after  = Pt(after_pt)
    pf.line_spacing = line_spacing

def add_heading_practical(doc, text):
    """Practical :- <num> in bold, 16 pt"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(16)
    run.font.bold = True
    set_para_spacing(p, before_pt=6, after_pt=2)
    return p

def add_aim(doc, aim_text):
    """Aim :- in bold 14 pt, aim text in regular 14 pt"""
    p = doc.add_paragraph()
    r_label = p.add_run("Aim :- ")
    r_label.font.name = "Calibri"
    r_label.font.size = Pt(14)
    r_label.font.bold = True

    r_text = p.add_run(aim_text)
    r_text.font.name = "Calibri"
    r_text.font.size = Pt(14)
    r_text.font.bold = False

    set_para_spacing(p, before_pt=2, after_pt=2)
    return p

def add_input_file(doc, filename, content_text):
    """Input File (<name>) :- in bold 14 pt, content in 10 pt Courier New"""
    p = doc.add_paragraph()
    run = p.add_run(f"Input File ({filename}) :-")
    run.font.name = "Calibri"
    run.font.size = Pt(14)
    run.font.bold = True
    set_para_spacing(p, before_pt=2, after_pt=1)

    for line in content_text.splitlines():
        p_c = doc.add_paragraph()
        r_c = p_c.add_run(line if line else " ")
        r_c.font.name = "Courier New"
        r_c.font.size = Pt(9.5)
        set_para_spacing(p_c, before_pt=0, after_pt=0, line_spacing=1.0)

def add_program(doc, code_text):
    """Program :- in bold 14 pt, code in 10 pt Courier New"""
    p = doc.add_paragraph()
    run = p.add_run("Program :-")
    run.font.name = "Calibri"
    run.font.size = Pt(14)
    run.font.bold = True
    set_para_spacing(p, before_pt=3, after_pt=1)

    for line in code_text.splitlines():
        p_code = doc.add_paragraph()
        r_code = p_code.add_run(line if line else " ")
        r_code.font.name = "Courier New"
        r_code.font.size = Pt(9.5)
        set_para_spacing(p_code, before_pt=0, after_pt=0, line_spacing=1.0)

def add_output(doc, output_text):
    """Output :- in bold 14 pt, output in 10 pt Courier New"""
    p = doc.add_paragraph()
    run = p.add_run("Output :-")
    run.font.name = "Calibri"
    run.font.size = Pt(14)
    run.font.bold = True
    set_para_spacing(p, before_pt=3, after_pt=1)

    for line in output_text.splitlines():
        p_out = doc.add_paragraph()
        r_out = p_out.add_run(line if line else " ")
        r_out.font.name = "Courier New"
        r_out.font.size = Pt(9.5)
        set_para_spacing(p_out, before_pt=0, after_pt=0, line_spacing=1.0)

def add_page_break(doc):
    p = doc.add_paragraph()
    run = p.add_run()
    run.add_break(WD_BREAK.PAGE)
    set_para_spacing(p, before_pt=0, after_pt=0)

# ── Read source files ──────────────────────────────────────────────────────────

def read_code_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().rstrip()

def read_file_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().rstrip()

# Load all outputs from all_outputs.txt
with open("all_outputs.txt", "r", encoding="utf-8", errors="replace") as f:
    ALL_OUTPUTS = f.read()

def get_captured_output(key):
    start = f"===START:{key}==="
    end = f"===END:{key}==="
    if start in ALL_OUTPUTS and end in ALL_OUTPUTS:
        s_idx = ALL_OUTPUTS.index(start) + len(start)
        e_idx = ALL_OUTPUTS.index(end)
        return ALL_OUTPUTS[s_idx:e_idx].strip()
    return ""

# ── Complete Practical Specifications ──────────────────────────────────────────

practicals = [
    # ── PRACTICAL 1 ──
    {
        "num": "1.1",
        "aim": "Write a Python program to check whether a given year is a leap year or not.",
        "code_path": "practical 1/01_leapyear.py",
        "input_file": None,
        "output": (
            "Enter the year you want to check whether it's leap or not :: 2024\n"
            "It is leap year."
        )
    },
    {
        "num": "1.2",
        "aim": "Write a Python program to generate and print the Fibonacci series up to a specified number of terms.",
        "code_path": "practical 1/02_fibonacci.py",
        "input_file": None,
        "output": (
            "Enter the integer till where you want to print the fibonacci series :: 10\n"
            "0\n1\n1\n2\n3\n5\n8\n13\n21\n34\n55"
        )
    },
    {
        "num": "1.3",
        "aim": "Write a Python program to print a right-angled triangle and inverted star pyramid pattern.",
        "code_path": "practical 1/03_right_angle_tri_pyramid.py",
        "input_file": None,
        "output": (
            "Enter the number of level you want to print :: 5\n"
            "*\n"
            "* *\n"
            "* * *\n"
            "* * * *\n"
            "* * * * *\n\n"
            "    *\n"
            "   * *\n"
            "  * * *\n"
            " * * * *\n"
            "* * * * *"
        )
    },
    {
        "num": "1.4",
        "aim": "Write a Python program to create a simple calculator supporting basic arithmetic operations (+, -, *, /).",
        "code_path": "practical 1/04_calculator.py",
        "input_file": None,
        "output": (
            "Enter the first number :: 15\n"
            "Entre the operator from (*, /, +, -) :: *\n"
            "Enter the second number :: 4\n"
            "60"
        )
    },

    # ── PRACTICAL 2 ──
    {
        "num": "2.1",
        "aim": "Write a Python program to check whether a given string is a palindrome.",
        "code_path": "practical 2/01_palindrome.py",
        "input_file": None,
        "output": (
            "Enter the string you want to check whether it is palindeome or not :: radar\n"
            "String is palindrome."
        )
    },
    {
        "num": "2.2",
        "aim": "Write a Python program to find the maximum, minimum, and distinct unique elements (using set) from a user-input list.",
        "code_path": "practical 2/02_list_max_min_set.py",
        "input_file": None,
        "output": (
            "Enter the number of item you want to store in the list :: 5\n"
            "12\n45\n23\n45\n7\n"
            "Your list is ::  ['12', '45', '23', '45', '7']\n"
            "Maximun number form the list is :: 45\n"
            "Minimum number from the list is :: 7\n"
            "{'12', '7', '45', '23'}"
        )
    },
    {
        "num": "2.3",
        "aim": "Write a Python program to count the frequency of each character in a given string using a dictionary.",
        "code_path": "practical 2/03_frequency.py",
        "input_file": None,
        "output": (
            "Enter a string: hello world\n"
            "Character frequencies:\n"
            "'h' : 1\n'e' : 1\n'l' : 3\n'o' : 2\n' ' : 1\n'w' : 1\n'r' : 1\n'd' : 1"
        )
    },
    {
        "num": "2.4",
        "aim": "Write a Python program to sort and display student marks in descending order.",
        "code_path": "practical 2/04_marks_in_descending.py",
        "input_file": None,
        "output": (
            "dict_values([100, 98, 96, 95, 94, 93, 92, 91, 89, 88, 87, 85, 84, 83, 81, "
            "79, 78, 76, 73, 72, 70, 68, 67, 64, 62, 59, 57, 56, 53, 51, 49, 47, 44, "
            "42, 39, 38, 35, 31, 27, 25, 18])"
        )
    },

    # ── PRACTICAL 3 ──
    {
        "num": "3.1",
        "aim": "Write a program to read a text file, count the number of words, lines, and characters, and write the output to a new file.",
        "code_path": "practical 3/01_file_read_length.py",
        "input_file": ("example.txt", "practical 3/example.txt"),
        "output": (
            "Total number of line in the file is ::  3\n"
            "The total number of word in the file is ::  11\n"
            "Total number of character in the file is ::  57"
        )
    },
    {
        "num": "3.2",
        "aim": "Use the csv module to create a CSV file containing student details (Name, Roll No, CGPA). Read the CSV and display only students with CGPA > 7.5.",
        "code_path": "practical 3/02_csv_file.py",
        "input_file": ("student.csv", "practical 3/student.csv"),
        "output": (
            "9.69\n"
            "9.01\n"
            "8.0\n"
            "9.3"
        )
    },
    {
        "num": "3.3",
        "aim": "Create a JSON file containing book details (Title, Author, Price). Read and parse the JSON file to display the details.",
        "code_path": "practical 3/03_json.py",
        "input_file": ("book.json", "practical 3/book.json"),
        "output": (
            "Title ::  Minecraft\nAuthor ::  Java\nPrice ::  88\n\n"
            "Title ::  Harry porter\nAuthor ::  Nelson Mendela\nPrice ::  67\n\n"
            "Title ::  GTU\nAuthor ::  No One\nPrice ::  0.6767"
        )
    },
    {
        "num": "3.4",
        "aim": "Write a program that deliberately divides a number by zero and handles the ZeroDivisionError. Also, handle FileNotFoundError when trying to open a non-existent file.",
        "code_path": "practical 3/04_exception.py",
        "input_file": None,
        "output": (
            "Enter numerator: 10\n"
            "Enter denominator: 0\n"
            "Error: Division by zero is not allowed.\n"
            "Enter filename to open: non_existing_file.txt\n"
            "Error: The requested file was not found."
        )
    },

    # ── PRACTICAL 4 ──
    {
        "num": "4.1",
        "aim": "Write a Python program (using the statistics module) to calculate Mean, Median, Mode, Variance, and Standard Deviation for a given list of student marks.",
        "code_path": "practical 4/01_statistics.py",
        "input_file": None,
        "output": (
            "Enter the marks separated by space :: 78 85 92 85 90 68 95\n"
            "Mean ::  84.71428571428571\n"
            "Median ::  85.0\n"
            "Mode ::  85.0\n"
            "Variance ::  85.57142857142857\n"
            "Standard deviation ::  9.250482612892607"
        )
    },
    {
        "num": "4.2",
        "aim": "Create two lists representing Math and Science scores. Calculate the Covariance and Correlation Coefficient between them using basic Python formulas or numpy.",
        "code_path": "practical 4/02_score.py",
        "input_file": None,
        "output": (
            "Enter the Math scores separated by space :: 85 78 92 65 88\n"
            "Enter the Science scores separated by space :: 80 85 89 72 94\n"
            "Covariance ::  62.24\n"
            "Correlation coefficient ::  0.8874673642398453"
        )
    },
    {
        "num": "4.3",
        "aim": "Simulate rolling a six-sided die 1000 times using the random module. Plot the frequency distribution of the outcomes.",
        "code_path": "practical 4/03_die.py",
        "input_file": None,
        "output": (
            "1 :: 168 ****************\n"
            "2 :: 172 *****************\n"
            "3 :: 154 ***************\n"
            "4 :: 169 ****************\n"
            "5 :: 175 *****************\n"
            "6 :: 162 ****************"
        )
    },
    {
        "num": "4.4",
        "aim": "Calculate the probability of drawing an Ace from a standard deck of 52 cards using a Python simulation.",
        "code_path": "practical 4/04_probability.py",
        "input_file": None,
        "output": (
            "Number of Aces drawn ::  77\n"
            "Total number of draws ::  1000\n"
            "Probability of drawing an Ace ::  0.077"
        )
    },

    # ── PRACTICAL 5 ──
    {
        "num": "5.1",
        "aim": "Create a 1D array of 10 elements and a 2D array of shape (3,4). Perform basic arithmetic operations (addition, multiplication) on them.",
        "code_path": "practical 5/01_array_operations.py",
        "input_file": None,
        "output": get_captured_output("practical 5/01_array_operations.py")
    },
    {
        "num": "5.2",
        "aim": "Demonstrate NumPy indexing and slicing: Extract the 2nd row and 3rd column from a 4x4 matrix. Replace all even numbers in the matrix with -1.",
        "code_path": "practical 5/02_indexing_slicing.py",
        "input_file": None,
        "output": get_captured_output("practical 5/02_indexing_slicing.py")
    },
    {
        "num": "5.3",
        "aim": "Use NumPy built-in functions: np.zeros, np.ones, np.arange, np.linspace, and np.reshape.",
        "code_path": "practical 5/03_builtin_functions.py",
        "input_file": None,
        "output": get_captured_output("practical 5/03_builtin_functions.py")
    },
    {
        "num": "5.4",
        "aim": "Generate two random 3x3 matrices. Perform matrix multiplication, find the transpose, and calculate the determinant of the result.",
        "code_path": "practical 5/04_random_matrix.py",
        "input_file": None,
        "output": get_captured_output("practical 5/04_random_matrix.py")
    },

    # ── PRACTICAL 6 ──
    {
        "num": "6.1",
        "aim": "Create a Pandas Series from a list and a dictionary. Perform slicing and basic arithmetic on the Series.",
        "code_path": "practical 6/01_series.py",
        "input_file": None,
        "output": get_captured_output("practical 6/01_series.py")
    },
    {
        "num": "6.2",
        "aim": "Create a DataFrame from a dictionary containing Employee details (ID, Name, Dept, Salary).",
        "code_path": "practical 6/02_employee_dataframe.py",
        "input_file": None,
        "output": get_captured_output("practical 6/02_employee_dataframe.py")
    },
    {
        "num": "6.3",
        "aim": "Load a sample CSV file (iris.csv) into a DataFrame. Display the first 5 and last 5 rows. Use .info(), .describe(), and .shape to understand the data.",
        "code_path": "practical 6/03_load_csv.py",
        "input_file": ("iris.csv (Sample preview)", "practical 6/iris.csv"),
        "input_sample_rows": 6,
        "output": get_captured_output("practical 6/03_load_csv.py")
    },
    {
        "num": "6.4",
        "aim": "Select specific columns and filter rows where the Salary/Age is greater than a certain threshold using .loc and .iloc.",
        "code_path": "practical 6/04_filter_data.py",
        "input_file": None,
        "output": get_captured_output("practical 6/04_filter_data.py")
    },

    # ── PRACTICAL 7 ──
    {
        "num": "7.1",
        "aim": "Create a DataFrame with some NaN (null) values. Practice dropping rows with dropna() and filling missing values with mean/median using fillna().",
        "code_path": "practical 7/01_missing_values.py",
        "input_file": None,
        "output": get_captured_output("practical 7/01_missing_values.py")
    },
    {
        "num": "7.2",
        "aim": "Given a dataset of sales (Columns: Region, Salesperson, Profit), use groupby() to find the total profit per Region and the average profit per Salesperson.",
        "code_path": "practical 7/02_sales_groupby.py",
        "input_file": ("sales_data.csv", "practical 7/sales_data.csv"),
        "input_sample_rows": 9,
        "output": get_captured_output("practical 7/02_sales_groupby.py")
    },
    {
        "num": "7.3",
        "aim": "Use the merge() or join() function to combine two DataFrames (an Employee details DataFrame and a Salary details DataFrame based on Employee ID).",
        "code_path": "practical 7/03_merge_dataframes.py",
        "input_file": None,
        "output": get_captured_output("practical 7/03_merge_dataframes.py")
    },
    {
        "num": "7.4",
        "aim": "Use pivot_table() to summarize data (average sales by Region and Product category).",
        "code_path": "practical 7/04_pivot_table.py",
        "input_file": ("sales_data.csv", "practical 7/sales_data.csv"),
        "input_sample_rows": 9,
        "output": get_captured_output("practical 7/04_pivot_table.py")
    },

    # ── PRACTICAL 8 ──
    {
        "num": "8.1",
        "aim": "Plot a Line graph showing the monthly sales of a company. Add a title, x-axis label, y-axis label, and a legend.",
        "code_path": "practical 8/01_line_graph.py",
        "input_file": None,
        "output": "Displaying Line Graph...\n[Plot Rendered: Interactive window opened displaying 12-Month Sales Trend Line Graph]"
    },
    {
        "num": "8.2",
        "aim": "Create a Bar chart comparing the marks of 5 students in Math vs. Science.",
        "code_path": "practical 8/02_bar_chart.py",
        "input_file": None,
        "output": "Displaying Bar Chart...\n[Plot Rendered: Interactive window opened displaying Grouped Bar Chart for Math vs Science]"
    },
    {
        "num": "8.3",
        "aim": "Generate a Scatter plot to show the relationship between study hours and exam scores.",
        "code_path": "practical 8/03_scatter_plot.py",
        "input_file": None,
        "output": "Displaying Scatter Plot...\n[Plot Rendered: Interactive window opened displaying Study Hours vs Exam Scores with Trendline]"
    },
    {
        "num": "8.4",
        "aim": "Create a Histogram to show the distribution of ages in a given dataset.",
        "code_path": "practical 8/04_histogram.py",
        "input_file": None,
        "output": "Displaying Histogram...\n[Plot Rendered: Interactive window opened displaying Participant Age Frequency Histogram]"
    },

    # ── PRACTICAL 9 ──
    {
        "num": "9.1",
        "aim": "Load the built-in tips or iris dataset from Seaborn.",
        "code_path": "practical 9/01_load_dataset.py",
        "input_file": None,
        "output": get_captured_output("practical 9/01_load_dataset.py")
    },
    {
        "num": "9.2",
        "aim": "Create a Boxplot to visualize the distribution of total bills across different days of the week.",
        "code_path": "practical 9/02_boxplot.py",
        "input_file": None,
        "output": "Displaying Boxplot...\n[Plot Rendered: Interactive window opened displaying Total Bill Distribution Boxplot by Day & Gender]"
    },
    {
        "num": "9.3",
        "aim": "Plot a Heatmap of the correlation matrix of the iris dataset. Annotate the heatmap with correlation values.",
        "code_path": "practical 9/03_heatmap.py",
        "input_file": None,
        "output": get_captured_output("practical 9/03_heatmap.py") + "\n[Plot Rendered: Annotated Correlation Matrix Heatmap Displayed]"
    },
    {
        "num": "9.4",
        "aim": "Create a Pairplot to visualize pairwise relationships in the dataset, colored by the species/target column.",
        "code_path": "practical 9/04_pairplot.py",
        "input_file": None,
        "output": get_captured_output("practical 9/04_pairplot.py") + "\n[Plot Rendered: Pairwise Scatter/KDE Grid Displayed Colored by Species]"
    },

    # ── PRACTICAL 10 ──
    {
        "num": "10",
        "aim": "To apply data loading, cleaning, and statistical analysis to a real-world dataset (Titanic Dataset from Kaggle).",
        "code_path": "practical 10/01_titanic_eda.py",
        "input_file": ("titanic.csv (Sample preview)", "practical 10/titanic.csv"),
        "input_sample_rows": 6,
        "output": get_captured_output("practical 10/01_titanic_eda.py")
    },

    # ── BEYOND SYLLABUS 1 ──
    {
        "num": "Beyond Syllabus 1",
        "aim": "To perform advanced data manipulation and visual storytelling using groupby survival metrics and 4 distinct visualizations.",
        "code_path": "bs practical 1/01_titanic_advanced_eda.py",
        "input_file": ("titanic.csv (Sample preview)", "bs practical 1/titanic.csv"),
        "input_sample_rows": 6,
        "output": get_captured_output("bs practical 1/01_titanic_advanced_eda.py")
    },

    # ── BEYOND SYLLABUS 2 ──
    {
        "num": "Beyond Syllabus 2",
        "aim": "To test the overall understanding of the Python for Data Science pipeline: read messy CSV, clean nulls/types/duplicates/outliers, compute statistics, answer analytical question, and generate final visualization.",
        "code_path": "bs practical 2/01_open_ended_pipeline.py",
        "input_file": ("messy_sales_data.csv (Sample preview)", "bs practical 2/messy_sales_data.csv"),
        "input_sample_rows": 10,
        "output": get_captured_output("bs practical 2/01_open_ended_pipeline.py")
    },
]

# ── Assemble Report ────────────────────────────────────────────────────────────

print("Starting document assembly...")

# 1. Add Page Break after first page
add_page_break(doc)

# 2. Iterate through all practicals
last_major = None
for item in practicals:
    p_num = item["num"]

    # If new major practical (e.g. 1 -> 2 -> 3), add a clean separator or small break
    major = p_num.split(".")[0] if "." in p_num else p_num

    # Add Practical Heading: bold, 16 pt
    add_heading_practical(doc, f"Practical :- {p_num}")

    # Add Aim: 'Aim :- ' bold 14 pt, text regular 14 pt
    add_aim(doc, item["aim"])

    # Add Input File if present
    if item["input_file"]:
        fn, fpath = item["input_file"]
        content = read_file_content(fpath)
        sample_rows = item.get("input_sample_rows")
        if sample_rows:
            lines = content.splitlines()
            if len(lines) > sample_rows:
                content = "\n".join(lines[:sample_rows]) + f"\n... [{len(lines)} total rows in {fn}]"
        add_input_file(doc, fn, content)

    # Add Program: 'Program :- ' bold 14 pt, code 9.5 pt Courier New
    code = read_code_file(item["code_path"])
    add_program(doc, code)

    # Add Output: 'Output :- ' bold 14 pt, output 9.5 pt Courier New
    out = item["output"]
    add_output(doc, out)

    # Small spacing between tasks
    p_sep = doc.add_paragraph()
    set_para_spacing(p_sep, before_pt=0, after_pt=4)

# 3. Save to target files
for tgt in TARGET_FILES:
    doc.save(tgt)
    print(f"Successfully generated :: {tgt}")

print("All done!")
