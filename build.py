import os
import subprocess

def set_environments():
    pipeline = {
        "DOCKER_IMAGE": os.getenv("DOCKER_IMAGE", "7002370412/myapp"),
        "DOCKER_TAG": os.getenv("DOCKER_TAG", "latest"),
        "DOCKER_REGISTRY": os.getenv("DOCKER_REGISTRY", "ghcr.io")

    }

    return pipeline

def build_image():

    environments = set_environments()
    print(environments)
    docker_image = environments['DOCKER_IMAGE']
    docker_tag = environments['DOCKER_TAG']

    command = f"docker build -t {docker_image}:{docker_tag} ."
    subprocess.run(command, shell=True)

build_image()
