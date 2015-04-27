angular.module('demo.services', ['ngResource'])
    .factory('Post', ['$resource', function($resource) {
        return $resource('/api/posts/:postId/', {}, {
            query: {
                method: 'GET',
                isArray: true,
                transformResponse: function (data, headersGetter) {
                    return JSON.parse(data).objects;
                }
            }
        });
    }]);