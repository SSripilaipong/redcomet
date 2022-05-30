class Location:
    def __init__(self, id_: str):
        self._id = id_

    def __eq__(self, other) -> bool:
        if not isinstance(other, Location):
            return False

        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)
