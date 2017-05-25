export const addInput = (text: string) => {
  return {
    type: 'ADD_INPUT',
    payload: {
      text,
    }
  }
}