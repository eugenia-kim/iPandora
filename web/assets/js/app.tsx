import * as React from "react";
import { Button, Intent } from "@blueprintjs/core";
import {Dispatch} from "redux";
import GivenInputBox from "./containers/given"

export class App extends React.Component<{}, {}> {

  public render() {
       return (
         <div>
           <GivenInputBox />
         </div>
       );
  }
}
