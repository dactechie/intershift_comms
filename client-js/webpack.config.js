module.exports = {
    module: {

        loaders: [
        //     {
        //   test: /\.js$/,
        //   loader: 'babel',
        //   exclude: /node_modules/
        // }, 
        {
          test: /\.vue$/,
          loader: 'vue'
        }, {
          test: /\.s[a|c]ss$/,
          loader: 'style!css!sass'
        }
    ]
      },
      vue: {
        loaders: {
          scss: 'style!css!sass'
        }
      }
  }