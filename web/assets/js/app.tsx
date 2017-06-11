import * as React from "react";
import {RouteComponentProps} from "react-router";
import { post } from "request";

import { Button } from "@blueprintjs/core";

export default class App extends React.Component<RouteComponentProps<void>, {}> {

  render() {
    return (
      <div>
        <Button
          text="Begin"
          onClick={() => post("http://localhost:8000/api/begin_proof/", (error, response, _body) => {
            this.props.history.push(new URL(response.url).pathname);
          })}
        />
      </div>
    );
  }
}
