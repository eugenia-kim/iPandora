import { assign } from "lodash";
import * as React from "react";

import { AnchorButton, Button, InputGroup, Intent, NumericInput, Tag, Tooltip } from "@blueprintjs/core";

import { StepData } from "../actions/index";
import { createImplication } from "../model/logicFormulaCreators";
import { BoxButtonComponent } from "./BoxButtonComponent";

export interface Input {
  id: number;
  text: string;
  boxId: string;
  isFirstStepInBox: boolean;
}
export interface StepComponentProps {
  boxId: string; // current box
  firstStepInBox: StepData;
  proofId: string;
  isFirstStepInBox: boolean; // current box
  lastStepInBox: StepData;
  inputType: string;
  givenIdList: number[]; // linenumber -> id
  stepIdList: number[];
  onAdd: (proofId: string,
          text: string,
          givenJust: number[],
          stepJust: number[],
          boxId: string,
          isFirstStepInBox: boolean) => void;
  onDelete: (proofId: string, id: number, text: string, boxId: string, isFirstStepInBox: boolean) => void;
  onCreateBox: (proofId: string, boxId: string) => void;
  onEndBox: (proofId: string, text: string, stepJust: number[], boxId: string) => void;
  dataList: StepData[];
  error: string;
  getData: (proofId: string) => void;
}

export interface StepComponentState {
  currentGivenLine?: number;
  currentStepLine?: number;
  text: string;
  givenLines: number[];
  stepLines: number[];
}

export class StepComponent extends React.Component<StepComponentProps, StepComponentState> {
  constructor() {
    super();
    this.state = {
      currentGivenLine: undefined,
      givenLines: [],
      stepLines: [],
      text: "",
    };
  }

  componentDidMount() {
    this.props.getData(this.props.proofId);
  }

  render() {
    // TODO: We most likely want to make render a smaller method which requires less variables
    const {
      inputType,
      onCreateBox,
      onEndBox,
      boxId,
      firstStepInBox,
      lastStepInBox,
      proofId,
      stepIdList,
    } = this.props;
    const { text, currentStepLine, currentGivenLine, givenLines, stepLines } = this.state;

    return (
      <div>
        <InputGroup
          placeholder={"Enter " + inputType + "..."}
          value={text}
          onChange={this.onChange}
          rightElement={this.renderError()}
        />

        <NumericInput
          placeholder="Given Line Numbers"
          value={currentGivenLine}
          intent={Intent.SUCCESS}
          onValueChange={this.onUpdateCurrentGivenLine}
        />
        <AnchorButton className="pt-minimal" iconName="add" onClick={this.onAddGivenJustification} />
        {this.renderProofLines(givenLines, Intent.SUCCESS, this.createOnDeleteGivenJustificationHandler)}
        <NumericInput
          placeholder="Step Line Numbers"
          value={currentStepLine}
          intent={Intent.WARNING}
          onValueChange={this.onUpdateCurrentStepLine}
        />
        <AnchorButton className="pt-minimal" iconName="add" onClick={this.onAddStepJustification} />
        {this.renderProofLines(stepLines, Intent.WARNING, this.createOnDeleteStepJustificationHandler)}

        <Button
          iconName="add"
          text="ADD PROOF"
          intent={Intent.PRIMARY}
          onClick={this.onAddStep}
        />
        {this.renderDataList()}

        <BoxButtonComponent
          type="-> I"
          firstStepInBox={firstStepInBox}
          lastStepInBox={lastStepInBox}
          proofId={proofId}
          stepIdList={stepIdList}
          boxId={boxId}
          onCreateBox={onCreateBox}
          onEndBox={onEndBox}
          getText={this.getImpliesText}
          getJustifications={this.getImpliesJustifications}
        />

        <BoxButtonComponent
          type="Exist E"
          firstStepInBox={firstStepInBox}
          lastStepInBox={lastStepInBox}
          proofId={proofId}
          stepIdList={stepIdList}
          boxId={boxId}
          onCreateBox={onCreateBox}
          onEndBox={onEndBox}
          getText={this.getExistsText}
          getJustifications={this.getExistsJustifications}
        />

      </div>
    );
  }

