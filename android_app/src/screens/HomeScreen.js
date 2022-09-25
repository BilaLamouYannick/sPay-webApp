import React from 'react';
import {Image, StyleSheet, Text, View, ScrollView} from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';
import {SafeAreaView} from 'react-native-safe-area-context';
import Card from '../components/Card';
import ListService from '../components/ListService';
import RecentTransaction from '../components/RecentTransaction';
import {useNavigation} from '@react-navigation/core';
import Wallet from './WalletScreen'
import Transfer from './TransferScreen'
import Deposit from './DepositScreen'
import Withdrawal from './WithdrawSreen'


import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from "@react-navigation/native";
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';

 const Stack = createStackNavigator()
 const Tab = createMaterialTopTabNavigator();
const HomeScreen = ({route}) => {

    
   
        return (
            <Tab.Navigator tabBarPosition={'bottom'} tabBarOptions={{ labelStyle: { fontSize: 10 },
                showLabel: true, showIcon: true,
                indicatorStyle: { backgroundColor: "black", height:3 }, 
            }}  >
                <Tab.Screen name="Wallet" component={Wallet} initialParams={{user: route.params.user, transactions: route.params.transactions, wallet: route.params.wallet}} 
                options={{
                  tabBarLabel: 'wallet',
                  
                  tabBarLabelStyle:{ color: 'black', fontSize:8, textAlign:'center'},
                    tabBarIcon: ({ focused }) => (
                        <View style={{ alignItems: 'center', justifyContent: 'center', }}>
                            <Image source={require('../assets/ic_wallet.png')}
                                style={{ height: 15, width: 15, }} />
                            
                        </View>
                    )
                }} />
                <Tab.Screen name="Transfer" component={Transfer} initialParams={{user: route.params.user, transactions: route.params.transactions, wallet: route.params.wallet}}
                options={{
                  tabBarLabel: 'Transfer',
                  tabBarLabelStyle:{ color: 'black', fontSize:8,},
                    tabBarIcon: ({ focused }) => (
                        <View style={{ alignItems: 'center', justifyContent: 'center', }}>
                            <Image source={require('../assets/ic_transfer.png')}
                                style={{ height: 15, width: 15,}} />
                            
                        </View>
                    )
                }} />
                <Tab.Screen name="Deposit" component={Deposit} initialParams={{user: route.params.user, transactions: route.params.transactions, wallet: route.params.wallet}}
                options={{
                  tabBarLabel: 'Deposit',
                  tabBarLabelStyle:{ color: 'black', fontSize:8,},
                    tabBarIcon: ({ focused }) => (
                        <View style={{ alignItems: 'center', justifyContent: 'center', }}>
                            <Image source={require('../assets/ic_pay.png')}
                                style={{ height: 15, width: 15, }} />
        
                        </View>
                    )
                }} />
                <Tab.Screen name="Withdrawal" component={Withdrawal} initialParams={{user: route.params.user, transactions: route.params.transactions, wallet: route.params.wallet}}
                options={{
                  tabBarLabel: 'Withdrawal',
                  tabBarLabelStyle:{ color: 'black', fontSize:8,},
                    tabBarIcon: ({ focused }) => (
                        <View style={{ alignItems: 'center', justifyContent: 'center', }}>
                            <Image source={require('../assets/ic_topup.png')}
                                style={{ height: 15, width: 15, }} />
        
                        </View>
                    )
                }} />
                {/* {console.log(route.params.user.first_name)} */}
                {/* {console.log(route.params.wallet)}  */}
            </Tab.Navigator>
        )
}
export default HomeScreen
// const HomeScreen = ({route}) => {
//   const [userName, setUserName]= React.useState(route.params.user.first_name)
//   const navigation = useNavigation();
//   return (
//     <SafeAreaView style={{flex: 1}}>
//       <View style={styles.container}>
//         <View style={styles.header}>
//           <View>
//             <Text>Hello</Text>
//             <Text style={styles.userName}>{userName}</Text>
//           </View>
//           <TouchableOpacity onPress={() => navigation.navigate('Notification')}>
//           <Image source={require('../assets/ic_notif.png')} />
//           </TouchableOpacity>
//         </View>
//         <View style={styles.card}>
//           <Card cardNumber={route.params.wallet.cart_number} cardHolder='Card holder' cardName='Nguyen Van A'/>
//         </View>
//         {/* <View style ={{}}>
//         <Text style ={{color:'black'}}>{route.params.paramKey.status}</Text></View> */}
//         {/* {console.log(route.params.wallet)} */}
//         <ListService user={route.params.user} transactions = {route.params.transactions} wallet={route.params.wallet} />
//       </View>
//     </SafeAreaView>
//   );
// };

// export default HomeScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    padding: 24,
  },
  userName: {
    fontWeight: 'bold',
    fontSize: 16,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  card: {
    paddingVertical: 5,
  },
});
