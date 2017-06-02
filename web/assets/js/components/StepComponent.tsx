import * as React from "react";
import {Alert, AnchorButton, Button, InputGroup, Intent, NumericInput, Tag, Tooltip} from "@blueprintjs/core";
import {assign} from "lodash";

export interface Input {
  id: number,
  text: string,
}
export interface StepComponentProps {
  proofId: string;
  inputType: string;
  givenIdList: number[];
  stepIdList: number[];
  onAdd: (proofId: string, text: string, given_just: number[], step_just: number[]) => void;
  onDelete: (proofId: string, id: number, text: string) => void;
  dataList: Input[];
  error: string;
  getData: (proofId: string) => void;
}

export interface StepComponentState {
  text: string;
  givenLines: number[];
  stepLines: number[]
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
    const { inputType, dataList, onDelete, onAdd, proofId, error, givenIdList, stepIdList, } = this.props;
    const { text, givenLines, stepLines } = this.state;
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
          iconName="add"
          text="ADD PROOF"
          intent={Intent.PRIMARY}
          onClick={() => {
            const given_just = this.getIds(givenLines, givenIdList);
            const step_just = this.getIds(stepLines, stepIdList);
            onAdd(proofId, text, given_just, step_just);
          }}
        />
        {
          dataList.map( (item: Input) => {
            return (
              <div key={currKey++} className="pt-card">
                [{currKey}] {item.text}
                <AnchorButton className="pt-minimal" iconName="delete" onClick={() => onDelete(proofId, item.id, item.text)} />
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
    this.setState(assign({}, this.state, { stepLines: this.state.givenLines.splice(this.state.givenLines.indexOf(line), 1)}));
  };

  private deleteStepTag = (line: number) => {
    this.setState(assign({}, this.state, { stepLines: this.state.stepLines.splice(this.state.stepLines.indexOf(line), 1)}));
  };

  private onChange = (event: React.FormEvent<HTMLElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState(assign({}, this.state, { text }));
  };
}