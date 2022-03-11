# import pytest
# from core.app.models import Product

# @pytest.mark.parametrize(
#     "title, category, description, slug, regular_price, discount_price, validity",
#     {
#         ("NewTitle", 1, "NewDescript", "slugg", "4.20","3.10", True),
#         ("NewTitle1", 1, "NewDescript1", "slugg", "3.20","2.10", True),
#     }
# )

# def test_product_instance(
#         db, 
#         product_factory, 
#         title, 
#         category, 
#         description, 
#         slug, 
#         regular_price, 
#         discount_price, 
#         validity
#     ):

#     test = product_factory (
#         title=title,
#         category_id=category,
#         description=description,
#         slug=slug,
#         regular_price=regular_price,
#         discount_price=discount_price
#     )

#     item = Product.objects.all().count()
#     assert item == validity