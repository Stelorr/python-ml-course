my_name = "Stephen Lorio"
my_age = 27
years_of_experience = 1
learning_ml = True
top_languages = ["Python", "C++", "JavaScript"]

print(f"Hello, my name is {my_name}. I am {my_age} years old with {years_of_experience} year of experience. I am currently learning machine learning: {learning_ml}. My top programming languages are: {', '.join(top_languages)}.")

months_of_experience = years_of_experience * 12
print(f"I have {months_of_experience} months of programming experience.")

total_characters_name = len(my_name)
print(f"My name has {total_characters_name} characters.")

add_language_rust = top_languages.append("Rust")
print(f"Updated list of top programming languages: {', '.join(top_languages)}.")

uppercased_name = my_name.upper()
print(f"My name in uppercase: {uppercased_name}.")
