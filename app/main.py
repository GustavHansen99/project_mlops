from http import HTTPStatus

import torch
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from google.cloud import storage
from PIL import Image
from torchvision import transforms

from src.models.model import EfficientNet

BUCKET_NAME = "group-55-dtumlops"
MODEL_FILE = "best_model.ckpt"

client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)
blob = bucket.get_blob(MODEL_FILE)
blob.download_to_filename("best_model.ckpt")

# Start application
app = FastAPI()

# Load model
model = EfficientNet.load_from_checkpoint("best_model.ckpt")

# Transform for inference
transform = transforms.Compose(
    [
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)),
    ]
)


@app.get("/")
def root():
    """Health check. Brain scan evaluation api live."""
    html_content = """
        <html>
            <title>Online HTML Editor</title>
            <body>
                <h1>Brain scan evaluation application: Online</h1>
            </body>
        </html>
                    """
    return HTMLResponse(content=html_content, status_code=200)


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
    uvicorn.run("main:app", host="0.0.0.0", port=80)
