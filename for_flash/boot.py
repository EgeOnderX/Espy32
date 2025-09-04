#boot.py
import machine, os, sys, time
from hal import *


# On-board LED for kernel panic
led = machine.Pin(2, machine.Pin.OUT)
# Try to mount SD card

def mount_sd():
    try:
        spi = machine.SPI(2, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19))
        cs = machine.Pin(5, machine.Pin.OUT)

        # Doğru: direkt SDCard kullan
        sd = SDCard(spi, cs)
        vfs = os.VfsFat(sd)
        os.mount(vfs, "/sd")

        print("[BOOT] SD card successfully mounted.")
        return True

    except OSError as e:
        print(f"[BOOT] Failed to mount SD card: {e}")
        return False


# Kernel panic function
def kernel_panic(missing_files):
    print("=== KERNEL PANIC ===")
    print("Missing critical files:", missing_files)
    for _ in range(5):
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)
    try:
        print("[BOOT] Entering rescue mode...")
        __import__("backup")
    except:
        print("backup.py failed to start! System halted.")
        led.value(1)
        time.sleep(5)
        sys.exit()

# Main boot procedure
def boot():
    print("=== Espy32 Bootloader ===")

    # Mount SD card first
    if not mount_sd():
        print("[BOOT] SD card not detected. Entering rescue mode...")
        __import__("backup")
        return

    # Check for required kernel files on SD card
    required_files = ["espinit.py", "startup.py"]
    sd_files = os.listdir("/sd")
    missing_files = [f for f in required_files if f not in sd_files]

    if missing_files:
        kernel_panic(missing_files)
        return

    # Start PY-DOS kernel from SD card
    sys.path.append("/sd")
    import espinit

    disk = Disk()
    espinit.start_terminal(disk)

boot()
