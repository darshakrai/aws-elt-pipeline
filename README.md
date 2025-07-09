# AWS ELT Data Pipeline

This project implements an end-to-end ELT pipeline using AWS S3, Glue, and Redshift Serverless.

## Components Used
- AWS S3 (Raw data layer)
- AWS Glue (Transform & Load)
- Redshift Serverless (Query & Analytics)
- IAM, VPC, Secrets Manager

## Steps
1. Raw booking data uploaded to S3 (`booking_raw/`)
2. AWS Glue job transforms and filters data (`tickets > 1`)
3. Cleaned data loaded into Redshift table `booking_clean`
4. IAM role with Glue and Redshift access
5. Redshift queries enable downstream analytics

## Sample Glue Script
See `glue_job_script.py`

---


