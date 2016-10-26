def includeme(config):
    """Add home, auth and API routes.

    :param config: The pyramid ``Configurator`` object for your app.
    :type config: ``pyramid.config.Configurator``
    """
    config.add_route('home', '/')
    config.add_route('robots', '/robots.txt')

    config.add_route('oauth2-google', '/auth/google')
    config.add_route('oauth2-facebook', '/auth/facebook')
    config.add_route('oauth2-live', '/auth/live')

    config.add_route('posts', '/api/v1/posts')
    config.add_route('post', '/api/v1/posts/{id}')

    config.add_static_view('static', 'static', cache_max_age=3600)
