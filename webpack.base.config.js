const path = require('path');
const ManifestPlugin = require('webpack-manifest-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  context: path.join(__dirname, 'src', 'assets', 'js'),
  entry: {
    app: './index.js',
  },
  target: 'web',
  module: {
    strictExportPresence: true,
    rules: [
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          cacheDirectory: true,
        },
      },
      {
        test: /\.s?[ac]ss$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
      },
      {
        test: /\.svg$/,
        loader: 'url-loader',
        options: {
          limit: 1,
          name: '[name].[hash:8].[ext]',
        },
      },
      {
        test: /\.jpe?g$/,
        loader: 'url-loader',
        options: {
          limit: 1,
          name: '[name].[hash:8].[ext]',
        },
      },
      {
        test: /\.(eot|otf|ttf|woff|woff2)$/,
        loader: 'url-loader',
        options: {
          limit: 1,
          name: '[name].[hash:8].[ext]',
        },
      },
    ],
  },
  output: {
    path: path.resolve(path.join(__dirname, 'src', 'canopus', 'static')),
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
        styles: {
          name: 'styles',
          test: /\.s?[ac]ss$/,
          minChunks: 1,
        },
      },
    },
    runtimeChunk: 'single',
    noEmitOnErrors: true,
  },
  plugins: [new ManifestPlugin({ writeToFileEmit: true })],
  resolve: {
    alias: {
      '~': path.resolve(path.join(__dirname, 'src', 'assets', 'js')),
      react: 'preact-compat',
      'react-dom': 'preact-compat',
      'react-redux': 'preact-redux',
    },
  },
};
