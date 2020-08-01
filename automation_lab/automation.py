import re

with open("./automation_lab/assets/potential-contacts.txt", "r") as myfile:
    potential = myfile.readlines()
    strang = ""
    for line in potential:
        strang += line + "\n"

with open("./automation_lab/assets/existing-contacts.txt", "r") as myfile:
    potential = myfile.readlines()
    existing_strang = ""
    for line in potential:
        existing_strang += line + "\n"


def format_phone_numbers(list_of_phone_numbers):
    formatted_phones = []
    for phone in list_of_phone_numbers:
        just_numbers = re.sub("[^0-9x]", "", phone[0])
        output = ""
        output += just_numbers[:3] + "-" + just_numbers[3:6] + "-" + just_numbers[6:]
        formatted_phones.append(output)
    return formatted_phones


def grab_emails_and_phone_numbers(strang: str) -> (list, list):
    email_regex = r"[a-zA-Z0-9_.+-]+?@.*?\...."
    phone_regex = r"(\d{3}(\.|-|\))\d{3}(-|.)\d{4}?x?\d*|\d{10})"
    emails = re.findall(email_regex, strang)
    phones = re.findall(phone_regex, strang)
    formatted_phones = format_phone_numbers(phones)
    return (emails, formatted_phones)


pot_emails, pot_phones = grab_emails_and_phone_numbers(strang)
exi_emails, exi_phones = grab_emails_and_phone_numbers(existing_strang)

new_emails = set()
new_phones = set()

for email in pot_emails:
    if email not in exi_emails:
        new_emails.add(email)

for phone in pot_phones:
    if phone not in exi_phones:
        new_phones.add(phone)


def write_set_to_file(write_set: set, write_file: str) -> bool:
    write_set = sorted(list(write_set))
    try:
        with open(write_file, "w") as filehandle:
            for item in write_set:
                filehandle.write("%s\n" % item)
    except:
        raise ("HECK!")

if __name__ == "__main__":
    print(len(pot_emails), "new emails")
    print(len(pot_phones), "new phone numbers")
    write_set_to_file(new_emails, "./emails.txt")
    write_set_to_file(new_phones, "./phone_numbers.txt")


