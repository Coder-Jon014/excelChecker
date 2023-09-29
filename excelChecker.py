import os
from dotenv import load_dotenv
import csv


load_dotenv()
# Input folder containing CSV files
input_folder = os.getenv("FOLDER_LOCATION")



# Word to search for
search_word = input("Enter the word to search for: ")

# Iterate through files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)

        # Open the CSV file
        found = False
        found_list = []
        with open(file_path, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if search_word in ' '.join(row):  # Concatenate row elements for the search
                    found = True
                    break

        # If the word is found, leave the file open
        if found:
            found_list.append(filename)
            print(f"Word '{search_word}' found in {filename}.")
        else:
            print(f"Word '{search_word}' not found in {filename}.")

# Print the list of found filenames at the end
if found_list:
    print("\nFiles with the word found:")
    for found_filename in found_list:
        print(found_filename)
else:
    print("\nNo files with the word found.")
