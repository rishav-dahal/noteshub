#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then







    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then







    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

## Starting some nice programs...

# Set a random wallpaper from my Backgrounds directory using Nitrogen
nitrogen --set-scaled --random ~/Pictures/Backgrounds &

# or just restore the previous one
#nitrogen --restore &

# Status bar for dwm
while true; do
    slstatus
done &

# Compositor (window transparency, blur, animations, etc.)
picom &

# Night Light
redshift &

# Autorepeat after 350 ms of delay and set delay rate to 60
# i.e. this makes scrolling faster than by default
xset r rate 330 60 &

# remove mouse when idle
unclutter &

# Notification daemon
dunst &

# Battery alert "daemon"
while true; do
    bash $HOME/.local/bin/battery-alert &&
    sleep 10m
done &

# enable touchpad tap-to-click features
xinput set-prop "SYNA3393:00 06CB:CD41 Touchpad" "libinput Tapping Enabled" 1 &

# remap caps lock key with escape 
#setxkbmap -option caps:swapescape & 

# Window manager
exec dbus-launch dwm
