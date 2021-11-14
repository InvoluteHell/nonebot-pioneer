from dependency_injector import containers, providers

from .android import Android


class PluginContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    android = providers.Singleton(Android, config.name)


container = PluginContainer()
container.config.from_dict({"name": "android"})
android = container.android()
android.listen()
