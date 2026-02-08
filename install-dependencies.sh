#!/usr/bin/env bash
set -euo pipefail

# Arch Linux dependency installer for this dotfiles repo.
# Keep this list pragmatic: only what the configs/scripts actually use.

PACMAN_PKGS=(
  hyprland
  waybar
  kitty
  ulauncher
  swaybg
  swaync
  nwg-dock-hyprland
  fastfetch
  figlet
  wl-clipboard
  grim
  slurp
  brightnessctl
  pamixer
  playerctl
  pavucontrol
  fcitx5
  blueman
  dunst
  light
  brillo
  python
  python-pip
)

echo "Installing pacman packages..."
sudo pacman -Syu --needed "${PACMAN_PKGS[@]}"

echo
echo "Optional (AUR): figlet-fonts"
echo "If you use yay: yay -S figlet-fonts"
