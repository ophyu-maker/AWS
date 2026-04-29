# AWS Fisheries Data Pipeline Capstone

AWS data pipeline case study using S3, Glue, Athena, and Parquet

## Project Overview

This project was completed for my Database Management / Data Engineering capstone course. The goal was to build an end-to-end cloud-based data pipeline using AWS services to ingest, transform, catalog, and query fisheries data from the "Sea Around Us" dataset.

The pipeline converts CSV files into Apache Parquet format, stores the transformed files in Amazon S3, uses AWS Glue to infer schema metadata, and uses Amazon Athena to run SQL queries for analysis.

## Business Problem

The project scenario was to create infrastructure that allows analysts to query fishing activity across open seas and Exclusive Economic Zones (EEZs). The analysis focused on Fiji fishing activity and mackerel catch trends using multiple source files.

## Tools and Services Used

- AWS Cloud9
- Amazon S3
- AWS Glue Crawler
- AWS Glue Data Catalog
- Amazon Athena
- Python
- pandas
- pyarrow / fastparquet
- SQL

## Dataset

The project used publicly available Sea Around Us fisheries data. The dataset contains yearly fishing catch information including:

- Year
- Fishing country/entity
- Fishing area
- Catch weight in tonnes
- Landed value in 2010 USD
- Fish/common name

Source: Sea Around Us  
License: Creative Commons Attribution Non-Commercial 4.0 International License

## Pipeline Architecture

1. Downloaded CSV source files in AWS Cloud9.
2. Inspected file structure and column headers.
3. Converted CSV files to Apache Parquet using Python and pandas.
4. Uploaded Parquet files to an Amazon S3 data-source bucket.
5. Created an AWS Glue database and Glue crawler.
6. Ran the crawler to infer schema and create a metadata table.
7. Queried the dataset using Amazon Athena.
8. Created Athena views for reusable analysis.
9. Validated that open seas and EEZ query results reconciled correctly.

## Data Files Used

The project used three fisheries data files:

| File | Description |
|---|---|
| `SAU-GLOBAL-1-v48-0.csv` | Global high seas fishing data |
| `SAU-HighSeas-71-v48-0.csv` | Pacific, Western Central high seas data |
| `SAU-EEZ-242-v48-0.csv` | Fiji EEZ fishing data |

## Data Transformation

The source CSV files were converted to Parquet format to improve query efficiency and compatibility with AWS analytics tools.

For the EEZ file, two columns were renamed so the schema aligned with the existing dataset:

| Original Column | Renamed Column |
|---|---|
| `fish_name` | `common_name` |
| `country` | `fishing_entity` |

## Key SQL Analysis

The Athena queries answered questions such as:

- What distinct fishing areas exist in the combined dataset?
- What was the value of fish caught by Fiji from the Pacific, Western Central high seas area since 2001?
- What was the value of all fish caught by Fiji from all high seas areas since 2001?
- What was the value of fish caught by Fiji from open seas vs. Fiji EEZ?
- Do open seas catch value plus EEZ catch value reconcile to the combined total?
- Which countries had the highest mackerel catch by year?

## Validation Logic

To validate the pipeline, I compared three query outputs:

1. Fiji open seas catch value
2. Fiji EEZ catch value
3. Fiji open seas + EEZ catch value

The expected result was:

```text
ValueOpenSeasCatch + ValueEEZCatch = ValueEEZAndOpenSeasCatch
