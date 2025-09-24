# Dictionary for displaying current skills 
my_skills = {"Python": 1, "Machine Learning": 0, "Problem Solving": 2}

print(f"Here are my skills and their corresponding proficiency levels: {my_skills}.")

# Funtion to add new key and value to my_skills dictonary
def add_something_to_collection(collection, new_key, new_value):
	collection[new_key] = new_value
	print(f"Added '{new_key} with level {new_value}")

# testing function
# add_something_to_collection(my_skills, "Javascript", 1)
# print(f"Here is an updated version of my skills: {my_skills}.")

# function to update a key's value in my_skills dictionary
def update_skill_level(collection, key_to_update, new_value):
	if key_to_update in collection:
		collection[key_to_update] = new_value
		print(f"Updated '{key_to_update}' to the value of '{new_value}'.")
	else:
		print(f"Skill '{key_to_update}' not found in the collection.")
        

# testing function
# update_skill_level(my_skills, "Python", 3)
# print(my_skills)

def show_items_by_level(collection, target_level):
	found_any = False
	for key in collection:
		value = collection[key]
		if value == target_level:
			print(f"{key}: Level {value}")
			found_any = True

	if not found_any:
		print("No skills found at this level.")

# testing function 
# show_items_by_level(my_skills, 3)

# function to calculate average proficiency
def average_proficiency(collection) -> float:
	average_calculation = sum(collection.values()) / len(collection)
	return average_calculation 

# testing function
avg = average_proficiency(my_skills)
print(f"My average proficiency level across all skills is: {avg}.")