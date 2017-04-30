import * as React from "react";
import { Button, Intent } from "@blueprintjs/core";

export class App extends React.Component<{}, {}> {

  public render() {
       return (
         <div>
               <h1>Sexy Geni.</h1>
               <Button text="YEAH!" intent={Intent.PRIMARY} />
         </div>
       );
  }
}
