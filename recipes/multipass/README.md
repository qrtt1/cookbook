# Multipass VM Management Guide

This guide explains how to create and manage a development VM using Multipass.

## Prerequisites

- [Multipass](https://multipass.run) installed on your system
- `gcloud-init.yaml` configuration file in your working directory

## Quick Start

### Creating a VM

Launch a new VM named "tools" with cloud-init configuration:

```bash
./create-tools-vm.sh
```

Or manually with:

```bash
multipass launch --name tools --cloud-init gcloud-init.yaml
```

### Setting Up Shared Directory

Mount your current working directory to the VM for easy file sharing:

```bash
multipass mount $(pwd) tools:/home/ubuntu/data
```

This creates a shared folder at `~/data` inside the VM that mirrors your current directory.

## Useful Commands

- Connect to VM shell:
  ```bash
  multipass shell tools
  ```

- Check VM status:
  ```bash
  multipass info tools
  ```

- Stop the VM:
  ```bash
  multipass stop tools
  ```

- Start the VM:
  ```bash
  multipass start tools
  ```

- Delete the VM:
  ```bash
  multipass delete tools --purge
  ```

## Troubleshooting

If the mount command fails:
1. Ensure the VM is running
2. Check if the target directory exists
3. Try unmounting first: `multipass unmount tools`