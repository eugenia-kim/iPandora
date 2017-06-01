import {Action, AppState} from "../reducers/index";
import {Dispatch} from "redux";
import {AddInputBox} from "../components/AddInputBox";
import {connect} from "react-redux";
import { del, get, post} from "request";
import {addToShow, deleteToShow, errToShow, setToShows} from "../actions/index";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    dataList: state.toShow.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    error: state.toShow.error,
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
        {json:true, url: 'http://localhost:8000/api/toShow/', form: {proofId: proofId, text: text}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            // TODO: if not validated with Z3 grammar
            console.log(body)
            dispatch(errToShow(body['text']));
          } else {
            dispatch(addToShow(body));
          }
        }
      )
    },
    onDelete: (proofId: string, id: number, text: string) => {
      del({json:true, url: 'http://localhost:8000/api/toShow/' + id + '/'},
        (error, response, body) => {
          dispatch(deleteToShow({proofId: proofId, id: id, text:text}));
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
