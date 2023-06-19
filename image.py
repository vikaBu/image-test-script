import imghdr
import requests

def determine_image_type(url):
    try:
        response = requests.get(url, stream=True)
        image_type = imghdr.what(None, h=response.content)
        return image_type
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

image_url = ""
image_type = determine_image_type(image_url)
if image_type:
    print(f"The image type is: {image_type}")
else:
    print("Failed to determine the image type.")
