import * as React from 'react';
import YearTile from './YearTile'
import fetchData from '../utils/fetchData';


type Props = {
    company: Company,
    selectedYears: string[],
}

type State = {
    isLoading: boolean,
    price: ''
}


class CompanyTile extends React.Component<Props, State> {
    constructor(props: any) {
        super(props);
        this.state = {
            isLoading: false,
            price: ''
        }
    }

    async componentWillMount() {
        const p = await fetchData('/price/',
            {'ticker': this.props.company.ticker});
        this.setState({
            price: p.price
        })
    }

    render() {
        if (this.state.isLoading) {
            return null; // or you can render laoding spinner here
        } else {
            return (
                <div style={{
                    display: 'inline-block',
                    // width: '95%',
                    // minWidth: '400px',
                    // maxWidth: '300px',
                    margin: '10px',
                    border: 'solid 2px black',
                    verticalAlign: 'top'
                }}>
                    <div>{this.props.company.ticker} - {this.props.company.name} </div>
                    <div>Price: ${this.state.price}</div>
                    <div>
                        {this.props.selectedYears.map(year => (
                            <YearTile
                                key={this.props.company.ticker + '-' + year}
                                company={this.props.company}
                                year={year}/>
                        ))}
                    </div>
                    {/*<div>*/}
                    {/*{Object.keys(value.ratios).map((ratio: string) =>*/}
                    {/*<RatiosSubGroup title={ratio} items={value.ratios[ratio]}/>*/}
                    {/*)}*/}
                    {/*</div>*/}
                </div>
            )
        }


    }
}

export default CompanyTile;