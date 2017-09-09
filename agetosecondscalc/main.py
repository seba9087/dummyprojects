def age_in_seconds(age):
	return age * 365 * 24 * 60 * 60

user_age = input("Enter your age: ")

print("Your age is {} and that equals to {} seconds".format(user_age, age_in_seconds(user_age)))
