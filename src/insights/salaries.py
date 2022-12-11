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


def veryfy_keys(jobs_keys):
    min_salaryes = jobs_keys["min_salary"]
    max_salaryes = jobs_keys["max_salary"]

    if max_salaryes < min_salaryes:
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        veryfy_keys(job)
    except ValueError:
        print("Erro")


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
