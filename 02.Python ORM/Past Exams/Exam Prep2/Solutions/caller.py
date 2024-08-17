import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Profile, Product, Order
from django.db.models import Count, Q, F


# # 4.Django Queries I


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = (Q(full_name__icontains=search_string) |
             Q(email__icontains=search_string) |
             Q(phone_number__icontains=search_string))

    found_profiles = Profile.objects.filter(query).order_by("full_name")
    if not found_profiles:
        return ""

    result = []
    for profile in found_profiles:
        num_of_orders = profile.profile_orders.count()
        result.append(f"Profile: {profile.full_name}, "
                      f"email: {profile.email}, "
                      f"phone number: {profile.phone_number}, "
                      f"orders: {num_of_orders}")

    return "\n".join(result)


# print(get_profiles("Profile1@Profile1.com"))


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()
    if not loyal_profiles:
        return ""

    return "\n".join(f"Profile: {profile.full_name}, orders: {profile.num_orders}" for profile in loyal_profiles)


# print(get_loyal_profiles())


def get_last_sold_products():
    latest_order = (Order.objects.prefetch_related("products").
                    order_by("-creation_date", "products__name").first())

    if not latest_order or latest_order.products.count() == 0:
        return ""

    all_products = ", ".join(p.name for p in latest_order.products.all())
    return f"Last sold products: {all_products}"


# print(get_last_sold_products())


# # 5.
def get_top_products():
    top_products = (Product.objects
                    .annotate(count_orders=Count("products_orders"))
                    .filter(count_orders__gt=0)
                    .order_by("-count_orders", "name"))[:5]

    if not top_products:
        return ""

    result = ["Top products:"]
    for product in top_products:
        result.append(f"{product.name}, sold {product.count_orders} times")

    return "\n".join(result)


# print(get_top_products())


def apply_discounts():
    orders_for_discount = (Order.objects.annotate(count_products=Count("products")).
                           filter(count_products__gt=2, is_completed=False))

    num_of_updated_orders = orders_for_discount.update(total_price=F("total_price") * 0.9)

    return f"Discount applied to {num_of_updated_orders} orders."


# print(apply_discounts())


def complete_order():
    oldest_order = (Order.objects.prefetch_related("products").filter(is_completed=False).
                    order_by("creation_date").first())

    if not oldest_order:
        return ""

    oldest_order.is_completed = True
    oldest_order.save()

    all_products = oldest_order.products.all()

    for product in all_products:
        product.in_stock -= 1
        if product.in_stock == 0:
            product.is_available = False
        product.save()

    return "Order has been completed!"


# print(complete_order())
