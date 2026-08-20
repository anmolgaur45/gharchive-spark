import urllib.request
from pathlib import Path
import time
from datetime import date, timedelta

BASE_URL = "https://data.gharchive.org"


def download_hour(date: str, hour: int, dest_dir: Path) -> bool:

    filename = f"{date}-{hour}.json.gz"
    url = f"{BASE_URL}/{filename}"

    file_path = dest_dir/filename

    if file_path.exists():
        print(f"File '{filename}' already exists. Skipping download")
        return True

    print(f"Downloading {url}...")

    try:

        req = urllib.request.Request(url, headers={"User-Agent": "gharchive-spark/0.1"})
        with urllib.request.urlopen(req) as response:
            file_path.write_bytes(response.read())
        print(f"Successfully downloaded to {file_path}")
        return True

    except Exception as e:
        print(f"Failed to download file. Error: {e}")
        return False


def download_day(date: str, dest_dir: Path) -> list[int]:

    errors = []

    dest_dir.mkdir(parents=True, exist_ok=True)

    for hour in range(24):

        if not download_hour(date, hour, dest_dir):
            errors.append(hour)

    time.sleep(0.5)
    return errors

from datetime import date, timedelta


def download_range(start: str, end: str, dest_dir: Path) -> dict[str, list[int]]:

    start_date = date.fromisoformat(start)
    end_date = date.fromisoformat(end)
    current_date = start_date

    failures = {}

    while current_date <= end_date:
        current_date_str = current_date.isoformat()

        failed_hours = download_day(current_date_str, dest_dir)

        if failed_hours:
            failures[current_date_str] = failed_hours

        current_date += timedelta(days=1)

    return failures