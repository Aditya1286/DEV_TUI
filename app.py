from textual.app import App, ComposeResult
from textual.widgets import Footer, Static
import psutil
import time
import socket
import requests

# ---------------- FIXED ASCII BANNER ----------------
class Banner(Static):
    def on_mount(self):
        banner = (
            "\n"
            "  ██████╗ ███████╗██╗   ██╗    ██████╗ ███████╗███████╗██╗  ██╗\n"
            "  ██╔══██╗██╔════╝██║   ██║    ██╔══██╗██╔════╝██╔════╝██║ ██╔╝\n"
            "  ██║  ██║█████╗  ██║   ██║    ██║  ██║█████╗  ███████╗█████╔╝ \n"
            "  ██║  ██║██╔══╝  ╚██╗ ██╔╝    ██║  ██║██╔══╝  ╚════██║██╔═██╗ \n"
            "  ██████╔╝███████╗ ╚████╔╝     ██████╔╝███████╗███████║██║  ██╗\n"
            "  ╚═════╝ ╚══════╝  ╚═══╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝\n"
            "\n"
            "                    🚀  DEV DESK"
        )
        self.update(banner)

# ---------------- CLOCK ----------------
class Clock(Static):
    def on_mount(self):
        self.set_interval(1, self.update_time)

    def update_time(self):
        self.update(f"🕒 TIME\n{time.strftime('%H:%M:%S')}")

# ---------------- SYSTEM ----------------
class SystemStats(Static):
    def on_mount(self):
        self.set_interval(1, self.update_stats)

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        self.update(f"💻 SYSTEM\nCPU: {cpu}%\nRAM: {ram}%")

# ---------------- NETWORK ----------------
class NetworkInfo(Static):
    def on_mount(self):
        self.set_interval(5, self.update_net)

    def update_net(self):
        hostname = socket.gethostname()
        try:
            ip = socket.gethostbyname(hostname)
        except:
            ip = "N/A"
        self.update(f"🌐 NETWORK\nHost: {hostname}\nIP: {ip}")

# ---------------- UPTIME ----------------
class Uptime(Static):
    def on_mount(self):
        self.set_interval(5, self.update_uptime)

    def update_uptime(self):
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
        self.update(f"⏱ UPTIME\n{uptime_string}")

# ---------------- DISK ----------------
class DiskUsage(Static):
    def on_mount(self):
        self.set_interval(5, self.update_disk)

    def update_disk(self):
        disk = psutil.disk_usage('/')
        self.update(f"💾 DISK\nUsage: {disk.percent}%")

# ---------------- LOGS ----------------
class LogsViewer(Static):
    def on_mount(self):
        self.set_interval(3, self.update_logs)

    def update_logs(self):
        try:
            with open("logs.txt", "r") as f:
                lines = f.readlines()[-8:]
                self.update("📜 LOGS\n" + "".join(lines))
        except:
            self.update("No logs found")

# ---------------- WEATHER ----------------
class Weather(Static):
    def on_mount(self):
        self.set_interval(600, self.update_weather)

    def update_weather(self):
        try:
            res = requests.get("https://wttr.in/?format=3")
            self.update(f"🌦 WEATHER\n{res.text}")
        except:
            self.update("Weather unavailable")

# ---------------- MAIN APP ----------------
class Dashboard(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "refresh", "Refresh"),
    ]

    CSS = """
    Screen {
        layout: grid;
        grid-size: 2 4;
        grid-gutter: 1;
        padding: 1;
    }

    #banner {
        column-span: 2;
        border: round cyan;
        padding: 0 1;
        background: #0f1117;
        color: #00ff00;
        content-align: left middle;
        height: 11;
        overflow: hidden;
    }

    Static {
        border: round #00ff00;
        padding: 1;
        background: #0f1117;
        color: #00ff00;
    }

    Footer {
        background: #111;
        color: cyan;
    }
    """

    def compose(self) -> ComposeResult:
        yield Banner(id="banner")
        yield Clock()
        yield SystemStats()
        yield NetworkInfo()
        yield Uptime()
        yield DiskUsage()
        yield LogsViewer()
        yield Weather()
        yield Footer()


if __name__ == "__main__":
    Dashboard().run()
