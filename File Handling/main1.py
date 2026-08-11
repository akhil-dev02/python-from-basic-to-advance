# import csv
# try:
#     with open('test.csv', 'w', newline = "") as file:
#         writer = csv.writer(file)
#         header = ['Name', "contact"]
#         writer.writerow(header)
#         data = [["Akhil", 7032943940]], [["sam", 9014534392]]
#         writer.writerows(data)
#         print("content added")
# except Exception as e:
#     print(f"something wrong in test.csv: {e}")

# reading csv file content
# import csv
# try:
#     with open('test.csv', 'r') as file:
#         reader = csv.reader(file)
#         print(list(reader))
# except Exception as e:
#     print(f"something wrong in test.csv: {e}")


## updating contact number
import csv
try:
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        name = input()
        new_contact = input()
        for ind, row in enumerate(contacts):
            if row[0]== name:
                contacts[ind][1] = new_contact
                break
        else:
            print("contact name nit exists")
except Exception as e:
    print(f"something wrong in test.csv: {e}")

# writing content into file
import csv
try:
    with open('test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
        print("content added")
except Exception as e:
    print(f"something wrong in test.csv: {e}")
