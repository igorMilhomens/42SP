import sys

from PIL import Image


def process_image(image: Image.Image) -> Image.Image:
    """Convert the image to grayscale and resize it to fit within 500x500 pixels."""
    converted = image.convert("L")
    converted.thumbnail((500, 500))
    return converted


if __name__ == "__main__":
    jpg_path = sys.argv[1]
    assert ".jpg" in jpg_path

    with Image.open(jpg_path) as img:
        converted_image = process_image(img)
        jpg_converted_path = jpg_path.replace(".jpg", "_converted.jpg")
        converted_image.save(jpg_converted_path)
        print(f"{jpg_converted_path} saved!")
