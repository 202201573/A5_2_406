import mlflow
import random

# Use local MLflow (no server needed)
mlflow.set_tracking_uri("file:./mlruns")

with mlflow.start_run() as run:
    # Change this value to test
    accuracy = 0.80  # <-- change to 0.90 later

    mlflow.log_metric("accuracy", accuracy)

    print("Accuracy:", accuracy)
    print("Run ID:", run.info.run_id)

    # Save run ID
    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)