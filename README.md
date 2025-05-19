# nomi-nom-user-tracking

Set up S3: Create your bucket and define data organization.
Choose Ingestion: Kinesis (high volume) or Lambda (lower volume).
Build FastAPI API: Create a Python API to receive events and send them to Kinesis/S3 using boto3. Deploy using ECS/EKS or Elastic Beanstalk.
(If using Kinesis) Configure Firehose: To move data from Kinesis to S3.
Set up Glue: Crawl S3 and create a Glue Catalog. Write Glue ETL jobs in Python (PySpark) to transform your data.
Use Athena: Query your data in S3 using SQL (you can interact with Athena using Python's boto3).
Visualize (Optional): Use QuickSight or build custom dashboards with Python (Dash, Streamlit).
Consider Redshift (Optional): For more complex analytics, interact with Redshift using Python libraries.
Consider TimescaleDB (Optional): For real-time dashboards, you can use Python libraries to interact with it.

Leveraging Python within the AWS ecosystem (FastAPI for the API, PySpark in Glue for ETL, and boto3 for interacting with various AWS services), we build a highly scalable and powerful analytics platform for our application. Using containerization (Docker) and managed AWS services (ECS/EKS, Glue, Athena, QuickSight) to achieve massive scalability and reduce operational overhead.

# Nomi Nom User Tracking

A FastAPI service for user tracking analytics.

## Local Development

1. Install dependencies using uv:
```bash
uv pip install .
```

2. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the server is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Docker

To run using Docker:

```bash
docker build -t nomi-nom-tracking .
docker run -p 8000:8000 nomi-nom-tracking
```