# Installation

pipx (`pip install pipx`) can manage a venv for this project:

```bash
pipx install --editable .
```

In Windows, this creates `~/pipx/venvs/upenter/Scripts/upenter.exe`, symlinked in `~/.local/bin/`.

You can also invoke its python directly:

```cmd
"%USERPROFILE%\pipx\venvs\upenter\Scripts\pythonw.exe" upenter.py
```

## Use from vscode

I have copied the launcher to a deterministic path and configured it as the vscode "external terminal":

```bash
cp -i ~/.local/bin/upenter.exe /c/dewi/bin/
```

Key binding: Ctrl+Shift+C
