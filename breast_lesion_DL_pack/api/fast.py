from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import storage
from breast_lesion_DL_pack.params import *
import requests
import tempfile
import os

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# 💡 Preload the model to accelerate the predictions

# app.state.model = load_model() ## CODE HERE - loading the model needs to be done

# Initialize Google Cloud Storage client
#uncomment - storage_client = storage.Client()

# Specify your bucket name
#uncomment - bucket_name = BUCKET_NAME

@app.get("/")
def root():
    return dict(greeting="Welcome to the breast lesion project ")


@app.post("/upload_from_file/")
def upload_from_file(file: UploadFile):
    ## upload picture and save it in GCS - return dict with params or maybe only URL?
    # Create a blob object with a unique name
    pass
    """blob_name = file.filename
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Upload the file to GCS
    blob.upload_from_file(file.file)

    # Generate a signed URL for the uploaded file
    signed_url = blob.generate_signed_url(
        version="v4", #latest & greatest
        expiration=None,  # Expiration time (None means the URL won't expire)
        method="GET"
    )

    # Return a dict with the parameters
    return {"filename": blob_name, "content_type": file.content_type, "url": signed_url}"""

@app.post("/upload_from_url/")
def upload_from_url(image_url: str):
    pass
    """try:
        response = requests.get(image_url)
        if response.status_code == 200:
            # Create a temporary file to store the image content
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(response.content)
                tmp_file_name = tmp_file.name

            # Upload the temporary file to GCS
            blob_name = os.path.basename(image_url)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(tmp_file_name)

            # Delete the temporary file
            os.unlink(tmp_file_name)

            # Generate a signed URL for the uploaded file
            signed_url = blob.generate_signed_url(
                version="v4",
                expiration=None,  # Expiration time (None means the URL won't expire)
                method="GET"
            )
            # Return a dict with the parameters
            return {"filename": blob_name, "content_type": file.content_type, "url": signed_url}
        else:
            return {"error": f"Failed to fetch image from URL: {image_url}. Status code: {response.status_code}"}

    except Exception as e:
            # If an exception occurs during the request, print the error message
        print(f"Error fetching image from URL: {image_url}. Exception: {e}")
        return None"""



@app.get("/predict")
def predict():
    ## CODE HERE
    ## preprocess the picture & predict with the model
    ## save_results?!
    pass
