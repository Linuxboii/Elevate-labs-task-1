# Network Port Scanner using Nmap & Tshark

This Python script scans your local network for devices with open ports using **Nmap**, and displays the results in a clean table using **PrettyTable**. It also checks if **Tshark** (Wireshark CLI) is installed, for optional live traffic analysis.

The script first uses the `nmap` module to perform a scan on a default subnet (`192.168.1.0/24`, which you can change), looking for open ports in the 1-1024 range. The scan results are then parsed and shown in a neat ASCII table showing the host IP, protocol, port number, port state (open/closed), and the detected service name.

Additionally, the script checks if `tshark` is installed on your system. While the current version doesn’t start a capture automatically, you can use the info it gives you to run your own packet captures using `tshark`.

To run this tool, you need a few dependencies. For Python packages, install them with: `pip install python-nmap prettytable`. For system tools, make sure you have `nmap` and `tshark` installed. On Debian-based systems (like Ubuntu), install them using: `sudo apt install nmap tshark`. On Windows, download and install [Nmap](https://nmap.org/download.html) and [Wireshark](https://www.wireshark.org/#download), and make sure to add both `nmap` and `tshark` to your system PATH.

Once the requirements are met, clone this repository and run the script using: `sudo python3 scanner.py`. It may require root permissions (sudo) for network scanning.
