import mlflow
import random

mlflow.set_tracking_uri("file:./mlruns")

with mlflow.start_run() as run:
    accuracy = 0.80  # change later for testing

    mlflow.log_metric("accuracy", accuracy)

    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)