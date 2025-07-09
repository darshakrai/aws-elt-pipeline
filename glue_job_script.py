import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.transforms import Filter

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

datasource = glueContext.create_dynamic_frame.from_catalog(
    database="moviedb",
    table_name="booking_raw"
)

transformed = Filter.apply(frame=datasource, f=lambda x: x["tickets"] > 1)

glueContext.write_dynamic_frame.from_options(
    frame=transformed,
    connection_type="redshift",
    connection_options={
        "database": "moviedb",
        "user": "admin",
        "password": "<your_redshift_password>",
        "url": "jdbc:redshift://<your_redshift_endpoint>:5439/dev",
        "dbtable": "booking_clean",
        "aws_iam_role": "<your-glue-iam-role-arn>"
    }
)

job.commit()


