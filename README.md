🛒 Retail Sales 2019 Pipeline

A complete ETL + Visualization pipeline for April 2019 retail sales data.
This project cleans raw CSV data, performs feature engineering, and generates 5 advanced visualizations with Plotly.

📂 Project Structure
retail-sales-2019-pipeline/
├─ 01_data/
│  ├─ raw/                     # Place Sales_April_2019.csv here
│  └─ processed/               # Cleaned data saved here
├─ 02_scripts/
│  ├─ o1_preprocessing.py      # Data cleaning + feature engineering
│  └─ o2_analysis_and_viz.py   # Analysis + visualizations
├─ 03_visualizations_final/    # Auto-generated PNG charts
⚡ Features

✅ Data Cleaning (remove nulls, fix types, drop duplicate headers)
✅ Feature Engineering (Sales, City, Hour)
✅ Correlation Heatmap (numeric features)
✅ Violin Plot (Top 5 product sales distribution)
✅ Choropleth Map (sales by US state)
✅ Waterfall Chart (city-wise sales contribution)
✅ 3D Scatter Plot (Price vs Quantity vs Hour)

🔧 Setup & Installation

Clone repo

git clone https://github.com/Narendran-ds/retail-sales-2019-pipeline.git
cd retail-sales-2019-pipeline

Install dependencies

pip install -r requirements.txt

Add raw data
Place your Sales_April_2019.csv inside 01_data/raw/.

🚀 Usage
1️⃣ Preprocess Data
python 02_scripts/o1_preprocessing.py

➡ Generates: 01_data/processed/cleaned_sales.parquet

2️⃣ Run Analysis & Visualizations
python 02_scripts/o2_analysis_and_viz.py

➡ Saves 5 PNG charts into 03_visualizations_final/

📊 Example Visuals

Correlation Heatmap

Sales Distribution (Violin Plot)

State-wise Sales (Choropleth)

City Sales Contribution (Waterfall)

3D Scatter (Price vs Quantity vs Hour)

(Check the /03_visualizations_final/ folder after running)

🛠 Tech Stack

Python 3.10+

pandas (data wrangling)

plotly + kaleido (interactive & exportable visualizations)

pyarrow (fast parquet I/O)

🌟 Why this project?

This repo shows how to go from raw sales data ➝ insights ➝ business-ready charts in a reproducible pipeline.
It’s a great starter for anyone learning ETL, EDA, and Visualization in Python.

👨‍💻 Author

Narendran L


🌐 Portfolio/Projects: https://github.com/Narendran-ds

💼 LinkedIn: www.linkedin.com/in/narendran-l1125

📧 Email: narendranlofficial@gmail.com


✨ Feel free to fork, star ⭐, or open issues for improvements!
