import * as React from "react";
import {Alert, AnchorButton, Button, Checkbox, InputGroup, Intent, NumericInput, Tag, Tooltip} from "@blueprintjs/core";
import {assign} from "lodash";
import {ENGINE_METHOD_NONE} from "constants";

export interface Input {
  id: number,
  text: string,
  boxId: string,
  firstStepInBox: boolean,
}
export interface StepComponentProps {
  proofId: string;
  boxId : string; // current box
  firstStepInBox: boolean; // current box
  inputType: string;
  givenIdList: number[];
  stepIdList: number[];
  onAdd: (proofId: string, text: string, given_just: number[], step_just: number[], boxId: string, firstStepInBox: boolean) => void;
  onDelete: (proofId: string, id: number, text: string, boxId: string, firstStepInBox: boolean) => void;
  onCreateBox: (boxId: string) => void;
  dataList: Input[];
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
    const { inputType, dataList, onDelete, onAdd, onCreateBox, boxId, firstStepInBox, proofId, error, givenIdList, stepIdList, } = this.props;
    const { text, givenLines, stepLines, } = this.state;
    let stepLine;
    let givenLine;
    let currKey = 0;
    let tagGivenKey = 0;
    let tagStepKey = 0;
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
          onValueChange={(valueAsNumber: number, valueAsString: string) => {
            givenLine = valueAsNumber;
          }}
        />
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => this.onAddGivenLine(givenLine)} />
        {
          givenLines.map( (line: number) => {
            return (
              <Tag key={tagGivenKey++} intent={Intent.PRIMARY} onRemove={() => this.deleteGivenTag(line)}> {line} </Tag>
            );
          })
        }
        <NumericInput
          placeholder="Step Line Numbers"
          value={stepLine}
          onValueChange={(valueAsNumber: number, valueAsString: string) => {
            stepLine = valueAsNumber;
          }}
        />
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => this.onAddStepLine(stepLine)} />

        {
          stepLines.map((line: number) => {
            return (
              <Tag key={tagStepKey++} intent={Intent.PRIMARY} onRemove={() => this.deleteStepTag(line)}> {line} </Tag>
            );
          })
        }

        <Button
          text="Enter Box"
          onClick={() => onCreateBox(this.props.boxId)}
        />

        <Button
          iconName="add"
          text="ADD PROOF"
          intent={Intent.PRIMARY}
          onClick={() => {
            this.setState(assign({}, this.state, { givenLine: null, stepLine: null, }));
            const given_just = this.getIds(givenLines, givenIdList);
            const step_just = this.getIds(stepLines, stepIdList);
            onAdd(proofId, text, given_just, step_just, boxId, firstStepInBox);
          }}
        />
        {
          dataList.map( (item: Input) => {
            return (
              <div key={currKey++} className="pt-card">
                [{currKey}] {item.text}
                <AnchorButton className="pt-minimal" iconName="delete" onClick={() => onDelete(proofId, item.id, item.text, item.boxId, item.firstStepInBox)} />
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
}