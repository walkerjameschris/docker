# `treehouse` 🌳🏘️

## Primary Setup

This repo contains configurations and services for my home server.
These steps define the primary requirements needed by the system
to get up and running.

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
  - Install `mdadm` with `sudo apt install mdadm`
  - Ensure all 4 drives are **partition free** and named `sd[a-d]`
  - Create the array `sudo mdadm --create /dev/md0 --level=6 --raid-devices=4 /dev/sda /dev/sdb /dev/sdc /dev/sdd` 
  - Determine the current location with `/proc/mdstat` (wait until complete, this can take a long time)
  - Format the array with `sudo fsck.ext4 /dev/md<location>`
  - Mount the array with `mkdir /mnt/raid; sudo mount /dev/md<location> /mnt/raid`
  - Determine the block ID with `sudo blkid /dev/md127`
  - Create a persistent mount with `sudo sh -c 'echo "UUID=<block ID> /mnt/raid ext4 defaults 0 0" >> /etc/fstab'`
- Install [Docker Desktop](https://docs.docker.com/desktop/setup/install/linux/ubuntu/) 
- Install [NVIDIA Container Dolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
- Set the NVIDIA toolkit to always run `sudo nvidia-ctk runtime configure --runtime=docker`
- Reboot with `sudo reboot`
- Run `lab/` with `sudo docker compose up --build`