  private getIds = (lines: number[], ids: number[]) => {
    return lines.map(l => ids[l - 1]);
  }

  private onAddGivenJustification = () => {
    const { currentGivenLine } = this.state;

    this.setState(assign({}, this.state, {
      currentGivenLine: undefined,
      givenLines: [...this.state.givenLines, currentGivenLine],
    }));
  }

  private onAddStepJustification = () => {
    const { currentStepLine } = this.state;

    this.setState(assign({}, this.state, {
      currentStepLine: undefined,
      stepLines: [...this.state.stepLines, currentStepLine],
    }));
  }

  private createOnDeleteGivenJustificationHandler = (line: number) => () => {
    this.setState(assign({}, this.state, {givenLines: this.state.givenLines.filter(item => item !== line) }));
  }

  private createOnDeleteStepJustificationHandler = (line: number) => () => {
    this.setState(assign({}, this.state, { stepLines: this.state.stepLines.filter(item => item !== line )}));
  }

  private onChange = (event: React.FormEvent<HTMLInputElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState(assign({}, this.state, { text }));
  }

  private assTag = (flag: boolean) => {
    if (flag) {
      return (
        <Tag intent={Intent.DANGER} > ass </Tag>
      );
    }
  }

  private onUpdateCurrentGivenLine = (valueAsNumber: number) => {
    this.setState(assign({}, this.state, {
      currentGivenLine: valueAsNumber,
    }));
  }

  private onUpdateCurrentStepLine = (valueAsNumber: number) => {
    this.setState(assign({}, this.state, {
      currentStepLine: valueAsNumber,
    }));
  }

  private onAddStep = () => {
    const { boxId, proofId, givenIdList, onAdd, stepIdList, isFirstStepInBox } = this.props;
    const { givenLines, stepLines, text } = this.state;

    this.setState( assign({}, this.state, { givenLines: [], stepLines: [] }) );
    const givenJust = this.getIds(givenLines, givenIdList);
    const stepJust = this.getIds(stepLines, stepIdList);
    onAdd(proofId, text, givenJust, stepJust, boxId, isFirstStepInBox);
  }

  private renderError = () => {
    const { error } = this.props;

    return error && (
      <Tooltip content={error}>
        <span className="pt-icon-error pt-intent-danger"/>
      </Tooltip>
    );
  }

  private renderDataList = () => {
    const { dataList, givenIdList, proofId, stepIdList } = this.props;

    let currentLineNumber = 0;

    dataList.map((item: StepData) => {
      return (
        <div key={currentLineNumber++} className="pt-card">
          [{currentLineNumber}] {item.text}
          {this.assTag(item.isFirstStepInBox)}
          {this.renderJustificationList(item.given_just, givenIdList, Intent.SUCCESS)}
          {this.renderJustificationList(item.step_just, stepIdList, Intent.WARNING)}
          <AnchorButton
            className="pt-minimal"
            iconName="delete"
            onClick={this.createOnDeleteStepHandler(proofId, item)}
          />
        </div>
      );
    });
  }

  private renderProofLines = (lines, intent, createOnDeleteHandler) =>
    lines.map(line => (<Tag key={line} intent={intent} onRemove={createOnDeleteHandler(line)}>{line}</Tag>))

  private renderJustificationList = (list, idList, intent) => {
    return list.map((n: number) => (
      <Tag key={n} intent={intent}>{idList.indexOf(n) + 1}</Tag>
    ));
  }

  private createOnDeleteStepHandler = (proofId, item) => () => {
    const { onDelete } = this.props;

    onDelete(proofId, item.id, item.text, item.boxId, item.isFirstStepInBox);
  }

  private getImpliesText = (premise: StepData, conclusion: StepData) =>
    createImplication(premise.text, conclusion.text)

  private getExistsText = (first: StepData, conclusion: StepData) => conclusion.text;

  private getImpliesJustifications = (ids: number[], premise: StepData, conclusion: StepData) =>
    [premise.id, conclusion.id]

  private getExistsJustifications = (ids: number[], first: StepData, conclusion: StepData) => {
    const firstStepId = first.id;
    const conclusionStepId = conclusion.id;
    return [ids[ids.indexOf(firstStepId) - 1], firstStepId, conclusionStepId];
  }
}
