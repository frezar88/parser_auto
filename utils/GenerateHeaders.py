from fake_headers import Headers


class GenerateHeaders:
    @staticmethod
    def generate_headers():
        headers = Headers(headers=True)
        return headers.generate()
