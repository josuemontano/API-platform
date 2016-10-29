Backbone = require 'backbone'
User = require '../../app/models/user'


describe "User", ->
  beforeEach ->
    @model = new User

  it "should be an instance of Backbone.Model", ->
    expect(@model instanceof Backbone.Model).toBe true

  it "should have the right urlRoot", ->
    expect(@model.urlRoot).toEqual '/api/v1/users'
