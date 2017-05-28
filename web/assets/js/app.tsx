import * as React from "react";
import { Button } from "@blueprintjs/core";
import {RouteComponentProps} from "react-router";
import { post } from "request";

export default class App extends React.Component<RouteComponentProps<void>, {}> {

  public render() {
       return (
         <div>
           <Button text="Begin" onClick={() => post('http://localhost:8000/api/begin_proof/', (error, response, body) => {
             this.props.history.push(new URL(response.url).pathname);
           })} />
         </div>
       );
  }
}

