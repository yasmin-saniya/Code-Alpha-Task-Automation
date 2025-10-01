import re


input_file = 'input.txt'  # Replace with your actual file name


output_file = 'extracted_emails.txt'


with open(input_file, 'r') as file:
    content = file.read()


emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)


unique_emails = sorted(set(emails))


with open(output_file, 'w') as file:
    for email in unique_emails:
        file.write(email + '\n')


print(f"Extracted {len(unique_emails)} unique email(s) and saved to '{output_file}'.")
