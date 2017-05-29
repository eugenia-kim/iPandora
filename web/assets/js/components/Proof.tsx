import * as React from "react";
import {RouteComponentProps} from "react-router";
import GivenInputBox from "../containers/GivenInputBox";
import TypeInputBox from "../containers/TypeInputBox";

export interface ProofUrlParams {
  proofId: string;
}

export class Proof extends React.Component<RouteComponentProps<ProofUrlParams>, {}> {
  render() {
    return (
      <div>
        SMART COOKIE: {this.props.match.params.proofId}
        <TypeInputBox inputType="Type" proofId={this.props.match.params.proofId} />
        <GivenInputBox inputType="Given" proofId={this.props.match.params.proofId} />
      </div>
    )
  }
}