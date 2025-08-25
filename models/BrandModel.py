from pydantic import BaseModel

class Brand(BaseModel): 
	name: str
	OwnerOfCompany: str
	YearOfEstablishment: str
	field: str
