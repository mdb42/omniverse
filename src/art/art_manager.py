from src.art.base_art_generator import BaseArtGenerator
from src.art.dall_e_generator import DALLEGenerator
from PIL import Image
from io import BytesIO
import os
from datetime import datetime

class ArtManager:
    def __init__(self):
        self.generator = DALLEGenerator()
        self.generated_image_data = None

    def generate_image(self, prompt: str):
        print(f"Generating image with prompt: {prompt}")
        self.generated_image_data = self.generator.generate_image(prompt)
        # print(f"Image generation complete. Image data: {self.generated_image_data}")
        if self.generated_image_data is not None:
            print("Saving image to file (1/2)...")
            self.save_image_to_file()
            print("Image saved to file.")
        else:
            print("Image generation failed.")
        return self.generated_image_data

    def save_image_to_file(self):
        print("Saving image to file (2/2)...")
        if self.generated_image_data is not None:
            current_date = datetime.now().strftime("%Y%m%d-%H%M%S")
            directory = "data/images"
            os.makedirs(directory, exist_ok=True)
            image_file_path = f"{directory}/{current_date}.png"
            print(f"Image saved to {image_file_path}")
            image = Image.open(BytesIO(self.generated_image_data))
            image.save(image_file_path, "PNG")
        else:
            print("No image data available to save")

