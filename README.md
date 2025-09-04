# Espy32 ( 1.0.6 )
An operating system fully based on MicroPython for ESP32. It can run Python scripts, load drivers, write programs in its built-in Python interpreter, and even play basic music.

**Developed from scratch by Ege.**

> **NOTE:** The previous version may run a bit slow due to some unexpected errors encountered today like this:
```
ets Jul 29 2019 12:21:46

rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0030,len:4112
load:0x40078000,len:15072
load:0x40080400,len:4
load:0x40080404,len:3332
entry 0x400805ac

MPY: soft reboot
=== Espy32 Bootloader ===
[BOOT] Failed to mount SD card: timeout waiting for response
[BOOT] SD card not detected. Entering rescue mode...
=== Espy32 Rescue Mode ===
SD card missing or kernel files are corrupted.
Available commands: dir | reboot | exit
rescue> REBOOT
mode:DIO, clock div:2
=== Espy32 Bootloader ===
[BOOT] Failed to mount SD card: no SD card
[BOOT] SD card not detected. Entering rescue mode...
=== Espy32 Rescue Mode ===
SD card missing or kernel files are corrupted.
Available commands: dir | reboot | exit
rescue> 
```
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
