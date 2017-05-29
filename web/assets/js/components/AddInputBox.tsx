import * as React from "react";
import {AnchorButton, InputGroup} from "@blueprintjs/core";
import {assign} from "lodash";

export interface AddInputBoxProps {
  proofId: string;
  inputType: string;
  onAdd: (proofId: string, text: string) => void;
  inputList: string[];
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

  render() {
    const { inputType, inputList, onAdd, proofId } = this.props;
    const { text } = this.state;
    let currKey = 0;
    console.error(inputType);
    return (
      <div>
        <InputGroup placeholder={ "Enter " + inputType + "..." } value={text} onChange={this.onChange} />
        <AnchorButton className="pt-minimal" iconName="add" onClick={() => onAdd(proofId, text)} />
        {
          inputList.map( (item: string) => {
            console.error(item);
            return (
              <div key={currKey++} className="pt-card">
                {item}
              </div>
            );
          })
        }
      </div>
    );
  }

  private onChange = (event: React.FormEvent<HTMLElement>) => {
    const text = (event.target as HTMLInputElement).value;
    this.setState({ text });
  }
}