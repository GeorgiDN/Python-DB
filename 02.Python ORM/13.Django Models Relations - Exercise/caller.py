import os

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, \
    Car
from datetime import timedelta, date, datetime
from populate_db_script import populate_model_with_data
import random
import string


# # 1.
def show_all_authors_with_their_books() -> str:
    all_authors = Author.objects.all().order_by("id")

    authors_with_books = []
    for author in all_authors:
        books = Book.objects.filter(author=author)

        if books:
            authors_with_books.append(
                f'{author.name} has written - {", ".join(b.title for b in books)}!'
            )

    return '\n'.join(authors_with_books)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )

# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)
#
# # Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())



# # 2.
def add_song_to_artist(artist_name: str, song_title: str):
    current_artist = Artist.objects.get(name=artist_name)
    current_song = Song.objects.get(title=song_title)
    current_artist.songs.add(current_song)


def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str):
    current_artist = Artist.objects.get(name=artist_name)
    current_song = Song.objects.get(title=song_title)
    current_artist.songs.remove(current_song)


# # Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")
#
# # Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")
#
# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
#
# # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")



# # 3.
def calculate_average_rating_for_product_by_name(product_name: str):
    product_object = Product.objects.get(name=product_name)
    reviews_object = product_object.reviews.all()

    total_rating = sum(r.rating for r in reviews_object)
    count_reviews = len(reviews_object)
    average_rating = total_rating / count_reviews
    return average_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews():
    get_products_with_no_reviews().delete()


# Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)

# # Run the function to get products without reviews
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
# # Run the function to delete products without reviews
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
#
# # Calculate and print the average rating
# print(calculate_average_rating_for_product_by_name("Laptop"))


# # 4.License
def calculate_licenses_expiration_dates():
    all_driving_licenses = DrivingLicense.objects.all().order_by("-license_number")
    licenses_data = {}
    result = ""

    for dr_license in all_driving_licenses:
        expiration_date = dr_license.issue_date + timedelta(days=365)
        expiration_date = expiration_date.strftime("%Y-%m-%d")
        if dr_license not in licenses_data:
            licenses_data[dr_license.license_number] = expiration_date

    for license_num, expiration_date in licenses_data.items():
        result += f"License with number: {license_num} expires on {expiration_date}!\n"

    return result.strip()


def get_drivers_with_expired_licenses(due_date: date):
    min_created_date = due_date - timedelta(days=365)
    drivers_with_expired_license = Driver.objects.filter(license__issue_date__gt=min_created_date)
    return drivers_with_expired_license


# # Create drivers
# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
#
# # Create licenses associated with drivers
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
#
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)
#
# # Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)
#
# # Get drivers with expired licenses
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
#
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")
#


# # 5.
def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car_id__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.registration = registration
    car.save()

    registration.registration_date = datetime.now()
    registration.car = car
    registration.save()

    return \
        f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."


# # Create owners
# owner1 = Owner.objects.create(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')
#
# # Create cars
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')
#
# print(register_car_by_owner(owner1))


#####################################################
# FOR TEST
# owner3 = Owner.objects.get(name="George Tyson")
# car3 = Car.objects.get(model="BMW", year=2000)
# registration3 = Registration.objects.get(registration_number="XZ0234")

# car3.owner = owner3
# car3.save()

# registration3.car = car3
# registration3.save()


# def generate_random_string(min_len=4, max_len=10):
#     length = random.randint(min_len, max_len)
#     characters = string.ascii_letters + string.digits  # Use letters and digits
#     random_string = ''.join(random.choice(characters) for _ in range(length))
#     return random_string
#
#
# for i in range(1, 11):
#     reg_number = generate_random_string(min_len=4, max_len=10)
#     Registration.objects.create(registration_number=reg_number, registration_date=datetime.now())
#
#


