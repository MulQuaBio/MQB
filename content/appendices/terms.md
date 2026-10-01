(mqb-terms)=
# Key computing terms

Use this page when an unfamiliar computing term appears in MQB. Each chapter explains a term again when it is needed for an activity; this page is a short place to look it up.

(terms-terminal)=
## Terminal

A **terminal** is an application window where you type commands and see their output. On macOS it is usually called Terminal; on Linux it may be Terminal, GNOME Terminal or a similar name. VS Code also has an integrated terminal.

(terms-shell)=
## Shell

A **shell** is the program inside a terminal that reads the commands you type and starts other programs. MQB mainly uses Bash. A terminal is the window; the shell is the command-reading program in that window.

(terms-paths)=
## Paths and the current directory

A **path** names the location of a file or folder. The **current directory** is the folder a terminal or program is using right now. The `pwd` command prints that folder.

An **absolute path** gives the complete location, starting at the top of the file system. For example, `/opt/homebrew/bin/brew` is an absolute path on many Apple Silicon Macs. A **relative path** starts from the current directory, such as `data/observations.csv`.

(terms-project-root)=
## Project root

A **project root** is the main folder for one piece of coursework or project. It commonly contains folders such as `code`, `data` and `results`. Open this folder in VS Code and return to it before following project-level commands.

(terms-path)=
## PATH

`PATH` is a list of folders that a shell searches when you type a command name. If the folder containing a program is on `PATH`, you can type the program's short name, such as `brew`, instead of its full path. `command -v NAME` shows the location the shell would use for a command named `NAME`.

(terms-startup-file)=
## Startup file

A **startup file** is a settings file that a shell reads when a new terminal session starts. A line added there affects future sessions. To apply the change to the current terminal, source the file explicitly or close and reopen the terminal. Your shell and the kind of terminal session determine which startup file it reads; follow the setup instructions for your own system and change only the line you added.

(terms-package-manager)=
## Package manager and package

A **package manager** installs, updates and removes software in a controlled way. Homebrew on macOS and APT on Ubuntu are package managers. A **package** is one unit of software managed this way; it may provide a command, a library or an application.

(terms-environment)=
## Python environment and interpreter

A Python **interpreter** is the program that runs Python code. A Python **environment** is a project-specific place where that interpreter uses its own installed packages. A `venv` is the standard Python tool for creating such an environment. Activating it tells the current terminal to use that project's Python first.

(terms-kernel)=
## Notebook kernel

A notebook **kernel** is the running program that executes notebook cells and keeps variables in memory. A Python interpreter selected for a script and a kernel selected for a notebook can be different, so check both when working in an editor.

(terms-repository)=
## Repository and remote

A Git **repository** is a project folder together with its saved history of changes. A **remote** is another copy of that repository, usually hosted on a service such as GitHub. `origin` is a conventional name for a remote; it is a label chosen in your local repository, not the name of a special GitHub server.

(terms-ssh)=
## SSH keys

SSH uses a pair of related files to prove that you control an account. The **private key** stays on your computer and must remain secret. The **public key** can be added to GitHub. A **passphrase** protects a private key if the file is copied; it is not your GitHub password.
