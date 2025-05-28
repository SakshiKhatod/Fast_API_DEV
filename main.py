from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Patient Management System"}


@app.get("/about")
def about():
    return {"message": "This is a fully functional Patient Management System API."}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


def load_data():
    with open("patients_data.json", "r") as file:
        return json.load(file)


@app.get("/view")
def view_all():
    patients = load_data()
    return {"patients": patients}


@app.get("/patient/{patient_id}")
def view_patient_by_id(
    patient_id: str = Path(
        ..., description="The ID of the patient from Db . Example-P001"
    )
):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on basis of hight,weight,bmi"),
    order: str = Query("asc", description="Order of sorting: asc or desc"),
):

    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}",
        )
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")

    sort_order = True if order == "desc" else False
    data = load_data()
    sorted_patients = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order
    )
    return sorted_patients
