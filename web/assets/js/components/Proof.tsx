import * as React from "react";
import {RouteComponentProps} from "react-router";

import GivenInputBox from "../containers/GivenInputBox";
import StepInputBox from "../containers/StepInputBox";
import ToShowInputBox from "../containers/ToShowInputBox";
import TypeInputBox from "../containers/TypeInputBox";

export interface ProofUrlParams {
  proofId: string;
}

export class Proof extends React.Component<RouteComponentProps<ProofUrlParams>, {}> {
  render() {
    return (
      <div className="proof">
        <div className="proof-inputs">
          <TypeInputBox inputType="Type" proofId={this.props.match.params.proofId} />
          <GivenInputBox inputType="Given" proofId={this.props.match.params.proofId} />
          <ToShowInputBox inputType="ToShow" proofId={this.props.match.params.proofId} />
        </div>
        <div className="proof-body">
          <StepInputBox inputType="Step" proofId={this.props.match.params.proofId} />
        </div>
      </div>
    );
  }
}
