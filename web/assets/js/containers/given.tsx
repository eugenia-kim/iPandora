import { connect } from 'react-redux';
import { addGiven } from '../actions';
import {AddInputBox} from "../components/addInputBox";
import {InputAction, InputState} from "../reducers/index";
import {Dispatch} from "redux";

const mapStateToProps = (state: InputState) => {
  return {
    inputList : state.inputList,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<InputAction>) => {
  return {
    onAdd: (text: string) => {
      dispatch(addGiven(text));
    }
  };
};

const GivenInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default GivenInputBox;