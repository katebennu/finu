/** Declaration file generated by dts-gen */
declare module 'react-refetch' {
    export class PromiseState<Type> {
        constructor(_ref: any);

        catch(onRejected: any): any;

        then(onFulFilled: any, onRejected: any): any;

        static all(iterable: any): any;

        static create(meta: any): any;

        static race(iterable: any): any;

        static refresh(previous: any, meta: any): any;

        static reject(reason: any, meta: any): any;

        static resolve(value: any, meta: any): any;

        fullfilled: boolean
        value: Type
        rejected: boolean
        reason: string
        pending: boolean

    }

    export function connect(map: any, ...args: any[]): any;
}