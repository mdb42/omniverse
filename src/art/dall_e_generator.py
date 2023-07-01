from local import constants
from src.art.base_art_generator import BaseArtGenerator
import requests
import os

class DALLEGenerator(BaseArtGenerator):
    def __init__(self):
        self.api_key = constants.OPENAI_API_KEY

    def generate_image(self, prompt: str, num_images=1, size="256x256"):
        print(f"Generating image with prompt: {prompt}")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        # print("Headers: " + str(headers))
        data = {
            "model": "image-alpha-001",
            "prompt": prompt,
            "num_images": num_images,
            "size": size,
            "response_format": "url",
        }
        # print("Data: " + str(data))
        response = requests.post(
            "https://api.openai.com/v1/images/generations", headers=headers, json=data
        )
        # print("Response: " + str(response))
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Error generating image: {e}")
            return None
        # print("Response JSON: " + str(response.json()))
        image_urls = [image["url"] for image in response.json()["data"]]
        # print("Image URLs: " + str(image_urls))
        image_data_list = [requests.get(url).content for url in image_urls]
        # print("Image data list: " + str(image_data_list))

        return image_data_list[0]  # return the first image data; you can modify this to return multiple images if needed