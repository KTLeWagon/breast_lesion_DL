import requests

def fetch_image_content(gcs_url, stream=True, verify=False):
    try:
        # Send a GET request to fetch the image content
        response = requests.get(gcs_url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # CODE HERE - either return the image as it is or return the masked image
            pass
        else:
            # If the request was not successful, print an error message
            print(f"Failed to fetch image from URL: {gcs_url}. Status code: {response.status_code}")
            return None
    except Exception as e:
            # If an exception occurs during the request, print the exception
        print(f"Error fetching image from URL: {gcs_url}. Exception: {e}")
        return None
