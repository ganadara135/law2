class Error(Exception):
    """Base class for other exceptions"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ElasticSearchError(Error):
    """Raised when elasticsearch error"""
