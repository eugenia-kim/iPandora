import * as React from "react";
import {Alert, AnchorButton, InputGroup, Tooltip} from "@blueprintjs/core";
import {assign} from "lodash";

export interface Input {
  id: number,
  text: string,
}
export interface AddInputBoxProps {
  proofId: string;
  inputType: string;
  onAdd: (proofId: string, text: string) => void;
  onDelete: (proofId: string, id: number, text: string) => void;
  dataList: Input[];
  error: string;
  getData: (proofId: string) => void;
}

export interface AddInputBoxState {
  text: string;
}

export class AddInputBox extends React.Component<AddInputBoxProps, AddInputBoxState> {
  constructor() {
    super();
    this.state = {
      text: "",
    };
  }

  componentDidMount() {
    this.props.getData(this.props.proofId);
  }

  render() {
    const { inputType, dataList, onDelete, onAdd, proofId, error } = this.props;
    const { text } = this.state;
    let currKey = 0;
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
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => onAdd(proofId, text)} />
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

  private onChange = (event: React.FormEvent<HTMLElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState({text});
  };

}