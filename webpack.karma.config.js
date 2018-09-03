const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: {
    app: path.join(__dirname, 'src', 'assets', 'js', 'index.js'),
  },
  target: 'web',
  mode: 'none',
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
    filename: '[name].js',
    chunkFilename: '[name].js',
  },
  plugins: [new MiniCssExtractPlugin()],
  resolve: {
    alias: {
      '~': path.resolve(path.join(__dirname, 'src', 'assets', 'js')),
      react: 'preact-compat',
      'react-dom': 'preact-compat',
      'react-redux': 'preact-redux',
    },
  },
};
