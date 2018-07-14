refrence_id = input("Enter the reference Id")
if len(refrence_id) != 12 and sum(char.isalnum() for char in refrence_id) != 12:
  print("Reference Id should be 12 alphanumeric chars only!")

import base64 # Used for encoding

refrence_id_encrypted = base64.b64encode(refrence_id.encode())
print(f"Congratulations!!! ReferenceID is encrypted, You are Safe from Hackers: {refrence_id_encrypted}")