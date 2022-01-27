def ReplaceStr():

    user_input = input('Please enter the user name :\n')
    if (len(user_input) < 3):
        print("please enter valid name")
    else:
        print(f"hello {user_input} how are you?")

    replace_name = input('Kindly enter the proper name :\n')
    output_str = user_input.replace(user_input, replace_name)
    print("Please find updated data below :")
    print("Hello",output_str,", How are you?")

ReplaceStr()