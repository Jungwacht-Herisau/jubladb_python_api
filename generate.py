#!/usr/bin/env python3
import glob
import os
import shutil
import subprocess

import requests
import tqdm
import setuptools.sandbox
import yaml

import build

import generate_roles

PACKAGE_VERSION = "0.0.3"

SPEC_FILE_NAME = "spec.yaml"

# OPENAPI_GENERATOR_CLI_VERSION = "8.0.0-SNAPSHOT"
# OPENAPI_GENERATOR_CLI_URL = f"https://oss.sonatype.org/content/repositories/snapshots/org/openapitools/openapi-generator-cli/{OPENAPI_GENERATOR_CLI_VERSION}/openapi-generator-cli-8.0.0-20240727.184357-6.jar"
OPENAPI_GENERATOR_CLI_VERSION = "7.12.0"
OPENAPI_GENERATOR_CLI_URL = f"https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/{OPENAPI_GENERATOR_CLI_VERSION}/openapi-generator-cli-{OPENAPI_GENERATOR_CLI_VERSION}.jar"

GENERATOR_FILE_NAME = f"openapi-generator-cli-{OPENAPI_GENERATOR_CLI_VERSION}.jar"

MODULE_NAME = "jubladb_api"



def update_openapi_contact2(name, email, url):
    with open(SPEC_FILE_NAME, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("email: info@hitobito.com", f"email: {email}")
    content = content.replace("name: Hitobito AG", f"name: {name}")
    content = content.replace("url: https://hitobito.com/", f"url: {url}")
    with open(SPEC_FILE_NAME, "w", encoding="utf-8") as f:
        f.write(content)

def update_openapi_contact(name, email, url):
    # Load the OpenAPI YAML file
    with open(SPEC_FILE_NAME, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    # Ensure the "info" section exists
    if "info" not in spec:
        spec["info"] = {}

    # Update or add the "contact" section
    spec["info"]["contact"] = {
        "name": name,
        "email": email,
        "url": url
    }

    # Save the modified OpenAPI file
    with open(SPEC_FILE_NAME, "w", encoding="utf-8") as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True)

    print(f"Updated contact info in {SPEC_FILE_NAME}")


def download_generator():
    if not os.path.exists(GENERATOR_FILE_NAME):
        print(f"Downloading OpenAPI Generator CLI from {OPENAPI_GENERATOR_CLI_URL}...")
        response = requests.get(OPENAPI_GENERATOR_CLI_URL, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024

        with tqdm.tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            with open(GENERATOR_FILE_NAME, "wb") as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
        if total_size != 0 and progress_bar.n != total_size:
            raise RuntimeError("Could not download OpenAPI Generator CLI file")
    else:
        print(f"OpenAPI Generator CLI already exists at {GENERATOR_FILE_NAME}")


def download_spec():
    response = requests.get("https://db.jubla.ch/api/openapi.yaml", stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024
    with tqdm.tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
        with open(SPEC_FILE_NAME, "wb") as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        if total_size != 0 and progress_bar.n != total_size:
            raise RuntimeError("Could not download spec file")


if __name__ == '__main__':
    download_generator()
    download_spec()
    update_openapi_contact2("Basil Bader", "oss@basilbader.com", "https://github.com/Jungwacht-Herisau/jubladb_python_api")

    generator_returncode = subprocess.call(["java", "-jar", GENERATOR_FILE_NAME,
                                            "generate",
                                            "-g", "python",
                                            "-i", SPEC_FILE_NAME,
                                            # "-o", f"src/{MODULE_NAME}",
                                            "-o", ".",
                                            "-c", "openapi_config.yaml",
                                            f"--additional-properties=packageName={MODULE_NAME},packageUrl=https://github.com/Jungwacht-Herisau/jubladb_python_api,packageVersion={PACKAGE_VERSION}",
                                            # f"--additional-properties=infoName=\"Basil Bader\"",
                                            ])

    if generator_returncode != 0:
        raise RuntimeError(f"OpenAPI Generator CLI exited with code {generator_returncode}")

    # os.remove(".travis.yml")
    # os.remove(".gitlab-ci.yml")
    # os.remove("git_push.sh")

    #for extfile in os.listdir("extensions"):
    #    shutil.copy2(os.path.join("extensions", extfile), os.path.join("src", MODULE_NAME, MODULE_NAME, extfile))

    #os.chdir(MODULE_NAME)
    try:
        #setuptools.sandbox.run_setup("setup.py", ["clean", "bdist_wheel"])
        subprocess.run(["python", "-m" "build"], check=True)
    finally:
        pass # os.chdir("..")

    # whl_files = glob.glob(f"{MODULE_NAME}/dist/*.whl")
    # if not whl_files:
    #     raise RuntimeError("Could not find any .whl files")
    # shutil.copy2(whl_files[0], ".")
    # print(f"\n\nGenerated {os.path.basename(whl_files[0])}")

    # shutil.rmtree(f"src/{MODULE_NAME}")

    generate_roles.generate_roles()
