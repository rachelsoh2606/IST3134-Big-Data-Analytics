# IST3134-Big-Data-Analytics: Big Data Analytics For Video Game Market Performance Using Apache Spark: A Comparative Analysis with Pandas
A group assignment for Mok Qi Yeng and Rachel Soh En Qi's 3rd year course: IST3134 - Big Data Analytics, titled Big Data Analytics For Video Game Market Performance Using Apache Spark: A Comparative Analysis with Pandas

## Project Overview
This repository provides a baseline data analytics solution designed to process and analyze video game market performance metrics using **Pandas**. Using structured data aggregation techniques, the project explores key revenue, pricing, and platform trends across large-scale video game market datasets.

This directory focuses specifically on single-machine processing, establishing an analytical and computational baseline. To evaluate distributed big data capabilities on the same dataset, refer to the **Apache Spark** implementation located in the designated separate folder (`/pyspark` or adjacent project folder).


---

## Repository Structure
Below is the directory tree for this repository:

```text
C:.
│   .gitattributes
│   column_pruning_comparison.py
│   pandas_baseline.py
│   README.md
│   structure.txt
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


## Getting Started & Cloning Notice

### Cloning the Repository
To clone this repository to your local machine, run:

```bash
git clone <repository-url>
cd <repository-folder>
```

> [!IMPORTANT]
> **Notice Regarding `/data/video_game_market.csv` (~672 MB):**
> 
> During execution of `git clone`, the terminal process may appear to pause or hang at:
> ```text
> Updating files: 100% (9/9), done.
> ```
> This occurs because Git is actively unpacking and checking out the large dataset file (`/data/video_game_market.csv`). **This behavior is expected.** Please allow the command to run uninterrupted until the terminal prompt returns.

---

## Prerequisites & Setup

<!-- TODO: Add prerequisites, required Python version, and dependency installation steps -->

### Prerequisites
- *[Placeholder: Add required OS / System specs]*
- *[Placeholder: Add required Python version, e.g., Python 3.8+]*
- *[Placeholder: Add required external software, e.g., Java / Apache Spark binaries]*

### Installation & Environment Setup
```bash
# [Placeholder: Environment setup command]
# e.g., python -m venv venv
# e.g., source venv/bin/activate  # On Windows: venv\Scripts\activate

# [Placeholder: Dependency installation command]
# e.g., pip install -r requirements.txt
```

### Running the Analysis
```bash
# [Placeholder: Script execution commands]
# e.g., python pandas_baseline.py
# e.g., python column_pruning_comparison.py
