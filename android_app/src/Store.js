import React, {createContext, useContext, useReducer} from 'react';

const initialState = {
    data:null
};

const reducer = (state, action) => {
   switch (action) {
       case 'setData':
       return {
           ...state,
           data: action.newData
       };
       default:
       return state;
   }
};

const DataContext = createContext();

export const DataConsumer = DataContext.Consumer;
export const DataConsumerHook = () => useContext(DataContext);

export const DataProvider = ({children}) => (
   <DataContext.Provider value={useReducer(reducer, initialState)}>
       {children}
   </DataContext.Provider>
);