"""Encode & decode an image in base64"""
import base64
from PIL import Image
from io import BytesIO


def base64_to_image(base64_str: str) -> Image.Image:
    """Decode a base64 encoded image"""
    byte_data = base64.b64decode(base64_str)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img


def image_to_base64(img: Image.Image) -> str:
    """Encode an image with base64"""
    output_buffer = BytesIO()
    img.save(output_buffer, format="JPEG")
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


if __name__ == '__main__':
    # Test image
    image = Image.new('RGB', size=(5, 5), color=(155, 0, 0))

    # Image to str
    base64_str = image_to_base64(image)

    # Str to Image
    img0 = base64_to_image(base64_str)

    # Check result
    import matplotlib.pyplot as plt
    plt.imshow(img0)
    plt.show()
    plt.close()