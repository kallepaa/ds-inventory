from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class InStock():
    order_id: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class OutOfStock():
    order_id: str