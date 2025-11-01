class HomePage:
    URL = "https://example.com"
    TITLE = "Example Domain"

    def __init__(self, driver):
        self.d = driver

    def open(self):
        self.d.get(self.URL)

    def title(self):
        return self.d.title
