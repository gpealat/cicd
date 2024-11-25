dvc init

dvc remote add -d databucket s3://dsti-mlops-labs
dvc remote modify databucket access_key_id XXX
dvc remote modify databucket secret_access_key XXXX
dvc remote list

dvc add data/winequality-red.csv

git add winequality-red.csv.dvc

dvc push

