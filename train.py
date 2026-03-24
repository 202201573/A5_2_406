import mlflow
import random

mlflow.set_tracking_uri("http://your-mlflow-server")  # will override via env

with mlflow.start_run() as run:
    accuracy = random.uniform(0.7, 0.95)

    mlflow.log_metric("accuracy", accuracy)

    print(f"Accuracy: {accuracy}")
    print(f"Run ID: {run.info.run_id}")

    # Save Run ID
    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)