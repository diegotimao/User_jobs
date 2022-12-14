from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    list_brazilian = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    for bras in list_brazilian:
        response = "title" in bras or "salary" in bras or "type" in bras

        assert response is True
