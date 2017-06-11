import { connect } from "react-redux";
import { Dispatch } from "redux";
import { del, get, post } from "request";

import { addToShow, deleteToShow, errToShow, setToShows } from "../actions/index";
import { AddInputBox } from "../components/AddInputBox";
import { Action, AppState } from "../reducers/index";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    dataList: state.toShow.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    error: state.toShow.error,
    ...ownProps,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
     get({json: true, url: "http://localhost:8000/api/toShow/", qs: {proofId}},
       (error, response, body) => {
          dispatch(setToShows(body));
       },
     );
    },
    onAdd: (proofId: string, text: string) => {
      post(
        {json: true, url: "http://localhost:8000/api/toShow/", form: {proofId, text}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            // TODO: if not validated with Z3 grammar
            dispatch(errToShow(body.text));
          } else {
            dispatch(addToShow(body));
          }
        },
      );
    },
    onDelete: (proofId: string, id: number, text: string) => {
      del({json: true, url: "http://localhost:8000/api/toShow/" + id + "/"},
        (error, response, body) => {
          dispatch(deleteToShow({proofId, id, text}));
        },
      );
    },
  };
};

const ToShowInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default ToShowInputBox;
