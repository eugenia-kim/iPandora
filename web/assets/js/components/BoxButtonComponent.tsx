import * as React from "react"
import {Button} from "@blueprintjs/core/dist";
import {StepData} from "../actions/index";
import {createImplication} from "../model/logicFormulaCreators";

export interface BoxButtonComponentProps {
  type: string;
  proofId: string;
  firstStepInBox: StepData;
  lastStepInBox: StepData;
  stepIdList: number[];
  boxId: string;
  onCreateBox: (proofId: string, boxId: string) => void;
  onEndBox: (proofId: string, text: string, step_just:number[], boxId: string) => void;
}

export interface BoxButtonComponentState {

}

export class ImpButtonComponent extends React.Component<BoxButtonComponentProps, BoxButtonComponentState> {
  render() {
    const { proofId, type, stepIdList, firstStepInBox, lastStepInBox, boxId, onCreateBox, onEndBox } = this.props;

    return(
      <div>
        <Button
          text={"Begin "  + type }
          onClick={() => onCreateBox(proofId, boxId)}
        />
        <Button
          text={"End " + type}
          onClick={() => {
            const text = this.getText(firstStepInBox, lastStepInBox);
            const step_just = this.getJust(stepIdList, firstStepInBox, lastStepInBox);
            onEndBox(proofId, text, step_just, boxId)
          }}
        />
      </div>
    );
  }

  private getText = (fst: StepData, last: StepData) => {
    return createImplication(fst.text, last.text);
  };

  private getJust = (ids: number[], fst: StepData, last: StepData) => {
    return  [fst.id, last.id];
  };

}

export class ExistButtonComponent extends React.Component<BoxButtonComponentProps, BoxButtonComponentState> {
  render() {
    const { proofId, type, stepIdList, firstStepInBox, lastStepInBox, boxId, onCreateBox, onEndBox } = this.props;

    return(
      <div>
        <Button
          text={"Begin "  + type }
          onClick={() => onCreateBox(proofId, boxId)}
        />
        <Button
          text={"End " + type}
          onClick={() => {
            const text = this.getText(firstStepInBox, lastStepInBox);
            const step_just = this.getJust(stepIdList, firstStepInBox, lastStepInBox);
            onEndBox(proofId, text, step_just, boxId)
          }}
        />
      </div>
    );
  }

  private getText = (fst: StepData, lst: StepData) => {
    return lst.text;
  };

  private getJust = (ids: number[], fst:StepData, lst:StepData) => {
    const firstStepId = fst.id;
    const lastStepId = lst.id;
    return [this.getPrevId(firstStepId, ids), firstStepId, lastStepId];
  };

  private getPrevId = (id:number, ids: number[]) => {
    return ids[ids.indexOf(id) - 1];
  };

}
