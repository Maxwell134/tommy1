import os
import subprocess

def get_branch_name():
    # Try to get branch name from workflow_dispatch input
    dispatch_ref = os.getenv('INPUT_REF')
    if dispatch_ref:
        print(f"Using branch from workflow_dispatch input: {dispatch_ref}")
        return dispatch_ref

    # Fallback to GitHub-provided ref (e.g., refs/heads/new)
    full_ref = os.getenv('GITHUB_REF', '')
    print(f"GITHUB_REF from environment: {full_ref}")
    if full_ref.startswith('refs/heads/'):
        return full_ref[len('refs/heads/'):]
    return None

def main():
    branch = get_branch_name()
    if not branch:
        print("Could not determine the branch name.")
        return

    print(f"Current branch: {branch}")

    # Branch-to-docker-tag logic
    if branch == "master":
        docker_tag = 'latest'
    elif branch == "new":
        docker_tag = 'v1.03'
    else:
        docker_tag = f"{branch}-snapshot"

    print(f"Using Docker tag: {docker_tag}")

    image_name = f"myapp:{docker_tag}"

    try:
        print(f"Building Docker image '{image_name}'...")
        subprocess.run(["docker", "build", "-t", image_name, "."], check=True)
        print(f"Successfully built {image_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to build Docker image: {e}")
        exit(1)

if __name__ == "__main__":
    main()
