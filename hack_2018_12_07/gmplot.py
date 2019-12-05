from geopy.distance import geodesic
from geopy.geocoders import Nominatim


class Adres_read():
    def __init__(self, adress):
        self.__geolocator = Nominatim(user_agent="specify_your_app_name_here")
        self.__location = self.__geolocator.geocode(adress)
        # self.__location_place = (self.__location.latitude, self.__location.longitude)

        self.__bounding = self.__location.raw['boundingbox']
        # print(self.__bounding[0])
        # geodesic(adress, self.__location_place).m)

    def get_points(self):
        return self.__bounding
