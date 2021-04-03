import csv

yapet_filename="yapet.csv"
bitwarden_filename="bitwarden.csv"
folder_name="FolderName"


yapet_entries = []
with open(yapet_filename, newline="") as yapet_csvfile:
    reader = csv.DictReader(yapet_csvfile)
    for row in reader:
        yapet_entries.append(row)


bitwarden_entries = []
for yapet_entry in yapet_entries:
    bitwarden_entry = {"folder": folder_name,
                 "favorite": 0,
                 "type": "login",
                 "name": yapet_entry["name"],
                 "notes": yapet_entry["comment"],
                 "fields": None,
                 "login_uri": yapet_entry["host"],
                 "login_username": yapet_entry["username"],
                 "login_password": yapet_entry["password"],
                 "login_totp": None}
    bitwarden_entries.append(bitwarden_entry)


keys = bitwarden_entries[0].keys()
with open(bitwarden_filename, "w", newline="")  as bitwarden_csvfile:
    dict_writer = csv.DictWriter(bitwarden_csvfile, keys)
    dict_writer.writeheader()
    dict_writer.writerows(bitwarden_entries)
