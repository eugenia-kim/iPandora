import * as React from "react";

import { Button } from "@blueprintjs/core";

import { StepData } from "../actions/index";
import { createImplication } from "../model/logicFormulaCreators";

export interface BoxButtonComponentProps {
  type: string;
  proofId: string;
  firstStepInBox: StepData;
  lastStepInBox: StepData;
  stepIdList: number[];
  boxId: string;
  depth: number;
  onCreateBox: (proofId: string, boxId: string) => void;
  onEndBox: (proofId: string, depth: number, text: string, stepJust: number[], boxId: string) => void;
  getText: (premise: StepData, conclusion: StepData) => string;
  getJustifications: (ids: number[], premise: StepData, conclusion: StepData) => number[];
}

export class BoxButtonComponent extends React.Component<BoxButtonComponentProps, void> {
  render() {
    const { type } = this.props;

    return(
      <div>
        <Button
          text={"Begin " + type}
          onClick={this.onCreateBoxHandler}
        />
        <Button
          text={"End " + type}
          onClick={this.onEndBoxHandler}
        />
      </div>
    );
  }

  private onCreateBoxHandler = () => {
    const { boxId, proofId, onCreateBox } = this.props;

    onCreateBox(proofId, boxId);
  }

  private onEndBoxHandler = () => {
    const {
      depth,
      firstStepInBox,
      lastStepInBox,
      stepIdList,
      proofId,
      boxId,
      onEndBox,
      getText,
      getJustifications } = this.props;

    const text = getText(firstStepInBox, lastStepInBox);
    const stepJust = getJustifications(stepIdList, firstStepInBox, lastStepInBox);

    onEndBox(proofId, depth, text, stepJust, boxId);
  }
}
