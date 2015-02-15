__author__ = 'Manu'

from backend.apps.providers.models import *


class Jbol(Provider):
    """
    Class to manage Jbol data import
    """

    class Meta:
        proxy = True # Set to false if new fields are defined for this provider

    def update(self):
        """
        Fetch data from Jbol
        :return: True if successful update
        """
        # Download inbound file to /public/files/inbound

        # Uncompress file

        # Clear data from database

        # Import data from file

