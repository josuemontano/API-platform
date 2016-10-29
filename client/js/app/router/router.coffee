Marionette = require 'backbone.marionette'


class Router extends Marionette.AppRouter
  appRoutes:
    '': 'index'
    'login(/)': 'login'
    'logout(/)': 'logout'


module.exports = Router
