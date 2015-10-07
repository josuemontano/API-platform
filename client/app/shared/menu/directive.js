angular.module('demo.controllers', [])
    .controller('MenuCtrl', ['$scope', '$auth', MenuCtrl]);

/**
 * @name MenuCtrl
 * @type {Function}
 */
function MenuCtrl ($scope, $auth) {
    $scope.isAuthenticated = function () {
        return $auth.isAuthenticated();
    };
}
