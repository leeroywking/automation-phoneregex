from automation_lab import __version__

from automation_lab.automation import grab_emails_and_phone_numbers, format_phone_numbers

def test_version():
    assert __version__ == '0.1.0'

def test_grab_emails_and_phone_numbers():
    test_string = "hello my name is leeroywking@gmail.com and my phonenumber is 123.456.7890"
    email, phone = grab_emails_and_phone_numbers(test_string)
    assert email[0] == "leeroywking@gmail.com"
    assert phone[0] == "123-456-7890"

def test_format_phone_numbers():
    input = [("1234567890",)] # format of regex findall group returns
    assert format_phone_numbers(input)[0] == "123-456-7890"

