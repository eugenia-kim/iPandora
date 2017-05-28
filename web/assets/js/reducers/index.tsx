import { ADD_GIVEN } from "../constants/type"

export interface InputState {
  inputList: string[];
}

export interface InputAction {
  type: string,
  payload: {
    text: string,
  }
}

export function givenReducer(state: InputState = { inputList: [] }, action: InputAction) {
  switch (action.type) {
    case ADD_GIVEN:
      const givenList = state.inputList;
      return {
        inputList: [...givenList, action.payload.text]
      };

    default:
      return state;
  }
}