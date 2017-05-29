import {Dispatch} from "redux";
import {Action, AppState} from "../reducers/index";
import {addType, errorType} from "../actions/index";
import {connect} from "react-redux";
import {AddInputBox} from "../components/AddInputBox";
import { post } from "request";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    inputList: state.type.inputList,
    ...ownProps
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    onAdd: (proofId: string, text: string) => {
      post(
        {url: 'http://localhost:8000/api/type/',  form: {proofId: proofId, text: text}},
        (error, response, body) => {
          if (error) {
            // TODO: if not validated with Z3 type grammar
            dispatch(errorType(error));
          } else {
            dispatch(addType(text));
          }
        }
      )
    }
  };
};

const TypeInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default TypeInputBox;