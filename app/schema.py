from marshmallow import Schema, fields
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class BlockData:
    blocks: List[Dict[str, str]]


class ListBlocksSchema(Schema):
    blocks = fields.List(fields.Dict())
