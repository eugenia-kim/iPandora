import { connect } from 'react-redux';
import {addGiven, errGiven, setGivens } from '../actions';
import {AddInputBox} from "../components/AddInputBox";
import {Action, AppState} from "../reducers/index";
import {Dispatch} from "redux";
import { post, get } from "request";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    dataList: state.given.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    error: state.given.error,
    ...ownProps
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
      get({json: true, url: 'http://localhost:8000/api/given/', qs: {proofId: proofId}},
       (error, response, body) => {
          console.error(body);
          dispatch(setGivens(body));
       }
     )
    },
    onAdd: (proofId: string, text: string) => {
      post(
        {json: true, url: 'http://localhost:8000/api/given/', form: {proofId: proofId, text: text}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            // TODO: if not validated with Z3 grammar
            dispatch(errGiven(body['text']));
          } else {
            dispatch(addGiven(body));
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