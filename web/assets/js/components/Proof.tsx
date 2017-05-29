import * as React from "react";
import {RouteComponentProps} from "react-router";
import GivenInputBox from "../containers/GivenInputBox";

export interface ProofUrlParams {
  proofId: string;
}

export class Proof extends React.Component<RouteComponentProps<ProofUrlParams>, {}> {
  render() {
    return (
      <div>
        SMART COOKIE: {this.props.match.params.proofId}
        <GivenInputBox proofId={this.props.match.params.proofId} />
      </div>
    )
  }
}