import * as React from 'react';
import { connect, PromiseState } from 'react-refetch';
import Menu from './components/Menu'
import Tiles from './components/Tiles'
import {isUndefined} from "util";

type Fetched = [
    {'data': StatementRatios[]},
    {'companies': Company[]}
]

type State = {
    selectedCompanies: Company[],
    selectedYears: string[]
}

class App extends React.Component<any, State> {
    constructor(props: any) {
        super(props);
        this.state = {
            selectedCompanies: [],
            selectedYears: []
        }
    }

    render () {
        const selectedCompanies = this.state.selectedCompanies;
        const selectedYears = this.state.selectedYears;
        const allData = this.props.fetched[0].data;
        return (
            <div style={{
                textAlign: 'center',
                width: '100%',
                maxWidth: '900px'
            }}>
                <div>
                    <Menu
                        companies={this.props.fetched[1].companies}
                        selectedCompanies={selectedCompanies}
                        selectedCompaniesOnChange={newValues => this.setState({
                            selectedCompanies: newValues
                        })}
                        years={['2014', '2015', '2016']}
                        selectedYears={selectedYears}
                        selectedYearsOnChange={newValues => this.setState({
                            selectedYears: newValues
                        })}
                    />
                    <Tiles data={
                        allData.filter((statement: StatementRatios) =>
                            !isUndefined(
                                selectedCompanies.find(
                                    (company: Company) => company.ticker === statement.company
                            )) && 
                            !isUndefined(
                                selectedYears.find(
                                    (year: string) => year === statement.year.toString()))
                        )
                    } />
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
};

export default connect(() => ({
    dataFetch: 'http://localhost:5000/all-rates/',
    companiesFetch: 'http://localhost:5000/companies/'
}))(LoadableApp);