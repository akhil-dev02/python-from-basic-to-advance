from patient_data import patients
from utils import title, get_int


def view_patients():
    title("VIEW PATIENTS")

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print(
            f"ID: {patient['id']} | "
            f"Name: {patient['name']} | "
            f"Age: {patient['age']} | "
            f"Gender: {patient['gender']} | "
            f"Phone: {patient['phone']} | "
            f"Blood Group: {patient['blood_group']}"
        )


def search_patient():
    title("SEARCH PATIENT")

    patient_id = get_int("Patient ID: ")

    patient = next(
        (p for p in patients if p["id"] == patient_id),
        None
    )

    if not patient:
        print("Patient not found.")
        return

    print(f"\nPatient ID  : {patient['id']}")
    print(f"Name        : {patient['name']}")
    print(f"Age         : {patient['age']}")
    print(f"Gender      : {patient['gender']}")
    print(f"Phone       : {patient['phone']}")
    print(f"Address     : {patient['address']}")
    print(f"Blood Group : {patient['blood_group']}")
