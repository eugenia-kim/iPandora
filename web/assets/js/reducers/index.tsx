import {ADD_GIVEN, ADD_TOSHOW, ADD_TYPE, ERR_GIVEN, ERR_TOSHOW, ERR_TYPE} from "../constants/type"
import { assign } from "lodash"
import {combineReducers} from "redux";

export interface AppState {
  given: InputState;
  type: InputState;
  toShow: InputState;
}

export interface InputState {
  inputList: string[];
  error: string;
}

export interface Action<T> {
  type: string;
  payload: T;
}

const initInputState  = {
  inputList: [],
  error: ""
};

export function givenReducer(state: InputState = initInputState, action: Action<string>) {
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

export function typeReducer(state: InputState = initInputState, action: Action<string>) {
  switch (action.type) {
    case ADD_TYPE:
      const typeList = state.inputList;
      return assign({}, state, {
        inputList: [...typeList, action.payload],
        error: ""
      });

    case ERR_TYPE:
      return assign({}, state, {
        error: action.payload
      });

    default:
      return state;
  }
}

export function toShowReducer(state: InputState = initInputState, action: Action<string>) {
  switch (action.type) {
    case ADD_TOSHOW:
      const toShowList = state.inputList;
      return assign({}, state, {
        inputList: [...toShowList, action.payload]
      });

    case ERR_TOSHOW:
      return assign({}, state, {
        error: action.payload
      });

    default:
      return state;
  }
}

export default combineReducers({
  given: givenReducer,
  type: typeReducer,
  toShow: toShowReducer,
});


