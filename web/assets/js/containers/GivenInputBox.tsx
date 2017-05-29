import { connect } from 'react-redux';
import {addGiven, errorGiven} from '../actions';
import {AddInputBox} from "../components/AddInputBox";
import {Action, AppState} from "../reducers/index";
import {Dispatch} from "redux";
import { post } from "request";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    inputList : state.given.inputList,
    ...ownProps
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    onAdd: (proofId: string, text: string) => {
      post(
        {url: 'http://localhost:8000/api/given/', form: {proofId: proofId, text: text}},
        (error, response, body) => {
          if (error) {
            // TODO: if not validated with Z3 grammar
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