from main import Session
from models import User

session = Session()

try:
    session.begin()

    session.query(User).delete()

    session.commit()
    print("All users deleted successfully")

except Exception as e:
    session.rollback()
    print("An error occurred:", str(e))

finally:
    session.close()
