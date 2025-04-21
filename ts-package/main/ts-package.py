import os
import sys

def ts_package():
    VERSION = "1.0.0"
    print(f"ts-package PACKAGE MANAGER VERSION: {VERSION}")

    while True:
        user_input = input(">> ts-package ")

        if user_input == "install":
            install_input = input(">> ts-package install Coolis1362/")

        if install_input:
            try:
                os.system(f"git clone https://github.com/Coolis1362/{install_input}")
            except Exception as e:
                print(f"ts-package install Coolis1362/{install_input}: ERROR FOUND: ERROR CODE 792: {e}")





if __name__ == "__main__":
    ts_package()