import { connect } from "react-redux";
import { Dispatch } from "redux";
import { del, get, post } from "request";

import { addGiven, deleteGiven, errGiven, setGivens } from "../actions";
import { AddInputBox } from "../components/AddInputBox";
import { Action, AppState } from "../reducers/index";

const mapStateToProps = (state: AppState, ownProps: any) => {
  return {
    dataList: state.given.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    error: state.given.error,
    ...ownProps,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
      get({json: true, url: "http://localhost:8000/api/given/", qs: {proofId}},
       (error, response, body) => {
          dispatch(setGivens(body));
       },
     );
    },
    onAdd: (proofId: string, text: string) => {
      post(
        {json: true, url: "http://localhost:8000/api/given/", form: {proofId, text}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            // TODO: if not validated with Z3 grammar
            dispatch(errGiven(body.text));
          } else {
            dispatch(addGiven(body));
          }
        },
      );
    },
    onDelete: (proofId: string, id: number, text: string) => {
      del({json: true, url: "http://localhost:8000/api/give/" + id + "/"},
        () => { dispatch(deleteGiven({proofId, id, text})); },
      );
    },
  };
};

const GivenInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default GivenInputBox;
