def email_validation(email):
    k = 0
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif not (i.isalnum()):
                            if i == "_" or i == "." or i == "@":
                                continue
                            else:
                                k = 1
                    if k == 1:
                        print("Wrong Email! Email can not contain special character except '_' and '.' ")
                    else:
                        print("Congratulations! You Entered a Right Email.")
                else:
                    print("Wrong Email! Check format again")
            else:
                print("Wrong Email! Email must have one '@' symbol")
        else:
            print("Wrong Email! Email should start with alphabet")
    else:
        print("Correct your email's length and format")


if __name__ == "__main__":
    # Min length of an Email is 6 like e@e.au
    # Covert the Email into lower case
    print(""" Email Rules
        1. Min length of an Email is 6 like e@e.au
        2. Email must be lower case
        3. Start with alphabet
        4. Must have only one '@' symbol
        5. Should follow the format
    """)
    user_email = input("Enter your Email: ").lower()
    email_validation(user_email)
