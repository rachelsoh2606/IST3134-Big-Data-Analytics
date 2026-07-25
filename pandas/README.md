# Video Game Market Analytics (Pandas Baseline Model)

> **Module:** Comparative Single-Node Baseline 
>
> **Framework:** Python / Pandas 
>
> **Project:** IST3134 Big Data Analytics - Video Game Market Performance Analysis

---

## 📌 Module Overview & Baseline Role
This directory contains the **traditional, single-machine baseline model** for the Video Game Market Performance Analysis project. 

In this module, **Pandas** is utilized as a comparative benchmark against the distributed **Apache Spark (`/pyspark`)** solution. The primary purpose of this baseline is to:
1. Establish standard analytical outputs (revenue rankings, pricing trends, and genre-platform aggregation).
2. Measure single-node performance, execution timing, and memory overhead when processing multi-gigabyte datasets.
3. Demonstrate the effectiveness and limitations of single-machine optimization techniques (such as **column pruning**) before scaling to distributed cluster processing.

### Repository Structure
Below is the directory tree for this repository:

```text
C:.
│   .gitattributes
│   column_pruning_comparison.py
│   pandas_baseline.py
│   README.md
│   structure.txt
|   requirements.txt
│   
├───data
│       video_game_market.csv
│       
└───outputs
        benchmark_performance.log
        genre_revenue_chart.png
        pandas_market_analysis.csv
        platform_revenue_chart.png
```

---

## Objectives
- **Income Trend Analysis:** Identify key revenue trends and market performance patterns across diverse gaming genres and platforms.
- **Big Data Benchmarking:** Benchmark single-machine data manipulation using Pandas against distributed cluster processing via Apache Spark.
- **Optimization Strategy:** Evaluate optimization techniques such as column pruning and memory management to process large-scale dataset inputs efficiently.

---
## Analytical Workflow & Implementation

### 1. Data Loading & Memory Optimization (Column Pruning)
The raw dataset contains 130 attributes (~4.75 GB). To optimize single-machine memory consumption and execution speed, column pruning was implemented to retain only the 4 required attributes (`genre`, `platform`, `current_price_usd`, and `revenue_cumulative`).

| Loading Strategy | Number of Attributes | Execution Time | Memory Usage |
| :--- | :---: | :---: | :---: |
| **Without Column Pruning** | 130 | 130.42 s | 11.39 GB |
| **With Column Pruning** | 4 | 48.96 s | 708.14 MB |

* **Memory Savings:** ~93.78% reduction (~11.39 GB down to ~708 MB).
* **Time Savings:** ~81.46 seconds faster during initial file parsing.

---

### 2. Market Analysis Focus Areas
Using Pandas `groupby` aggregations, the codebase performs four key market evaluations:

* **Market Revenue by Game Genre:** Aggregates cumulative revenue to identify top-performing genres and profitable market segments.
* **Market Revenue by Gaming Platform:** Summarizes cumulative revenue by supported platform to evaluate consumer purchasing preferences.
* **Pricing Pattern Analysis across Genres:** Calculates average selling prices (`current_price_usd`) across genres to examine pricing strategies and positioning.
* **Genre-Platform Performance Summary:** Performs multi-attribute aggregation to compute total revenue, average price, and total game count per genre-platform pair.

---

### 3. Analytics Output Summary
Execution of `pandas_baseline.py` automatically generates structured logs and visual artifacts stored in the `outputs/` folder:
- `pandas_market_analysis.csv`: Detailed summary table with aggregated metrics across genres and platforms.
- `genre_revenue_chart.png` & `platform_revenue_chart.png`: Visual representations of market revenue distributions.
- `benchmark_performance.log`: Memory and execution time logs.


## Getting Started 

### Cloning the Repository
To clone this repository to your local machine, run:

```bash
git clone https://github.com/rachelsoh2606/IST3134-Big-Data-Analytics.git
cd <repository-folder>
```

> [!IMPORTANT]
> **Notice Regarding `/data/video_game_market.csv` (~672 MB):**
> 
> During execution of `git clone`, the terminal process may appear to pause or hang at:
> ```text
> Updating files: 100% (9/9), done.
> — OR —
> Resolving deltas: 100% (12/12), done.
> ```
> This occurs because Git is actively unpacking and checking out the large dataset file (`/data/video_game_market.csv`). **This behavior is expected.** Please allow the command to run uninterrupted until the terminal prompt returns.

---

## Prerequisites & Setup

### Prerequisites
- **Operating System:** Windows 10/11, macOS, or Linux
- **Python Version:** Python 3.8+ recommended

### Installation & Environment Setup

1. **Create a Virtual Environment:**
   ```bash
   # Windows (Command Prompt)
   python -m venv venv
   
   # Windows (PowerShell)
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**
   ```bash
   # Windows (Command Prompt)
   venv\Scripts\activate
   
   # Windows (PowerShell)
   .\venv\Scripts\activate.ps1
   
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis
```bash
# Execute memory optimization benchmark
python column_pruning_comparison.py

# Execute full market analysis baseline
python pandas_baseline.py
```
