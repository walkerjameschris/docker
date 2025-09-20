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
  - `sudo apt install mdadm`
  - Ensure all 4 drives are **partition free** and named `sd[a-d]`
  - `sudo mdadm --create /dev/md0 --level=6 --raid-devices=4 /dev/sda /dev/sdb /dev/sdc /dev/sdd`
