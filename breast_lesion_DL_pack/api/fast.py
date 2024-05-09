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
import os
from pydantic import BaseModel
from breast_lesion_DL_pack.preprocessor import preprocessing
from keras.models import load_model
import tensorflow as tf


app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

full_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
app.state.model = load_model(os.path.join(full_path,'models','model_best.keras'))


# Initialize Google Cloud Storage client
#uncomment - storage_client = storage.Client()

# Specify your bucket name
#uncomment - bucket_name = BUCKET_NAME

@app.get("/")
def root():
    return dict(greeting="Welcome to the breast lesion project ")
'''
@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()
    image = Image.open(io.BytesIO(contents)).convert("L")
    image = Image.open(io.BytesIO(contents)).resize((224,224))

   # nparr = np.fromstring(contents, np.uint8)
    #cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray
    #colour_response=find_pink_imported_img(cv2_img)

    #preprocessed_image = preprocessing(contents)
    #return preprocessed_image
    return Response(content=image.tobytes(), media_type="image/png")
    ### Encoding and responding with the image
    #im = cv2.imencode('.png', annotated_img)[1] # extension depends on which format is sent from Streamlit
    #Response(content=im.tobytes(), media_type="image/png")
'''

#old code
@app.post("/upload_image/")
async def receive_image(img: UploadFile=File(...)):

    try:
    ### Receiving and decoding the image
        contents = await img.read()

        nparr = np.fromstring(contents, np.uint8)

        #print(resized_nparr.shape)
        cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

        #image_opened = Image.fromarray(cv2_img,'RGB')
        #image_opened = image_opened.convert("L")
        resized_image = cv2.resize(cv2_img, (224,224))
        resized_image2 = np.expand_dims(resized_image,axis=0)

             # Load the model from a file with .keras extension

        # Predict with the model

        result = app.state.model.predict(resized_image2)[0].tolist()
        return {"pred": result}



        ### Encoding and responding with the image
        #im = cv2.imencode('.png', resized_image)[1] # extension depends on which format is sent from Streamlit
        #image_final = Response(content=im.tobytes(), media_type="image/png")


        #return image_final

    except Exception as e:
            # If an exception occurs during the request, print the error message
        print(f"Error fetching image. Exception: {e}")
        return None


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





@app.get("/predict")
def predict(preprocessed_image):
    img = tf.keras.preprocessing.image.img_to_array(preprocessed_image)

    # Load the model from a file with .keras extension
    model = load_model('\models\best_model.keras')

    # Predict with the model
    result = model.predict(img)
    return result
