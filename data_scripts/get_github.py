import git
import os
import glob
import shutil
import logging
import json

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clone_repo(url, clone_to_path):
    if os.path.exists(clone_to_path):
        shutil.rmtree(clone_to_path)
    logging.info(f"Cloning repository from {url} to {clone_to_path}")
    return git.Repo.clone_from(url, clone_to_path, depth=1)


def process_file(file_path, output_directory, repo_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # Determine content type based on file extension
        if file_path.endswith('.md'):
            content_type = 'doc'
        elif file_path.endswith('.py'):
            content_type = 'code'
        else:
            return  # Skip files that are neither documentation nor code
        save_docs_to_file(content, content_type, output_directory, file_path, repo_path)
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")

def save_docs_to_file(docs, content_type, output_directory, original_path, repo_path):
    # Compute the relative path of the file with respect to the cloned repository's root directory
    relative_path = os.path.relpath(original_path, start=repo_path)
    # Construct the output filename (JSON file)
    output_filename = os.path.splitext(os.path.basename(original_path))[0] + '.json'
    output_path = os.path.join(output_directory, output_filename)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save content in a structured JSON format
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump({
            "type": content_type,
            "path": relative_path,
            "content": docs
        }, file, ensure_ascii=False, indent=4)
    logging.info(f"Saved structured content to {output_path}")

def process_directory(repo_path, output_directory, file_extensions):
    for extension in file_extensions:
        for file_path in glob.glob(os.path.join(repo_path, '**', '*' + extension), recursive=True):
            process_file(file_path, output_directory, repo_path)

def main():
    repo_url = "https://github.com/pytorch/pytorch.git"
    clone_to_path = "/tmp/pytorch_repo"
    output_directory = "../data/step_1_torch_repo/full_codebase"

    os.makedirs(output_directory, exist_ok=True)
    repo = clone_repo(repo_url, clone_to_path)

    # Specify the types of files you are interested in (e.g., Python files and Markdown documentation)
    file_extensions = ['.py', '.md']
    process_directory(clone_to_path, output_directory, file_extensions)
    logging.info(f"Processing complete. Structured content saved to {output_directory}")

if __name__ == "__main__":
    main()
