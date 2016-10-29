Backbone = require 'backbone'


class User extends Backbone.Model
  urlRoot : '/api/v1/users'


module.exports = User
