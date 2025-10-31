import cowsay


def greeting(name: str) -> None:
    """receives a name and cowsay.cow a greeting"""
    cowsay.cow(f"Hello {name}")
