#!/bin/bash

# Define the root directory
root_dir="ClassificationofMangoDiseases"

# Define the directory structure
directories=(
    "$root_dir/documents/references"
    "$root_dir/documents/usage"
    "$root_dir/documents/reports"
)

# Create directories
for dir in "${directories[@]}"; do
    mkdir -p "$dir"
done

# Define the files with their paths
files=(
    "$root_dir/documents/references/reference1.pdf"
    "$root_dir/documents/usage/usage1.pdf"
    "$root_dir/documents/reports/report_v0.pdf"
    "$root_dir/documents/reports/report_v0.docx"
    "$root_dir/documents/reports/report_v0.pptx"
)

# Create files and add "TODO" content
for file in "${files[@]}"; do
    echo "TODO" > "$file"
done

echo "Directory structure created successfully."
