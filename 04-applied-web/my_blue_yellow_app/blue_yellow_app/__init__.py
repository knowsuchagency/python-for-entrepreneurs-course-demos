from pyramid.config import Configurator
from pyramid.static import QueryStringConstantCacheBuster
import time


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # add template engine
    config.include('pyramid_chameleon')

    # add static view
    config.add_static_view('static', 'static', cache_max_age=3600)
    # add cache-busting
    config.add_cache_buster(
        'blue_yellow_app:static/',
        QueryStringConstantCacheBuster(str(int(time.time()))))

    # add routes
    config.add_route('home', '/')
    config.scan()

    return config.make_wsgi_app()
