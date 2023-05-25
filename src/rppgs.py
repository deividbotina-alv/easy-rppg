import numpy as np
from filters import Filter

class RPPG:
    def __init__(self, filter:Filter=None):
        self.filter = filter

    def getRPPG(self, faces:np.array, is_filter:bool):
        raise NotImplementedError("Subclasses must implement getRPPG method.")

class Green(RPPG):
    def __init__(self, filter:Filter=None):
        super().__init__(filter)

    def getRPPG(self, faces:np.array, is_filter:bool):
        pass

if __name__ == '__main__':
    # Test
    from filters import BandPass
    BP = BandPass()
    Rppg = Green(filter=BP)