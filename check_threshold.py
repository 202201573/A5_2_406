import mlflow
import sys

mlflow.set_tracking_uri("http://your-mlflow-server")

with open("model_info.txt") as f:
    run_id = f.read().strip()

run = mlflow.get_run(run_id)
accuracy = run.data.metrics.get("accuracy", 0)

print(f"Model accuracy: {accuracy}")

if accuracy < 0.85:
    print("❌ Accuracy below threshold!")
    sys.exit(1)
else:
    print("✅ Model passed threshold!")