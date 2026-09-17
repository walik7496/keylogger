# ⌨️ Python Keyboard Logger

A simple educational Python project for working with keyboard events using the [`pynput`](https://github.com/moses-palmer/pynput) library.

The program listens for keyboard events and writes received characters to a `log.txt` file.

> ⚠️ **Disclaimer:** This project is intended for educational purposes only. Use it only on your own computer or with the explicit consent of the person using the device. Do not use it to collect passwords, private messages, financial information, or other sensitive data without authorization.

---

## 📌 Features

* Keyboard event handling with `pynput`
* Regular character handling
* Space key support
* Enter key support
* `Esc` key for stopping the listener
* UTF-8 text encoding
* Writes data to `log.txt`
* Opens the log file once instead of reopening it for every keystroke
* Guarantees that the log file is closed when the program exits
* Simple and easy-to-understand implementation

---

## 🛠️ Requirements

* Python **3.8 or newer**
* `pynput`

Install the dependency with:

```bash
pip install pynput
```

Or:

```bash
python -m pip install pynput
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/walik7496/keylogger.git
```

Enter the project directory:

```bash
cd keylogger
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

The program starts listening for keyboard events and writes received characters to:

```text
log.txt
```

Press:

```text
Esc
```

to stop the listener.

---

## 📂 Project Structure

```text
python-keyboard-logger/
│
├── main.py
├── log.txt
├── README.md
```

### `main.py`

Contains the main application logic and keyboard event handling.

### `log.txt`

Stores the generated text output.

---

## ⚙️ How It Works

The program creates a keyboard listener:

```python
Listener(on_press=write_to_file)
```

Whenever a key is pressed, the `write_to_file()` function is called:

```python
def write_to_file(key):
    ...
```

Regular characters are obtained from:

```python
key.char
```

Special keys are handled separately:

```python
if key == Key.space:
    letter = " "
elif key == Key.enter:
    letter = "\n"
elif key == Key.esc:
    return False
```

The log file is opened once when the program starts:

```python
log_file = open("log.txt", "a", encoding="utf-8")
```

Characters can then be written without repeatedly opening and closing the file:

```python
log_file.write(letter)
```

Finally, the file is closed when the program exits:

```python
finally:
    log_file.close()
```

---

## 💡 Why Open the File Only Once?

Opening and closing the file for every single keyboard event is unnecessary.

For example, this approach:

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(letter)
```

opens and closes the file every time the function is called.

Instead, the project keeps the file open while the listener is running:

```python
log_file = open("log.txt", "a", encoding="utf-8")
```

and closes it only when the program finishes.

This reduces unnecessary file operations and makes the implementation cleaner.

---

## 🧪 Example

If the following text is entered:

```text
Hello World!
```

the resulting `log.txt` file may contain:

```text
Hello World!
```

Pressing `Enter` adds a new line.

---

## ⚠️ Limitations

This is a simple educational implementation and should not be considered a fully featured text editor or input recorder.

For example, `Backspace` and `Delete` do not modify previously written data. As a result, the contents of `log.txt` represent the sequence of recorded characters rather than necessarily matching the final text visible on screen.

Keyboard behavior can also vary depending on:

* Operating system
* Keyboard layout
* Python version
* `pynput` version
* System permissions

---

## 🔐 Privacy & Security

Use this software responsibly.

Do **not** use it to:

* Monitor other people without their knowledge
* Capture passwords or authentication codes
* Collect banking or payment information
* Record private communications
* Bypass security or privacy controls

Only use the software where you have the appropriate authorization.

---

## 🧪 Educational Purpose

This project can be useful for learning about:

* Python functions
* Exception handling
* File I/O
* Context managers
* Event listeners
* Keyboard events
* External Python libraries
* Resource management
