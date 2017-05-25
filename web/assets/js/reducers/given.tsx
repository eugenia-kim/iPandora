export interface GivenState {
  givenList: string[];
}

export interface GivenAction {
  type: string,
  payload: {
    text: string,
  }
}

export function givenReducer(state: GivenState = { givenList: [] }, action: GivenAction) {
  switch (action.type) {
    case 'ADD_INPUT':
      const list = state.givenList;
      return {
        givenList: [...list, action.payload.text]
      };

    default:
      return state;
  }
}