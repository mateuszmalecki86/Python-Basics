is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are NOT a male NOR tall")



if is_male and is_tall:
    print("You are a male and tall")

elif is_male and not is_tall:
    print("You are a male but not tall")

elif not is_male and is_tall:
    print("You are not a male but you are tall")

else:
    print("You are not a male and not tall")