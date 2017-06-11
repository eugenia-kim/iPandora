import * as React from "react";
import * as ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { applyMiddleware, createStore } from "redux";
import { logger } from "redux-logger";

import App from "./app";
import { Proof } from "./components/Proof";
import reducer from "./reducers/index";

const store = createStore(reducer, applyMiddleware(logger));

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <div>
        <Route exact={true} path="/" component={App} />
        <Route path="/:proofId" component={Proof} />
      </div>
    </Router>
  </Provider>,
  document.getElementById("react-app"),
);
