from pathlib import Path
import roboflow

# Get the base directory
BASE_DIR = Path(__file__).resolve(strict=True).parent


rf = roboflow.Roboflow(api_key="Your_key")

workspace = rf.workspace("max-dji4l")
project = workspace.project("lego-person-detection")
version = project.version("1")

# upload model weights
version.deploy(model_type="yolov8", model_path= f"{BASE_DIR}/runs/detect/train/")