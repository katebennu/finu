import * as React from 'react';
import SelectableOptions from './Selectables';

// const SortableOptions = () => (
//     <div>
//
//     </div>
// );

const Menu = ({
                  companies,
                  selectedCompanies,
                  selectedCompaniesOnChange,
                  years,
                  selectedYears,
                  selectedYearsOnChange,
                  industries,
                  selectedIndustries,
                  selectedIndustriesOnChange
                  // sortOptions
              }: {
    companies: Company[],
    selectedCompanies: Company[],
    selectedCompaniesOnChange: (selectedCompanies: Company[]) => void,
    years: string[],
    selectedYears: string[],
    selectedYearsOnChange: (selectedYears: string[]) => void,
    industries: string[],
    selectedIndustries: string[],
    selectedIndustriesOnChange: (selectedYears: string[]) => void
}) => (
    <div style={{
        border: 'solid 1px',
        marginBottom: '10px'
    }}>
        <div>Menu</div>
        <div>
            <SelectableOptions
                options={companies}
                selectedOptions={selectedCompanies}
                selectedOptionsOnChange={selectedCompaniesOnChange}
                stringify={company => company.ticker}
            />
        </div>
        <div style={{
            margin: '20px'
        }}>
            <SelectableOptions
                options={years}
                selectedOptions={selectedYears}
                selectedOptionsOnChange={selectedYearsOnChange}
                stringify={year => year}
            />
        </div>
        <div style={{
            margin: '20px'
        }}>
            <SelectableOptions
                options={industries}
                selectedOptions={selectedIndustries}
                selectedOptionsOnChange={selectedIndustriesOnChange}
                stringify={industry => industry}
            />
        </div>
    </div>
);

export default Menu;