import os

project_name = input()
# project_name = 'test'

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to gitignore.txt
file_path = os.path.join(script_dir, "gitignore.txt")

# Read the content of gitignore.txt
with open(file_path, "r") as git_ignore_file:
    git_ignore_content = git_ignore_file.read()

def create_file(file_path, content=None):
    """Create a file with optional content."""
    with open(file_path, 'w') as file:
        if content:
            file.write(content)

def create_folder_structure(base_dir):
    """Create the folder structure for the project."""
    # Define the folder structure
    folders = [
        os.path.join(base_dir, f"src/{project_name}/tools"),
        os.path.join(base_dir, f"src/{project_name}/config")
    ]

    files = {
        os.path.join(base_dir, ".gitignore"): git_ignore_content,
        os.path.join(base_dir, "pyproject.toml"): "",
        os.path.join(base_dir, "README.md"): "# My Project\n",
        os.path.join(base_dir, ".env"): "",
        os.path.join(base_dir, f"src/{project_name}/__init__.py"): "",
        os.path.join(base_dir, f"src/{project_name}/main.py"): "# Main entry point",
        os.path.join(base_dir, f"src/{project_name}/tools/__init__.py"): "",
        os.path.join(base_dir, f"src/{project_name}/tools/custom_tool.py"): "# Custom tool module",
        os.path.join(base_dir, f"src/{project_name}/config/agents.yaml"): "# Configuration for agents",
        os.path.join(base_dir, f"src/{project_name}/config/tasks.yaml"): "# Configuration for tasks",
    }

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files
    for file_path, content in files.items():
        create_file(file_path, content)

if __name__ == "__main__":
    project = project_name
    create_folder_structure(project)
    print(f"Project '{project}' structure created successfully!")
