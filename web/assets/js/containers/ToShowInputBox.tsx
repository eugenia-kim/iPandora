import {Action, AppState} from "../reducers/index";
import {Dispatch} from "redux";
import {AddInputBox} from "../components/AddInputBox";
import {connect} from "react-redux";
import {post} from "request";
import {addToShow, errToShow} from "../actions/index";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    inputList : state.toShow.inputList,
    ...ownProps
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    onAdd: (proofId: string, text: string) => {
      post(
        {url: 'http://localhost:8000/api/toShow/', form: {proofId: proofId, text: text}},
        (error, response, body) => {
          if (error) {
            // TODO: if not validated with Z3 grammar
            dispatch(errToShow(error));
          } else {
            dispatch(addToShow(text));
          }
        }
      )
    }
  };
};

const ToShowInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default ToShowInputBox;
