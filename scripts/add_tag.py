import os

input_directory = '../database_files/edited_files'
output_directory = '../database_files/tagged_files'
tag_to_insert = 'tags: job_hunt'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    input_path = os.path.join(input_directory, filename)
    output_path = os.path.join(output_directory, filename)

    with open(input_path, 'r', encoding='utf-8') as input_file:
        content = input_file.readlines()
        content.insert(1, f"{tag_to_insert}\n")

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(content)

print("Files processed successfully.")
