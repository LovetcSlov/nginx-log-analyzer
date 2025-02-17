import re

# Регулярное выражение для парсинга времени ответа из логов
log_pattern = re.compile(r".* (\d+\.\d+)$")


def parse_logs(file_path):
    response_times = []
    with open(file_path, "r") as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                response_time = float(match.group(1))
                response_times.append(response_time)
    return response_times
