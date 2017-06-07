import * as actionType from "../constants/type"
import { assign } from "lodash"
import {combineReducers} from "redux";
import {BoxData, GivenData, StepData, ToShowData, TypeData} from "../actions/index";

export interface AppState {
  given: InputState<GivenData>;
  type: InputState<TypeData>;
  toShow: InputState<ToShowData>;
  step: InputState<StepData>;
  box: BoxState;
}

export interface BoxState {
  proofId : string;
  boxStack: string[];
  firstStepMap: { boxId: string, step: StepData }[]
  lastStep: StepData;
  isEmpty: boolean;
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

const initBoxState = {
  proofId: null,
  boxStack : [],
  firstStepMap: [],
  lastStep : null,
  isEmpty : false,
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

export function boxReducer(state: BoxState = initBoxState,
                           action: Action<BoxData> | Action<StepData>) {
  switch (action.type) {
    case actionType.CREATE_BOX:
      return assign({}, state, {
        proofId: action.payload.proofId,
        boxStack: [...state.boxStack, action.payload.id],
        isEmpty: true,
      });

    case actionType.ASSUME_BOX:
      return assign({}, state, {
        proofId: (action as Action<StepData>).payload.proofId,
        isEmpty: false,
        lastStep: (action as Action<StepData>).payload,
        firstStepMap: [
          ...state.firstStepMap,
          {boxId: (action as Action<StepData>).payload.boxId, step: (action as Action<StepData>).payload }
          ],
      });

    case actionType.UPDATE_BOX:
      return assign({}, state, {
        lastStep: (action as Action<StepData>).payload
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
  box: boxReducer,
});

