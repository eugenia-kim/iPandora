import * as actionType from "../constants/type"
import { assign } from "lodash"
import {combineReducers} from "redux";
import {GivenData, StepData, ToShowData, TypeData} from "../actions/index";

export interface AppState {
  given: InputState<GivenData>;
  type: InputState<TypeData>;
  toShow: InputState<ToShowData>;
  step: InputState<StepData>;
}

export interface InputState<T> {
  data: T[];
  error: string;
}

export interface Action<T> {
  type: string;
  payload: T;
}

const initInputState  = {
  data: [],
  error: "",
};

export function givenReducer(state: InputState<GivenData> = initInputState,
                             action: Action<GivenData> | Action<GivenData[]> | Action<string>) {
  switch (action.type) {
    case actionType.SET_GIVENS:
      return assign({}, state, {
        data: (action as Action<GivenData[]>).payload,
        error: "",
      });

    case actionType.ADD_GIVEN:
      const givenList = state.data;
      return assign({}, state, {
        data: [...givenList, action.payload]
      });

    case actionType.ERR_GIVEN:
      return assign({}, state, {
        error: action.payload
      });

    case actionType.DELETE_GIVEN:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<GivenData>).payload.id),
      });

    default:
      return state;
  }
}

export function typeReducer(state: InputState<TypeData> = initInputState,
                            action: Action<TypeData> | Action<TypeData[]> | Action<string>) {
  switch (action.type) {

    case actionType.SET_TYPES:
      return assign({}, state, {
        data: (action as Action<TypeData[]>).payload,
        error: "",
      });

    case actionType.ADD_TYPE:
      const typeList = state.data;
      return assign({}, state, {
        data: [...typeList, action.payload],
        error: ""
      });

    case actionType.ERR_TYPE:
      return assign({}, state, {
        error: action.payload
      });

    case actionType.DELETE_TYPE:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<TypeData>).payload.id),
      });

    default:
      return state;
  }
}

export function toShowReducer(state: InputState<ToShowData> = initInputState,
                              action: Action<ToShowData> | Action<ToShowData[]> | Action<string>) {
  switch (action.type) {
    case actionType.SET_TOSHOWS:
      return assign({}, state, {
        data: (action as Action<ToShowData[]>).payload,
        error: "",
      });

    case actionType.ADD_TOSHOW:
      const toShowList = state.data;
      return assign({}, state, {
        data: [...toShowList, action.payload]
      });

    case actionType.ERR_TOSHOW:
      return assign({}, state, {
        error: action.payload
      });

    case actionType.DELETE_TOSHOW:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<ToShowData>).payload.id),
      });

    default:
      return state;
  }
}

export function stepReducer(state: InputState<StepData> = initInputState,
                            action: Action<StepData> | Action<StepData[]> | Action<string>) {
  switch (action.type) {
    case actionType.SET_STEPS:
      return assign({}, state, {
        data: (action as Action<StepData[]>).payload,
        error: "",
      });

    case actionType.ADD_STEP:
      const stepList = state.data;
      return assign({}, state, {
        data: [...stepList, action.payload]
      });

    case actionType.ERR_STEP:
      return assign({}, state, {
        error: action.payload
      });

    case actionType.DELETE_STEP:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<StepData>).payload.id),
      });

    default:
      return state;
  }
}

export default combineReducers({
  given: givenReducer,
  type: typeReducer,
  toShow: toShowReducer,
  step: stepReducer,
});


