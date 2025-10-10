# `treehouse` 🌳🏘️

## Primary Setup

This repo contains configurations and services for my home server.
These steps define the primary requirements needed by the system
to get up and running.

- Settings >> Power >> Performance >> Screen Blank (Never)
- Install NVIDIA driver with:
  - Determine driver with `sudo ubuntu-drivers devices`
  - Update lists with `sudo apt-get update`
  - Install NVIDIA recommended driver (most likely `nvidia-driver-570`)
  - `sudo reboot`
- Install `curl` with `sudo apt install curl`
- Install `tailscale` for VPN with:
  - `curl -fsSL https://tailscale.com/install.sh | sh`
  - `sudo tailscale up`
  - `sudo tailscale set --ssh`
- Install `git` to clone this repo with `sudo apt install git`
- Install `gh` for auth with:
  - `sudo apt install gh`
  - `gh auth login`
- Setup RAID 6 array with:
  - Install `mdadm` with `sudo apt install mdadm`
  - **New System:**
    - Ensure all 4 drives are **partition free** and named `sd[a-d]`
    - Create the array `sudo mdadm --create /dev/md0 --level=6 --raid-devices=4 /dev/sda /dev/sdb /dev/sdc /dev/sdd`
    - Determine the current location with `cat /proc/mdstat` (wait until complete, this can take a long time)
    - Format the array with `sudo fsck.ext4 /dev/md<location>`
  - **Reinstall OS, Existing RAID:**
    - Find drives with `sudo mdadm --examine --scan`
    - Attach drives with `sudo mdadm --assemble --scan`
    - Determine the current location with `cat /proc/mdstat`
  - **Finish Setup:**
    - Determine the block ID with `sudo blkid /dev/<location>`
    - Create a persistent mount with `sudo sh -c 'echo "UUID=<block ID> /mnt/raid ext4 defaults 0 0" >> /etc/fstab'`
- Install [Docker](https://docs.docker.com/engine/install/ubuntu/) with `apt`
    - Be sure to run the post install steps (e.g., so you can run `docker` without `sudo`)
- Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
- Set the NVIDIA toolkit to always run `sudo nvidia-ctk runtime configure --runtime=docker`
- Reboot with `sudo reboot`
- Run containers with `sudo docker compose up --build` in the root and in `immich/`
