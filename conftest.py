# import pytest
# from django.contrib.auth.models import User
# from pytest_factoryboy import register
# from tests.factories import UserFactory, ProductFactory, CategoryFactory

# register(UserFactory)
# register(ProductFactory)
# register(CategoryFactory)

# # @pytest.fixture()
# # def user_1(db):
# #     print("create-user")
# #     user = User.objects.create_user("test-user")
# #     return user

# # @pytest.fixture()
# # def new_user_factory(db):

# #     def create_app_user(
# #         username: str,
# #         password: str = None,
# #         first_name: str = "firstname",
# #         last_name: str = "lastname",
# #         email: str = "test@test.com",
# #         is_staff: str = False,
# #         is_superuser: str = False,
# #         is_active: str = True,
# #     ):
# #         user = User.objects.create_user(
# #             username=username,
# #             password=password,
# #             first_name=first_name,
# #             last_name=last_name,
# #             email=email,
# #             is_staff=is_staff,
# #             is_superuser=is_superuser,
# #             is_active=is_active,
# #         )
# #         return user

# #     return create_app_user

# # @pytest.fixture
# # def new_user1(db, new_user_factory):
# #     return new_user_factory("Test_user","password","MyName")

# # @pytest.fixture
# # def new_user2(db, new_user_factory):
# #     return new_user_factory("Test_user","password", "MyName", is_staff="True")

# # Factory
# def new_user1(db, user_factory):
#     user = user_factory.build() # Apenas monta, mas não salva
#     assert user

