import * as React from 'react';
// import { connect, PromiseState } from 'react-refetch';
import Menu from './components/Menu'
import Tiles from './components/Tiles'
// import {isUndefined} from "util";

// type Companies = {
//     'companies': Company[]
// }
type Props = {
    companies: Company[]
}

type State = {
    selectedCompanies: Company[],
    selectedYears: string[],
    selectedIndustries: string[]
}

const allYears = ['2014', '2015', '2016'];

// TODO: fetch together with companies data
const allIndustries = ['Electronics', 'Software', 'Internet', 'Food', 'Pharma', 'Auto'];

// const sortOptions = []

export default class App extends React.Component<Props, State> {

    constructor(props: any) {
        super(props);
        this.state = {
            selectedCompanies: this.props.companies,
            selectedYears: allYears,
            selectedIndustries: allIndustries
        }
    }

    render () {
        const selectedCompanies = this.state.selectedCompanies;
        const selectedYears = this.state.selectedYears;
        const selectedIndustries = this.state.selectedIndustries;
        // const allData = this.props.fetched[0].data;
        return (
            <div style={{
                textAlign: 'center',
                width: '100%',
                maxWidth: '900px'
            }}>
                <div>
                    {/*<div>{JSON.stringify(this.props.companies)}</div>*/}
                    <Menu
                        companies={this.props.companies}
                        selectedCompanies={selectedCompanies}
                        selectedCompaniesOnChange={newValues => this.setState({
                            selectedCompanies: newValues
                        })}
                        years={allYears}
                        selectedYears={selectedYears}
                        selectedYearsOnChange={newValues => this.setState({
                            selectedYears: newValues
                        })}

                        industries={allIndustries}
                        selectedIndustries={selectedIndustries}
                        selectedIndustriesOnChange={newValues => this.setState({
                            selectedIndustries: newValues
                        })}
                    />
                    <Tiles selectedCompanies={selectedCompanies}
                           selectedYears={selectedYears}
                            selectedIndustries={selectedIndustries}/>
                </div>
            </div>
        )
    }
}