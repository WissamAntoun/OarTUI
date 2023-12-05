# OarTUI
TUI for browsing, canceling, and inspecting OAR jobs on a cluster using only the terminal. just run `oartui` and you're good to go.

# Available utils
- `oartui` : Shows the list of jobs running on the cluster and allows to select one to view it's logs (stderr or stdout), it's full information, delete it or connect to it's node. Other aliases: `oarui`, `oui`

 <!-- show image -->
![jobui](./img/Screenshot%202023-08-11%20144426.png)

# FAQ

### How to select text in the App?
JobUI is running a Textual app which puts your terminal in to application mode which disables clicking and dragging to select text. Most terminal emulators offer a modifier key which you can hold while you click and drag to restore the behavior you may expect from the command line. The exact modifier key depends on the terminal and platform you are running on.

- iTerm Hold the OPTION key.
- Gnome Terminal Hold the SHIFT key.
- Windows Terminal Hold the SHIFT key.

Refer to the documentation for your terminal emulator, if it is not listed above.