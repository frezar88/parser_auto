from datetime import datetime


class ErrorHandler:
    @staticmethod
    def error_logging(msg, method='', logs_path='logs/log.txt'):
        with open(logs_path, 'a') as file:
            file.write(f"{datetime.now()} --- {method} --- {msg}\n --------------------\n")
