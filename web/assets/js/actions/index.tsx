import { ADD_GIVEN } from "../constants/type"

export const addGiven = (text: string) => {
  return {
    type: ADD_GIVEN,
    payload: {
      text,
    }
  }
}