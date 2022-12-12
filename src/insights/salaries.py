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
    if not isinstance(jobs["min_salary"], int) or not isinstance(
        jobs["max_salary"], int
    ):
        raise ValueError

    if jobs["max_salary"] < jobs["min_salary"]:
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        verify_data_jobs(job)
        verify_salary(salary)
        return salary <= job["max_salary"] and salary >= job["min_salary"]
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
