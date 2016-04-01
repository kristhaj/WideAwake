

class UnusableSystemException(Exception):
    def __init__(self,value):
        self.value = value

    def __init__(self):
        self.value = "We don't know what happend? It must have been black magic!"

    def __str__(self):
        return repr(self.value)