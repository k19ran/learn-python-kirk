'''
Create a show_version variable that contains the following
 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
'''
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
my_var = show_version.rstrip()
split_var = my_var.split()
#print("{:^20}{:^20}{:^20}".format(*split_var))
original_string = split_var
model = split_var[1]
serial = split_var[2]
model_lower = "cisco" in split_var[1].lower()
print("Is cisco in model number:{}".format(model_lower))
serial_lower = "881" in split_var[1]
print("Is 881 in model number:{}".format(serial_lower))
print("Serial Number:{}".format(split_var[2]))
print("Model Number:{}".format(split_var[1]))
