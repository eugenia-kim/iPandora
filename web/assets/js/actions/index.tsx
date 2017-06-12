import * as type from "../model/type";

export interface InitializerData { // Type || Given || ToShow
  id: number;
  proofId: string;
  text: string;
}

export interface StepData {
  id: number;
  depth: number;
  proofId: string;
  text: string;
  given_just: number[];
  step_just: number[];
  boxId: string;
  isFirstStepInBox: boolean;
}

export interface BoxData {
  id: string;
  proofId: string;
  parentId: string;
}

export const setTypes = (dataList: InitializerData[]) => {
  return {
    type: type.SET_TYPES,
    payload: dataList,
  };
};

export const setGivens = (dataList: InitializerData[]) => {
  return {
    type: type.SET_GIVENS,
    payload: dataList,
  };
};

export const setToShows = (dataList: InitializerData[]) => {
  return {
    type: type.SET_TOSHOWS,
    payload: dataList,
  };
};

export const setSteps = (dataList: StepData[]) => {
  return {
    type: type.SET_STEPS,
    payload: dataList,
  };
};

export const addType = (data: InitializerData) => {
  return {
    type: type.ADD_TYPE,
    payload: data,
  };
};

export const addGiven = (data: InitializerData) => {
  return {
    type: type.ADD_GIVEN,
    payload: data,
  };
};

export const addToShow = (data: InitializerData) => {
  return {
    type: type.ADD_TOSHOW,
    payload: data,
  };
};

export const addStep = (data: StepData) => {
  return {
    type: type.ADD_STEP,
    payload: data,
  };
};

export const errGiven = (error: string) => {
  return {
    type: type.ERR_GIVEN,
    payload: error,
  };
};

export const errType = (error: string) => {
  return {
    type: type.ERR_TYPE,
    payload: error,
  };
};

export const errToShow = (error: string) => {
  return {
    type: type.ERR_TOSHOW,
    payload: error,
  };
};

export const errStep = (error: string) => {
  return {
    type: type.ERR_STEP,
    payload: error,
  };
};

export const deleteType = (data: InitializerData) => {
  return {
    type: type.DELETE_TYPE,
    payload: data,
  };
};

export const deleteGiven = (data: InitializerData) => {
  return {
    type: type.DELETE_GIVEN,
    payload: data,
  };
};

export const deleteToShow = (data: InitializerData) => {
  return {
    type: type.DELETE_TOSHOW,
    payload: data,
  };
};

export const deleteStep = (id: number) => {
  return {
    type: type.DELETE_STEP,
    payload: id,
  };
};

export const createBox = (data: BoxData) => {
  return {
    type: type.CREATE_BOX,
    payload: data,
  };
};

export const updateBox = (data: StepData) => {
  return {
    type: type.UPDATE_BOX,
    payload: data,
  };
};

export const assumeBox = (data: StepData) => {
 return {
   type: type.ASSUME_BOX,
   payload: data,
 };
};

export const endBox = (data: StepData) => {
  return {
    type: type.END_BOX,
    payload: data, // not used though
  };
};
