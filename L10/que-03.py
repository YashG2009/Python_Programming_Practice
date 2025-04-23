# Program que-03.py
# Accept contact details from the user and create a vCard file that can be stored in a mobile

def create_vcard(filename, name, phone, email):
    vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
END:VCARD
"""
    with open(filename, 'w') as file:
        file.write(vcard_content)
    print(f"vCard saved to {filename}")

print("Enter contact details to create a vCard:")
name = input("Name: ")
phone = input("Phone number: ")
email = input("Email address: ")
output_dir = "que-03-output"
import os
os.makedirs(output_dir, exist_ok=True)
vcard_file = os.path.join(output_dir, f"{name.replace(' ', '_')}.vcf")
create_vcard(vcard_file, name, phone, email)
