from pyramid.config import Configurator


def includeme(config: Configurator):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('auth-google', '/auth/google')
    config.add_route('auth-facebook', '/auth/facebook')
    config.add_route('auth-windows', '/auth/windows')

    config.add_route('home', '/')
    config.add_route('login', '/login')
