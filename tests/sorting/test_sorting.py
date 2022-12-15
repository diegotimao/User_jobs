from src.pre_built.sorting import sort_by

mock_jobs = [
    {
        "date_posted": "2018-03-03",
        "max_salary": "1650",
        "min_salary": "1600",
    },
    {
        "date_posted": "2018-03-01",
        "max_salary": "2500",
        "min_salary": "1000",
    },
    {
        "date_posted": "2018-03-02",
        "max_salary": "1900",
        "min_salary": "1500",
    },
]


mock_jobs_sorted_min_salary = [
    {
        "date_posted": "2018-03-01",
        "max_salary": "2500",
        "min_salary": "1000",
    },
    {
        "date_posted": "2018-03-02",
        "max_salary": "1900",
        "min_salary": "1500",
    },
    {
        "date_posted": "2018-03-03",
        "max_salary": "1650",
        "min_salary": "1600",
    },
]


def test_sort_by_criteria():
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == mock_jobs_sorted_min_salary
