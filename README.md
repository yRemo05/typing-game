# Typing Game

A small desktop typing game built with Python and PyQt5. The app shows a rolling list of words, accepts typed input, starts the timer on the first key press, and tracks basic typing statistics for the session.

## Project Status

Currently implemented:

- [x] PyQt5 desktop window.
- [x] Main entry point in `Main.py`.
- [x] Batch launcher with `start.bat`.
- [x] GUI class in `Source/Graphics.py`.
- [x] Word list loaded from `Data/words.json`.
- [x] Initial round generation from the configured word buffer.
- [x] Rolling word queue that advances after each submitted word.
- [x] Correct word counter.
- [x] Mistyped word counter used for final accuracy.
- [x] Letter key hit counter.
- [x] On-screen keys-hit, correct-words and time-left labels.
- [x] Input field temporarily disables after the timer finishes.

## Requirements

- Python 3
- PyQt5

Install PyQt5 if it is not already available:

```powershell
pip install PyQt5
```

## Running

From the project root:

```powershell
python Main.py
```

Or run the Windows launcher:

```powershell
.\start.bat
```

## Project Structure

```text
Typing_Game/
|-- Data/
|   |-- intent.json
|   `-- words.json
|-- Source/
|   `-- Graphics.py
|-- Main.py
|-- README.md
`-- start.bat
```

## Notes

- `Main.py` currently starts the game with `GUI(25, 2)`, so the configured buffer is 25 words and the configured session length is 2 minutes.
- The visible UI currently creates five word labels, so only five active words are displayed even when a larger word buffer is configured.
- The reset button is styled and shown, but no reset click handler is currently connected.
- `Data/intent.json` exists but is not currently loaded by the application.
