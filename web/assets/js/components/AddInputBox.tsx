import * as React from "react";

import { AnchorButton, InputGroup, Tooltip } from "@blueprintjs/core";

export interface Input {
  id: number;
  text: string;
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
    const { inputType } = this.props;
    const { text } = this.state;

    return (
      <div>
        <div className="add-group">
          <InputGroup
            placeholder={"Enter " + inputType + "..."}
            value={text}
            onChange={this.onChange}
            rightElement={this.renderError()}
          />
          <AnchorButton className="pt-minimal" iconName="add" onClick={this.onAdd} />
        </div>
        {this.renderData()}
      </div>
    );
  }

  private onChange = (event: React.FormEvent<HTMLElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState({text});
  }

  private onAdd = () => {
    const { proofId, onAdd } = this.props;
    const { text } = this.state;

    onAdd(proofId, text);
  }

  private createOnDeleteHandler = (proofId: string, item: Input) => () => {
    const { onDelete } = this.props;
    onDelete(proofId, item.id, item.text);
  }

  private renderData = () => {
    const { dataList, proofId } = this.props;

    let currKey = 0;

    return dataList.map((item: Input) => {
      return (
        <div key={currKey++} className="pt-card">
          [{currKey}] {item.text}
          <AnchorButton
            className="pt-minimal"
            iconName="delete"
            onClick={this.createOnDeleteHandler(proofId, item)}
          />
        </div>
      );
    });
  }

  private renderError = () => {
    const { error } = this.props;

    return error && (
        <Tooltip content={error}>
          <span className="pt-icon-error pt-intent-danger" />
        </Tooltip>
    );
  }

}
