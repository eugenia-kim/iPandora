import * as type from "../constants/type"

export interface TypeData {
  id: number;
  proofId: string;
  text: string;
}

export interface GivenData {
  id: number;
  proofID: string;
  text: string;
}

export interface ToShowData {
  id: number;
  proofID: string;
  text: string;
}

export const setTypes = (dataList: TypeData[]) => {
  return {
    type: type.SET_TYPES,
    payload: dataList,
  };
};

export const setGivens = (dataList: GivenData[]) => {
  return {
    type: type.SET_GIVENS,
    payload: dataList,
  }
};

export const setToShows = (dataList: ToShowData[]) => {
  return {
    type: type.SET_TOSHOWS,
    payload: dataList,
  }
};

export const addType = (data: TypeData) => {
  return {
    type: type.ADD_TYPE,
    payload: data
  };
};

export const addGiven = (data: GivenData) => {
  return {
    type: type.ADD_GIVEN,
    payload: data
  };
};

export const addToShow = (data: ToShowData) => {
  return {
    type: type.ADD_TOSHOW,
    payload: data
  }
}

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
  }
}

export const errToShow = (error: string) => {
  return {
    type: type.ERR_TOSHOW,
    payload: error,
  }
}

export const deleteType = (data: TypeData) => {
  return {
    type: type.DELETE_TYPE,
    payload: data,
  }
}
