# Project Creation

Creating a program that automatically updates `pyproject.toml` with data for a PyPi project on every git commit requires a combination of git hooks and a script to update the `pyproject.toml` file. Below is a step-by-step approach to achieve this:

### Step 1: Create a Python Script to Update `pyproject.toml`

Create a script called `update_pyproject.py` with the following content:

```python
import toml
import subprocess

def update_pyproject_toml():
    data = {
        "tool": {
            "poetry": {
                "name": "your_project_name",
                "version": "0.1.0",  # Update version as needed
                "description": "Your project description",
                # ... other necessary fields
            }
        }
    }

    # Write data to pyproject.toml
    with open('pyproject.toml', 'w') as file:
        toml.dump(data, file)

if __name__ == "__main__":
    update_pyproject_toml()
```

### Step 2: Create a Git Pre-commit Hook

1. Navigate to your project's `.git/hooks` directory.
2. Create a new file named `pre-commit` (without any file extension).
3. Make the `pre-commit` file executable by running `chmod +x pre-commit` in your terminal.
4. Open the `pre-commit` file in a text editor and add the following content:

```bash
#!/bin/bash
python update_pyproject.py
git add pyproject.toml
```

Now, every time you make a commit, the `pre-commit` hook will run the `update_pyproject.py` script to update the `pyproject.toml` file, and stage the updated `pyproject.toml` file to be included in the commit.

### Notes:

- Ensure that the `update_pyproject.py` script is in the root of your project directory, or adjust the path in the `pre-commit` hook accordingly.
- Update the `update_pyproject.py` script to gather the necessary data for your `pyproject.toml` file as needed for your project.
- Git hooks are local to the repository and will not be shared with others when the repository is cloned or pulled. If you want to share this automation with others, you might need to look into a more complex solution, such as setting up a CI/CD pipeline.
