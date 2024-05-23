import os
import subprocess
import sys

def run_command(command, working_directory=None):
    """Run a command in a subprocess and check for errors."""
    result = subprocess.run(command, shell=True, cwd=working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}")
        print(f"stdout: {result.stdout.decode('utf-8')}")
        print(f"stderr: {result.stderr.decode('utf-8')}")
        sys.exit(result.returncode)
    return result.stdout.decode('utf-8')

def build_project(baseUrl):
    """Build the .NET project."""
    print("Building the project...")
    command = f'dotnet build /p:BaseUrl={baseUrl}'
    run_command(command)
    print("Build completed successfully.")

def run_tests(test_project_path):
    """Run NUnit tests in the specified project."""
    print("Running tests...")
    command = f'dotnet test {test_project_path} --no-build'
    run_command(command)
    print("Tests completed successfully.")

if __name__ == "__main__":
    # Get parameters from environment variables
    test_project_path = os.getenv('TEST_PROJECT_PATH', './Tests')
    baseUrl = os.getenv('BaseUrl', 'DefaultBaseUrl')

    try:
        build_project(baseUrl)
        run_tests(test_project_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

