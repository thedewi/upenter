# upenter

Presses up, enter in your terminal.

Windows only.

## Installation

```bash
# Make sure uv is installed
winget install --interactive --id astral-sh.uv
uv tool update-shell

# Install as global tool
uv tool install git+https://github.com/thedewi/upenter.git
```

## Use from VS Code

This tool can be installed as the "External Terminal" so it can be easily triggered with a key binding.

Open "User Settings" and edit the JSON to include:

```json
{
    "terminal.external.windowsExec": "upenter",
}
```

Open "Keyboard Shortcuts" and edit the JSON to add these two bindings:

```json
[
    {
        "key": "alt+d",
        "command": "runCommands",
        "args": {
            "commands": [
                {
                    "command": "workbench.action.files.save"
                },
                {
                    "command": "workbench.action.terminal.sendSequence",
                    "args": {
                        "text": "\u001b[A\r"
                    }
                }
            ]
        },
        "when": "view.terminal.visible"
    },
    {
        "key": "alt+d",
        "command": "runCommands",
        "args": {
            "commands": [
                {
                    "command": "workbench.action.files.save"
                },
                {
                    "command": "workbench.action.terminal.openNativeConsole",
                }
            ]
        },
        "when": "!view.terminal.visible"
    }
]
```
