import utils as utilExercise

# First function
print("- First function")
outputFileName = "first_func.txt"
utilExercise.first_function("./", outputFileName)

# Second function
print("- Second function")
outputFileName = "second_func.txt"
utilExercise.second_function("./", outputFileName)

# Third function
print("- Third function")
lst_files = ["./test.txt", "./test8.txt"]
utilExercise.third_function(lst_files)

# Fourth function
print("- Fourth function")
lst_files = ["./text_with_emails.txt", "./text_with_emails2.txt"]
utilExercise.fourth_function(lst_files)

# Fifth function
print("- Fifth function")
outputFileName = "fifth_func.txt"
lst_files = ["./random_md_file2.md", "random_md_file.md"]
utilExercise.fifth_function(lst_files)