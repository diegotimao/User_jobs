from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    file_csv = read(path)

    return max(
        [
            int(salary["max_salary"])
            for salary in file_csv
            if (salary["max_salary"]).isdigit()
        ]
    )


def get_min_salary(path: str) -> int:
    file_csv = read(path)

    return min(
        [
            int(salary["min_salary"])
            for salary in file_csv
            if (salary["min_salary"]).isdigit()
        ]
    )


def verify_data_jobs(jobs):
    if "min_salary" not in jobs or "max_salary" not in jobs:
        raise ValueError

    if not isinstance(jobs["min_salary"], (int, str)) or not isinstance(
        jobs["max_salary"], (int, str)
    ):
        raise ValueError

    if (
        not str(jobs["min_salary"]).isnumeric()
        or not str(jobs["max_salary"]).isnumeric()
    ):
        raise ValueError

    if int(jobs["min_salary"]) > int(jobs["max_salary"]):
        raise ValueError


def verify_salary(salary):
    if isinstance(salary, (int, str, float)) is False:
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    verify_data_jobs(job)
    verify_salary(salary)
    return int(salary) <= int(job["max_salary"]) and int(salary) >= int(
        job["min_salary"]
    )


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    range_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                range_jobs.append(job)
        except ValueError:
            pass
    return range_jobs
