import gc
import os
import time
import pandas as pd
import logging

file_path = "data/video_game_market.csv"
required_cols = ["genre", "platform", "current_price_usd", "revenue_cumulative"]

# Get exact raw file size on disk for baseline reference
file_size_bytes = os.path.getsize(file_path)
file_size_mb = file_size_bytes / (1024**2)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("outputs/benchmark_performance.log"),  # Saves to file
        logging.StreamHandler(),  # Also prints to terminal
    ],
)

logging.info("Starting Baseline Benchmark Test...")
logging.info(f"Raw File Size on Disk: {file_size_bytes:,} Bytes ({file_size_mb:.2f} MB)")
logging.info("=" * 60)

# ---------------------------------------------------------
# STEP 1: WITHOUT Column Pruning (Full 130 Columns)
# ---------------------------------------------------------
logging.info("1. Testing FULL dataset loading (130 columns)...")
full_dataset_failed = False
mem_full = None
time_full = None

try:
    start_full = time.time()
    df_full = pd.read_csv(file_path, low_memory=False)
    time_full = time.time() - start_full
    mem_full = df_full.memory_usage(deep=True).sum()

    logging.info(f"   [SUCCESS] Loaded in {time_full:.2f} seconds")
    logging.info(f"   [RAM Usage] {mem_full:,} Bytes ({mem_full / (1024**2):.2f} MB)")

    del df_full
    gc.collect()

except (MemoryError, pd.errors.ParserError) as e:
    full_dataset_failed = True
    logging.info("   [CRASH] OutOfMemoryError / ParserError!")
    logging.info("   -> Single-node Pandas ran out of RAM reading 130 columns.")

gc.collect()

# ---------------------------------------------------------
# STEP 2: WITH Column Pruning (4 Selected Columns)
# ---------------------------------------------------------
logging.info("2. Testing PRUNED dataset loading (4 columns)...")
start_pruned = time.time()

df_pruned = pd.read_csv(file_path, usecols=required_cols)

time_pruned = time.time() - start_pruned
mem_pruned = df_pruned.memory_usage(deep=True).sum()

logging.info(f"   [SUCCESS] Loaded in {time_pruned:.2f} seconds")
logging.info(f"   [RAM Usage] {mem_pruned:,} Bytes ({mem_pruned / (1024**2):.2f} MB)")

del df_pruned
gc.collect()

# ---------------------------------------------------------
# PRINT FINAL BENCHMARK SUMMARY FOR REPORT
# ---------------------------------------------------------
logging.info("=" * 60)
logging.info("             BENCHMARK RESULTS & MEMORY ANALYSIS           ")
logging.info("=" * 60)

logging.info(f"Raw CSV Disk Size : {file_size_bytes:,} Bytes ({file_size_mb:.2f} MB)")

if full_dataset_failed:
    logging.info("[Without Column Pruning - 130 Columns]")
    logging.info("Status         : FAILED (Memory Exhaustion / OutOfMemoryError)")
    logging.info("RAM Allocated  : > Available Machine Memory Limit")

    logging.info("[With Column Pruning - 4 Columns]")
    logging.info(f"Execution Time : {time_pruned:.2f} seconds")
    logging.info(
        f"RAM Allocated  : {mem_pruned:,} Bytes ({mem_pruned / (1024**2):.2f} MB)"
    )

    logging.info("=" * 60)
    logging.info("KEY TAKEAWAY FOR REPORT:")
    logging.info(
        "Column pruning reduced memory allocation enough to prevent a fatal "
    )
    logging.info("C-engine parser crash, enabling processing on a single machine.")
    logging.info("=" * 60)

else:
    mem_saved_bytes = mem_full - mem_pruned
    pct_saved = (mem_saved_bytes / mem_full) * 100

    logging.info("[Without Column Pruning - 130 Columns]")
    logging.info(f"Execution Time : {time_full:.2f} seconds")
    logging.info(
        f"RAM Allocated  : {mem_full:,} Bytes ({mem_full / (1024**2):.2f} MB)"
    )

    logging.info("[With Column Pruning - 4 Columns]")
    logging.info(f"Execution Time : {time_pruned:.2f} seconds")
    logging.info(
        f"RAM Allocated  : {mem_pruned:,} Bytes ({mem_pruned / (1024**2):.2f} MB)"
    )

    logging.info("=" * 60)
    logging.info(
        f"Memory Saved     : {mem_saved_bytes:,} Bytes ({mem_saved_bytes / (1024**2):.2f} MB)"
    )
    logging.info(f"Memory Reduction : {pct_saved:.2f}%")
    logging.info("=" * 60)