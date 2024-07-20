import sys
from pathlib import Path
from collections import Counter

def parse_log_line(line: str) -> dict:
    """
    Function to write line in a dictionary 

    Returns:
        Dictionary {Date : value, Time : value, Level : value, Message : value}
    """
    parsed_line = line.split()
    message = " ".join(parsed_line[3:])
    return {"Date" : parsed_line[0], "Time" : parsed_line[1],
            "Level" : parsed_line[2], "Message" : message}

def load_logs(file_path: str) -> list:
    """
    Function to parse file and write logs into list

    Returns: 
        List of logs
    """
    if file_path.exists() and file_path.is_file():
        with open(file_path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
        parsed_lines = []
        for line in lines:
            parsed_lines.append(parse_log_line(line))
        return parsed_lines
    else:
        print("Wrong path") 

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Function to filter input logs by level key

    Returns:
        Filtered list
    """
    result = []
    for line in logs:
        if line["Level"] == level:
            result.append(line)
    return result

def count_logs_by_level(logs: list) -> dict:
    """
    Function to count logs with same level key

    Returns:
        Dictionary with counted pairs Level : Count
    """
    return dict(Counter(log["Level"] for log in logs))

def display_log_counts(counts: dict):
    """
    Function to print logs
    """
    print("Рівень логування | Кількість")
    print("-" * 17 + "|" + "-" * 10)
    for key in counts:
        print(f"{key:17}| {counts[key]:<4}")

def main():
    if sys.argv.len() < 2:
        print("Please enter path")
        exit()
    file_path = Path(sys.argv[1])
    parsed_file = load_logs(file_path)
    counted_logs = count_logs_by_level(parsed_file)
    display_log_counts(counted_logs)
    if sys.argv.len() > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(parsed_file, level)
        print(f"Деталі логів для рівня '{level}':")
        for line in filtered_logs:
            print(line["Date"] + " " + line["Time"] + " - " + line["Message"])

if __name__ == "__main__":
    main()
