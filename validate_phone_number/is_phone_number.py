import re

def isPhoneNumber(phonenumber_str):
	"""

	:param phonenumber_str: User Input.We expect he/she introduces a phone number in any point in the string
	:return: The numbered entered, without the rest of the string

	:extranote: /d{3} look for a digit three times
	"""
	phonenumber_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
	mo = phonenumber_regex.search(phonenumber_str)
	return mo.group()