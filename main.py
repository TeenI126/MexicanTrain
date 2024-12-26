class domino:
    left: int
    right: int

    def __init__(self, left: int, right: int):
         self.left = left
         self.right = right

    def swap(self):
        temp = self.right
        self.right = self.left
        self.left = temp

mypieces : list(domino)

if __name__ == "__main__":
    pass
    