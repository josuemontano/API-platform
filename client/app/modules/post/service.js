angular.module('demo.post.service', ['restangular'])
    .factory('Posts', ['Restangular', PostsFactory]);

/**
 * @name PostsFactory
 * @type {Function}
 */
function PostsFactory (Restangular) {
    return Restangular.service('posts');
}
