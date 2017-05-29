import {ADD_GIVEN, ERR_GIVEN} from "../constants/type"
import { assign } from "lodash"

export interface InputState {
  inputList: string[];
  error: string;
}

export interface Action<T> {
  type: string;
  payload: T;
}

export function givenReducer(state: InputState = { error: "", inputList: [] }, action: Action<string>) {
  switch (action.type) {
    case ADD_GIVEN:
      const givenList = state.inputList;
      return assign({}, state, {
        inputList: [...givenList, action.payload]
      });

    case ERR_GIVEN:
      return assign({}, state, {
        error: action.payload
      });


    default:
      return state;
  }
}

export function toShowReducer(state: InputState, action: Action<string>) {

}

