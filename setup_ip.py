#!/usr/bin/env python3
import subprocess
import time

SSID = "IOT LAB"
PASSWORD = "Dixon#10TL@b"
STATIC_IP = "10.1.40.2/23"
ROUTER = "10.1.40.1"
DNS = "10.1.40.1"

def configure_wifi():
    wpa_config = f"""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IN

network={{
    ssid=\"{SSID}\"
    psk=\"{PASSWORD}\"
    key_mgmt=WPA-PSK
}}"""
    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
        f.write(wpa_config)
    print("✅ Wi-Fi configuration set for 'IOT LAB'.")

def configure_static_ip():
    static_config = f"""
interface wlan0
static ip_address={STATIC_IP}
static routers={ROUTER}
static domain_name_servers={DNS}"""
    with open("/etc/dhcpcd.conf", "a") as f:
        f.write(static_config)
    print("✅ Static IP configuration applied.")

def reboot_system():
    print("🔁 Rebooting in 5 seconds to apply changes...")
    time.sleep(5)
    subprocess.run(["sudo", "reboot"])

def main():
    configure_wifi()
    configure_static_ip()
    reboot_system()

if __name__ == "__main__":
    main()
