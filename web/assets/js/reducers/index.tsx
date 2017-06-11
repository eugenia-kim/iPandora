import { assign } from "lodash";
import { combineReducers } from "redux";

import { BoxData, InitializerData, StepData } from "../actions/index";
import * as actionType from "../model/type";

export interface AppState {
  given: InputState<InitializerData>;
  type: InputState<InitializerData>;
  toShow: InputState<InitializerData>;
  step: InputState<StepData>;
  box: BoxState;
}

export interface BoxState {
  boxStack: string[];
  firstStepMap: { [boxId: string]: StepData };
  isEmpty: boolean;
  lastStep: StepData;
  proofId: string;
}

export interface InputState<T> {
  data: T[];
  error: string;
}

export interface Action<T> {
  type: string;
  payload: T;
}

const initInputState = {
  data: Array<InitializerData>(),
  error: "",
};

const initBoxState: BoxState = {
  boxStack : [],
  firstStepMap: {},
  isEmpty : false,
  lastStep : null,
  proofId: null,
};

export function givenReducer(state: InputState<InitializerData> = initInputState,
                             action: Action<InitializerData> | Action<InitializerData[]> | Action<string>) {
  switch (action.type) {
    case actionType.SET_GIVENS:
      return assign({}, state, {
        data: (action as Action<InitializerData[]>).payload,
        error: "",
      });

    case actionType.ADD_GIVEN:
      const givenList = state.data;
      return assign({}, state, {
        data: [...givenList, action.payload],
      });

    case actionType.ERR_GIVEN:
      return assign({}, state, {
        error: action.payload,
      });

    case actionType.DELETE_GIVEN:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<InitializerData>).payload.id),
      });

    default:
      return state;
  }
}

export function typeReducer(state: InputState<InitializerData> = initInputState,
                            action: Action<InitializerData> | Action<InitializerData[]> | Action<string>) {
  switch (action.type) {

    case actionType.SET_TYPES:
      return assign({}, state, {
        data: (action as Action<InitializerData[]>).payload,
        error: "",
      });

    case actionType.ADD_TYPE:
      const typeList = state.data;
      return assign({}, state, {
        data: [...typeList, action.payload],
        error: "",
      });

    case actionType.ERR_TYPE:
      return assign({}, state, {
        error: action.payload,
      });

    case actionType.DELETE_TYPE:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<InitializerData>).payload.id),
      });

    default:
      return state;
  }
}

export function toShowReducer(state: InputState<InitializerData> = initInputState,
                              action: Action<InitializerData> | Action<InitializerData[]> | Action<string>) {
  switch (action.type) {
    case actionType.SET_TOSHOWS:
      return assign({}, state, {
        data: (action as Action<InitializerData[]>).payload,
        error: "",
      });

    case actionType.ADD_TOSHOW:
      const toShowList = state.data;
      return assign({}, state, {
        data: [...toShowList, action.payload],
      });

    case actionType.ERR_TOSHOW:
      return assign({}, state, {
        error: action.payload,
      });

    case actionType.DELETE_TOSHOW:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<InitializerData>).payload.id),
      });

    default:
      return state;
  }
}

export function stepReducer(state: InputState<StepData> = { data: Array<StepData>(), error: "" },
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
        data: [...stepList, action.payload],
      });

    case actionType.ERR_STEP:
      return assign({}, state, {
        error: action.payload,
      });

    case actionType.DELETE_STEP:
      return assign({}, state, {
        data: state.data.filter(item => item.id !== (action as Action<StepData>).payload.id),
      });

    default:
      return state;
  }
}

export function boxReducer(state: BoxState = initBoxState,
                           action: Action<BoxData> | Action<StepData>) {
  switch (action.type) {
    case actionType.CREATE_BOX:
      return assign({}, state, {
        boxStack: [...state.boxStack, action.payload.id],
        isEmpty: true,
        proofId: action.payload.proofId,
      });

    case actionType.ASSUME_BOX:
      const typedAction = action as Action<StepData>;
      const boxId = typedAction.payload.boxId;
      const step = typedAction.payload;

      return assign({}, state, {
        firstStepMap: {
          ...state.firstStepMap,
          [boxId]: step,
        },
        isEmpty: false,
        lastStep: typedAction.payload,
        proofId: typedAction.payload.proofId,
      });

    case actionType.UPDATE_BOX:
      return assign({}, state, {
        lastStep: (action as Action<StepData>).payload,
      });

    case actionType.END_BOX:
      const stack = state.boxStack.slice();
      stack.pop();
      return assign({}, state, {
        boxStack: stack,
        isEmpty: false,
      });

    default:
      return state;
  }
}

export default combineReducers({
  box: boxReducer,
  given: givenReducer,
  step: stepReducer,
  toShow: toShowReducer,
  type: typeReducer,
});
