# Espy32 ( 1.0.6 )
An operating system fully based on MicroPython for ESP32. It can run Python scripts, load drivers, write programs in its built-in Python interpreter, and even play basic music.

**Developed from scratch by Ege.**

## Features
- 16GB SDHC card support.
- Independent kernel error indicator via D1 pin.
- Improved editor application.
- Bug fixes.
- SD card library embedded into `hal.py`.
- Kernel and boot separation implemented.  
  On ESP32 flash: `hal.py`, `boot.py`, `backup.py`.  
  On SD card: `espinit`, `startup`, `edit`.  
  **Reason:** Prevent flash wear and avoid filling up internal storage.
- Basic system recovery introduced with `backup.py`:
  - Available commands: `dir`, `esboot`, `exit`.
- `get_abs_path` function made secure.
- Maximum depth limit added to the `tree` command.
- `record` command removed due to limited RAM.
- AMS (Anti Malware Service) removed.  
  *(Planned behavior: Core 1 runs the system, Core 2 runs AMS to monitor apps. If abnormal RAM or CPU usage is detected, AMS flags the issue and sends event data to Core 1. Currently not implemented.)*
- You can now directly run Python files using the `run` command.
- `ram` class removed.
- Tested successfully with **16GB SanDisk SDHC** using the **HW-203 SD card module**.
- Deleted format command.

---

## Test Components and Environment:
- **Board:** ESP32 DevKit V1 + passive heatsink  
- **Storage:** HW-203 SD module + 16GB SD card  
- **Audio:** Basic speaker system controlled by **BD139** with passive cooling  
- **I/O:** 2× USB, 2× jack input/output  
- **Power:** 3000mAh battery + 1200mAh charging circuit  
- **Protection:** USB reverse current protection + USB short-circuit protection  

> **Note:** Circuit diagram is unavailable since no schematic exists.

## **Why this project exists while other ESP32 operating systems already exist:**  
Because this system is **fully based on MicroPython**, unlike others that run at a **low hardware level**.  
*(This is also why dual-core support is currently unavailable.)*
## Future Plans
- Add display (screen) support.
- Enable dual-core support for better multitasking.

---

## Version Plan
- This is the **first release** of Espy32.  
- Evolution path:  
  **Py-DOS (Simulator)** → **Py-DOS on ESP32** *(partial operating system)* → **Espy32** *(towards a fully functional operating system)*


**Thank you for checking out this project!**  
⭐ If you like it, consider giving it a star!
