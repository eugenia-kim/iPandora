import {ADD_GIVEN, ADD_TYPE, ERR_GIVEN, ERR_TYPE} from "../constants/type"
import { assign } from "lodash"
import {combineReducers} from "redux";

export interface AppState {
  given: InputState;
  type: InputState;
}

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

export function typeReducer(state: InputState = { error: "", inputList: []}, action: Action<string>) {
  switch (action.type) {
    case ADD_TYPE:
      const typeList = state.inputList;
      return assign({}, state, {
        inputList: [...typeList, action.payload]
      });

    case ERR_TYPE:
      return assign({}, state, {
        error: action.payload
      });

    default:
      return state;
  }
}

export function toShowReducer(state: InputState, action: Action<string>) {

}

export default combineReducers({
  given: givenReducer,
  type: typeReducer,
});


