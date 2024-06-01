import imaplib
import email
import csv
import re
import uuid
import configparser


# Gmail credentials
user = "abdelrahmanprinceamr@gmail.com"
password = "zjnr hqul"  # This should be your application-specific password



# URL for IMAP connection
imap_url = 'imap.gmail.com'

# Connection with GMAIL using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in using your credentials
my_mail.login(user, password)

# Select the Inbox to fetch messages
my_mail.select('Inbox')

# Define Key and Value for email search
key = 'FROM'
value = 'omgitsboom82@gmail.com'
_, data = my_mail.search(None, key, value)

mail_id_list = data[0].split()

# Function to check if a URL is present in the text
def has_url(text):
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    if re.search(url_pattern, text):
        return 1
    else:
        return 0

# Initialize CSV file paths
csv_file_path = "new_data.csv"
message_ids_file_path = "message_ids.csv"

# Check if the message IDs CSV file exists or not
try:
    with open(message_ids_file_path, mode='r', newline='', encoding='utf-8') as id_file:
        reader = csv.reader(id_file)
        has_ids_content = any(row for row in reader)

except FileNotFoundError:
    has_ids_content = False

if not has_ids_content:
    with open(message_ids_file_path, mode='w', newline='', encoding='utf-8') as id_file:
        writer = csv.writer(id_file)
        writer.writerow(['message_id', 'uid'])

processed_ids = set()
if has_ids_content:
    with open(message_ids_file_path, mode='r', newline='', encoding='utf-8') as id_file:
        reader = csv.reader(id_file)
        for row in reader:
            processed_ids.add(row[1])

# If the CSV file has no content, write the header row
if not processed_ids:
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['label', 'urls', 'combined_text'])

# Iterate through each email message
for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])

    # Get the email UID
    uid = my_mail.fetch(num, '(UID)')[1][0].split()[2].decode()

    # Check if the UID is already processed
    if uid not in processed_ids:
        # Generate a UUID for the message
        message_id = str(uuid.uuid4())

        # Extract email content
        combined_text = ""
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                combined_text += part.get_payload() + "\n"

        has_url_value = has_url(combined_text)

        # Update the existing CSV files with the email content, URL presence, message ID, and UID
        try:
            with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['', has_url_value, combined_text])

            # Write the message ID and UID to the message IDs CSV file
            with open(message_ids_file_path, mode='a', newline='', encoding='utf-8') as id_file:
                writer = csv.writer(id_file)
                writer.writerow([message_id, uid])

            processed_ids.add(uid)

            print("Email content, URL presence, message ID, and UID have been successfully added to the CSV files.")

        except Exception as e:
            print(f"An error occurred: {e}")
