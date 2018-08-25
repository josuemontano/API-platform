const baseConfig = require('./webpack.base.config.js');
const merge = require('webpack-merge');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = merge(baseConfig, {
  mode: 'development',
  devServer: {
    headers: { 'Access-Control-Allow-Origin': '*' },
  },
  output: {
    filename: '[name].js',
    chunkFilename: '[name].js',
  },
  plugins: [new MiniCssExtractPlugin()],
});
