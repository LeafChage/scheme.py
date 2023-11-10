class String:
    @staticmethod
    def split(x: str, n: int) -> tuple[str, str]:
        if len(x) > n:
            return (x[:n], x[n:])
        elif len(x) == n:
            return (x, "")
        else:
            raise IndexError()
