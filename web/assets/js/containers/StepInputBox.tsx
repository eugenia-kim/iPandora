import { assign, last } from "lodash";
import { connect } from "react-redux";
import { Dispatch } from "redux";
import { del, get, post } from "request";

import {
  addStep,
  assumeBox,
  createBox,
  deleteStep,
  endBox,
  errStep,
  setSteps,
  updateBox,
} from "../actions/index";
import { StepComponent } from "../components/StepComponent";
import { Action, AppState } from "../reducers/index";

const mapStateToProps = (state: AppState, ownProps: any) => {
  const boxId = last(state.box.boxStack);

  return {
    boxId,
    dataList: state.step.data,
    error: state.step.error,
    firstStepInBox: state.box.firstStepMap[boxId],
    givenIdList: state.given.data.map(d => d.id),
    isFirstStepInBox: state.box.isEmpty,
    lastStepInBox: state.box.lastStep,
    stepIdList: state.step.data.map(d => d.id),
    ...ownProps,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action<string>>) => {
  return {
    getData: (proofId: string) => {
      get({json: true, url: "http://localhost:8000/api/step/", qs: { proofId }},
        (error, response, body) => {
          dispatch(setSteps(body));
        },
      );
    },

    onAdd: (proofId: string,
            text: string,
            givenJust: number[],
            stepJust: number[],
            boxId: string,
            isFirstStepInBox: boolean) => {

      if (isFirstStepInBox) {
        post(
          {
            form: { proofId, text, boxId, isFirstStepInBox },
            json: true,
            url: "http://localhost:8000/api/step/",
          },
          (error, response, body) => {
            if (response.statusCode === 400) {
              // TODO: if not validated with Z3 grammar
              dispatch(errStep(body.text));
            } else {
              const stepData = assign({}, body, { given_just: [], step_just: []});
              dispatch(addStep(stepData));
              dispatch(assumeBox(stepData));
            }
          },
        );

      } else {
        post(
          {
            form: { proofId, text, givenJust, stepJust, boxId, isFirstStepInBox },
            json: true,
            qsStringifyOptions: { arrayFormat: "repeat" },
            url: "http://localhost:8000/api/step/",
          },
          (error, response, body) => {
            if (response.statusCode === 400) {
              dispatch(errStep(body.text));
            } else {
              // not assumption
              dispatch(addStep(body));
              dispatch(updateBox(body));
            }
          },
        );
      }
    },

    onCreateBox: (proofId: string, boxId: string) => {
      post(
        {json: true, url: "http://localhost:8000/api/box/", form: {proofId, parentId: boxId}},
        (error, response, body) => {
          dispatch(createBox(body));
        });
    },

    onDelete: (proofId: string, id: number, text: string, boxId: string, isFirstStepInBox: boolean) => {
      del(
        {
          json: true,
          url: "http://localhost:8000/api/step/" + id + "/",
        },
        () => {
          dispatch(deleteStep({proofId, id, text, step_just: [], given_just: [], isFirstStepInBox, boxId}));
          // TODO if isFirstStepInBox, then make box isEmpty true
        },
      );
    },

    onEndBox: (proofId: string, text: string, stepJust: number[], boxId: string) => {
      post(
        {
          form: { proofId, text, stepJust, boxId },
          json: true,
          qsStringifyOptions: {arrayFormat: "repeat"},
          url: "http://localhost:8000/api/step/",
        },
        (error, response, body) => {
          if (response.statusCode === 400) {
            dispatch(errStep(body.text));
          } else {
            dispatch(endBox(body));
            dispatch(addStep(body));
            dispatch(updateBox(body));
          }
        },
      );
    },
  };
};

const StepInputBox = connect (
  mapStateToProps,
  mapDispatchToProps,
)(StepComponent);

export default StepInputBox;
