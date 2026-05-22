from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):
    username: str
    password: str
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str 
    
class TokenPayLoad(BaseModel):
    sub: str
    role: str
    team: Optional[str] = None