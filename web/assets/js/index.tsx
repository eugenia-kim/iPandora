import * as ReactDOM from "react-dom";
import * as React from "react";
import App from "./app";
import { Provider } from 'react-redux';
import {applyMiddleware, createStore, } from 'redux';
import { logger } from 'redux-logger';
import reducer from "./reducers/index";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";
import {Proof} from "./components/Proof";

let store = createStore(reducer, applyMiddleware(logger));

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <div>
        <Route exact={true} path="/" component={App} />
        <Route path="/:proofId" component={Proof} />
      </div>
    </Router>
  </Provider>,
  document.getElementById('react-app')
);
