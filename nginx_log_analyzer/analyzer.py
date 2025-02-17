import statistics
from parser import parse_logs

# Путь к файлу логов
log_file_path = r"D:\study\MyPythonProjects\nginx-log-analyzer\logs\access.log"


def generate_report(response_times):
    if not response_times:
        print("Нет данных для анализа.")
        return

    average_time = statistics.mean(response_times)
    median_time = statistics.median(response_times)
    max_time = max(response_times)
    min_time = min(response_times)

    print(f"Среднее время ответа: {average_time:.2f} сек")
    print(f"Медианное время ответа: {median_time:.2f} сек")
    print(f"Максимальное время ответа: {max_time:.2f} сек")
    print(f"Минимальное время ответа: {min_time:.2f} сек")


def main():
    response_times = parse_logs(log_file_path)
    generate_report(response_times)


if __name__ == "__main__":
    main()
