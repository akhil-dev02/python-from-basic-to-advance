from register_patient import register_patient
from view_patient import view_patients, search_patient
from update_patient import update_patient
from delete_patient import delete_patient
from utils import title, pause


def main():
    while True:
        title("PATIENT MANAGEMENT SYSTEM")

        print("1. Register Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            register_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "0":
            print("\nThank you for using Patient Management System.")
            break
        else:
            print("\nInvalid choice.")

        if choice != "0":
            pause()


if __name__ == "__main__":
    main()
