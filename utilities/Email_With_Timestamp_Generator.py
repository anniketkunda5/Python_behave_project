from datetime import datetime
def get_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y%m%d%I:%M:%S%p")
    invalid_email = "mail" + time_stamp + "@gmail.com"
    return invalid_email
def get_password_with_timestamp():
    time_stamp = datetime.now().strftime("%Y%m%d%I:%M:%S%p")
    invalid_password = "pwd" + time_stamp
    return invalid_password