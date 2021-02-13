###--- IMPORTS ---###
import pycountry
from phone_iso3166.country import phone_country
import settings


###--- FUNCTIONS ---###
def get_country_code():
    code = phone_country(settings.PHONE_NUMBER)
    print(code)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    get_country_code()
