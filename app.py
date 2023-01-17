import argparse
from http import HTTPStatus

import torch
import uvicorn
from fastapi import FastAPI, File, UploadFile
from omegaconf import OmegaConf
from PIL import Image
from torchvision import transforms

from src.models.model import EfficientNet

# Start application
app = FastAPI()

# Parse configuration file
parser = argparse.ArgumentParser()
parser.add_argument(
    "-p",
    "--path",
    type=str,
    default="config/infer.yaml",
    help="Configuration file path",
)
args = parser.parse_args()

# loading
config = OmegaConf.load(args.path)

# Load model
model = EfficientNet.load_from_checkpoint(
    config.hyperparameters.checkpoint_path
)

# Transform for inference
transform = transforms.Compose(
    [
        transforms.Resize(
            (config.hyperparameters.resize_x, config.hyperparameters.resize_y)
        ),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)),
    ]
)


@app.get("/")
def root():
    """Health check. Brain scan evaluation api live."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response


@app.post("/infer/")
async def cv_model(data: UploadFile = File(...)):
    with open("image.jpg", "wb") as image:
        content = await data.read()
        image.write(content)
        image.close()

    # Read image and infer
    image = Image.open("image.jpg").convert("RGB")
    y_hat = model(transform(image).unsqueeze(0))

    # Calculate result
    ps = torch.exp(y_hat)
    tumor = ps.max(1)[1][0].numpy()

    if tumor == 1:
        tumor = True
    else:
        tumor = False

    response = {
        "input": data,
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "tumor": tumor,
    }

    return response


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)
