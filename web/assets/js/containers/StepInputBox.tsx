import { assign, last, take } from "lodash";
import { connect } from "react-redux";
import { Dispatch } from "redux";
import { del, get, post } from "request";

import {
  addStep,
  assumeBox,
  BoxData,
  createBox,
  deleteStep,
  endBox,
  errStep,
  setBoxes,
  setSteps,
  StepData,
  updateBox,
} from "../actions/index";
import { StepComponent } from "../components/StepComponent";
import { Action, AppState } from "../reducers/index";

const getBoxes = (steps: StepData[]) => {
  const boxesStack = Array<BoxData>();
  const firstStepMap: { [boxId: string]: StepData } = {};

  let lastStep: StepData;
  let lastStepDepth = 0;

  steps.forEach(step => {
    const type = (step.exist && "E") || (step.forall && "A") || "I";
    boxesStack[step.depth] = assign({}, { id: step.boxId, parentId: null, proofId: step.proofId, type });
    lastStepDepth = step.depth;

    lastStep = step;

    if (step.isFirstStepInBox) {
      firstStepMap[step.boxId] = step;
    }
  });

  return {
    boxStack: take(boxesStack, lastStepDepth),
    firstStepMap,
    isEmpty: false,
    lastStep,
  };
};

const mapStateToProps = (state: AppState, ownProps: any) => {
  const currentBox = last(state.box.boxStack);
  const boxId = (currentBox && currentBox.id) || null;
  const boxType = (currentBox && currentBox.type) || null;

  return {
    boxId: boxId,
    boxType: boxType,
    depth: state.box.boxStack.length,
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
          dispatch(setBoxes(assign(getBoxes(body), { proofId })));
        },
      );
    },

    onAdd: (proofId: string,
            depth: number,
            text: string,
            givenJust: number[],
            stepJust: number[],
            boxId: string,
            isFirstStepInBox: boolean) => {

      if (isFirstStepInBox) {
        post(
          {
            form: { proofId, depth, text, boxId, isFirstStepInBox },
            json: true,
            url: "http://localhost:8000/api/step/",
          },
          (error, response, body) => {
            if (response.statusCode === 400) {
              // TODO: if not validated with Z3 grammar
              dispatch(errStep(body.text));
            } else {
              const stepData = assign({}, body, { depth, givenJust: [], stepJust: []});
              dispatch(addStep(stepData));
              dispatch(assumeBox(stepData));
            }
          },
        );

      } else {
        post(
          {
            form: { proofId, depth, text, givenJust, stepJust, boxId, isFirstStepInBox },
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

    onCreateBox: (proofId: string, boxId: string, type: string) => {
      post(
        {json: true, url: "http://localhost:8000/api/box/", form: {proofId, parentId: boxId, type }},
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
          dispatch(deleteStep(id));
          // TODO if isFirstStepInBox, then make box isEmpty true
        },
      );
    },

    onEndBox: (proofId: string, depth: number, text: string, stepJust: number[], boxId: string) => {
      post(
        {
          form: {
            proofId,
            depth: depth - 1,
            text,
            stepJust,
            boxId,
          },
          json: true,
          qsStringifyOptions: {arrayFormat: "repeat"},
          url: "http://localhost:8000/api/step/",
        },
        (error, response, body) => {
          if (response.statusCode === 400) {
            dispatch(errStep(body.text));
          } else {
            const stepData = assign({}, body, { depth: depth - 1 });
            dispatch(endBox(stepData));
            dispatch(addStep(stepData));
            dispatch(updateBox(stepData));
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
