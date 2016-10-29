Router = require './router/router'
Controller = require './router/controller'


app.router = new Router(controller: new Controller())
app.start()
