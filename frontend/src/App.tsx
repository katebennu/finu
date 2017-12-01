import * as React from 'react';
// import { connect, PromiseState } from 'react-refetch';
// import Menu from './components/Menu'
// import Tiles from './components/Tiles'
// import {isUndefined} from "util";

type Companies = {
    'companies': string[]
}
type Props = {
    companies: Companies
}

// type State = {
//     selectedCompanies: Company[],
//     selectedYears: string[]
// }

// const allYears = ['2014', '2015', '2016'];
// const sortOptions = []

export default class App extends React.Component<Props> {

    // constructor(props: any) {
    //     super(props);
    //     this.state = {
    //         selectedCompanies: this.props.companies,
    //         selectedYears: allYears
    //     }
    // }

    render () {
        // const selectedCompanies = this.state.selectedCompanies;
        // const selectedYears = this.state.selectedYears;
        // const allData = this.props.fetched[0].data;
        return (
            <div style={{
                textAlign: 'center',
                width: '100%',
                maxWidth: '900px'
            }}>
                <div>
                    <div>{JSON.stringify(this.props.companies)}</div>
                    {/*<Menu*/}
                        {/*companies={this.props.companies}*/}
                    {/*/>*/}
                    {/*<Tiles data={*/}
                        {/*allData.filter((statement: StatementRatios) =>*/}
                            {/*!isUndefined(*/}
                                {/*selectedCompanies.find(*/}
                                    {/*(company: Company) => company.ticker === statement.company*/}
                            {/*)) &&*/}
                            {/*!isUndefined(*/}
                                {/*selectedYears.find(*/}
                                    {/*(year: string) => year === statement.year.toString()))*/}
                        {/*)*/}
                    {/*} />*/}
                </div>
            </div>
        )
    }
}