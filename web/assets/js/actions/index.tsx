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

export const addToShow = (text: string) => {
  return {
    type: type.ADD_TOSHOW,
    payload: text
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
    type: type.ERR_GIVEN,
    payload: error,
  }
}

export const errToShow = (text: string) => {
  return {
    type: type.ERR_TOSHOW,
    payload: text
  }
}
