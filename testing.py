import os
import subprocess

def get_branch_name():
    ref = os.getenv('GITHUB_REF', '')
    if ref.startswith('refs/heads/'):
        return ref[len('refs/heads/'):]
    return None

def main():
    branch = get_branch_name()
    if not branch:
        print("Could not determine the branch name.")
        return

    print(f"Current branch: {branch}")

    docker_tag = None

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
