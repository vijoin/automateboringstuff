import is_phone_number as ipn

if __name__ == "__main__":
	mock_input = 'My number is 415-555-4242'
	phonenumber = ipn.isPhoneNumber(mock_input)
	print("The user entered the number {}".format(phonenumber))
