




import os
import shutil
import numpy as np
import random
import sys

file_to_delete = "coalCloud1Positions"
source_file = "MTcoalCloud1Positions"
destination_file = "coalCloud1Positions"


current_directory = os.getcwd()


delete_file_path = os.path.join(current_directory, file_to_delete)
source_file_path = os.path.join(current_directory, source_file)
destination_file_path = os.path.join(current_directory, destination_file)


if os.path.exists(delete_file_path):
    os.remove(delete_file_path)
    print(f"{file_to_delete} deleted successfully.")
else:
    print(f"{file_to_delete} not found in the directory.")

shutil.copy2(source_file_path, destination_file_path)
print(f"{source_file} copied to {destination_file} successfully.")

num_points = 500000
radius = 0.1675


def generate_point_in_sphere(r):
    while True:
        x = round(random.uniform(-r, r), 2)
        y = round(random.uniform(-r, r), 2)
        z = round(random.uniform(-r, r), 2)
        if x**2 + y**2 + z**2 <= r**2:
            return (x, y, z)


points = [generate_point_in_sphere(1) for _ in range(num_points)]


x,y,z = zip(*points)


x = np.array(x)
y = np.array(y)
z = np.array(z)

small_value = sys.float_info.epsilon
R = np.sqrt(x**2 + y**2 + z**2)
phi = np.arccos(z / (R+small_value))
theta = np.arctan2(y, x)


# n = 1e5

# r = (1 - np.exp(-R/10))*radius
# r = (R**(n/(1+n)))*radius 
PHI = 1
r = (R**(PHI))*radius



X = np.round(r * np.sin(phi) * np.cos(theta),6)
Y = np.round(r * np.sin(phi) * np.sin(theta),6)
Z = np.round(r * np.cos(phi),6)

file_path = 'coalCloud1Positions'

with open(file_path, 'r') as file:
    content = file.read()

insert_position = content.find('(') + 1

formatted_points = [f"({X[i]} {Y[i]} {Z[i]})" for i in range(num_points)]


modified_content = content[:insert_position] + "\n" + '\n'.join(formatted_points) + "\n" + content[insert_position:]

with open(file_path, 'w') as file:
    file.write(modified_content)

print("Script executed successfully.", file_path)
