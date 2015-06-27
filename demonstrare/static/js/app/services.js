/**
 * @name PostsFactory
 * @type {Function}
 */
function PostsFactory (Restangular) {
    return Restangular.service('posts');
}

angular.module('demo.services', ['restangular'])
    .factory('Posts', ['Restangular', PostsFactory]);
