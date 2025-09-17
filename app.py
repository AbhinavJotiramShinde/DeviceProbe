"""
DeviceProbe:
A Flask-based app created for network scanning. Once the devices connected to gateway are known, it conducts a port
scanning of all the discovered devices. Output is displayed on HTTP page.
"""

from flask import Flask, render_template, request, jsonify
from scanner import discover_hosts, scan_ports

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan_network', methods=['POST'])
def scan_network():
    data = request.json
    gateway = data.get('gateway')
    subnet = data.get('subnet')

    if not gateway or not subnet:
        return jsonify({'error': 'Gateway or subnet missing'}), 400

    cidr = f"{gateway}/{subnet}"
    hosts = discover_hosts(cidr)
    return jsonify(hosts)

@app.route('/scan_device', methods=['POST'])
def scan_device():
    data = request.json
    ip = data.get('ip')
    start_port = int(data.get('start_port'))
    end_port = int(data.get('end_port'))

    ports = scan_ports(ip, start_port, end_port)
    return jsonify({'ip': ip, 'open_ports': ports})

if __name__ == '__main__':
    app.run(debug=True)

