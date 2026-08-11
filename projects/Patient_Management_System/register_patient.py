from patient_data import patients
from utils import title, get_int


def register_patient():
    title("REGISTER PATIENT")

    patient_id = get_int("Patient ID: ")

    if any(patient["id"] == patient_id for patient in patients):
        print("Patient ID already exists.")
        return

    patient = {
        "id": patient_id,
        "name": input("Name: ").strip(),
        "age": get_int("Age: "),
        "gender": input("Gender: ").strip(),
        "phone": input("Phone: ").strip(),
        "address": input("Address: ").strip(),
        "blood_group": input("Blood Group: ").strip()
    }

    patients.append(patient)
    print("\nPatient registered successfully.")
