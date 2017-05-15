from pyramid.config import Configurator
from pyramid.static import QueryStringConstantCacheBuster
from .controllers import home_controller as home
import time


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    init_includes(config)

    init_routing(config)

    return config.make_wsgi_app()


def init_includes(config):
    # add template engine
    config.include('pyramid_chameleon')
    # add pyramid handlers
    config.include('pyramid_handlers')


def init_routing(config):
    # add static view
    config.add_static_view('static', 'static', cache_max_age=3600)
    # add cache-busting
    config.add_cache_buster(
        'blue_yellow_app:static/',
        QueryStringConstantCacheBuster(str(int(time.time()))))
    # add routes
    config.add_route('home', '/')

    # add handlers
    config.add_handler('home_ctrl', '/home/{action}',
                       handler=home.HomeController)

    config.scan()
