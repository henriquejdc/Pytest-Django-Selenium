# import pytest
# from django.contrib.auth.models import User

# # function  run once per test
# # class     run once per class of tests
# # module    run once per module
# # session   run once per session

# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test', 'test@test.com', 'test')
#     assert User.objects.count() == 1

# @pytest.mark.django_db
# def test_user_create1():
#     count = User.objects.all().count()
#     assert count == 0