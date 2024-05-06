/* eslint-disable no-undef */
const path = require('path');
const autoprefixer = require('autoprefixer')
const HtmlWebpackPlugin = require('html-webpack-plugin')
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
                test: /\.(scss)$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'postcss-loader',
                        options: {
                            postcssOptions: {
                                plugins: () => [autoprefixer()]
                            }
                        }
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            }
            // {
            //     test: /\.(scss)$/,
            //     use: [
            //       {
            //         // Adds CSS to the DOM by injecting a `<style>` tag
            //         loader: 'style-loader'
            //       },
            //       {
            //         // Interprets `@import` and `url()` like `import/require()` and will resolve them
            //         loader: 'css-loader'
            //       },
            //       {
            //         // Loader for webpack to process CSS with PostCSS
            //         loader: 'postcss-loader',
            //         options: {
            //           postcssOptions: {
            //                 plugins: () => [autoprefixer()] // Configure autoprefixer
            //             }
            //         }
            //       },
            //       {
            //         // Loads a SASS/SCSS file and compiles it to CSS
            //         loader: 'sass-loader'
            //       }
            //     ]
            // },
            // {
            //     test: /\.css$/,
            //     include: path.resolve(__dirname, 'assets/styles'),
            //     use: [MiniCssExtractPlugin.loader, 'css-loader']
            // }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({ template: './stabby_web/templates/stabby_web/_base.html' }),
        new MiniCssExtractPlugin({
            filename: 'css/bundle.css'
        })
    ]
};
