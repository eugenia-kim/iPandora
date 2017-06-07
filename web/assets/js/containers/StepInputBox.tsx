import {Action, AppState} from "../reducers/index";
import {Dispatch} from "redux";
import {StepComponent} from "../components/StepComponent";
import {connect} from "react-redux";
import { del, get, post} from "request";
import {
  addStep, assumeBox, createBox, deleteStep, endBox, errStep, setSteps, updateBox,
} from "../actions/index";
import { last, assign } from "lodash";

const mapStateToProps = (state: AppState, ownProps) => {
  const boxId = last(state.box.boxStack);

  return {
    dataList: state.step.data.map(d => {
      return {id: d.id, text: d.text, boxId: d.boxId, isFirstStepInBox: d.isFirstStepInBox};
    }),
    givenIdList: state.given.data.map(d => d.id),
    stepIdList: state.step.data.map(d => d.id),
    error: state.step.error,
    boxId: boxId,
    isFirstStepInBox: state.box.isEmpty,
    firstStepInBox: state.box.firstStepMap[boxId],
    lastStepInBox: state.box.lastStep,
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

    onAdd: (proofId: string, text: string, given_just:number[], step_just: number[], boxId: string, isFirstStepInBox: boolean) => {

      if (isFirstStepInBox) {
        post(
          {json: true, url: 'http://localhost:8000/api/step/',
            form: {proofId: proofId, text: text, boxId: boxId, isFirstStepInBox: isFirstStepInBox}},
          (error, response, body) => {
            if (response.statusCode === 400) {
              // TODO: if not validated with Z3 grammar
              dispatch(errStep(body['text']));
            } else {
              const stepData = assign({}, body, { given_just: [], step_just: []});
              dispatch(addStep(stepData));
              dispatch(assumeBox(stepData));
            }
          }
        )

      } else {
        post(
          {json: true, url: 'http://localhost:8000/api/step/',
            form: {proofId: proofId, text: text, given_just: given_just, step_just: step_just, boxId: boxId, isFirstStepInBox: isFirstStepInBox},
            qsStringifyOptions: {arrayFormat: 'repeat'}},
          (error, response, body) => {
            if (response.statusCode === 400) {
              dispatch(errStep(body['text']));
            } else {
              // not assumption
              dispatch(addStep(body));
              dispatch(updateBox(body));
            }
          }
        )
      }
    },

    onDelete: (proofId: string, id: number, text: string, boxId: string, isFirstStepInBox: boolean) => {
      del({json: true, url: 'http://localhost:8000/api/step/' + id + '/'},
        (error, response, body) => {
          dispatch(deleteStep({proofId: proofId, id: id, text: text, step_just: [], given_just: [], isFirstStepInBox: isFirstStepInBox, boxId: boxId}));
          // TODO if isFirstStepInBox, then make box isEmpty true
        }
      )
    },

    onCreateBox: (proofId: string, boxId: string) => {
      post(
        {json: true, url: 'http://localhost:8000/api/box/', form: {proofId: proofId, parentId: boxId,}},
        (error, response, body) => {
          dispatch(createBox(body));
        })
    },

    onEndBox: (proofId: string, text: string, step_just: number[], boxId: string) => {
      post(
        {json: true, url: 'http://localhost:8000/api/step/',
         form: { proofId, text, step_just, boxId, },
         qsStringifyOptions: {arrayFormat: 'repeat'}},
        (error, response, body) => {
          if (response.statusCode === 400) {
            dispatch(errStep(body['text']));
          } else {
            dispatch(endBox(body));
            dispatch(addStep(body));
            dispatch(updateBox(body));
          }
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