# Orpha lookup frontend

## Overview

This folder contains fronted part of the product. It uses `react` as a view library
and `mobx-state-tree` as a main state management library.

## Project structure

Project structure follows the general `Create React App` approach:

```
+ public/             (static files)
+ src/                (source code directory)
+   components/       (reusable components: cards, lookup fields, etc.)
+   mobx/             (mobx state-related code)
+     extensions/     (mobx useful extensions)
+     models/         (essential orpha mobx models)
+     stores/         (application mobx stores)
+     Environment.ts  (application environment enables access to services that shared across stores)
+     Root.store.ts   (root store of the applicaiton contains links to descendant stores)
+     setupStore.ts   (code that initialize environment and root store)
+   pages/            (entrypoints for each route)
+   services/         (reusable services)
+   theme/            (material UI theme options)
+   App.tsx           (high-level App component)
+   index.tsx         (react entry point)
```

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.
