from fastapi import FastAPI, UploadFile, File, Response
from fastapi.responses import FileResponse
import requests
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import storage
from breast_lesion_DL_pack.params import *
import numpy as np
from PIL import Image
import cv2
import io
from pydantic import BaseModel

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



# Initialize Google Cloud Storage client
#uncomment - storage_client = storage.Client()

# Specify your bucket name
#uncomment - bucket_name = BUCKET_NAME

@app.get("/")
def root():
    return dict(greeting="Welcome to the breast lesion project ")


@app.post("/upload_from_file/")
async def receive_image(img: UploadFile=File(...)):
    try:
    ### Receiving and decoding the image
        contents = await img.read()

        nparr = np.fromstring(contents, np.uint8)
        cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

        ### Do cool stuff with your image.... For example face detection
        #annotated_img = annotate_face(cv2_img)

        ### Encoding and responding with the image
        im = cv2.imencode('.png', cv2_img)[1] # extension depends on which format is sent from Streamlit
        image = Response(content=im.tobytes(), media_type="image/png")
        return image

    except Exception as e:
            # If an exception occurs during the request, print the error message
        print(f"Error fetching image from URL: {image_url}. Exception: {e}")
        return None

'''
@app.post("/upload_from_url/")
async def upload_from_url(image_url: str):
    try:
        response = requests.get(image_url)
        img = Image.open(io.BytesIO(response.content)).convert("L")
# other preprocessing if needed
        return img
    except Exception as e:
        # If an exception occurs during the request, print the error message
        print(f"Error fetching image from URL: {image_url}. Exception: {e}")
        return None

'''



@app.get("/predict")
def predict():
    # Preprocess the picture
    preprcessing(data)


    # Predict with the model
    predict()

    return result
