import random
import time
from datetime import datetime

# Параметры для генерации логов
ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
urls = ["/login", "/home", "/dashboard"]
statuses = [200, 404, 500]
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
]
referers = ["https://example.com", "https://another-example.com"]


def generate_log_entry():
    ip = random.choice(ip_addresses)
    url = random.choice(urls)
    status = random.choice(statuses)
    user_agent = random.choice(user_agents)
    referer = random.choice(referers)
    response_size = random.randint(500, 5000)
    response_time = round(random.uniform(0.1, 1.5), 3)  # Время ответа в секундах
    timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")

    log_entry = (
        f'{ip} - - [{timestamp}] "GET {url} HTTP/1.1" {status} {response_size} '
        f'"{referer}" "{user_agent}" {response_time}'
    )
    return log_entry


def generate_logs(file_path, num_entries=100):
    with open(file_path, "w") as log_file:
        for _ in range(num_entries):
            log_entry = generate_log_entry()
            log_file.write(log_entry + "\n")
            time.sleep(0.1)  # Задержка для имитации реального времени


# Генерация логов
log_file_path = r"D:\study\MyPythonProjects\nginx-log-analyzer\logs\access.log"
generate_logs(log_file_path, num_entries=5000)
