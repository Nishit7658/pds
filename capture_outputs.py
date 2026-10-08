import subprocess, sys, os

scripts = [
    ("practical 5", "01_array_operations.py"),
    ("practical 5", "02_indexing_slicing.py"),
    ("practical 5", "03_builtin_functions.py"),
    ("practical 5", "04_random_matrix.py"),
    ("practical 6", "01_series.py"),
    ("practical 6", "02_employee_dataframe.py"),
    ("practical 6", "03_load_csv.py"),
    ("practical 6", "04_filter_data.py"),
    ("practical 7", "01_missing_values.py"),
    ("practical 7", "02_sales_groupby.py"),
    ("practical 7", "03_merge_dataframes.py"),
    ("practical 7", "04_pivot_table.py"),
    ("practical 8", "01_line_graph.py"),
    ("practical 8", "02_bar_chart.py"),
    ("practical 8", "03_scatter_plot.py"),
    ("practical 8", "04_histogram.py"),
    ("practical 9", "01_load_dataset.py"),
    ("practical 9", "02_boxplot.py"),
    ("practical 9", "03_heatmap.py"),
    ("practical 9", "04_pairplot.py"),
    ("practical 10", "01_titanic_eda.py"),
    ("bs practical 1", "01_titanic_advanced_eda.py"),
    ("bs practical 2", "01_open_ended_pipeline.py"),
]

env = os.environ.copy()
env["MPLBACKEND"] = "Agg"

for folder, script in scripts:
    path = os.path.join(folder, script)
    result = subprocess.run([sys.executable, path], capture_output=True, text=True, env=env)
    output = result.stdout.strip()
    key = f"{folder}/{script}"
    # Print separator + key + output
    print(f"===START:{key}===")
    print(output)
    print(f"===END:{key}===")
