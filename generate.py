#!/usr/bin/env python3
import os
import subprocess

import aenum
import openapi_parser
import requests
import tqdm
import yaml

import generate_entities
import generate_metamodel
import generate_roles

# PACKAGE_VERSION = "0.1.1"

SPEC_FILE_NAME = "spec.yaml"
MODULE_NAME = "jubladb_api"

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

def patch_openapi_parser():
    aenum.extend_enum(openapi_parser.parser.ContentType, "JSON_API", "application/vnd.api+json")
    aenum.extend_enum(openapi_parser.parser.StringFormat, "URI_REFERENCE", "uri-reference")

GENERATE_METAMODEL = False

if __name__ == '__main__':
    if GENERATE_METAMODEL:
        download_spec()

        print("Parsing OpenAPI spec... ")
        patch_openapi_parser()
        spec = openapi_parser.parse(SPEC_FILE_NAME)
        print("Parsed OpenAPI spec successfully.")

        entities = generate_metamodel.generate_metamodel(spec)
    else:
        from jubladb_api.metamodel.model import ENTITIES
        entities = list(ENTITIES.values())

    generate_entities.generate_entities(entities)

    generate_roles.generate_roles()
