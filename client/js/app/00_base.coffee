$ = require 'jquery'
_ = require 'underscore'
Backbone = require 'backbone'
Backbone.$ = $


# Patch Backbone. Redirect to login view if response is 401 or 403 and
# add JWT Authorization header
_sync = Backbone.sync
Backbone.sync = (method, model, options) ->
  options.beforeSend = (xhr) ->
    token = localStorage.getItem('access_token')
    xhr.setRequestHeader('Authorization', "JWT #{token}")

  xhr = _sync.call(this, method, model, options)
  xhr.fail (jqXHR, textStatus, error) ->
    if jqXHR.status == 401 || jqXHR.status == 403
      window.app.triggerMethod('request:forbidden')
  xhr
