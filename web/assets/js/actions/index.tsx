import * as type from "../constants/type"

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