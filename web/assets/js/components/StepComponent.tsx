import * as React from "react";
import {Alert, AnchorButton, InputGroup, Intent, NumericInput, Tag, Tooltip} from "@blueprintjs/core";
import {assign} from "lodash";

export interface Input {
  id: number,
  text: string,
}
export interface StepComponentProps {
  proofId: string;
  inputType: string;
  givenIdList: number[];
  onAdd: (proofId: string, text: string, given_just: number[], step_just: number[]) => void;
  onDelete: (proofId: string, id: number, text: string) => void;
  dataList: Input[];
  error: string;
  getData: (proofId: string) => void;
}

export interface StepComponentState {
  text: string;
  givenLines: number[];
}

export class StepComponent extends React.Component<StepComponentProps, StepComponentState> {
  constructor() {
    super();
    this.state = {
      text: "",
      givenLines: [],
    };
  }

  componentDidMount() {
    this.props.getData(this.props.proofId);
  }

  render() {
    const { inputType, dataList, onDelete, onAdd, proofId, error, givenIdList } = this.props;
    const { text, givenLines } = this.state;
    let givenLine = -1;
    let currKey = 0;
    let tagKey = 0;
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
          value={givenLine}
          placeholder="Enter Line Numbers: Given"
          onValueChange={(valueAsNumber: number, valueAsString: string) => {
            givenLine = valueAsNumber;
          }}
        />
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => this.onAddLine(givenLine)} />
        {
          givenLines.map( (line: number) => {
            return (
              <Tag key={tagKey++} intent={Intent.PRIMARY}> {line} </Tag>
            );
          })
        }

        <AnchorButton
          className="pt-minimal"
          iconName="add"
          onClick={() => {
            const given_just = this.getIds(givenLines, givenIdList);
            onAdd(proofId, text, given_just, []);
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

  private onAddLine = (line : number) => {
    this.setState(assign({}, this.state, { givenLines: [...this.state.givenLines, line]}));
  };

  private onChange = (event: React.FormEvent<HTMLElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState(assign({}, this.state, { text }));
  };
}