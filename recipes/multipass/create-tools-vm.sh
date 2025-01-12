#!/usr/bin/env bash

# Check if multipass is installed
if ! command -v multipass &> /dev/null; then
    echo "Error: multipass is not installed" >&2
    exit 1
fi

multipass launch --name tools --cloud-init gcloud-init.yaml