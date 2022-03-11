# import pytest

# # function  run once per test
# # class     run once per class of tests
# # module    run once per module
# # session   run once per session

# @pytest.fixture(scope="session")
# def fixture_1():
#     return 1

# @pytest.mark.slow
# def test_example(fixture_1):
#     num = fixture_1
#     assert num == 1

# @pytest.mark.skip # Skip test
# def test_example1():
#     assert 1 == 1