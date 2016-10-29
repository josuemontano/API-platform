Marionette = require 'backbone.marionette'


class Controller extends Marionette.Object
  login: ->
    localStorage.clear()
    layout = app.getView()
    layout.triggerMethod('show:user:login')

  logout: ->
    @login()

  index: ->
    layout = app.getView()
    layout.triggerMethod('show:dashboard:main')


module.exports = Controller
