#!/bin/bash

mkdir -p csv

echo "Data to csv"
python3 base_csv.py

mkdir -p html
# Needs pip install -U kaleido
mkdir -p images

echo "Create boxplot"
python3 boxplot_overhead.py

echo "Create lineplot"
python3 line_base_overhead.py

echo "Create barplot"
python3 bar_base_overhead.py