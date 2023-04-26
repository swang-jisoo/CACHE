# Import libraries
import os
import pandas as pd
from google.cloud import bigquery 

# Run the codes below on terminal
# gcloud auth login
# gcloud auth application-default login
# gcloud iam service-accounts create GOOGLE_ACCOUNT
# gcloud config set project clinical-entity-extraction

# https://github.com/MIT-LCP/mimic-code/discussions/1154

project_id = 'clinical-entity-extraction'
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id

# Read data from BigQuery into pandas dataframes.
def run_query(query, project_id=project_id):
  return pd.io.gbq.read_gbq(
      query,
      project_id=project_id,
      dialect='standard')

dataset = 'mimiciii_demo'
subject_id = 10017

query = f"""
SELECT *
FROM `physionet-data.{dataset}.patients`
WHERE subject_id = {subject_id}
"""
pt = run_query(query)
# pt['anchor_year'] = pt['anchor_year']
pt