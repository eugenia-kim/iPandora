import * as React from "react";
import {Alert, AnchorButton, Button, Checkbox, InputGroup, Intent, NumericInput, Tag, Tooltip} from "@blueprintjs/core";
import {assign} from "lodash";
import {ENGINE_METHOD_NONE} from "constants";
import {StepData} from "../actions/index";
import {createImplication} from "../model/logicFormulaCreators";

export interface Input {
  id: number,
  text: string,
  boxId: string,
  isFirstStepInBox: boolean,
}
export interface StepComponentProps {
  proofId: string;
  boxId : string; // current box
  isFirstStepInBox: boolean; // current box
  firstStepInBox: StepData;
  lastStepInBox: StepData;
  inputType: string;
  givenIdList: number[];
  stepIdList: number[];
  onAdd: (proofId: string, text: string, given_just: number[], step_just: number[], boxId: string, isFirstStepInBox: boolean) => void;
  onDelete: (proofId: string, id: number, text: string, boxId: string, isFirstStepInBox: boolean) => void;
  onCreateBox: (proofId: string, boxId: string) => void;
  onEndBox: (proofId: string, text: string, step_just: number[], boxId: string) => void;
  dataList: StepData[];
  error: string;
  getData: (proofId: string) => void;
}

export interface StepComponentState {
  text: string;
  givenLines: number[];
  stepLines: number[];
}

export class StepComponent extends React.Component<StepComponentProps, StepComponentState> {
  constructor() {
    super();
    this.state = {
      text: "",
      givenLines: [],
      stepLines: [],
    };
  }

  componentDidMount() {
    this.props.getData(this.props.proofId);
  }

  render() {
    const { inputType, dataList, onDelete, onAdd, onCreateBox, onEndBox, boxId, isFirstStepInBox, firstStepInBox, lastStepInBox, proofId, error, givenIdList, stepIdList, } = this.props;
    const { text, givenLines, stepLines, } = this.state;
    let stepLine;
    let givenLine;
    let currKey = 0;
    let tagGivenKey = 0;
    let tagStepKey = 0;
    let givenJustKey = 0;
    let stepJustKey = 0;
    return (
      <div>
        <InputGroup
          placeholder={ "Enter " + inputType + "..." }
          value={text}
          onChange={this.onChange}
          rightElement={
            error && (
              <Tooltip content={error}>
                <span className="pt-icon-error pt-intent-danger" />
              </Tooltip>
            )
          }
        />

        <NumericInput
          placeholder="Given Line Numbers"
          value={givenLine}
          intent={Intent.SUCCESS}
          onValueChange={(valueAsNumber: number, valueAsString: string) => {
            givenLine = valueAsNumber;
          }}
        />
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => this.onAddGivenLine(givenLine)} />
        {
          givenLines.map( (line: number) => {
            return (
              <Tag key={tagGivenKey++} intent={Intent.SUCCESS} onRemove={() => this.deleteGivenTag(line)}> {line} </Tag>
            );
          })
        }
        <NumericInput
          placeholder="Step Line Numbers"
          value={stepLine}
          intent={Intent.WARNING}
          onValueChange={(valueAsNumber: number, valueAsString: string) => {
            stepLine = valueAsNumber;
          }}
        />
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => this.onAddStepLine(stepLine)} />

        {
          stepLines.map((line: number) => {
            return (
              <Tag key={tagStepKey++} intent={Intent.WARNING} onRemove={() => this.deleteStepTag(line)}> {line} </Tag>
            );
          })
        }

        <Button
          text="Enter Box"
          onClick={() => onCreateBox(proofId, boxId)}
        />
        <Button
          text="End Box"
          onClick={() => {
            const text = createImplication(firstStepInBox.text, lastStepInBox.text);
            const step_just = [firstStepInBox.id, lastStepInBox.id];
            onEndBox(proofId,text, step_just, boxId)
          }}
        />
        <Button
          iconName="add"
          text="ADD PROOF"
          intent={Intent.PRIMARY}
          onClick={() => {
            this.setState(assign({}, this.state, { givenLine: null, stepLine: null, }));
            const given_just = this.getIds(givenLines, givenIdList);
            const step_just = this.getIds(stepLines, stepIdList);
            onAdd(proofId, text, given_just, step_just, boxId, isFirstStepInBox);
          }}
        />
        {
          dataList.map( (item: StepData) => {
            return (
              <div key={currKey++} className="pt-card">
                [{currKey}] {item.text}
                {
                  this.assTag(item.isFirstStepInBox)
                }
                {
                  item.given_just.map( (n: number) => {
                    return (
                      <Tag key={givenJustKey++} intent={Intent.SUCCESS}> {givenIdList.indexOf(n) + 1} </Tag>
                    );
                  })
                }
                {
                  item.step_just.map( (n: number) => {
                    return (
                      <Tag key={stepJustKey++} intent={Intent.WARNING}> {stepIdList.indexOf(n) + 1} </Tag>
                    );
                  })
                }
                <AnchorButton className="pt-minimal" iconName="delete" onClick={() => onDelete(proofId, item.id, item.text, item.boxId, item.isFirstStepInBox)} />
              </div>
            );
          })
        }

      </div>
    );
  }

  private getIds = (lines: number[], ids: number[]) => {
    return lines.map(l => ids[l - 1])
  };

  private onAddGivenLine = (line : number) => {
    this.setState(assign({}, this.state, { givenLines: [...this.state.givenLines, line]}));
  };

  private onAddStepLine = (line: number) => {
    this.setState(assign({}, this.state, { stepLines: [...this.state.stepLines, line]}));
  };

  private deleteGivenTag = (line: number) => {
    this.setState(assign({}, this.state, { givenLines: this.state.givenLines.filter((item) => item !== line) }));
  };

  private deleteStepTag = (line: number) => {
    this.setState(assign({}, this.state, { stepLines: this.state.stepLines.filter((item) => item !== line )}));
  };

  private onChange = (event: React.FormEvent<HTMLInputElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState(assign({}, this.state, { text }));
  };

  private handleAssume = (event: React.FormEvent<HTMLInputElement>) => {
    const checked = (event.target as HTMLInputElement).value;
    this.setState(assign({}, this.state, { assume: checked }));
  };

  private  assTag = (flag: boolean) => {
    if (flag) {
      return (
        <Tag intent={Intent.DANGER} > ass </Tag>
      );
    }
  };
}