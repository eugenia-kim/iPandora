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
  boxType: string;
  depth: number;
  onCreateBox: (proofId: string, boxId: string, type: string) => void;
  onEndBox: (proofId: string, depth: number, text: string, stepJust: number[], boxId: string) => void;
  getText: (premise: StepData, conclusion: StepData) => string;
  getJustifications: (ids: number[], premise: StepData, conclusion: StepData) => number[];
}

export class BoxButtonComponent extends React.Component<BoxButtonComponentProps, void> {
  render() {
    const { type, boxType, lastStepInBox } = this.props;
    const typeName = this.getType(type);
    return(
      <div>
        <Button
          disabled={this.disableButton(type, lastStepInBox)}
          text={"Begin " + typeName}
          onClick={this.onCreateBoxHandler}
        />
        {
          (boxType === type) &&  <Button
          text={"End " + typeName}
          onClick={this.onEndBoxHandler}
          />
        }
      </div>
    );
  }

  private onCreateBoxHandler = () => {
    const { boxId, proofId, onCreateBox, type } = this.props;

    onCreateBox(proofId, boxId, type);
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

  private disableButton = (type: string, lstStep: StepData) => {
    switch (type) {
      case "I": {
        return false;
      }
      case "E": {
        return !lstStep || (lstStep && !lstStep.exist);
      }
      case "A": {
        return !lstStep || (lstStep && !lstStep.forall);
      }
      default: {
        return true;
      }
    }
  }

  private getType = (type: string) => {
    switch (type) {
      case "I": {
        return "Implication";
      }
      case "E": {
        return "Exist";
      }
      case "A": {
        return "ForAll";
      }
      default: {
        return "";
      }
    }
  }
}
