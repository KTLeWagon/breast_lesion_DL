from tensorflow.keras import preprocessing
import os

def preprocessing(image):
    # Path to your single image file
    image_path = image

    # Create a temporary directory
    temp_dir = "temp_dir"
    os.makedirs(temp_dir, exist_ok=True)

    # Move the image file into the temporary directory
    temp_image_path = os.path.join(temp_dir, "image.jpg")
    os.rename(image_path, temp_image_path)

    # Use image_dataset_from_directory on the temporary directory
    preprocessed_picture = preprocessing.image_dataset_from_directory(
        directory=temp_dir,
        shuffle=True,
        image_size=(224, 224),
        color_mode='grayscale',
        batch_size=32)

    # Remove the temporary directory
    os.system(f"rm -rf {temp_dir}")

    return preprocessed_picture
