import base64
import sys


def decode_image(base64_str: str) -> bytes:
    """Decode a base64 string to bytes."""
    return base64.b64decode(base64_lines)


if __name__ == "__main__":
    base64_str = sys.argv[1]
    with open(base64_str) as file:
        base64_lines = file.readline().replace("data:image/jpeg;base64,", "")
        image_bytes = decode_image(base64_lines)

        image_filename = base64_str.replace("txt", "jpg")
        with open(image_filename, "wb") as file_jpg:
            file_jpg.write(image_bytes)
            print(f"{image_filename} saved!")
