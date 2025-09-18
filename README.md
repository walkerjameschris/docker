# docker

## Primary Setup

This repo contains Docker image configurations for my home server.
Before installing Docker and running the images, I set up a few
things on the server running **Ubuntu 24.04 LTS:**

- Settings >> Power >> Performance >> Screen Blank (Never)
- Install `curl` with `sudo apt install curl`
- Install `tailscale` for VPN with:
  - `curl -fsSL https://tailscale.com/install.sh | sh`
  - `sudo tailscale up`
  - `sudo tailscale set --ssh`
- Install drivers with `sudo ubuntu-drivers install` (then `sudo reboot`)
- Install `git` to clone this repo with `sudo apt install git`
- Install `gh` for auth with:
  - `sudo apt install gh`
  - `gh auth login`
- Setup RAID 6 array with:
  - `sudo apt install mdadm`
  - Ensure all 4 drives are **partition free** and named `sd[a-d]`
  - `sudo mdadm --create /dev/md0 --level=6 --raid-devices=4 /dev/sda /dev/sdb /dev/sdc /dev/sdd`

## NVIDIA Container Runtime

There are extra steps to install the NVIDIA container runtime. This
is necessary to run a Docker container with GPU access.

```sh
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update

export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
sudo apt-get install -y \
  nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```
 
