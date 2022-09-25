import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import StartingPageScreen from '../screens/StartingPageScreen';
import HomeScreen from '../screens/HomeScreen';
import WelcomeScreen from '../screens/WelcomeScreen';
import LoginScreen from '../screens/LoginScreen';
import WalletScreen from '../screens/WalletScreen';
import TransferScreen from '../screens/TransferScreen';
import DepositScreen from '../screens/DepositScreen';
import WithdrawScreen from '../screens/WithdrawSreen';
import NotificationScreen from '../screens/NotificationScreen';
import AuthNavigation from './AuthNavigation';

const Stack = createStackNavigator();

const Navigator = () => {
  return (
    <>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Welcome">
          <Stack.Screen
            name="AuthNavigation"
            component={AuthNavigation}
            options={{headerShown: false}}
  />
          <Stack.Screen
            name="Home"
            component={HomeScreen}
            options={{headerShown: false}}
          />
          <Stack.Screen
            name="Welcome"
            component={WelcomeScreen}
            options={{headerShown: false}}
          />
          <Stack.Screen
            name="Login"
            component={LoginScreen}
            options={{headerShown: false}}
          />
          <Stack.Screen
            name="Wallet"
            component={WalletScreen}
            options={{headerShown: false}}
          />
          <Stack.Screen
            name="Transfer"
            component={TransferScreen}
            options={{headerShown: false}}
          />
          <Stack.Screen
            name="Deposit"
            component={DepositScreen}
            options={{headerShown: false}}
          />
          <Stack.Screen
            name="Withdraw"
            component={WithdrawScreen}
            options={{headerShown: false}}
          />
          <Stack.Screen
            name="Notification"
            component={NotificationScreen}
            options={{headerShown: false}}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </>
  );
};

export default Navigator;
