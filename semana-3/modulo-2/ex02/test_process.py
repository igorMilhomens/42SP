from PIL import Image
from process import process_image


def test_image_size():
    with Image.open("image1.jpg") as img:
        converted = process_image(img)

        assert converted.size <= (500, 500)


def test_image_in_mode_l():
    with Image.open("image1.jpg") as img:
        converted = process_image(img)

        assert converted.mode == "L"
