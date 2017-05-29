import * as type from "../constants/type"

export const addType = (text: string) => {
  return {
    type: type.ADD_TYPE,
    payload: text
  };
};

export const addGiven = (text: string) => {
  return {
    type: type.ADD_GIVEN,
    payload: text
  };
};

export const errorGiven = (error: string) => {
  return {
    type: type.ERR_GIVEN,
    payload: error,
  };
};

export const errorType = (error: string) => {
  return {
    type: type.ERR_GIVEN,
    payload: error,
  }
}