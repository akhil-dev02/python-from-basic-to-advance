from patient_data import patients
from utils import title, get_int


def update_patient():
    title("UPDATE PATIENT")

    patient_id = get_int("Patient ID: ")

    patient = next(
        (p for p in patients if p["id"] == patient_id),
        None
    )

    if not patient:
        print("Patient not found.")
        return

    print("\nPress Enter to keep the existing value.")

    name = input(f"Name [{patient['name']}]: ").strip()
    if name:
        patient["name"] = name

    age = input(f"Age [{patient['age']}]: ").strip()
    if age:
        try:
            patient["age"] = int(age)
        except ValueError:
            print("Invalid age. Existing age kept.")

    gender = input(f"Gender [{patient['gender']}]: ").strip()
    if gender:
        patient["gender"] = gender

    phone = input(f"Phone [{patient['phone']}]: ").strip()
    if phone:
        patient["phone"] = phone

    address = input(f"Address [{patient['address']}]: ").strip()
    if address:
        patient["address"] = address

    blood_group = input(
        f"Blood Group [{patient['blood_group']}]: "
    ).strip()
    if blood_group:
        patient["blood_group"] = blood_group

    print("\nPatient updated successfully.")
