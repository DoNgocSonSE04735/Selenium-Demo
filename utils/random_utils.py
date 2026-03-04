import secrets, random, string

class RandomUtils():
    @staticmethod
    def _random_digits(n: int) -> str:
        return ''.join(secrets.choice(string.digits) for _ in range(n))