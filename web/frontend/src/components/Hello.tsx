import * as React from "react";

export interface HelloProps { compiler: string; framework: string; apiAddr: string; }
interface HelloState { serverState: string; randNumber: number | null; }

// 'HelloProps' describes the shape of props.
// State is never set so we use the 'undefined' type.
export class Hello extends React.Component<HelloProps, HelloState> {
  constructor() {
    super()

    this.state = { serverState: "unchecked", randNumber: null }
  }

  componentDidMount() {
    let that = this;

    fetch(this.props.apiAddr + '/health')
      .then((res) => {
        let promise = res.json() //Promise<JSON>
        promise.then((json) => { this.setState({ serverState: json.alive }) })
      })
  }

  fetchRandomNumber() {
    fetch(this.props.apiAddr + '/rand')
      .then((res) => {
        let promise = res.json()
        promise.then((json) => { this.setState({ randNumber: json.rand }) })
      })
  }

  render() {
    return (
      <div>
        <h1>Hello from {this.props.compiler} and {this.props.framework}!</h1>
        <hr />
        <h3>server state: {this.state.serverState}</h3>
        <hr />
        <h3>my random number is {this.state.randNumber? this.state.randNumber: "some number"}</h3>
        <button onClick={this.fetchRandomNumber.bind(this)}>Grab Number</button>
      </div>
    )
  }
}
