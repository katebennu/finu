import * as React from 'react';
import { connect, PromiseState } from 'react-refetch';
import Menu from './components/Menu'
import Tiles from './components/Tiles'

type Fetched = [
    {'data': StatementRatios[]},
    {'companies': Company[]}
]

class App extends React.Component<any, any> {
    constructor(props: any) {
        super(props);
        this.state = {
            selectedCompany: 'all'
        }
    }

    handleClick = (c: string) => {
        this.setState({
            selectedCompany: c
        });
    }
    render () {
        return (
            <div style={{
                textAlign: 'center',
                width: '100%',
                maxWidth: '900px'
            }}>
                <div>
                    {/*{JSON.stringify(fetched)}*/}
                    <Menu companies={this.props.fetched[1].companies}
                          onClick={c => this.handleClick(c)}/>
                    <Tiles data={this.props.fetched[0].data.filter((statement: StatementRatios) => statement.company === this.state.selectedCompany)}/>
                </div>
            </div>
        )
    }
}

const LoadableApp = ({dataFetch, companiesFetch}: {
    dataFetch: PromiseState<Fetched[0]>,
    companiesFetch: PromiseState<Fetched[1]>
}) => {
    const allFetches = PromiseState.all([dataFetch, companiesFetch]);
    if (allFetches.rejected) {
        return <p>{allFetches.reason}</p>
    } else if (allFetches.pending) {
        return <p>Loading...</p>
    } else {
        return <App fetched={allFetches.value} />
    }
}

export default connect(() => ({
    dataFetch: 'http://localhost:5000/all-rates/',
    companiesFetch: 'http://localhost:5000/companies/'
}))(LoadableApp);