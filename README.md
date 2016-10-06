
HospETL
=======

Generate a schema for fictional hospital data to deliver a prototype of an analytics platform. URL: www.hospetl.website 

Investigate Amazon Redshift as a distributed data warehouse solution, in order to deliver a dashboard in Flask to display reporting metrics such as:
- Inpatient Activity
- Emergency Activity including waiting time breaches
- Frequent Flyer report (patients who frequently visit the emergency department)

I benchmarked the performance of best practice measures within Redshift, such as applying the distribution key, sort key, columnar compression.

## Details

I created the schema for operational activity data:
- Inpatient and outpatient activity
- Elective Bookings, Check-ins, Check-outs
- Emergency Encounters
- Patient Demographics
- Reference Data

## Pre-requisites

Python 3 to generate the data, using the Faker package

AWS account

Boto3: to upload files to Amazon S3.

Amazon Redshift cluster: this project used 4 dc1.large nodes.

Flask: running from an AWS t2.micro instance.



