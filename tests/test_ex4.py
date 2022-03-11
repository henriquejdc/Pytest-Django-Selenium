# import pytest
# from django.contrib.auth.models import User

# # function  run once per test
# # class     run once per class of tests
# # module    run once per module
# # session   run once per session

# # @pytest.mark.django_db
# # def test_set_check_password(user_1):
# #     user_1.set_password("new-password")
# #     assert user_1.check_password("new-password") is True

# # def test_set_check_password1(user_1):
# #     print("check-user1")
# #     assert user_1.username == "test-user"

# # def test_set_check_password2(user_1):
# #     print("check-user2")
# #     assert user_1.username == "test-user"

# # def test_new_user(new_user2):
# #     print(new_user2.is_staff)
# #     assert new_user2.first_name == "MyName"

# # @pytest.mark.django_db
# # def test_new_user(db, user_factory):
# #     user = user_factory.create() # Cria e salva
# #     count = User.objects.all().count()
# #     print(user.username, count)
# #     assert True

# # def test_new_user(new_user1):
# #     print(new_user1.username)
# #     assert True

# def test_product(db, product_factory):
#     product = product_factory.create()
#     print(product.description)
#     assert True