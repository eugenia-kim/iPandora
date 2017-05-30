import * as React from "react";
import {Alert, AnchorButton, InputGroup} from "@blueprintjs/core";
import {assign} from "lodash";

export interface AddInputBoxProps {
  proofId: string;
  inputType: string;
  onAdd: (proofId: string, text: string) => void;
  inputList: string[];
  error: string;
}

export interface AddInputBoxState {
  text: string;
  isOpenError: boolean;
}

export class AddInputBox extends React.Component<AddInputBoxProps, AddInputBoxState> {
  constructor() {
    super();
    this.state = {
      text: "",
      isOpenError: false,
    };
  }

  componentWillReceiveProps(nextProps) {
    console.error(this.props.error);
    if(nextProps.error !== "") {
      // Check if it's a new error
           this.handleOpenError();
    }
  }

  render() {
    const { inputType, inputList, onAdd, proofId } = this.props;
    const { text } = this.state;
    let currKey = 0;
    return (
      <div>
        <InputGroup placeholder={ "Enter " + inputType + "..." } value={text} onChange={this.onChange} />
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => onAdd(proofId, text)} />
        {
          inputList.map( (item: string) => {
            return (
              <div key={currKey++} className="pt-card">
                {item}
              </div>
            );
          })
        }
        <Alert isOpen={ this.state.isOpenError} onConfirm={this.handleCloseError}>
          <p> {this.props.error} </p>
        </Alert>
      </div>
    );
  }

  private onChange = (event: React.FormEvent<HTMLElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState({text});
  };

  private handleOpenError = () => this.setState({ isOpenError: true });
  private handleCloseError = () => this.setState({ isOpenError: false });
}