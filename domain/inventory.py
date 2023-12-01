from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Inventory():
    id: int
    product_name: str
    price: float = 0.0
    balance: int = 0
