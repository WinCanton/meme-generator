from PIL import Image, ImageDraw, ImageFont
from random import randint
import textwrap


class MemeEngine():

    def __init__(self, path):
        self.output_path = path

    @staticmethod
    def _randomise_location(image):
        """Create a random coordinate for text on an image.

        :param image {PIL.Image}: an image object of a PIL.Image type
        :return {tuple}: a tuple of random x, y coordinate
        """
        image_width, image_height = image.size
        start_x = int(randint(10, 30) * image_width / 100)
        start_y = int(randint(10, 50) * image_height / 100)
        return start_x, start_y

    def _draw_multiple_line_text(self, image, body, author, font,
                                 text_color, width):
        """Draw multiple lines of quote's body as well as author, in-place.

        Inspiration for developing this function came from the following
        source: https://stackoverflow.com/questions/7698231/
        python-pil-draw-multiline-text-on-image

        :param image {PIL.Image}: an image object of a PIL.Image type
        :param body {str}: a body text of a Quote
        :param author {str}: author of a quote
        :param font {ImageFont}: font object
        :param text_color {tuple}: colour fill in RGB tuple format
        :param width {int}: the length of characters of text in one line
        :return: None
        """
        draw = ImageDraw.Draw(image)
        lines = textwrap.wrap(body, width)
        lines.append(f'<{author}>')
        print(lines)
        x_text, y_text = self._randomise_location(image)
        for line in lines:
            line_width, line_height = font.getsize(line)
            draw.text((x_text, y_text),
                      line, font=font, fill=text_color)
            y_text += line_height

    def make_meme(self, img_path, body, author, width=500) -> str:
        """Create meme with provided arguments and default width.

        :param img_path {str}: path to input image:
        :param body {str}: body text of a quote
        :param author {str}: author of a quote
        :param width {int}: the length of characters of text in one line
        :return {str}: path to output meme file
        """
        # try - except here
        image = Image.open(img_path)

        # Resize Image
        im_width, im_length = image.size
        aspect_ratio = im_width / im_length
        image = image.resize((width, int(width * 1 / aspect_ratio)))

        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=30)
        text_start_height = 0
        text_color = (255, 255, 163)
        width = 30
        self._draw_multiple_line_text(image, body, author, font, text_color, text_start_height, width)

        output_meme = f'{self.output_path}/output.jpg'
        image.save(output_meme)

        return output_meme
