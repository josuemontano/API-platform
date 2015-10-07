angular.module('demo.auth.controller', [])
    .controller('LoginCtrl', ['$auth', LoginCtrl])
    .controller('LogoutCtrl', ['$auth', LogoutCtrl]);

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
