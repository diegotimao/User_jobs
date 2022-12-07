from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    file_csv = read(path)
    data = set()

    for item in file_csv:
        if item["industry"] != "":
            data.add(item["industry"])

    return data


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [item for item in jobs if item["industry"] == industry]
