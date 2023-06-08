import os
from PIL import Image

source_folder = "./images"
destination_folder = "./resized_images"

def resize_image(image_path, width):
    image = Image.open(image_path)
    original_width, original_height = image.size

    aspect_ratio = original_height / original_width

    resized_image = image.resize((width, int(width * aspect_ratio)), Image.ANTIALIAS)
    return resized_image

def watch_folder():
    desired_width = int(input("Enter the desired width in pixels: "))

    files = os.listdir(source_folder)
    new_files = [f for f in files if not f.startswith('.')]

    for file in new_files:
        file_path = os.path.join(source_folder, file)

        resized_image = resize_image(file_path, desired_width)

        filename, extension = os.path.splitext(file)
        new_filename = filename + "_RESIZED" + extension

        destination_path = os.path.join(destination_folder, new_filename)
        resized_image.save(destination_path)

        # os.remove(file_path)


if __name__ == '__main__':
    watch_folder()
