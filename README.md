# 🖥️ DEV_TUI — Terminal Developer Dashboard

A sleek, real-time **TUI (Text User Interface) developer dashboard** built with Python and [Textual](https://github.com/Textualize/textual). Monitor your system vitals, network info, logs, and even the weather — all without leaving your terminal.

---

## ✨ Features

| Widget | Description |
|---|---|
| 🚀 **ASCII Banner** | Stylish DEV DESK header rendered in ASCII art |
| 🕒 **Live Clock** | Real-time clock updated every second |
| 💻 **System Stats** | Live CPU and RAM usage percentage |
| 🌐 **Network Info** | Hostname and local IP address |
| ⏱️ **Uptime** | System uptime since last boot |
| 💾 **Disk Usage** | Root partition disk usage percentage |
| 📜 **Logs Viewer** | Tails the last 8 lines from `logs.txt` in real time |
| 🌦️ **Weather** | Current weather via [wttr.in](https://wttr.in) (refreshes every 10 min) |

---

## 📁 File Structure

```
DEV_TUI/
├── app.py       # Main application — all widgets and dashboard layout
└── logs.txt     # Log file read by the Logs Viewer widget
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Aditya1286/DEV_TUI.git
cd DEV_TUI
```

**2. Install dependencies**

```bash
pip install textual psutil requests
```

### Running the Dashboard

```bash
python app.py
```

---

## ⌨️ Keybindings

| Key | Action |
|-----|--------|
| `q` | Quit the dashboard |
| `r` | Refresh the dashboard |

---

## 🔧 Configuration

### Custom Logs

The **Logs Viewer** reads from `logs.txt` in the project root. You can point it to any log file by editing this line in `app.py`:

```python
with open("logs.txt", "r") as f:
```

Replace `"logs.txt"` with the path to your desired log file (e.g., `/var/log/syslog`).

### Weather Location

By default, weather is auto-detected by IP. To pin a specific location, update the weather request URL in `app.py`:

```python
res = requests.get("https://wttr.in/YourCity?format=3")
```

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| [textual](https://github.com/Textualize/textual) | TUI framework for building the dashboard UI |
| [psutil](https://github.com/giampaolo/psutil) | System and process utilities (CPU, RAM, Disk, Uptime) |
| [requests](https://github.com/psf/requests) | HTTP requests for weather data |
| `socket` | Standard library — hostname and IP resolution |
| `time` | Standard library — clock and uptime formatting |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **TUI Framework:** [Textual](https://textual.textualize.io/)
- **System Monitoring:** psutil
- **Weather API:** [wttr.in](https://wttr.in)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Feel free to use and modify it.

---

## 👨‍💻 Author

**Aditya1286** — [GitHub Profile](https://github.com/Aditya1286)

---

> *Built with ❤️ for developers who live in the terminal.*
