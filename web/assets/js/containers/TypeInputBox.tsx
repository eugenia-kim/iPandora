import {Dispatch} from "redux";
import {Action, AppState} from "../reducers/index";
import {addType, deleteType, errType, setTypes} from "../actions/index";
import {connect} from "react-redux";
import {AddInputBox} from "../components/AddInputBox";
import { del, get, post } from "request";


const mapStateToProps = (state: AppState, ownProps) => {
  return {
    dataList: state.type.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    error: state.type.error,
    ...ownProps
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
      get({json: true, url: 'http://localhost:8000/api/type/', qs: {proofId: proofId}},
        (error, response, body) => {
          console.error(body);
          dispatch(setTypes(body));
        }
      )
    },
    onAdd: (proofId: string, text: string) => {
      post({json: true, url: 'http://localhost:8000/api/type/', form: {proofId: proofId, text: text}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            dispatch(errType(body['text']));
          } else {
            dispatch(addType(body));
          }
        }
      )
    },
    onDelete: (proofId: string, id: number, text: string) => {
      del({json: true, url: 'http://localhost:8000/api/type/' + id + '/'},
        (error, response, body) => {
          dispatch(deleteType({proofId: proofId, id: id, text: text}));
        }
      )
    }
  }
};

const TypeInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(AddInputBox);

export default TypeInputBox;