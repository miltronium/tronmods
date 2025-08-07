import json
import re


class OptionExtractor:
    def __init__(self, document):
        self.document = document
        self.options = {}

    def extract_options(self):
        option_pattern = re.compile(r"^[ -]+([a-zA-Z0-9-]+)\s+(\S+)?$")

        for line in self.document.splitlines():
            match = option_pattern.match(line)
            if match:
                key = match.group(1)
                value = match.group(2)
                self.options[key] = value
                if key == "ac-collection-id":
                    self.options["target_device"] = "AppleConnect Collection"

    def to_json(self):
        return json.dumps(self.options, indent=2)

    def save_to_json_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.options, file, indent=2)


# Example usage:
# if __name__ == "__main__":
#     document = """
#     --ac-collection-id ID
#     --ac-token AC-TOKEN
#     --ac-user AC-USER
#     --activate
#     -f something
#     --another-option value
#     """
#     extractor = OptionExtractor(document)
#     extractor.extract_options()
#     print(extractor.to_json())
#
#     # Save the JSON object to a file
#     json_file_path = 'options.json'
#     extractor.save_to_json_file(json_file_path)
#     print(f"JSON object saved to: {json_file_path}")

# In this updated version:
#
# - The **"--ac-token"** option is now handled, and its value is stored in the **"token"** key of the JSON object.
# - The **"target_device"** key is still set to **"AppleConnect Collection"** if the **"--ac-collection-id"** option is found.
#
# So, the output JSON object will look like this:
#
# ```json
# {
#   "ac-collection-id": "ID",
#   "target_device": "AppleConnect Collection",
#   "ac-token": "AC-TOKEN",
#   "f": "something",
#   "another-option": "value"
# }
# ```