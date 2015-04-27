angular.module('demo.controllers', ['demo.services'])
    .controller('HomeCtrl', ['$scope', function($scope) {
        $scope.message = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
    }])
    // Login & logout
    .controller('LoginCtrl', ['$scope', '$auth', function($scope, $auth) {
        $scope.authenticate = function(provider) {
            $auth.authenticate(provider);
        };
    }])
    .controller('LogoutCtrl', ['$auth', function($auth) {
        if (!$auth.isAuthenticated())
            return;
        $auth.logout();
    }])
    // Dashboard (private)
    .controller('DashboardCtrl', ['$scope', 'Post', function($scope, Post) {
        Post.query(function(data) {
            $scope.posts = data;
        });
    }]);