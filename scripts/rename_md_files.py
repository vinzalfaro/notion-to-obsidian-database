import os

def rename_md_files(directory):
    files = [file for file in os.listdir(directory) if file.endswith('.md')]

    for filename in files:
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()

        new_filename = first_line[2:].strip() + '.md'

        counter = 2
        while os.path.exists(os.path.join(directory, new_filename)):
            if new_filename.endswith(f'{counter - 1}.md'):
                new_filename = f"{new_filename.replace(f'{counter - 1}.md', '')}{counter}.md"
            else:
                new_filename = f"{new_filename.replace(f'.md', '')} {counter}.md"
            counter += 1

        new_file_path = os.path.join(directory, new_filename)
        os.rename(file_path, new_file_path)


directory_path = 'Job Hunt/Job Applications'

rename_md_files(directory_path)
print("Files renamed successfully.")



