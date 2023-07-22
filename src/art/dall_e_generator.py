from src.art.art_generator_base import ArtGeneratorBase
import requests
from src.data import data_utils

class DALLEGenerator(ArtGeneratorBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"DALLEGenerator session: {self.session}")
        # print(f"DALLEGenerator test key: {self.session.get_key('OpenAI')}")
        pass

    def generate_image(self, prompt: str, num_images=1, size="256x256"):
        print(f"Generating image with prompt: {prompt}")
        headers = {
            "Authorization": f"Bearer {data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key)}",
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