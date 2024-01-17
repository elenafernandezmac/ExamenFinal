import json
import math
import numpy as np

def calculate_horizontal_distance(initial_velocity, launch_angle):
    """
    Calculate the maximum horizontal distance for a projectile.
    
    Parameters:
    - initial_velocity: Initial velocity of the projectile in meters per second.
    - launch_angle: Launch angle of the projectile in degrees.
    
    Returns:
    - Maximum horizontal distance in meters.
    """
    # Convert launch angle to radians
    angle_rad = math.radians(launch_angle)
    
    # Calculate horizontal distance using the projectile motion formula
    horizontal_distance = (initial_velocity**2 * math.sin(2 * angle_rad)) / 9.8
    
    return horizontal_distance

def calculate_max_height(initial_velocity, launch_angle):
    """
    Calculate the maximum height for a projectile.
    
    Parameters:
    - initial_velocity: Initial velocity of the projectile in meters per second.
    - launch_angle: Launch angle of the projectile in degrees.
    
    Returns:
    - Maximum height in meters.
    """
    # Convert launch angle to radians
    angle_rad = math.radians(launch_angle)
    
    # Calculate maximum height using the projectile motion formula
    max_height = (initial_velocity**2 * math.sin(angle_rad)**2) / (2 * 9.8)
    
    return max_height

def calculate_flight_time(initial_velocity, launch_angle):
    """
    Calculate the flight time for a projectile.
    
    Parameters:
    - initial_velocity: Initial velocity of the projectile in meters per second.
    - launch_angle: Launch angle of the projectile in degrees.
    
    Returns:
    - Flight time in seconds.
    """
    # Convert launch angle to radians
    angle_rad = math.radians(launch_angle)
    
    # Calculate flight time using the projectile motion formula
    flight_time = (2 * initial_velocity * math.sin(angle_rad)) / 9.8
    
    return flight_time

def calculate_max_horizontal_distances_and_height(json_file_path, min_flight_time=4.0):
    """
    Calculate the maximum horizontal distances and maximum height for projectiles described in a JSON file.
    
    Parameters:
    - json_file_path: Path to the JSON file containing projectile information.
    - min_flight_time: Minimum flight time to filter launches (default is 5.0 seconds).
    
    Returns:
    - Dictionary with projectile names as keys and their corresponding maximum horizontal distances and heights.
    """
    with open('file.json', 'r') as file:
        data = json.load(file)
    
    distances = {}
    heights = {}
    long_flight_time_launches = {}
    
    for idx, projectile in enumerate(data):
        name = f"Projectile{idx + 1}"
        velocity = projectile["InitialVelocity"]
        angle = projectile["LaunchAngle"]
        
        # Calculate the maximum horizontal distance
        distance = calculate_horizontal_distance(velocity, angle)
        
        # Calculate the maximum height
        height = calculate_max_height(velocity, angle)
        
        # Calculate the flight time
        flight_time = calculate_flight_time(velocity, angle)
        
        # Store the results in the dictionaries
        distances[name] = distance
        heights[name] = height
        
        # Check if flight time exceeds the minimum
        if flight_time > min_flight_time:
            long_flight_time_launches[name] = flight_time
    
    return distances, heights, long_flight_time_launches

# Example usage
json_file_path = "file.json"  # Replace with the path to your JSON file
distances, heights, long_flight_time_launches = calculate_max_horizontal_distances_and_height(json_file_path)

# Print the results
for projectile, distance in distances.items():
    print(f"{projectile}: Max Distance - {distance} meters")

# Find and print the projectile with the highest maximum height
max_height_projectile = max(heights, key=heights.get)
print(f"\nProjectile with Highest Maximum Height: {max_height_projectile} - Max Height: {heights[max_height_projectile]} meters")

# Print launches with flight time exceeding 5 seconds
print("\nLaunches with Flight Time Exceeding 4 Seconds:")
for projectile, flight_time in long_flight_time_launches.items():
    print(f"{projectile}: Flight Time - {flight_time} seconds")

