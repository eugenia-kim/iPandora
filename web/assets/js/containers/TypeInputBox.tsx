import { connect } from "react-redux";
import { Dispatch } from "redux";
import { del, get, post } from "request";

import { addType, deleteType, errType, setTypes } from "../actions/index";
import { AddInputBox } from "../components/AddInputBox";
import { Action, AppState } from "../reducers/index";

const mapStateToProps = (state: AppState, ownProps: any) => {
  return {
    dataList: state.type.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    error: state.type.error,
    ...ownProps,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
      get({json: true, url: "http://localhost:8000/api/type/", qs: {proofId}},
        (error, response, body) => {
          dispatch(setTypes(body));
        },
      );
    },
    onAdd: (proofId: string, text: string) => {
      post({json: true, url: "http://localhost:8000/api/type/", form: {proofId, text}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            dispatch(errType(body.text));
          } else {
            dispatch(addType(body));
          }
        },
      );
    },
    onDelete: (proofId: string, id: number, text: string) => {
      del({json: true, url: "http://localhost:8000/api/type/" + id + "/"},
        () => { dispatch(deleteType({proofId, id, text})); },
      );
    },
  };
};

const TypeInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default TypeInputBox;
