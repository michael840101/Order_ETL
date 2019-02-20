
# Project Abstract

An ETL (Extract, Transform, Load) pipeline to make shopify Order API data is consumable by business analysts.

#Instruction

Every day there will be a .zip file containing retail order data in the raw JSON format to be placed in the input directory. This pipeline will support business analysts so that they can query that data using SQL from a PSQL database. The newly created tables will be sanely structured and those steps should be reproducible with the expectation that the ETL would run daily.

# My Solution
1.Setup the cron job to check the input directory every midnight
2.Once the Zip file detected, copy and unzip the JSON files which has order details into the data_stage directory
3.Run the python program to parse the json file into User and Order object
4.Utilize the SQLAlchemy to map the User Product and Order Objects to relational DB table in Postgresql
5.Persistent the User Product and Order into Postgresql user, product and order table respectively
6.If whole ETL processed completely without error, delete the original Zip file from input forlder, else try one more time and send alter to support team.

#Data pipeline

Input directory ----unzip---> data_stage ---python parser--> Postgresql DB

# Instruction to run the project
Setup the cron job to run the run.sh script in the project directory with desired start time every night.
