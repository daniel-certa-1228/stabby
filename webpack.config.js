/* eslint-disable no-undef */
const path = require('path');
const autoprefixer = require('autoprefixer');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: './assets/scripts/index.js',
    output: {
        path: path.resolve(__dirname, 'stabby_web/static/stabby_web'),
        filename: 'js/bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.m?js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.(scss|css)$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    {
                        loader: 'postcss-loader',
                        options: {
                            postcssOptions: {
                                plugins: [autoprefixer()]
                            }
                        }
                    },
                    'sass-loader'
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'css/bundle.css'
        })
    ],
    resolve: {
        extensions: ['.js', '.jsx', '.scss', '.css']
    }
};