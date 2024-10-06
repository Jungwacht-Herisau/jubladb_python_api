#!/usr/bin/env python3
import glob
import os
import shutil
import subprocess

import requests
import tqdm
import setuptools.sandbox

OPENAPI_GENERATOR_CLI_VERSION = "7.9.0-SNAPSHOT"
OPENAPI_GENERATOR_CLI_URL = f"https://oss.sonatype.org/content/repositories/snapshots/org/openapitools/openapi-generator-cli/{OPENAPI_GENERATOR_CLI_VERSION}/openapi-generator-cli-7.9.0-20241004.151047-108.jar"
# OPENAPI_GENERATOR_CLI_VERSION = "7.8.0"
# OPENAPI_GENERATOR_CLI_URL = f"https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/{OPENAPI_GENERATOR_CLI_VERSION}/openapi-generator-cli-{OPENAPI_GENERATOR_CLI_VERSION}.jar"

MODULE_NAME = "jubladb_api"

if __name__ == '__main__':
    generator_file_name = f"openapi-generator-cli-{OPENAPI_GENERATOR_CLI_VERSION}.jar"
    if not os.path.exists(generator_file_name):
        print(f"Downloading OpenAPI Generator CLI from {OPENAPI_GENERATOR_CLI_URL}...")
        response = requests.get(OPENAPI_GENERATOR_CLI_URL, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024

        with tqdm.tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            with open(generator_file_name, "wb") as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
        if total_size != 0 and progress_bar.n != total_size:
            raise RuntimeError("Could not download file")
    else:
        print(f"OpenAPI Generator CLI already exists at {generator_file_name}")

    generator_returncode = subprocess.call(["java", "-jar", generator_file_name,
                                            "generate",
                                            "-g", "python",
                                            "-i", "https://db.jubla.ch/api/openapi.yaml",
                                            "-o", MODULE_NAME,
                                            "-c", "openapi_config.yaml",
                                            f"--additional-properties=packageName={MODULE_NAME}"])

    if generator_returncode != 0:
        raise RuntimeError(f"OpenAPI Generator CLI exited with code {generator_returncode}")

    for extfile in os.listdir("extensions"):
        shutil.copy2(os.path.join("extensions", extfile), os.path.join(MODULE_NAME, MODULE_NAME, extfile))

    os.chdir(MODULE_NAME)
    try:
        setuptools.sandbox.run_setup("setup.py", ["clean", "bdist_wheel"])
    finally:
        os.chdir("..")

    whl_files = glob.glob(f"{MODULE_NAME}/dist/*.whl")
    if not whl_files:
        raise RuntimeError("Could not find any .whl files")
    shutil.copy2(whl_files[0], ".")
    print(f"\n\nGenerated {os.path.basename(whl_files[0])}")

    shutil.rmtree(MODULE_NAME)
