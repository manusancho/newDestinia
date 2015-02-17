__author__ = 'Manu'
from os.path import *

from django.apps import AppConfig
from backend.apps.providers.plugins import jbol
from yapsy.PluginManager import PluginManager

class ProvidersConfig(AppConfig):

    name = 'backend.apps.providers'
    verbose_name = "Providers"
    plugins_loaded = False

    def ready(self):
        # startup code here
        #self.load_plugins()
        myjbol = jbol.Jbol().activate()
        pass


    def load_plugins(self):

        # Build the manager
        providers_plugin_manager = PluginManager()

        # Tell it the default place(s) where to find plugins
        providers_plugin_manager.setPluginPlaces([join(dirname(abspath(__file__)), 'plugins')])

        # Load all plugins
        providers_plugin_manager.collectPlugins()

        print "Loading provider plugins..."

        # Activate all loaded plugins
        for plugin in providers_plugin_manager.getAllPlugins():
            providers_plugin_manager.activatePluginByName(plugin.name)