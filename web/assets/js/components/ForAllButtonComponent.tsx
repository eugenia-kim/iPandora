import * as React from "react";

import { AnchorButton, Button, InputGroup } from "@blueprintjs/core";
import { assign } from "lodash";

import { StepData } from "../actions/index";
import { replaceConstWithVar } from "../model/logicFormulaCreators";

export interface ForAllButtonComponentProps {
  proofId: string;
  firstStepInBox: StepData;
  lastStepInBox: StepData;
  boxId: string;
  boxType: string;
  depth: number;
  onCreateForAllBox: (proofId: string,
                      depth: number,
                      boxId: string,
                      type: string,
                      variable: string,
                      constant: string) => void;
  onEndForAllBox: (proofId: string,
                   depth: number,
                   text: string,
                   boxId: string,
                   stepJust: number[]) => void;
}

export interface ForAllButtonComponentState {
  variable: string;
  constant: string;
}

export class ForAllButtonComponent extends React.Component<ForAllButtonComponentProps, ForAllButtonComponentState> {
  constructor() {
    super();
    this.state = {
      variable: "",
      constant: "",
    };
  }
  render() {
    const { boxType, lastStepInBox } = this.props;
    const { variable, constant } = this.state;
    return(
      <div>
        {
          <div className="add-var-const-group">
            <InputGroup
              placeholder="Variable"
              value={variable}
              onChange={this.onVariableChange}
            />
            <InputGroup
              placeholder="Constant"
              value={constant}
              onChange={this.onConstantChange}
            />
            <AnchorButton className="pt-minimal" iconName="add" onClick={this.onCreateBoxHandler} />
          </div>
        }
        {
          (boxType === "A") &&  <Button
            text="End ForAll Introduction"
            onClick={this.onEndBoxHandler}
          />
        }
      </div>
    );
  }

  private onVariableChange = (event: React.FormEvent<HTMLElement>) => {
    const variable = (event.target as HTMLInputElement).value;
    this.setState(assign(this.state, {variable}));
  }

  private onConstantChange = (event: React.FormEvent<HTMLElement>) => {
    const constant = (event.target as HTMLInputElement).value;
    this.setState(assign(this.state, {constant}));
  }

  private onCreateBoxHandler = () => {
    const { boxId, proofId, onCreateForAllBox, depth } = this.props;
    const { variable, constant } = this.state;

    onCreateForAllBox(proofId, depth, boxId, "A", variable, constant);
  }

  private onEndBoxHandler = () => {
    const {
      depth,
      firstStepInBox,
      lastStepInBox,
      proofId,
      boxId,
      onEndForAllBox,
    } = this.props;

    const stepJust = [firstStepInBox.id, lastStepInBox.id];
    onEndForAllBox(proofId, depth, lastStepInBox.text, boxId, stepJust);
  }
}
