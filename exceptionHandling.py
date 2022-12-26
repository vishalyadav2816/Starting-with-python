# #try:
#     a this block of code will run and throw errors ift6p0 there are any


# except:
#     this wil raise the errors 

# else;
# this wiil execute if there are no error

# finally:
#     this will execute regardies the result of try and expect


try:
    f = open("demo.py")
    try:
        f.write("ABC")

    except:
        print("Eroor in the file ")

    finally:
        f.close()

except:6