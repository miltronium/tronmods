import json
import plistlib

class JSONtoPLISTConverter:
    def __init__(self, json_file_path, plist_file_path):
        self.json_file_path = json_file_path
        self.plist_file_path = plist_file_path

    def convert(self):
        try:
            # Read the JSON data from the file
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)

            # Convert the JSON data to a plist data
            plist_data = plistlib.dumps(data)

            # Write the plist data to the file
            with open(self.plist_file_path, 'wb') as file:
                file.write(plist_data)
            print(f"JSON file converted to plist file successfully: {self.plist_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
# if __name__ == "__main__":
#     json_file_path = 'path/to/your/json_file.json'
#     plist_file_path = 'path/to/your/plist_file.plist'
#     converter = JSONtoPLISTConverter(json_file_path, plist_file_path)
#     converter.convert()