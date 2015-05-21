angular.module('demo.controllers', ['restangular'])
    .controller('MenuCtrl', ['$scope', '$auth', function($scope, $auth) {
        $scope.isAuthenticated = function() {
            return $auth.isAuthenticated();
        };
    }])
    .controller('HomeCtrl', ['$scope', function($scope) {
        $scope.message = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
    }])
    // Login & logout
    .controller('LoginCtrl', ['$scope', '$auth', function($scope, $auth) {
        $scope.authenticate = function(provider) {
            $auth.authenticate(provider)
            .then(function(response) {
            }, function(error) {
                if (error.status === 400)
                    $scope.error = 'You cannot login to this site. Request an account.';
                else
                    $scope.error = 'An unexpected problem occured, please try again.';
            });
        };
    }])
    .controller('LogoutCtrl', ['$auth', function($auth) {
        if (!$auth.isAuthenticated())
            return;
        $auth.logout();
    }])
    // Dashboard (private)
    .controller('PostsCtrl', ['$scope', 'Restangular', function($scope, Restangular) {
        $scope.posts = Restangular.all('posts').getList().$object;
    }]);