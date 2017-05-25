import { connect } from 'react-redux';
import { addInput } from '../actions';
import {AddInputBox} from "../components/addInputBox";
import {GivenAction, GivenState} from "../reducers/given";
import {Dispatch} from "redux";

const mapStateToProps = (state: GivenState) => {
  return {
    givenList : state.givenList,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<GivenAction>) => {
  return {
    onAdd: (text: string) => {
      dispatch(addInput(text));
    }
  };
};

const GivenInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default GivenInputBox;