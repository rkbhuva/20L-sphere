import random
import os
import shutil

# Specify the file names
file_to_delete = "coalCloud1Positions"
source_file = "MTcoalCloud1Positions"
destination_file = "coalCloud1Positions"

# Get the current directory
current_directory = os.getcwd()

# Construct the file paths
delete_file_path = os.path.join(current_directory, file_to_delete)
source_file_path = os.path.join(current_directory, source_file)
destination_file_path = os.path.join(current_directory, destination_file)

# Delete the FOAMFile if it exists
if os.path.exists(delete_file_path):
    os.remove(delete_file_path)
    print(f"{file_to_delete} deleted successfully.")
else:
    print(f"{file_to_delete} not found in the directory.")

# Copy MTcoalCloud1Positions to coalCloud1Positions
shutil.copy2(source_file_path, destination_file_path)
print(f"{source_file} copied to {destination_file} successfully.")




def generate_random_point_in_sphere(radius):
    while True:
        x = round(random.uniform(-radius, radius), 2)
        y = round(random.uniform(-radius, radius), 2)
        z = round(random.uniform(-radius, radius), 2)
        if x**2 + y**2 + z**2 <= radius**2:
            return (x, y, z)

file_path = 'coalCloud1Positions'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Find the position to insert the new data
insert_position = content.find('(') + 1

# Generate 100 random points within the volume of the sphere
num_points = 100000
radius = 0.168
random_points = [generate_random_point_in_sphere(radius) for _ in range(num_points)]

# Format the random points between brackets
formatted_points = [f"({point[0]} {point[1]} {point[2]})" for point in random_points]

# Join the formatted points with newline and insert between brackets
modified_content = content[:insert_position] + "\n" + '\n'.join(formatted_points) + "\n" + content[insert_position:]

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(modified_content)

print("Script executed successfully.", file_path)
