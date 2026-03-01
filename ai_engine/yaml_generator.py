# YAML Generator (AI DevOps Copilot)
def generate_pipeline(app):

    return f"""
name: CI Pipeline

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Build Docker
      run: docker build -t {app}:latest .
"""
