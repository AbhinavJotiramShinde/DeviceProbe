# DEVICE PROBE
A Flask-based web application created for network scanning. Once the devices connected to gateway are known, it conducts a port scanning of all the discovered devices. Output is displayed on HTTP page.


Function:
Discover devices on a local network using ARP requests.
Retrieve IP, MAC address, and Hostname of each device.
Perform on-demand TCP port scans on any discovered host.


Features:
Network Discovery: Enter Gateway & Subnet to find all active hosts.
MAC & Hostname Resolution: Automatically fetches MAC address and reverse-DNS hostname.
Port Scanning: Click on any detected device to scan its open TCP ports.
Multi-threaded Scanning: Faster results using Python threads.
Simple Web UI: Built with HTML, CSS, and JavaScript.


Project Structure:
DeviceProbe/
├─ app.py                 # Flask backend entry point
├─ network_scan.py        # ARP-based network device scanner
├─ port_scan.py           # TCP port scanner
├─ templates/
│   └─ index.html         # Web interface
└─ static/
    └─ style.css          # Frontend styles


Installation & Setup:
1. Clone the repository:
git clone https://github.com/AbhinavJotiramShinde/DeviceProbe.git
cd netscope

2. Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Running the App:
python app.py

5. Then open your browser and go to:
http://127.0.0.1:5000


How It Works:
User enters Gateway and Subnet mask.
The backend sends ARP requests to detect live hosts.
For each host it:
a.Retrieves IP & MAC address
b.Resolves hostname (if available)
c.Click “Scan Ports” on any host to run a TCP port scan and display the open ports.


Author: Abhinav Jotiram Shinde
