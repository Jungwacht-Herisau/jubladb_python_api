# How to create a release
1. Edit the `VERSION` in `generate.py`
2. Run `generate.py`
3. Commit the changes and push them
4. Wait until GitHub Actions Build is finished and download the packages (`.whl` and `.tar.gz`)
5. Create a tag and a release on GitHub (upload the build files)