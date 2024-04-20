const path = require('path');

module.exports = {
    entry: './assets/scripts/index.js',
    output: {
        'path': path.resolve(__dirname, 'stabby_web/static/stabby_web', 'js'),
        'filename': 'bundle.js'
    }
}