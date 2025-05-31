from pydantic import BaseModel
from typing import Optional, Dict, Any

class ColumnRule(BaseModel):
    type: str  # 'length', 'unique', 'regex'
    min_length: Optional[int] = None
    pattern: Optional[str] = None  # pour regex

class RuleSet(BaseModel):
    rules: Dict[str, ColumnRule]
