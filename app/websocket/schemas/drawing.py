from pydantic import BaseModel
from typing import Optional,List


class Point(BaseModel):
    x: int
    y: int

class DrawEvent(BaseModel):
    type: str
    x1: int
    y1: int
    x2: int
    y2: int
    color: str
    size: int
    shape: Optional[str] = None 
    path: Optional[List[Point]] = None  # ← add this
    sid: Optional[int] = None 