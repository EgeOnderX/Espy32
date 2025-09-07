# Espy32 (v1.0.7)
An operating system fully based on MicroPython for ESP32. It can run Python scripts, load drivers, write programs in its built-in Python interpreter, and even play basic music.

**Developed from scratch by Ege.**

## Features
- 16GB SDHC card support.
- Independent kernel error indicator via **D1 pin**.
- Default editor application (`edit.py`) to write and modify code.
- SD card library embedded into `hal.py`.
- Separated kernel-bootloader system.
- Run Python files directly using the `RUN` command.

---

## Test Components and Environment
- **Board:** ESP32 DevKit V1 + passive heatsink  
- **Storage:** HW-203 SD module + 16GB SD card  
- **Audio:** Basic speaker system controlled by **BD139** with passive cooling  
- **I/O:** 2× USB, 2× jack input/output  
- **Power:** 3000mAh battery + 1200mAh charging circuit  
- **Protection:** USB reverse current protection + USB short-circuit protection  

---

## Why Espy32?
Unlike other ESP32 operating systems that run at a low hardware level, Espy32 is **fully based on MicroPython**, making it easier to run Python scripts and customize behavior.  

*(This is also why dual-core support is currently unavailable.)*

---

## Future Plans
- Add display (screen) support.
- Enable dual-core support for better multitasking.

---

## Commands

- **DIR**       : List files and directories in the current folder
- **TREE**      : Show folder structure recursively
- **TYPE**      : Display the content of a file (`TYPE filename`)
- **WRITE**     : Create or overwrite a file (`WRITE filename content`)
- **DEL**       : Delete a file (`DEL filename`)
- **RENAME**    : Rename a file (`RENAME old_name new_name`)
- **COPY**      : Copy a file (`COPY source_file dest_file`)
- **MKDIR**     : Create a new folder (`MKDIR foldername`)
- **CD**        : Change directory (`CD foldername`, `CD ..`)
- **RUN**       : Execute a Python file (`RUN filename`)
- **SYSINFO**   : Display system and disk information
- **REBOOT**    : Restart Espy32
- **PRINT**     : Print text to screen (`PRINT text`)
- **EDIT**      : Open the editor to modify files
- **RESCUE**    : Enter rescue/backup mode
- **EXIT**      : Exit Espy32
---

## Error Codes
If you see an error like this, take a closer look at the error codes:  

'''
:( Espy32 ran into a problem and needs to restart.
            
Technical information:
            
*** STOP: INVALID_CURRENT_DIR

More info : https://github.com/EgeOnderX/Espy32/
Press any key to restart.
'''

## Error Codes
If Espy32 encounters a problem, the kernel will call the `bsod` function (Bad Screen of Death) and display a stop message. Here's what each error code means:

- `EMPTY_PATH`  
  The path provided to a command is empty or contains only whitespace. Make sure to specify a valid file or folder path.

- `INVALID_CURRENT_DIR`  
  The current working directory (`current_dir`) is invalid (None or not a string). Navigate to a valid directory using `CD`.

- `PATH_NOT_FOUND`  
  The path you specified does not exist on the disk. Check that the file or folder exists.

- `INVALID_PATH`  
  An unexpected exception occurred while resolving the path. This usually means the path format is invalid or contains illegal characters.

- `UNKNOWN ERROR`  
  Used by `bsod` when no error code is provided. Indicates an unspecified problem.


## Security
- A folder depth limit has been added for the `tree` command.
- Security measures have been implemented in `get_abs_path` to prevent invalid paths.
- On every boot, the kernel checks whether the files on the SD card exist.
- If a system file is missing, the **D1 LED** will blink **twice**. You can monitor this via the serial port.


## Version Plan
- Evolution path:  
  **Py-DOS (Python) (Simulator)** → **Py-DOS on ESP32** *(partial operating system)* → **Espy32** *(towards a fully functional operating system)*


**Thank you for checking out this project!**  
⭐ If you like it, consider giving it a star!
