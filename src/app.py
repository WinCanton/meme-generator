"""A module to generate a meme using web-based application.

An image is selected randomly from a collection located in defined
directory location. Similarly with quotes, which can be ingested
from different file formats located in different directory locations.
The generated meme is then displayed on the browser using Flask.
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    body = request.form.get('body', '')
    author = request.form.get('author', 'anonymous')

    try:
        image = requests.get(image_url)
        input_image = f'./temp.jpg'
        with open(input_image, 'wb') as f:
            f.write(image.content)
    except Exception:
        raise FileNotFoundError("Remote file can not be found!")

    path = meme.make_meme(input_image, body, author)
    os.remove(input_image)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
