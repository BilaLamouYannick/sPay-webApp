/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

// import React from 'react';
import * as React from 'react';
import { StyleSheet } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import Navigator from './src/navigation';
import Login from './src/screens/LoginScreen';

import { DataProvider } from './src/Store';

 const App = () => {
        return  <DataProvider> 
        < Navigator / >  
        { /* <Login / > ; */ } 
        </DataProvider>
         };

        const styles = StyleSheet.create({
            container: {
                flex: 1,
            },
        });

        export default App;