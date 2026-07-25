# IST3134 Big Data Analytics: Video Game Market Performance Analysis

> **Course Assignment:** IST3134 - Big Data Analytics  
> **Authors:** Mok Qi Yeng & Rachel Soh En Qi (3rd Year)  
> **Topic:** Big Data Analytics For Video Game Market Performance Using Apache Spark: A Comparative Analysis with Pandas

---

## Project Overview
This project presents a comparative big data analytics study analyzing performance metrics across the global video game industry. As the gaming market generates vast volumes of data across platforms, genres, pricing strategies, and sales records, evaluating financial success requires scalable and efficient computational workflows.

To evaluate performance, execution efficiency, and resource scalability when processing multi-gigabyte datasets, this project implements two analytical solutions:
1. **Pandas Baseline (`/pandas`):** A traditional single-machine implementation establishing performance, memory, and analytical baselines.
2. **Apache Spark Solution (`/pyspark`):** A distributed big data processing engine designed to handle large-scale datasets across parallel execution nodes.

---

## High-Level Repository Architecture
This repository separates the single-machine comparative baseline from the distributed big data implementation into dedicated subdirectories:

```text
IST3134-Big-Data-Analytics/
│
├── README.md       <-- General Project Overview & High-Level Documentation
│
├── pandas/         <-- Single-Node Baseline (Pandas code, sub-README, & outputs)
│
└── pyspark/        <-- Distributed Big Data Engine (Apache Spark/PySpark code)
