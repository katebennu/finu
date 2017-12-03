import * as React from 'react';
import fetchData from '../utils/fetchData';


// const RatiosSubGroup = ({title, items}: { title: string, items: object }) => (
//     <div style={{
//             border: 'solid 1px gray'
//         }}>
//         <b>{title}</b>
//         <ul>
//             {Object.keys(items).map((item: string) => (
//                     <li>{item}: {items[item].toFixed(2)}</li>
//                 )
//             )}
//         </ul>
//     </div>
// );

type Props = {
    company: Company,
    year: string,
    price?: number
}

type State = {
    isLoading: boolean,
    rates: object
}


class YearTile extends React.Component<Props, State> {
    constructor(props: any) {
        super(props);
        this.state = {
            isLoading: false,
            rates: {}
        }
    }

    async componentWillMount() {
        const rates = await fetchData('/company-rates/',
            {'ticker': this.props.company.ticker,
                     'year': this.props.year});
        this.setState({
            rates: rates
        })
    }

    render() {
        if (this.state.isLoading) {
            return null; // or you can render laoding spinner here
        } else {
            return (
                <div style={{
                    display: 'inline-block',
                    // width: '30%',
                    minWidth: '200px',
                    maxWidth: '500px',
                    margin: '10px',
                    border: 'solid 2px black'
                }}>
                    <div>{this.props.year}</div>
                    <div>{JSON.stringify(this.state.rates)}</div>
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
export default YearTile;