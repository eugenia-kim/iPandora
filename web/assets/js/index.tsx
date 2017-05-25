import * as ReactDOM from "react-dom";
import * as React from "react";
import { App } from "./app";
import { Provider } from 'react-redux';
import {applyMiddleware, createStore, } from 'redux';
import { logger } from 'redux-logger';
import { givenReducer } from "./reducers/given";

let store = createStore(givenReducer, applyMiddleware(logger));

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('react-app')
);
