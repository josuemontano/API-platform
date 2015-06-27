/**
 * @name MenuCtrl
 * @type {Function}
 */
function MenuCtrl ($scope, $auth) {
    $scope.isAuthenticated = function () {
        return $auth.isAuthenticated();
    };
}

/**
 * @name HomeCtrl
 * @type {Function}
 */
function HomeCtrl () {
    var vm = this;
    vm.message = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
}

/**
 * @name LoginCtrl
 * @type {Function}
 */
function LoginCtrl ($auth) {
    var vm = this;
    vm.authenticate = function (provider) {
        $auth.authenticate(provider)
        .then(function (response) {
        }, function (error) {
            if (error.status === 400)
                vm.error = 'You cannot login to this site. Request an account.';
            else
                vm.error = 'An unexpected problem occured, please try again.';
        });
    };
}

/**
 * @name LogoutCtrl
 * @type {Function}
 */
function LogoutCtrl ($auth) {
    $auth.logout();
}

angular.module('demo.controllers', [])
    .controller('MenuCtrl', ['$scope', '$auth', MenuCtrl])
    .controller('HomeCtrl', [HomeCtrl])
    // Login & logout
    .controller('LoginCtrl', ['$auth', LoginCtrl])
    .controller('LogoutCtrl', ['$auth', LogoutCtrl]);
