import {Action, AppState} from "../reducers/index";
import {Dispatch} from "redux";
import {AddInputBox} from "../components/AddInputBox";
import {connect} from "react-redux";
import { get, post} from "request";
import {addToShow, errToShow, setToShows} from "../actions/index";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    dataList: state.toShow.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    ...ownProps
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
     get({json: true, url: 'http://localhost:8000/api/toShow/', qs: {proofId: proofId}},
       (error, response, body) => {
          console.error(body);
          dispatch(setToShows(body));
       }
     )
    },
    onAdd: (proofId: string, text: string) => {
      post(
        {url: 'http://localhost:8000/api/toShow/', form: {proofId: proofId, text: text}},
        (error, response, body) => {
          if (error) {
            // TODO: if not validated with Z3 grammar
            dispatch(errToShow(error));
          } else {
            dispatch(addToShow(body));
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
