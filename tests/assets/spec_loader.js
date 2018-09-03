const testContext = require.context('./js', true, /\.spec\.js$/);
function requireAll(requireContext) {
  return requireContext.keys().map(requireContext);
}

var modules = requireAll(testContext);
