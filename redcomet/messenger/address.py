class Address:
    def __init__(self, text: str):
        self._text = text

    def __eq__(self, other) -> bool:
        if not isinstance(other, Address):
            return False
        return self._text == other._text
