import {Action, AppState} from "../reducers/index";
import {Dispatch} from "redux";
import {StepComponent} from "../components/StepComponent";
import {connect} from "react-redux";
import { del, get, post} from "request";
import {
  addStep, addToShow, deleteStep, deleteToShow, errStep, errToShow, setSteps, setToShows,
  StepData
} from "../actions/index";

const mapStateToProps = (state: AppState, ownProps) => {
  return {
    dataList: state.step.data.map(d => {
      return {id: d.id, text: d.text};
    }),
    givenIdList: state.given.data.map(d => d.id),
    stepIdList: state.step.data.map(d => d.id),
    error: state.step.error,
    ...ownProps
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
      get({json: true, url: 'http://localhost:8000/api/step/', qs: {proofId: proofId}},
        (error, response, body) => {
          dispatch(setSteps(body));
        }
      )
    },

    onAdd: (proofId: string, text: string, given_just:number[], step_just: number[]) => {
      post(
        {json: true, url: 'http://localhost:8000/api/step/',
          form: {proofId: proofId, text: text, given_just: given_just, step_just: step_just},
          qsStringifyOptions: {arrayFormat: 'repeat'}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            dispatch(errStep(body['text']));
          } else {
            dispatch(addStep(body));
          }
        }
      )
    },

    onDelete: (proofId: string, id: number, text: string) => {
      del({json: true, url: 'http://localhost:8000/api/step/' + id + '/'},
        (error, response, body) => {
          dispatch(deleteStep({proofId: proofId, id: id, text: text, step_just: [], given_just: []}));
        }
      )
    }
  };
};

const StepInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(StepComponent);

  export default StepInputBox;