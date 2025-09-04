#backup.py
import os, sys

print("=== Espy32 Rescue Mode ===")
print("SD card missing or kernel files are corrupted.")
print("Available commands: dir | reboot | exit")

while True:
    cmd = input("rescue> ").strip().lower()

    if cmd == "dir":
        try:
            print("Flash contents:", os.listdir("/flash"))
            if "sd" in os.listdir("/"):
                print("SD contents:", os.listdir("/sd"))
            else:
                print("SD card is not detected.")
        except Exception as e:
            print(f"[ERROR] {e}")

    elif cmd == "reboot":
        print("Rebooting device...")
        sys.exit()

    elif cmd == "exit":
        print("Exiting rescue mode.")
        break
    else:
        pass
