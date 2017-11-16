import * as React from 'react';
import {Set} from 'immutable';

const Button = ({
                    value,
                    onClick,
                    isSelected
                }: {
    value: string,
    onClick: () => void,
    isSelected: boolean
}) => (
    <button style={{
        display: 'inline-block',
        padding: '5px',
        color: isSelected ? 'red' : 'black'
    }}
            key={value}
            onClick={(e) => onClick()}
    >
        {value}
    </button>
);

const SelectableOptions = <ItemType extends {}>({
                                                    options,
                                                    selectedOptions,
                                                    selectedOptionsOnChange,
                                                    stringify
                                                }: {
    options: ItemType[],
    selectedOptions: ItemType[],
    selectedOptionsOnChange: (selectedOptions: ItemType[]) => void,
    stringify: (item: ItemType) => string
}) => (
    <div>
        {options.map(option => (
            <Button
                value={stringify(option)}
                onClick={() => {
                    const selection = Set(selectedOptions);
                    if (selection.contains(option)) {
                        selectedOptionsOnChange(selection.remove(option).toArray());
                    } else {
                        selectedOptionsOnChange(selection.add(option).toArray());
                    }
                }}
                isSelected={selectedOptions.indexOf(option) >= 0}
            />
        ))}
        <br />
        <Button value={selectedOptions.length < options.length ? 'select all' : 'unselect all'}
                onClick={() => {
                    selectedOptions.length < options.length ?
                        selectedOptionsOnChange(options) : selectedOptionsOnChange([]);
                }}
                isSelected={false}/>
    </div>);

export default SelectableOptions;