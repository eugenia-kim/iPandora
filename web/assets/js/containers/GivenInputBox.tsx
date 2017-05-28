import { connect } from 'react-redux';
import {addGiven, errorGiven} from '../actions';
import {AddInputBox} from "../components/AddInputBox";
import {Action, InputState} from "../reducers/index";
import {Dispatch} from "redux";
import { post } from "request";

const mapStateToProps = (state: InputState) => {
  return {
    inputList : state.inputList,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    onAdd: (proofId: string, text: string) => {
      post(
        "http://localhost:8000/api/" + proofId + "/add_given",
        (error, response, body) => {
          if (error) {
            dispatch(errorGiven(error));
          } else {
            dispatch(addGiven(text));
          }
        }
      )
    }
  };
};

const GivenInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default GivenInputBox;