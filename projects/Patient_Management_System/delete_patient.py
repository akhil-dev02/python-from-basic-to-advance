from patient_data import patients
from utils import title, get_int, confirm


def delete_patient():
    title("DELETE PATIENT")

    patient_id = get_int("Patient ID: ")

    patient = next(
        (p for p in patients if p["id"] == patient_id),
        None
    )

    if not patient:
        print("Patient not found.")
        return

    print(f"\nPatient: {patient['name']}")

    if confirm("Are you sure you want to delete? (yes/no): "):
        patients.remove(patient)
        print("\nPatient deleted successfully.")
    else:
        print("\nDelete cancelled.")
