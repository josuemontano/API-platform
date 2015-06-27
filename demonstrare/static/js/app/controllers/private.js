/**
 * @name PostsCtrl
 * @type {Function}
 */
function PostsCtrl (posts) {
    var vm = this;
    vm.posts = posts;
}

angular.module('demo.controllers')
    // Dashboard (private)
    .controller('PostsCtrl', ['posts', PostsCtrl]);
