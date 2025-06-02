from pydantic import BaseModel
from typing import Optional,List,Dict


class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married=bool = False
    allergies= Optional[List[str]] = None
    contact: Dict[str, str]


def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted patient successfully")


patient_info = {"name": "John Doe", "age": 30}
patient = Patient(**patient_info)
insert_patient(patient)
