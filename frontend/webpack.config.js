module.exports = {
    // change to .tsx if necessary
    entry: "./src/index.tsx",
    output: {
        filename: './dist/bundle.js',
        path: __dirname + "/dist"
    },
    resolve: {
        // changed from extensions: [".js", ".jsx"]
        extensions: [".ts", ".tsx", ".js", ".jsx", ".json"]
    },
    module: {
        rules: [
            // changed from { test: /\.jsx?$/, use: { loader: 'babel-loader' } },
            {test: /\.(t|j)sx?$/, use: {loader: 'awesome-typescript-loader'}},
            // addition - add source-map support
            {enforce: "pre", test: /\.js$/, loader: "source-map-loader"}
        ]
    },
    externals: {
        "react": "React",
        "react-dom": "ReactDOM",
    },
    // addition - add source-map support
    devtool: "source-map"
}