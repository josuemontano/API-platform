angular.module('demo.post.controller', [])
    .controller('PostsCtrl', ['posts', PostsCtrl]);

/**
 * @name PostsCtrl
 * @type {Function}
 */
function PostsCtrl (posts) {
    var vm = this;
    vm.posts = posts;
}
