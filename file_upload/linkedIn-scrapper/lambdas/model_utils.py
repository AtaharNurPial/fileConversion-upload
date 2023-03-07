from pydantic import BaseModel
from aws_lambda_powertools.utilities.parser.pydantic import constr

class GetObjectModel(BaseModel):
    key: constr(min_length=3)