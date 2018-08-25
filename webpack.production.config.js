const baseConfig = require('./webpack.base.config.js');
const merge = require('webpack-merge');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const WebpackCleanupPlugin = require('webpack-cleanup-plugin');

module.exports = merge(baseConfig, {
  bail: true,
  devtool: 'source-map',
  mode: 'production',
  output: {
    filename: '[name].[hash:8].js',
    chunkFilename: '[name].[hash:8].js',
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash:8].css',
      chunkFilename: '[name].[contenthash:8].css',
    }),
    new OptimizeCSSAssetsPlugin({
      cssProcessorOptions: { discardComments: { removeAll: true } },
      canPrint: false,
    }),
    new WebpackCleanupPlugin({
      exclude: ['robots.txt', 'favicon-32x32.png', 'favicon-48x48.png'],
    }),
  ],
});
