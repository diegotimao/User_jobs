from src.pre_built.sorting import sort_by

mock_jobs = [
    {
        "title": "Back end developer",
        "2000": "full time",
        "min_salary": "1600",
        "max_salary": "1650",
        "date_posted": "2018-03-03",
    },
    {
        "title": "Front",
        "salary": "2000",
        "tupe": "trainee",
        "min_salary": "1000",
        "max_salary": "2500",
        "date_posted": "2018-03-01",
    },
    {
        "title": "Full stack end developer",
        "4000": "full time",
        "min_salary": "1500",
        "max_salary": "1900",
        "date_posted": "2018-03-02",
    },
]


mock_jobs_sorted_min_salary = [
    {
        "title": "Front",
        "salary": "2000",
        "tupe": "trainee",
        "min_salary": "1000",
        "max_salary": "2500",
        "date_posted": "2018-03-01",
    },
    {
        "title": "Full stack end developer",
        "4000": "full time",
        "min_salary": "1500",
        "max_salary": "1900",
        "date_posted": "2018-03-02",
    },
    {
        "title": "Back end developer",
        "2000": "full time",
        "min_salary": "1600",
        "max_salary": "1650",
        "date_posted": "2018-03-03",
    },
]


def test_sort_by_criteria():
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == mock_jobs_sorted_min_salary
