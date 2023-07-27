from src.art.art_generator_base import ArtGeneratorBase
import requests
from src.data import data_utils
from src.logger_utils import create_logger
from src import constants

class DALLEGenerator(ArtGeneratorBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)
        self.logger.info("DALLEGenerator: Initializing")
        pass

    def generate_image(self, prompt: str, num_images=1, size="256x256"):
        print(f"Generating image with prompt: {prompt}")
        headers = {
            "Authorization": f"Bearer {data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key)}",
            "Content-Type": "application/json",
        }
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
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"Error generating image: {e}")
            return None
        image_urls = [image["url"] for image in response.json()["data"]]
        image_data_list = [requests.get(url).content for url in image_urls]

        return image_data_list[0]  # return the first image data; you can modify this to return multiple images if needed