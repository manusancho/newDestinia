__author__ = 'Manu'

from backend.apps.providers.models import *

from yapsy.IPlugin import IPlugin

class Jbol(Provider):
    """
    Class to manage Jbol data import
    """

    def __init__(self):

        super(IPlugin)
        super(Provider)

        self.machine_name = "jbol"
        self.name = "Jumbo Tours"

        self.activate()


    class Meta:
        proxy = True # Set to false if new fields are defined for this provider


    def activate(self):

        try:
            _, created = Provider.objects.update_or_create(
                machine_name=self.machine_name,
                name=self.name,
            )

            if created:
                print "Added provider %s" % self.name
            else:
                print "Provider %s already registered!" % self.name

        except Exception, e:
            print "Can't register plugin %s . %s" % (self.name, e)


    def update(self):
        """
        Fetch data from Jbol
        :return: True if successful update
        """
        # Download inbound file to /public/files/inbound

        # Uncompress file

        # Clear data from database

        # Import data from file

