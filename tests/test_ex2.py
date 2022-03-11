# import pytest

# # function  run once per test
# # class     run once per class of tests
# # module    run once per module
# # session   run once per session

# @pytest.fixture(scope="session")
# def yield_fixture():
#     print("Start test phase")
#     yield 6
#     print("End test phase")

# @pytest.mark.slow
# def test_example(yield_fixture):
#     print("run-example-1")
#     assert yield_fixture == 6