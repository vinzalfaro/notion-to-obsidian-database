import os
import re
from datetime import datetime

def transform_md_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_dir, filename)
            output_filepath = os.path.join(output_dir, filename)

            with open(input_filepath, "r", encoding='utf-8') as input_file:
                lines = input_file.readlines()[2:]
                transformed_lines = transform_lines(lines, filename)

                with open(output_filepath, "w", encoding='utf-8') as output_file:
                    output_file.writelines(transformed_lines)

def transform_lines(lines, filename):
    transformed_lines = []
    pattern = re.compile(r"^(Company|Location|Arrangement|Job Posting|Status|Date Applied|Resume Sent): (.*)$")

    try:
        job_posting_line = None

        for line in lines:
            match = pattern.match(line)
            if match:
                key = match.group(1).lower().replace(" ", "-")
                value = match.group(2)
                if key == "job-posting":
                    urls = re.findall(r'(https://[^\s,]+)', value)
                    links = ", ".join(f"[link]({url})" for url in urls)
                    job_posting_line = f"\nJob Posting: {links}\n"
                elif key == "resume-sent":
                    continue
                elif key == "date-applied":
                    date_obj = datetime.strptime(value, "%B %d, %Y")
                    transformed_date = date_obj.strftime("%Y-%m-%d")
                    transformed_lines.append(f"{key}: {transformed_date}\n")
                    transformed_lines.append("---\n")
                    if job_posting_line:
                        transformed_lines.append(job_posting_line)
                else:
                    transformed_lines.append(f"{key}: {value}\n")

            else:
                transformed_lines.append(line)

        position = os.path.splitext(filename)[0].rstrip('0123456789 ')
        position_line = f"---\nposition: {position}\n"
        transformed_lines.insert(0, position_line)

    except Exception as e:
        print(f"Error processing lines: {e}")

    return transformed_lines



input_directory = "files"
output_directory = "edited_files"

transform_md_files(input_directory, output_directory)
