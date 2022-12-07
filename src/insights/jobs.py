from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf8") as arquivo:
        arquivo_csv = csv.DictReader(arquivo, delimiter=",")
        return [row for row in arquivo_csv]


def get_unique_job_types(path: str) -> List[str]:
    lista_data = read(path)
    data = set()

    for item in lista_data:
        if item["job_type"] != "":
            data.add(item["job_type"])

    return data


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [item for item in jobs if item["job_type"] == job_type]
