import json
import sys
from decimal import Decimal

from pydantic import BaseModel, ValidationError


class Account(BaseModel):
    name: str
    age: int
    email: str
    balance: Decimal


if __name__ == "__main__":
    path = sys.argv[1]

    with open(path) as file:
        member = json.loads("".join(file.readlines()))
        try:
            Account.model_validate(member)
        except ValidationError:
            print("Os dados não estão validos.")
