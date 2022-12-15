from src.pre_built.sorting import sort_by

mock_jobs_min = [
    {"date_posted": "2018-03-03", "max_salary": "3950", "min_salary": "1600"},
    {"date_posted": "2018-03-01", "max_salary": "2100", "min_salary": "1500"},
    {"date_posted": "2018-03-02", "max_salary": "1900", "min_salary": "1200"},
]

mock_jobs_min_sorted = [
    {"date_posted": "2018-03-02", "max_salary": "1900", "min_salary": "1200"},
    {"date_posted": "2018-03-01", "max_salary": "2100", "min_salary": "1500"},
    {"date_posted": "2018-03-03", "max_salary": "3950", "min_salary": "1600"},
]


def test_sort_by_criteria():

    sort_by(mock_jobs_min, "min_salary")
    assert mock_jobs_min == mock_jobs_min_sorted
