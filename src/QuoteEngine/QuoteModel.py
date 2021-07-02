"""A class that defines and constructs Quote object.

This class is used as part of the process of extracting Quote
data from various types of input files. Having managed to extract
data, ingestors shall utilise this class definition to construct
Quote objects.
"""


class QuoteModel:
    """A class container that defines and construct a QuoteModel.

    This class will be used by ingestor classes to construct Quote
    objects following extraction of data from various different
    file types, performed uniquely and independently by different
    ingestor classes.
    """

    def __init__(self, body, author):
        """Initialise Quote object using provided information.

        This object constructor uses `body` and `author` information
        passed to it to create a Quote object.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Define object representation in a string format."""
        return f'{self.body} ({self.author})'
